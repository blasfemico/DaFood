from fastapi import APIRouter, HTTPException, Depends
from ...services.payment_services import PaymentService

router = APIRouter()
payment_service = PaymentService()

@router.post("/create_payment")
def create_payment(item_title: str, item_quantity: int, item_price: float):
    try:
        payment_url = payment_service.create_preference(item_title, item_quantity, item_price)
        return {"payment_url": payment_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/webhook")
def webhook(payment_data: dict):
    result = payment_service.process_payment_notification(payment_data)
    return {"message": result}
