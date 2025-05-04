# CloudRun-AI: Serverless REST API for Lightweight AI Inference

CloudRun-AI is a production-ready serverless backend that hosts a lightweight AI model on Google Cloud Run. It allows users to deploy machine learning inference as an HTTP API with auto-scaling, minimal cost, and CI/CD integration.

## Features

- ✅ Fully serverless on Google Cloud Run
- ⚡ Fast cold-start: loads a quantized model under 200ms
- 🧠 Built-in demo model (e.g., sentiment analysis)
- 🛠️ Dockerized, stateless, and deployable via `gcloud`
- 📊 Logging, monitoring, and versioning ready

## Tech Stack

- Python + FastAPI
- Pretrained model (e.g., HuggingFace DistilBERT)
- Google Cloud Run + Artifact Registry + GitHub Actions

## Deployment

```bash
# Build container
docker build -t gcr.io/<project-id>/cloudrun-ai .

# Deploy to Cloud Run
gcloud run deploy cloudrun-ai \
  --image gcr.io/<project-id>/cloudrun-ai \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## API Endpoints

```http
POST /predict
Content-Type: application/json

{
  "input": "This is a great day!"
}

Response:
{
  "prediction": "positive",
  "confidence": 0.92
}
```

## License

MIT License

## Author

Zhang Deao (Allen)
