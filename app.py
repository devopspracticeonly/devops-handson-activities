import os

import boto3
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

REGION = os.getenv("AWS_REGION", "ap-south-1")
MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "amazon.nova-lite-v1:0")

bedrock = boto3.client("bedrock-runtime", region_name=REGION)
app = FastAPI(title="Bedrock AI Agent")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Bedrock AI Agent</title>
      <style>
        body { font-family: Arial; max-width: 720px; margin: 40px auto;
               padding: 16px; background: #f5f7fb; }
        h1 { color: #172554; }
        textarea { width: 100%; box-sizing: border-box; padding: 12px; }
        button { padding: 10px 18px; margin-top: 10px; cursor: pointer; }
        pre { white-space: pre-wrap; background: white; padding: 16px;
              border-radius: 8px; min-height: 100px; }
      </style>
    </head>
    <body>
      <h1>Bedrock AI Agent</h1>
      <textarea id="message" rows="4"
        placeholder="Ask your AI agent a question"></textarea>
      <button onclick="sendMessage()">Send</button>
      <pre id="answer">Your answer will appear here.</pre>
      <script>
        async function sendMessage() {
          const message = document.getElementById("message").value.trim();
          const answer = document.getElementById("answer");
          if (!message) {
            answer.textContent = "Enter a message first.";
            return;
          }
          answer.textContent = "Thinking...";
          try {
            const response = await fetch("/chat", {
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: JSON.stringify({message})
            });
            const data = await response.json();
            if (!response.ok) throw new Error(data.detail || "Request failed");
            answer.textContent = data.answer;
          } catch (error) {
            answer.textContent = "Error: " + error.message;
          }
        }
      </script>
    </body>
    </html>
    """


@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = bedrock.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": request.message}],
                }
            ],
            inferenceConfig={"maxTokens": 500, "temperature": 0.3},
        )
        answer = "".join(
            block.get("text", "")
            for block in response["output"]["message"]["content"]
        )
        return {"answer": answer}
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Bedrock request failed. Check model access and pod logs.",
        )