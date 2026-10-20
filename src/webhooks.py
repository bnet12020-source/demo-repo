"""Webhook handling module."""


def handle_webhook(event_type, payload):
    """Handle incoming webhook events."""
    if event_type == "ping":
        return {"status": "ok", "message": "pong"}
    return {"status": "ignored", "message": f"Unhandled event type: {event_type}"}
