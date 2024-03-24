import trax
from trax.fastmath import numpy as jnp

import textwrap
wrapper = textwrap.TextWrapper(width=70)

import time

def measure_time(func):
  """Decorator to measure the execution time of a function."""
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
    return result
  return wrapper


def tokenize(input, EOS=1, vocab_dir='vocab_dir/'):
  pass

def detokenize(integers, vocab_dir='vocab_dir/'):
  pass

def create_tensor(t):
  """Create tensor from list of lists"""
  return jnp.array(t)


def display_tensor(t, name):
  """Display shape and tensor"""
  print(f'{name} shape: {t.shape}\n')
  print(f'{t}\n')