# Phone sensor server

This is the server for the phonesensory app developed for the 6G Soft project. The main function of the server is:
1. To receive a prompt sent by the phonensensor app as a http request.
2. Send the prompt to Ollama for processing and response generation.
3. Receive the response from Ollama and print both the prompt and the response.


## How to run the server in a development container

### Step 1: Install Docker and Visual Studio Code

You need Docker for running the phone-sensor-server and Ollama in containers. If you don't have Docker installed on your computer already you can install it from here: https://docs.docker.com/engine/install/.

VS Code can be installed frome here: https://code.visualstudio.com/download.


### Step 2: Clone the phone-sensor-server project and install extensions in VS Code

Clone the phone-sensor-server project from this github page onto you machine. 

After that open VS Code and install the Dev Containers extension.


### Step 3: Open the phone-sensor-server folder in a dev container

Open the phone-sensor-server folder in the workspace in VS Code. Then open the folder in a dev container by searching and selecting 
```
>dev container: reopen in container
```
in the command palette.


### Step 4: Run the server application

Open a terminal in VS Code and run the server by running this command in the terminal: 
```
fastapi dev main.py
```
.

If everything went well, the application is now available in the browser! In browser a page is opened in http://127.0.0.1:8000/  which just shows the contents of the README file. But you can view API documentation and test posting prompts to the server in http://127.0.0.1:8000/docs.


### Step 5: Run Ollama in a container

Run Ollama in a container by running this command in a terminal:
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```


## Calling ollama (this should not be important or necessary for running the phone-sensor-server and Ollama)

```
curl http://172.17.0.2:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "Why is the sky blue?",
  "stream": false
}'

```


