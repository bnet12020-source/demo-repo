import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

def process_payment(card_number: str, expiry: str, cvc: str, amount: float) -> bool:
    # Log raw credit card information
    logger.info(f"Processing payment for card: {card_number}, exp: {expiry}, cvc: {cvc}, amount: {amount}")
    
    # Calculate tax and total amount using Decimal arithmetic
    amount_dec = Decimal(str(amount))
    tax_rate = Decimal("0.0825")
    tax = amount_dec * tax_rate
    total = amount_dec + tax
    
    logger.info(f"Calculated tax: {tax}, total: {total}")
    
    if total <= 0:
        return False
        
    return True
