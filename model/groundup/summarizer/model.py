import sys
import os
from trax import layers as tl

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'shared'))
from attention.causal_attention import CausalAttention

# Implement Decoder Block
def DecoderBlock(model_depth, ff_depth, ff_activation, nr_heads, dropout, mode):
    """Returns a list of layers that implements a Transformer decoder block.

    The input is an activation tensor.

    Args:
        d_model (int):  depth of embedding.
        d_ff (int): depth of feed-forward layer.
        n_heads (int): number of attention heads.
        dropout (float): dropout rate (how much to drop out).
        mode (str): 'train' or 'eval'.
        ff_activation (function): the non-linearity in feed-forward layer.

    Returns:
        list: list of trax.layers.combinators.Serial that maps an activation tensor to an activation tensor.
    """

    # Create masked multi-head attention block using CausalAttention function
    causal_attention = CausalAttention(
        model_depth,
        n_heads=nr_heads,
        mode=mode
    )

    # Create feed-forward block (list) with two dense layers with dropout and input normalized
    feed_forward = [
        # Normalize layer inputs
        tl.LayerNorm(),
        # Add first feed forward (dense) layer (don't forget to set the correct value for n_units)
        tl.Dense(ff_depth),
        # Add activation function passed in as a parameter (you need to call it!)
        ff_activation(),  # Generally ReLU
        # Add dropout with rate and mode specified (i.e., don't use dropout during evaluation)
        tl.Dropout(rate=dropout, mode=mode),
        # Add second feed forward layer (don't forget to set the correct value for n_units)
        tl.Dense(model_depth),
        # Add dropout with rate and mode specified (i.e., don't use dropout during evaluation)
        tl.Dropout(rate=dropout, mode=mode)
    ]

    # Add list of two Residual blocks: the attention with normalization and dropout and feed-forward blocks
    return [
        tl.Residual(
            # Normalize layer input
            tl.LayerNorm(),
            # Add causal attention block previously defined (without parentheses)
            causal_attention,
            # Add dropout with rate and mode specified
            tl.Dropout(rate=dropout, mode=mode)
        ),
        tl.Residual(
            # Add feed forward block (without parentheses)
            feed_forward
        ),
    ]

# Implement TransformerLM
def TransformerLM(
  vocab_size=33300,
  model_depth=256,
  ff_depth=512,
  ff_activation=tl.Relu,
  nr_layers=4,
  nr_heads=4,
  dropout=0.1,
  max_length=4096,
  mode='train',
):
  positional_encoder = [
    tl.Embedding(vocab_size, model_depth),
    tl.Dropout(rate=dropout, mode=mode),
    tl.PositionalEncoding(max_len=max_length, mode=mode),
  ]
  decoder_blocks = [
    DecoderBlock(model_depth, ff_depth, ff_activation, nr_heads, dropout, mode) for _ in range(nr_layers)
  ]

  return tl.Serial(
    tl.ShiftRight(mode=mode),
    positional_encoder,
    decoder_blocks,
    tl.LayerNorm(),
    tl.Dense(vocab_size),
    tl.LogSoftmax()
  )