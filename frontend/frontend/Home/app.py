from flask import Flask, request, jsonify
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model.eval()  # Set the model to evaluation mode
model.to('cuda' if torch.cuda.is_available() else 'cpu')  # Move model to GPU if available

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/generate-slogan', methods=['GET', 'POST'])
def generate_slogan():
    if request.method == 'POST':
        # Process form data if POST request comes from form submission
        company_name = request.form.get('companyName')
        description = request.form.get('description')
    else:
        # Process JSON data if it's a POST request with JSON
        if request.is_json:
            data = request.get_json()
            company_name = data.get('companyName')
            description = data.get('description')
        else:
            return generate_slogan_form()

    if not company_name or not description:
        return jsonify({'error': 'Missing or empty companyName or description'}), 400

    try:
        prompt = f"{company_name}, {description}"
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to('cuda' if torch.cuda.is_available() else 'cpu')
        output_ids = model.generate(input_ids, max_length=70, num_return_sequences=1, no_repeat_ngram_size=2)[0]
        slogan = tokenizer.decode(output_ids, skip_special_tokens=True)
        return jsonify(slogan=slogan)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_slogan_form():
    # Provide a simple form for testing
    return '''
    <html>
        <body>
            <form action="/generate-slogan" method="post">
                Company Name:<br>
                <input type="text" name="companyName"><br>
                Description:<br>
                <input type="text" name="description"><br>
                <input type="submit" value="Generate Slogan">
            </form>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
