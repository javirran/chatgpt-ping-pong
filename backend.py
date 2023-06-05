from flask import Flask, request, jsonify
from flask_cors import cross_origin
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define the endpoint for receiving user messages
@app.route('/follow-ball', methods=['POST'])
@cross_origin()
def follow_ball():
    # Get user input from the request
    user_input = request.json['input']
    print('*user_input*, ' + user_input)

    # Call the ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=50,  # Adjust the max tokens as per your needs
        temperature=0.6,  # Adjust the temperature as per your needs
        n=1,
        stop=None,
        timeout=15
    )

    # Extract the generated message from the API response
    message = response.choices[0].text.strip()

    # Prepare the response to be sent back to the frontend
    response_data = {
        'message': message
    }

    response = jsonify(response_data)

    return response

if __name__ == '__main__':
    app.run()
