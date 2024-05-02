from flask import Flask, request, jsonify
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Set up the directory path for the BART model and tokenizer
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
model_dir = os.path.join(base_dir, 'final_bart_model')

# Load pre-trained BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained(model_dir)
tokenizer = BartTokenizer.from_pretrained(model_dir)

# Set the model to evaluation mode and move model to GPU if available
model.eval()
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/generate-slogan', methods=['POST'])
def generate_slogan():
    # Ensure the request is in JSON format
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 415

    # Extract data from the JSON request
    data = request.get_json()
    company_name = data.get('companyName')
    description = data.get('description')

    if not company_name or not description:
        return jsonify({'error': 'Missing or empty companyName or description'}), 400

    try:
        prompt = f"{company_name}, {description}"
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
        output_ids = model.generate(        
        input_ids,
        max_length=80,
        num_beams=5,
        early_stopping=True,
        do_sample=True,
        temperature=0.7,  # Ensures some creativity
        top_k=50,
        top_p=0.95)[0]
        slogan = tokenizer.decode(output_ids, skip_special_tokens=True)
        return jsonify({'slogan': slogan})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
