FROM python:3.12-slim

# Prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    WO_ANKI=1

WORKDIR /app

# System deps: compilers, headers, audio libs, rust toolchain
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libffi-dev \
    libssl-dev \
    pkg-config \
    rustc \
    cargo \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and upgrade pip first (helps build wheels)
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r /app/requirements.txt

# Copy app after dependencies (better caching)
COPY . /app

EXPOSE 5050
CMD ["python", "run_server.py"]
