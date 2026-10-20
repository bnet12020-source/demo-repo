import time
from collections import defaultdict


class RateLimiter:
    """A simple sliding window rate limiter."""

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)

    def is_allowed(self, key: str) -> bool:
        """Check if a request under key is allowed within the rate limit window."""
        now = time.time()
        cutoff = now - self.window_seconds

        # Remove requests older than the time window
        self.requests[key] = [ts for ts in self.requests[key] if ts > cutoff]

        if len(self.requests[key]) < self.max_requests:
            self.requests[key].append(now)
            return True
        return False
