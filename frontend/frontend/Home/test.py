import unittest
from app import app  # Import your Flask app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Set up a test client
        self.app.testing = True       # Enable testing mode

    def test_generate_slogan(self):
        # Define the payload
        payload = {
            "companyName": "Jenish Coffee",
            "description": "the comany produce fresh coffee which make user life fresh morning start"
        }
        # Send a POST request
        response = self.app.post('/generate-slogan', json=payload)
        self.assertEqual(response.status_code, 200)  # Assert the status code
        response_json = response.get_json()  # Get the JSON response
        self.assertIn('slogan', response_json)  # Check if 'slogan' key exists in the response
        print("Generated Slogan:", response_json['slogan'])  # Print the slogan

if __name__ == '__main__':
    unittest.main()
