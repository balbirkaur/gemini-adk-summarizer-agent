FROM python:3.11

WORKDIR /app

# Copy only requirements first (for clean install)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Then copy code
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]