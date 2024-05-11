import numpy as np

def decode_greedy(input_sentence, model, EOS, PAD, tokenize, detokenize, verbose=True):
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
    
    cur_output_tokens = tokenize(input_sentence, EOS) + [PAD]  
    generated_output = [] 
    cur_output = 0 
    
    while cur_output != EOS:
        cur_output = None 
        
        cur_output = next_symbol_greedy(cur_output_tokens, model)
        cur_output_tokens.append(cur_output)

        generated_output.append(cur_output)
        
        if verbose:
            print(generated_output)
            print(detokenize(generated_output))
    
        
    return detokenize(generated_output)

def next_symbol_greedy(cur_output_tokens, model):
  """
  Args:
      cur_output_tokens (list): tokenized sentence with EOS and PAD tokens at the end.
      model (trax.layers.combinators.Serial): The transformer model.

  Returns:
      int: tokenized symbol.
  """
  
  token_length = len(cur_output_tokens)
  # calculate the minimum power of 2 big enough to store token_length
  # add 1 to token_length so np.log2() doesn't receive 0 when token_length is 0
  padded_length = 2**int(np.ceil(np.log2(token_length + 1)))

  # Fill cur_output_tokens with 0's until it reaches padded_length
  padded = cur_output_tokens + [0] * (padded_length - token_length)
  padded_with_batch = np.array(padded)[None, :]

  # model expects a tuple containing two padded tensors (with batch)
  output, _ = model((padded_with_batch, padded_with_batch)) 
  log_probs = output[0, token_length, :]
  
  return int(np.argmax(log_probs))