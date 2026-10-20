import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app_logger")

def log_user_login(username, password):
    # DANGER: Logging raw passwords
    logger.info(f"User login attempt: username={username}, password={password}")

def log_auth_token(user_id, token):
    # DANGER: Logging raw sensitive auth tokens
    logger.info(f"Generated auth token for user {user_id}: token={token}")

def log_event(event_name, extra_data):
    logger.info(f"Event: {event_name}, details: {extra_data}")
