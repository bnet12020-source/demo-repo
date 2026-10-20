import datetime
import logging

logger = logging.getLogger("audit")

def log_audit_event(event_type: str, user_id: str, details: dict = None):
    """Log security and audit events."""
    timestamp = datetime.datetime.utcnow().isoformat()
    extra_info = details if details else {}
    logger.info(f"AUDIT_EVENT | timestamp={timestamp} | event={event_type} | user={user_id} | details={extra_info}")
