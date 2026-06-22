from fastapi import APIRouter
from sqlalchemy import text

from database.postgres import SessionLocal

router = APIRouter()

@router.get("/order/{order_id}")
def get_order(order_id: int):

    db = SessionLocal()

    query = text(
        """
        SELECT *
        FROM orders
        WHERE id = :order_id
        """
    )

    result = db.execute(
        query,
        {"order_id": order_id}
    ).fetchone()

    db.close()

    if not result:
        return {
            "error": "Order not found"
        }

    return {
        "id": result.id,
        "customer_name": result.customer_name,
        "status": result.status,
        "tracking_number": result.tracking_number,
        "delivery_date": str(result.delivery_date)
    }