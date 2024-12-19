# syntax=docker/dockerfile:1
FROM ubuntu:20.04

# Evitar prompts interactivos durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    unzip \
    curl \
    gnupg \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Instalar Terraform
RUN wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list
RUN apt-get update && apt-get install -y terraform

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt .
COPY src/ ./src/

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Punto de entrada
ENTRYPOINT ["python3", "src/main.py"] 