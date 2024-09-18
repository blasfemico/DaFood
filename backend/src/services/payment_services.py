import mercadopago
from fastapi import HTTPException
from ..config.database import MERCADOPAGO_ACCESS_TOKEN

class PaymentService:
    def __init__(self):
        self.mp = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

    def create_preference(self, item_title: str, item_quantity: int, item_price: float):
        preference_data = {
            "items": [
                {
                    "title": item_title,
                    "quantity": item_quantity,
                    "unit_price": item_price,
                }
            ],
            "payment_methods": {
                "excluded_payment_types": [{"id": "ticket"}],  # Excluir pagos en efectivo
                "installments": 1  # Limitar a una sola cuota
            },
            "payer": {
                "email": "email_del_cliente@ejemplo.com"  # Cambiar por el email del cliente
            },
            "back_urls": {
                "success": "https://ripe-carpets-return.loca.lt/success",  # URL de éxito
                "failure": "https://ripe-carpets-return.loca.lt/failure",  # URL de fallo
                "pending": "https://ripe-carpets-return.loca.lt/pending"   # URL de estado pendiente
            },
            "auto_return": "approved"
        }

        try:
            preference = self.mp.preference().create(preference_data)
            return preference["response"]["init_point"]  # URL para redirigir al cliente a MercadoPago
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def process_payment_notification(self, payment_data: dict):
        payment_status = payment_data.get("status")
        payment_id = payment_data.get("id")

        if payment_status == "approved":
            return f"Pago aprobado, ID de pago: {payment_id}"
        elif payment_status == "in_process":
            return f"Pago en proceso, ID de pago: {payment_id}"
        else:
            return f"Pago fallido o rechazado, ID de pago: {payment_id}"
