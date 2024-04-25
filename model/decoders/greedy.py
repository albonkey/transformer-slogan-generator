from Tokenization.Tokenization import tokenize_text
import numpy as np
from helpers import tokenize, detokenize, measure_time

def decode_greedy(input_sentence, model, tokenize=tokenize, detokenize=detokenize, verbose=True):
    """Decode function.

    Args:
        input_sentence (string): a sentence or article.
        model (trax.layers.combinators.Serial): Transformer model.

    Returns:
        string: summary of the input.
    """
    
    # Use tokenize()
    cur_output_tokens = tokenize(input_sentence) + [50257]  
    print(cur_output_tokens) 
    generated_output = [] 
    cur_output = 0 
    EOS = 50260
    
    while cur_output != EOS:
        # Get next symbol
        cur_output = None 
        
        cur_output = next_symbol_greedy(cur_output_tokens, model)

        # Append next symbol to original sentence
        cur_output_tokens.append(cur_output)
        # Append next symbol to generated sentence
        generated_output.append(cur_output)
        
        if verbose:
            print(generated_output)
            print(detokenize(generated_output))
    
        
    return detokenize(generated_output)

def next_symbol_greedy(cur_output_tokens, model):
  """Returns the next symbol for a given sentence.

  Args:
      cur_output_tokens (list): tokenized sentence with EOS and PAD tokens at the end.
      model (trax.layers.combinators.Serial): The transformer model.

  Returns:
      int: tokenized symbol.
  """
  
  # current output tokens length
  token_length = len(cur_output_tokens)
  # calculate the minimum power of 2 big enough to store token_length
  # add 1 to token_length so np.log2() doesn't receive 0 when token_length is 0
  padded_length = 2**int(np.ceil(np.log2(token_length + 1)))

  # Fill cur_output_tokens with 0's until it reaches padded_length
  padded = cur_output_tokens + [0] * (padded_length - token_length)
  padded_with_batch = np.array(padded)[None, :] # Don't replace this None! This is a way of setting the batch dim

  # model expects a tuple containing two padded tensors (with batch)
  output, _ = model((padded_with_batch, padded_with_batch)) 
  log_probs = output[0, token_length, :]
  
  return int(np.argmax(log_probs))
