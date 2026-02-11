FROM python:3.12-slim

# Basic runtime hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    WO_ANKI=1

WORKDIR /app

# Install deps first (better build caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the app
COPY . /app

# The server is expected on 5050 per README
EXPOSE 5050

# NOTE: If the server binds only to 127.0.0.1 inside the container,
# you may need to adjust run_server.py to bind 0.0.0.0.
CMD ["python", "run_server.py"]