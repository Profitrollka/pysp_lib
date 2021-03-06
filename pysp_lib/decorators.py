from datetime import datetime, timedelta
from functools import wraps

def time_counter(func):

    """Decorator for calculating the time of the function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(f'Start function {func.__name__}: {start}')
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'End function {func.__name__} {end}')
        print(f'Total time for function {func.__name__}: {str(end-start)[0]} hours {str(end-start)[2:4]} minutes {str(end-start)[5:7]} seconds')
        return result
    return wrapper