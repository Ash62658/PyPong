# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3-pip \
    python3-setuptools \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    pkg-config \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    zlib1g-dev

# Install Buildozer
RUN pip install --no-cache-dir buildozer

# Copy the current directory contents into the container at /app
COPY . /app

# Build the APK using Buildozer
RUN buildozer -v android debug

# Set the entry point for the container
ENTRYPOINT ["tail", "-f", "/dev/null"]
