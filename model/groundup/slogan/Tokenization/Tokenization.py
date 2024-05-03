import pandas as pd
import csv
from transformers import GPT2Tokenizer
from sklearn.model_selection import train_test_split

# Define the model name
model_name = "distilgpt2"

# Define special tokens directly as strings
pad_token = "<pad>"
company_token = "<company>"
description_token = "<description>"
slogan_token = "<slogan>"

# Initialize the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(model_name, pad_token=pad_token)

# Add these special tokens to the vocabulary and resize model's embeddings:
special_tokens_dict = {
    'pad_token': pad_token,
    'additional_special_tokens': [company_token, description_token, slogan_token]
}
tokenizer.add_special_tokens(special_tokens_dict)

# Specify the CSV file path
csv_file_path = 'groundup/slogan/data/kaggle_valid_cleansed.csv'

# Read the CSV file
data = pd.read_csv(csv_file_path)

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

def tokenize_text(text):
    """Tokenize a text."""
    return tokenizer.tokenize(text, add_prefix_space=True)

def convert_tokens_to_ids(tokens):
    """Convert a list of tokens to their corresponding IDs."""
    return tokenizer.convert_tokens_to_ids(tokens)

def decode_and_skip_special_tokens(token_ids):
    """Decode token IDs to text, skipping the decoding of special tokens."""
    return tokenizer.decode(token_ids, skip_special_tokens=True)

# Function to process a chunk of data and save to a file
def process_and_save_chunk(chunk, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        field = ['company', 'description', 'slogan']
        writer.writerow(field)

        for index, row in chunk.iterrows():
            # Convert the texts to strings to ensure compatibility with tokenizer
            company_text = str(row['company'])
            description_text = str(row['description'])
            slogan_text = str(row['slogan'])

            # Tokenize the texts
            company_tokens = tokenizer.tokenize(company_text, add_prefix_space=True)
            description_tokens = tokenizer.tokenize(description_text, add_prefix_space=True)
            slogan_tokens = tokenizer.tokenize(slogan_text, add_prefix_space=True)

            writer.writerow([' '.join(company_tokens), ' '.join(description_tokens), ' '.join(slogan_tokens)])

# Process and save the training and testing data
print("Processing and saving training data...")
process_and_save_chunk(train_data, 'groundup/slogan/data/train_data_tokens.csv')

print("Processing and saving testing data...")
process_and_save_chunk(test_data, 'groundup/slogan/data/test_data_tokens.csv')
