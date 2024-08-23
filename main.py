from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Dict
import httpx


app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    file = open('README.md')
    content = file.read()
    return Response(content=content, media_type="text/plain")

@app.post("/prompt")
async def prompt(prompt_request: PromptRequest):
    prompt = prompt_request.prompt
    print("Prompt:\n" + prompt)
    print("-------------------------------------------------------------------------------------------------")
    response = process_prompt_with_llm(prompt)
    print("\n")
    print("Response:\n" + response)
    return {"response": response}

def process_prompt_with_llm(prompt: str) -> str:

    # formatted_prompt = f"Anwer on the following question like an old man: {prompt}"

    ### TODO make this address configurable
    res = httpx.post('http://172.17.0.1:11434/api/generate', json={
        'model': 'phi3',
        'prompt': prompt,
        'stream': False
    }, timeout=120)
    data = res.json()
    response = data['response']

    return response


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
