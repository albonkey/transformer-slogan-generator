import trax
from trax import layers as tl
from trax.fastmath import numpy as jnp

# Implement Decoder Block
def DecoderBlock(model_depth, ff_depth, ff_activation, nr_heads, dropout, mode):
  pass

# Implement TransformerLM
def TransformerLM(
  vocab_size=33300,
  model_depth=512,
  ff_depth=2048,
  ff_activation=tl.Relu,
  nr_layers=6,
  nr_heads=8,
  dropout=0.1,
  max_length=4096,
  mode='train',
):
  positional_encoder = [
    tl.Embedding(vocab_size, model_depth),
    tl.Dropout(rate=dropout, mode=mode),
    tl.PositionalEncoding(max_length=max_length, mode=mode),
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