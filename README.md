# Phone sensor server

This is the server for the phonesensory app developed for the 6G Soft project. The main function of the server is:
1. To receive a prompt sent by the phonensensor app as a http request
2. Send the prompt to ollama for processing and response generation.
3. Receive the response from ollama and print both the prompt and the response.

NOTE: To be able to send the prompt to ollama, you need to have it installed locally on your machine.

## How to run the app

### Step 1: Install Docker

You need Docker for running the phone-sensor-server and ollama in containers. If you don't have Docker installed on your computer already you can install it from here: https://docs.docker.com/engine/install/.

### Step 2: Clone the phone-sensor-server project

Clone the phone-sensor-server project from this github page onto you machine.

### Step 3: coming soon...

## Calling ollama

```
curl http://172.17.0.2:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "Why is the sky blue?",
  "stream": false
}'

```


docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama


