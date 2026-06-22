from fastapi import APIRouter
from services.gemini_service import ask_gemini
from pydantic import BaseModel
from sqlalchemy import text
from database.postgres import SessionLocal
from rag.retriever import search_docs
from services.sentiment_service import detect_sentiment
import re




router = APIRouter()
class ChatRequest(BaseModel):
    message: str
@router.post("/chat")
def chat(request: ChatRequest):
    sentiment = detect_sentiment(request.message)

    if sentiment == "angry":

        db = SessionLocal()

        db.execute(
            text("""
                INSERT INTO tickets
                (customer_message, priority, status)
                VALUES
                (:message, :priority, :status)
            """),
            {
                "message": request.message,
                "priority": "HIGH",
                "status": "OPEN"
            }
        )

        db.commit()
        db.close()

        prompt = f"""
        You are a professional customer support agent.

        Customer Message:
        {request.message}

        The customer appears frustrated.

        Be empathetic and offer escalation.
        """

        response = ask_gemini(prompt)

        return {
            "priority": "HIGH",
            "escalation": True,
            "response": response
        }


    order_match = re.search(r"#(\d+)", request.message)

    if order_match:

        order_id = int(order_match.group(1))

        db = SessionLocal()

        query = text("""
            SELECT *
            FROM orders
            WHERE id = :order_id
        """)

        order = db.execute(
            query,
            {"order_id": order_id}
        ).fetchone()

        db.close()

        if not order:
            return {
                "response": "Sorry, I could not find that order."
            }

        prompt = f"""
        You are a professional customer support agent.

        Customer Name: {order.customer_name}
        Order ID: {order.id}
        Order Status: {order.status}
        Tracking Number: {order.tracking_number}
        Delivery Date: {order.delivery_date}

        Generate a helpful customer support response.
        """

        response = ask_gemini(prompt)

        return {
            "response": response
        }

    context = search_docs(request.message)

    prompt = f"""
    You are a professional customer support agent.

    Use the following company policy information to answer the customer.

    Context:
    {context}

    Customer Question:
    {request.message}

    Provide a helpful and concise answer.
    """

    response = ask_gemini(prompt)

    return {
        "response": response
    }