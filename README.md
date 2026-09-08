# Student ML API

A FastAPI application containerized with Docker and automatically published to GitHub Container Registry (GHCR) using GitHub Actions.

## API Endpoints

* **GET `/health`**: Returns the health status, application name, and version.
* **POST `/predict`**: Takes a numerical value and returns a prediction payload.

## Local Running via Docker (GHCR)

To pull and run the published container image directly from GHCR:

```bash
# Pull the release image
sudo docker pull ghcr.io/umama123/student-ml-api:v1.0.0

# Run the container on port 8000
sudo docker run -d --name student-ml-api -p 8000:8000 ghcr.io/umama123/student-ml-api:v1.0.0

# Verify health endpoint
curl http://localhost:8000/health  

# Install dependencies
pip install -r requirements.txt

# Run pytest unit tests
pytest

# Build local Docker image
sudo docker build -t student-ml-api:1.0.0 .
