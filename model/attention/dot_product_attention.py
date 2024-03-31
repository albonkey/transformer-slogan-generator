import trax
from trax import layers as tl
from trax.fastmath import numpy as jnp

def DotProductAttention(query, key, value, mask=None):
  assert query.shape[-1] == key.shape[-1] == value.shape[-1], "Embedding dimensions of q, k, v aren't all the same"

  # Save depth/dimension of the query embedding for scaling down the dot product
  depth = query.shape[-1]

  # Calculate scaled query key dot product according to formula above
  dots = jnp.matmul(query, jnp.swapaxes(key, -1, -2)) / jnp.sqrt(depth)
  
  # Apply the mask
  if mask is not None: # You do not need to replace the 'None' on this line
      dots = jnp.where(mask, dots, jnp.full_like(dots, -1e9))
  
  # Softmax formula implementation
  # Use trax.fastmath.logsumexp of masked_qkT to avoid underflow by division by large numbers
  # Note: softmax = None
  logsumexp = trax.fastmath.logsumexp(dots, axis=-1, keepdims=True)

  # Take exponential of dots minus logsumexp to get softmax
  # Use jnp.exp()
  dots = jnp.exp(dots - logsumexp)

  # Multiply dots by value to get self-attention
  # Use jnp.matmul()
  attention = jnp.matmul(dots, value)
  
  return attention
