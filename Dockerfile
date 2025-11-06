FROM python:3.11-slim

WORKDIR /app

# Instalación de herramientas necesarias (si requiere compilar paquetes)
RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar código
COPY . .

EXPOSE 5000

# Espera a la DB y arranca la app
CMD ["sh", "-c", "python app/wait_for_db.py && python run.py"]
