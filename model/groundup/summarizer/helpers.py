import trax
import textwrap
wrapper = textwrap.TextWrapper(width=70)

def tokenize(input, EOS=1, vocab_dir='groundup/summarizer/vocab_dir/'):
  inputs = next(trax.data.tokenize(iter([input]),
                                    vocab_dir=vocab_dir,
                                    vocab_file='summarize32k.subword.subwords'
                                    ))
  return list(inputs) + [EOS]

def detokenize(integers, vocab_dir='groundup/summarizer/vocab_dir/'):
  """List of ints to str"""
  
  wrapper = textwrap.TextWrapper(width=70)
  s = trax.data.detokenize(integers,
                            vocab_dir=vocab_dir,
                            vocab_file='summarize32k.subword.subwords')
  
  return wrapper.fill(s)