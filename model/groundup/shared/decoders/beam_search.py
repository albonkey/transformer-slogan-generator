import numpy as np

def decode_beam_search(input_sentence, model, beam_width, tokenize, detokenize, verbose=False):
  """Beam search decoding function.

  Args:
      input_sentence (string): A sentence or article.
      model (trax.layers.combinators.Serial): Transformer model.
      beam_width (int): Number of candidate sequences to consider.
      tokenize (function): Tokenization function.
      detokenize (function): Detokenization function.
      vocab_dir (string): Directory path for vocabulary.
      verbose (bool): Flag to print intermediate decoding steps.

  Returns:
      string: Summary of the input.
  """

  cur_output_tokens = tokenize(input_sentence) + [0]
  generated_outputs = [[]] * beam_width
  EOS = 1

  while len(generated_outputs[0]) == 0 or generated_outputs[0][-1] != EOS:
      beam_candidates = []

      for output_idx in range(beam_width):
          # Get next symbols for each candidate sequence
          cur_output = generated_outputs[output_idx]
          cur_output_tokens_temp = cur_output_tokens + cur_output

          # Use beam search decoder for next symbol selection
          next_symbols = next_symbols_beam_search(cur_output_tokens_temp, model, beam_width)

          for symbol_idx, next_symbol in enumerate(next_symbols):
              # Add the next symbol to candidate sequence
              candidate_sequence = cur_output + [next_symbol]
              beam_candidates.append((output_idx, candidate_sequence))

      # Update the generated outputs
      generated_outputs = [generated_outputs[output_idx] + [candidate_sequence[-1]] for output_idx, candidate_sequence in beam_candidates]

      if verbose:
          for idx, output in enumerate(generated_outputs):
              print(detokenize(output))

  return detokenize(generated_outputs[0])

def next_symbols_beam_search(current_tokens, model, beam_width):
  """Beam search decoding function for the next symbol.

  Args:
      cur_output_tokens (list): Tokenized sentence with EOS and PAD tokens at the end.
      model (trax.layers.combinators.Serial): Transformer model.
      beam_width (int): Number of candidate symbols to consider.

  Returns:
      list: Candidate symbols.
  """
  token_length = len(current_tokens)
  padded_length = 2 ** int(np.ceil(np.log2(token_length + 1)))
  padded = current_tokens + [0] * (padded_length - token_length)
  padded_with_batch = np.array(padded)[None, :]

  output, _ = model((padded_with_batch, padded_with_batch))
  log_probs = output[0, token_length, :]

  # Convert log probabilities to probabilities using softmax
  probs = np.exp(log_probs) / np.sum(np.exp(log_probs))

  # Select the top-k candidate symbols based on probabilities
  topk_symbols = np.argsort(probs)[-beam_width:][::-1]

  return topk_symbols