# 1) Imagen base Python
FROM python:3.11-slim

# 2) Instala dependencias del SO + Xvfb
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    curl \
    gnupg \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    python3-tk \
    python3-dev \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# 3) Instala Google Chrome
RUN wget -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y /tmp/chrome.deb && \
    rm /tmp/chrome.deb


# 4) Directorio de trabajo
WORKDIR /app

# 5) Copia e instala requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copia el resto del código
COPY . .

# 7) Define DISPLAY para Xvfb
ENV DISPLAY=:99

# 8) Ejecuta tu script dentro de Xvfb
CMD ["/bin/bash", "-c", "Xvfb :99 -screen 0 1920x1080x24 -nolisten tcp & export DISPLAY=:99 && python main.py"]