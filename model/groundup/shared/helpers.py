from trax.fastmath import numpy as jnp
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

def create_tensor(t):
    return jnp.array(t)


def display_tensor(t, name):
    print(f'{name} shape: {t.shape}\n')
    print(f'{t}\n')