FROM python:3.12-slim

WORKDIR /app

# compy requirements.txt in app folder workdir
COPY requirements.txt .

#  install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Source Code
COPY . .

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]