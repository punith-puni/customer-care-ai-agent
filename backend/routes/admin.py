from fastapi import APIRouter
from sqlalchemy import text

from database.postgres import SessionLocal

router = APIRouter()

@router.get("/admin/stats")
def admin_stats():

    db = SessionLocal()

    total_orders = db.execute(
        text("SELECT COUNT(*) FROM orders")
    ).scalar()

    total_tickets = db.execute(
        text("SELECT COUNT(*) FROM tickets")
    ).scalar()

    open_tickets = db.execute(
        text("""
            SELECT COUNT(*)
            FROM tickets
            WHERE status = 'OPEN'
        """)
    ).scalar()

    escalated_tickets = db.execute(
        text("""
            SELECT COUNT(*)
            FROM tickets
            WHERE priority = 'HIGH'
        """)
    ).scalar()

    db.close()

    return {
        "total_orders": total_orders,
        "total_tickets": total_tickets,
        "open_tickets": open_tickets,
        "escalated_tickets": escalated_tickets
    }

@router.get("/admin/tickets")
def get_tickets():
    db = SessionLocal()

    tickets = db.execute(
        text("""
            SELECT id,
                   customer_message,
                   priority,
                   status
            FROM tickets
            ORDER BY id DESC
        """)
    ).mappings().all()

    db.close()

    return tickets