from trax import layers as tl
from trax.fastmath import numpy as jnp

from attention.dot_product_attention import dot_product_self_attention

def MaskedMultiHeadAttention(d_feature, n_heads, mode='train'):
    """
    Args:
        d_feature (int):  dimensionality of feature embedding.
        n_heads (int): number of attention heads.
        mode (str): 'train' or 'eval'.

    Returns:
        trax.layers.combinators.Serial: Multi-headed self-attention model.
    """
    def compute_attention_heads(x):
        """
        Args:
            x (jax.interpreters.xla.DeviceArray): tensor with shape (n_batch, seqlen, n_heads X d_head).
        Returns:
            jax.interpreters.xla.DeviceArray: reshaped tensor with shape (n_batch X n_heads, seqlen, d_head).
        """
        
        # Size of the x's batch dimension
        batch_size = x.shape[0]
        # Length of the sequence
        seqlen = x.shape[1]

        # n_batch, seqlen, n_heads*d_head -> n_batch, seqlen, n_heads, d_head
        x = jnp.reshape(x, (batch_size, seqlen, n_heads, d_head))

        # n_batch, seqlen, n_heads, d_head -> n_batch, n_heads, seqlen, d_head
        x = jnp.transpose(x, (0, 2, 1, 3))
  
        # n_batch, n_heads, seqlen, d_head -> n_batch*n_heads, seqlen, d_head
        x = jnp.reshape(x, (-1, seqlen, d_head))
        
        return x

    def compute_attention_output(x):
        """
        Args:
            x (jax.interpreters.xla.DeviceArray): tensor with shape (n_batch X n_heads, seqlen, d_head).
        Returns:
            jax.interpreters.xla.DeviceArray: reshaped tensor with shape (n_batch, seqlen, n_heads X d_head).
        """
        
        # Length of the sequence
        seqlen = x.shape[1]
        # Reshape to (n_batch, n_heads, seqlen, d_head)
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