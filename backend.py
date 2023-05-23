from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define the endpoint for receiving user messages
@app.route('/follow-ball', methods=['POST'])
def follow_ball():
    # Get user input from the request
    user_input = request.json['input']

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

    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
