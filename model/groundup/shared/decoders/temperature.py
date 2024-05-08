import numpy as np

def softmax(logits, temperature=1.0):
    """Apply softmax with temperature to logits. Adjusts the temperature to ensure 
    a balance between randomness and determinism if set to zero."""
    if temperature == 0.0:
        temperature = 0.8  # Default to standard softmax if temperature is zero
    logits = np.array(logits) / temperature
    exps = np.exp(logits - np.max(logits))  # Numerical stability
    return exps / np.sum(exps)

def decode_temperature(logits, temperature=0.8):
    """Decode the most probable symbol from logits after applying temperature.
    A moderate temperature is used by default to promote creativity."""
    probabilities = softmax(logits, temperature)
    # Get the index of the highest probability which corresponds to the most likely symbol
    most_probable_index = np.argmax(probabilities)
    return most_probable_index

def next_symbol_temperature(logits, temperature=0.8):
    """Sample the next symbol from logits using temperature-scaled probabilities.
    The default moderate temperature enhances creativity while maintaining relevance."""
    probabilities = softmax(logits, temperature)
    # Randomly sample an index based on the softmax probabilities
    sampled_index = np.random.choice(len(logits), p=probabilities)
    return sampled_index