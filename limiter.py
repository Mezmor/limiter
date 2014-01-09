"""
A decorator for limiting the call-rate of a function
Lucas 'Mezmor' Pfister
"""
from datetime import datetime, timedelta

def calls_per_sec(calls=1, seconds=1):
    def limiter(function):
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, 'last_updated'):
                wrapper.last_updated = datetime.now()
            # Are we calling it within X seconds of the last successful call?
            # If so, remove from our allowance
            if (datetime.now() - wrapper.last_updated) <= timedelta(seconds = seconds):
                wrapper.calls_allowed -= 1
                # We don't have any calls left, abort!
                if wrapper.calls_allowed < 0:
                    return None
            else:
                wrapper.calls_allowed = calls
                wrapper.last_updated = datetime.now()
            return function(*args, **kwargs)
        wrapper.calls_allowed = calls
        return wrapper
    return limiter
