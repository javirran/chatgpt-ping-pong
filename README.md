# Pre-requisites

### Install Flask and the OpenAI library (openai) before running the server application:

- `pip install flask openai flask-cors`

### Run the server

- `python backend.py`

### Post request

- `curl -d '{"input":"some test prompt"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/follow-ball` 

### Run ping pong application

- Open pingpong.html in your browsers
