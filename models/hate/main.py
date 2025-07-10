from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased").cuda()

@app.post("/")
async def predict(req: Request):
    data = await req.json()
    inputs = tokenizer(data["text"], return_tensors="pt", truncation=True).to("cuda")
    logits = model(**inputs).logits
    score = torch.softmax(logits, dim=1)[0][1].item()
    return {"score": score}
