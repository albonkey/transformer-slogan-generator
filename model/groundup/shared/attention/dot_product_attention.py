import trax
from trax.fastmath import numpy as jnp

def dot_product_attention(query, key, value, mask=None):
  """Dot product attention.
  Args:
      query (jax.interpreters.xla.DeviceArray): array of query representations with shape (L_q by d)
      key (jax.interpreters.xla.DeviceArray): array of key representations with shape (L_k by d)
      value (jax.interpreters.xla.DeviceArray): array of value representations with shape (L_k by d) where L_v = L_k
      mask (jax.interpreters.xla.DeviceArray): mask that filters out unwanted tokens. '0' values indicate padding.
  """
  
  assert query.shape[-1] == key.shape[-1] == value.shape[-1], "Embedding dimensions of q, k, v aren't all the same"

  # Q * K^T
  dot_product = jnp.matmul(query, jnp.swapaxes(key, -1, -2))

  # Scale dot_product (dot product / sqrt(dk)
  depth = query.shape[-1]
  dot_product_scaled = dot_product / jnp.sqrt(depth)
  
  if mask is not None:
      dot_product_scaled = jnp.where(mask, dot_product_scaled, jnp.full_like(dot_product_scaled, -1e9))
  
  # Softmax formula implementation
  logsumexp = trax.fastmath.logsumexp(dot_product_scaled, axis=-1, keepdims=True)

  # Take exponential of dots minus logsumexp to get softmax
  dot_with_softmax = jnp.exp(dot_product_scaled - logsumexp)

  # Multiply dots by value to get self-attention
  attention = jnp.matmul(dot_with_softmax, value)
  
  return attention

def dot_product_self_attention(q, k, v):
  """ Dot product self attention.
  Args:
      q (jax.interpreters.xla.DeviceArray): queries.
      k (jax.interpreters.xla.DeviceArray): keys.
      v (jax.interpreters.xla.DeviceArray): values.
  Returns:
      jax.interpreters.xla.DeviceArray: masked dot product self attention tensor.
  """
  mask_size = q.shape[1]

  # Creates a matrix with ones below the diagonal and 0s above.
  mask = jnp.tril(jnp.ones((1, mask_size, mask_size), dtype=jnp.bool_), k=0)
  
  return dot_product_attention(q, k, v, mask)
