FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime
RUN pip install fastapi uvicorn transformers
COPY . /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
