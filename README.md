Limiter.py
=======

A decorator for limiting the call-rate of a function.
This is achieved by returning None instead of calling the function when it is called beyond a given threshold.

Usage
-------
The usage is easy:
```python
from limiter import *

@calls_per_sec(calls=1, seconds=1) # These are the default values
def foo():
  ...
  
@calls_per_sec(1) # One call per second
def foo():
  ...
```
This limits the ```foo()``` function to one call every second starting from the first function call.

Limiter also works with fractions of seconds:
```python
from limiter import *

@calls_per_sec(calls=5, seconds=0.25)
def foo():
  ...
```
This limits the ```foo()``` function to ten calls every quarter second.

Note that ```@calls_per_sec(5, 0.25)``` is **not** the same as ```@calls_per_sec(20, 1)```.

Consider the case when a function is called 20 times in 0.5 seconds:
- If we use ```@calls_per_sec(5, 0.25)```, we drop 10 function calls.
- If we use ```@calls_per_sec(20, 1)```, we drop none of the function calls, but every subsequent call for the next 0.5 seconds will be dropped.

This is because the call allowance is reset every X seconds.
