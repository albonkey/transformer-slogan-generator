import numpy as np

def decode_sampling(input_sentence, model, EOS, PAD, tokenize, detokenize, verbose=True):
  """
  Args:
    input_sentence (string): a sentence or article.
    model (trax.layers.combinators.Serial): Transformer model.
    EOS (int): End-of-sentence token.
    PAD (int): Padding token.
    tokenize (function): Tokenization function.
    detokenize (function): Detokenization function.

  Returns:
    string: summary of the input.
  """
  
  cur_output_tokens = tokenize(input_sentence) + [PAD]    
  generated_output = [] 
  cur_output = 0 
  
  while cur_output != EOS:
    # Get next symbol
    cur_output = None 

    cur_output = next_symbol_sampling(cur_output_tokens, model)

    # Append next symbol to original sentence
    cur_output_tokens.append(cur_output)
    # Append next symbol to generated sentence
    generated_output.append(cur_output)
    
    if verbose:
        print(detokenize(generated_output))
  
      
  return detokenize(generated_output)

def next_symbol_sampling(cur_output_tokens, model):
  """
  Args:
      cur_output_tokens (list): tokenized sentence with EOS and PAD tokens at the end.
      model (trax.layers.combinators.Serial): The transformer model.

  Returns:
      int: tokenized symbol.
  """

  token_length = len(cur_output_tokens)
  padded_length = 2 ** int(np.ceil(np.log2(token_length + 1)))

  padded = cur_output_tokens + [0] * (padded_length - token_length)
  padded_with_batch = np.array(padded)[None, :]

  output, _ = model((padded_with_batch, padded_with_batch))
  log_probs = output[0, token_length, :]
  
  probs = np.exp(log_probs) / np.sum(np.exp(log_probs))
  
  sample_next_symbol = int(np.random.choice(len(probs), p=probs))
  
  return sample_next_symbol