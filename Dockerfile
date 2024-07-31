FROM alpine:latest



# Instalar dependencias necesarias

RUN apk add --no-cache python3 py3-pip dcron su-exec



# Crear directorio de trabajo y copiar los archivos

WORKDIR /app

COPY requirements.txt /app/



# Crear y activar un entorno virtual

RUN python3 -m venv /app/venv

ENV PATH="/app/venv/bin:$PATH"



# Verificar el contenido del entorno virtual

RUN ls -la /app/venv



# Instalar dependencias

RUN pip install --no-cache-dir -r requirements.txt



# Copiar el resto de los archivos del proyecto

COPY . /app/



# Configurar cron job para ejecutar main.py una vez al día

RUN echo "0 0 * * * /app/venv/bin/python /app/src/app/main.py >> /var/log/cron.log 2>&1" > /etc/crontabs/root

RUN chmod 0644 /etc/crontabs/root && touch /var/log/cron.log



# Copiar y dar permisos al script de inicio

COPY start.sh /app/start.sh

RUN chmod +x /app/start.sh



# Comando por defecto para ejecutar al iniciar el contenedor

CMD ["/app/start.sh"]

