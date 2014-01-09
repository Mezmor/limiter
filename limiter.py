"""
A decorator for limiting the call-rate of a function
Lucas 'Mezmor' Pfister

@param  calls    : number of calls allowed per unit time. Default = 1.
        seconds  : number of seconds per unit time. Default = 1.

Example usages:
    from limiter import *
    
    @calls_per_sec(1, 10) # foo() allowed 1 call every 10 seconds
    def foo():
        ...
        
    @calls_per_sec(10, 0) # bar() allowed 10 calls during app lifetime
    def bar():
        ...

"""
from datetime import datetime, timedelta

def calls_per_sec(calls=1, seconds=1):
    def limiter(function):
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, 'last_called'):
                wrapper.last_called = datetime.now()
            # Are we calling it within X seconds of the last successful call?
            # If so, remove from our allowance
            if (datetime.now() - wrapper.last_called) <= timedelta(seconds = seconds):
                wrapper.calls_allowed -= 1
                # We don't have any calls left, abort!
                if wrapper.calls_allowed < 0:                                          
                    return None
            wrapper.last_called = datetime.now()
            return function(*args, **kwargs)
        wrapper.calls_allowed = calls
        return wrapper
    return limiter