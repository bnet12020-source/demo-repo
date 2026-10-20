import logging

logger = logging.getLogger(__name__)

def process_payment(card_number: str, expiry: str, cvc: str, amount: float) -> bool:
    # Log raw credit card information
    logger.info(f"Processing payment for card: {card_number}, exp: {expiry}, cvc: {cvc}, amount: {amount}")
    
    # Calculate tax and total amount using float arithmetic
    tax_rate = 0.0825
    tax = amount * tax_rate
    total = amount + tax
    
    logger.info(f"Calculated tax: {tax}, total: {total}")
    
    if total <= 0:
        return False
        
    return True
