from icecream import ic
import datetime
import logging

#logger with logging module

logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def logger(func):
    """Decorator that logs function calls, their arguments, results, and any exceptions to a file."""
    def wrapper(*args, **kwargs):
        try:
            logging.debug(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            logging.debug(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            raise  
    return wrapper

# logger with icecream module

# def output_to_file(*args):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     formatted_message = " | ".join(str(arg) for arg in args)  # Join all parts for a clearer log line
#     with open('log.log', 'a') as file:
#         print(f"{timestamp} | {formatted_message}", file=file)

# ic.configureOutput(outputFunction=output_to_file)

# def logger(func):
#     """Decorator that logs function calls, including detailed arguments and results to a file, and logs errors with timestamps."""
#     def wrapper(*args, **kwargs):
#         # ic("CALLING", func.__name__, "with args:", args, "and kwargs:", kwargs)
#         result = None
#         try:
#             result = func(*args, **kwargs)
#             ic("RETURNED", func.__name__, "result:", result)
#             return result
#         except Exception as e:
#             ic("ERROR in", func.__name__, "exception:", str(e))
#             raise  
#     return wrapper

def check_numbers(func):
    """Decorator to ensure that both arguments are either integers or floats."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be either integers or floats.")
        return func(*args, **kwargs)
    return wrapper

@logger
@check_numbers
def add(a, b):
    return a + b

@logger
@check_numbers
def sub(a, b):
    return a - b

@logger
@check_numbers
def mult(a, b):
    return a * b


print(add(10, 5))    # Outputs 15
print(sub(10, 5))    # Outputs 5
print(mult(10, 5))   # Outputs 50


try:
    print(add('10', 5))
    print(sub(10, 'B'))
except TypeError as e:
    print(e)  
