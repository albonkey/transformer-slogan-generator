from Tokenization.Tokenization import decode_and_skip_special_tokens, convert_tokens_to_ids, tokenize_text

def tokenize(input, EOS=50260):
    """List of str to ints"""
    tokens = tokenize_text(input)
    inputs = convert_tokens_to_ids(tokens)
    return list(inputs) + [EOS]

def detokenize(integers):
    """List of ints to str"""
    return decode_and_skip_special_tokens(integers)
