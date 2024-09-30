# Use an official Python runtime as a base image
FROM python:3.12-slim as build

LABEL maintainer="beaverU"

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for Poetry and build tools
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

# Install Poetry (with version pinning to avoid breaking changes)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH for global use
ENV PATH="/root/.local/bin:$PATH"

# Copy only the Poetry config files to cache the dependencies first
COPY pyproject.toml poetry.lock ./

# Install project dependencies using Poetry (no virtualenv creation)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Expose the port that your Flask app will run on
EXPOSE 5000

# Set the environment variables for Flask
ENV FLASK_APP=server.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "server.py"]