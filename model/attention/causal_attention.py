import trax
from trax import layers as tl
from trax.fastmath import numpy as jnp

def CausalAttention(d_feature, n_heads, mode='train'):
    """Transformer-style multi-headed causal attention.

    Args:
        d_feature (int):  dimensionality of feature embedding.
        n_heads (int): number of attention heads.
        mode (str): 'train' or 'eval'.

    Returns:
        trax.layers.combinators.Serial: Multi-headed self-attention model.
    """
    def compute_attention_heads(x):
        """ Compute the attention heads.
        Args:
            x (jax.interpreters.xla.DeviceArray): tensor with shape (n_batch, seqlen, n_heads X d_head).
        Returns:
            jax.interpreters.xla.DeviceArray: reshaped tensor with shape (n_batch X n_heads, seqlen, d_head).
        """
        
        # Size of the x's batch dimension
        batch_size = x.shape[0]
        # Length of the sequence
        # Should be size of x's first dimension without counting the batch dim
        seqlen = x.shape[1]
        # Reshape x using jnp.reshape()
        # n_batch, seqlen, n_heads*d_head -> n_batch, seqlen, n_heads, d_head
        x = jnp.reshape(x, (batch_size, seqlen, n_heads, d_head))
        # Transpose x using jnp.transpose()
        # n_batch, seqlen, n_heads, d_head -> n_batch, n_heads, seqlen, d_head
        # Note that the values within the tuple are the indexes of the dimensions of x and you must rearrange them
        x = jnp.transpose(x, (0, 2, 1, 3))
        # Reshape x using jnp.reshape()
        # n_batch, n_heads, seqlen, d_head -> n_batch*n_heads, seqlen, d_head
        x = jnp.reshape(x, (-1, seqlen, d_head))
        
        return x
    
    def dot_product_self_attention(q, k, v):
        """ Masked dot product self attention.
        Args:
            q (jax.interpreters.xla.DeviceArray): queries.
            k (jax.interpreters.xla.DeviceArray): keys.
            v (jax.interpreters.xla.DeviceArray): values.
        Returns:
            jax.interpreters.xla.DeviceArray: masked dot product self attention tensor.
        """
        mask_size = q.shape[1]

        # Creates a matrix with ones below the diagonal and 0s above. It should have shape (1, mask_size, mask_size)
        # Notice that 1's and 0's get casted to True/False by setting dtype to jnp.bool_
        # Use jnp.tril() - Lower triangle of an array and jnp.ones()
        mask = jnp.tril(jnp.ones((1, mask_size, mask_size), dtype=jnp.bool_), k=0)
        
        return DotProductAttention(q, k, v, mask)

    def compute_attention_output(x):
        """ Compute the attention output.
        Args:
            x (jax.interpreters.xla.DeviceArray): tensor with shape (n_batch X n_heads, seqlen, d_head).
        Returns:
            jax.interpreters.xla.DeviceArray: reshaped tensor with shape (n_batch, seqlen, n_heads X d_head).
        """
        
        # Length of the sequence
        # Should be size of x's first dimension without counting the batch dim
        seqlen = x.shape[1]
        # Reshape x using jnp.reshape() to shape (n_batch, n_heads, seqlen, d_head)
        x = jnp.reshape(x, (-1, n_heads, seqlen, d_head))
        # Transpose x using jnp.transpose() to shape (n_batch, seqlen, n_heads, d_head)
        x = jnp.transpose(x, (0, 2, 1, 3))
        
        # Reshape to allow to concatenate the heads
        return jnp.reshape(x, (-1, seqlen, n_heads * d_head))
    
    assert d_feature % n_heads == 0
    d_head = d_feature // n_heads

    ComputeAttentionHeads = tl.Fn('AttnHeads', compute_attention_heads, n_out=1)
        
    return tl.Serial(
        tl.Branch( # creates three towers for one input, takes activations and creates queries keys and values
            [tl.Dense(d_feature), ComputeAttentionHeads], # queries
            [tl.Dense(d_feature), ComputeAttentionHeads], # keys
            [tl.Dense(d_feature), ComputeAttentionHeads], # values
        ),
        
        tl.Fn('DotProductAttn', dot_product_self_attention, n_out=1), # takes QKV
        tl.Fn('AttnOutput', compute_attention_output, n_out=1), # to allow for parallel
        tl.Dense(d_feature)
    )
