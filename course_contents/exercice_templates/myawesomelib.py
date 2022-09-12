

import time
def timed(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        print(f"the {fn.__name__} has taken {time.time() - start_time}s")
        return result
    return wrapper

def logged(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print("the result has been saved")
        return result
    return wrapper

def debug(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"the function {fn.__name__} with inputs {args} {kwargs} has returned {result}")
        return result
    return wrapper