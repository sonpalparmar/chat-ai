# Use official Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and buffer outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install PostgreSQL development libraries and build tools for psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# If any dependencies need Rust, install Rust and Cargo using rustup (optional)
# Uncomment the lines below if your project requires Rust for building certain packages
# RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && \
#     /root/.cargo/bin/rustup default stable && \
#     /root/.cargo/bin/rustc --version

# Copy requirements.txt first and install Python dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

# Set working directory
WORKDIR /app

# Copy all necessary application files
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/alembic.ini
COPY ./app /app/app

# Expose the port that your FastAPI app will run on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
