import logging

logger = logging.getLogger('wallet')


def log_errors(coro):
    """Decorator function that logs errors in Python async/await coroutines."""

    async def wrapper(*args, **kwargs):
        try:
            return await coro(*args, **kwargs)
        except Exception as e:
            logger.error('Error in coroutine: %s', e, exc_info=True)
            raise  # Re-raise to ensure it propagates

    return wrapper
