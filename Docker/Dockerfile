FROM python:3.9

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libzbar0 \
    && apt-get clean

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y preparar los requisitos
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY ../ .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Realizar las migraciones antes de iniciar el servidor
CMD ["sh", "-c", "python manage.py makemigrations && \
                   python manage.py makemigrations AuthService && \
                   python manage.py makemigrations logs && \
                   python manage.py migrate && \
                   python manage.py migrate --database=auth_db AuthService && \
                   python manage.py migrate --database=log_db logs && \
                   daphne -b 0.0.0.0 -p 8000 MecanicaProyect.asgi:application"]
