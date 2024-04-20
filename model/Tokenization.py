import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from sklearn.model_selection import train_test_split

# Define the model name
model_name = "distilgpt2"

# Define special tokens directly as strings
pad_token = "<pad>"
company_token = "<company>"
description_token = "<description>"
slogan_token = "<slogan>"

# Initialize the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_name, pad_token=pad_token)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Add these special tokens to the vocabulary and resize model's embeddings:
special_tokens_dict = {
    'pad_token': pad_token,
    'additional_special_tokens': [company_token, description_token, slogan_token]
}
tokenizer.add_special_tokens(special_tokens_dict)
model.resize_token_embeddings(len(tokenizer))

# Specify the CSV file path
csv_file_path = 'C://Users//ssisodi3//OneDrive - Cal State LA/Desktop//pro//kaggle_valid_cleansed.csv'

# Read the CSV file
data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Function to process a chunk of data and save to a file
def process_and_save_chunk(chunk, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for index, row in chunk.iterrows():
            # Convert the texts to strings to ensure compatibility with tokenizer
            company_text = str(row['company'])
            description_text = str(row['description'])
            slogan_text = str(row['slogan'])

            # Tokenize the texts without special tokens
            company_tokens = tokenizer.tokenize(company_text, add_prefix_space=True)
            description_tokens = tokenizer.tokenize(description_text, add_prefix_space=True)
            slogan_tokens = tokenizer.tokenize(slogan_text, add_prefix_space=True)

            # Combine tokens with special tokens for clarity
            tokenized_output = [company_token] + company_tokens + \
                               [description_token] + description_tokens + \
                               [slogan_token] + slogan_tokens
            
            # Format and write the output to the file
            file.write(f" {' '.join(tokenized_output)}\n")

# Process and save the training and testing data
print("Processing and saving training data...")
process_and_save_chunk(train_data, 'train_data_tokens.txt')

print("Processing and saving testing data...")
process_and_save_chunk(test_data, 'test_data_tokens.txt')
