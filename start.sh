#!/bin/sh

# Iniciar crond
crond

# Listar el contenido del directorio para depuración
echo "Listing /app/venv/bin contents:"
ls -la /app/venv/bin

# Ejecutar main.py inmediatamente usando python si python3 no está disponible
if [ -f /app/venv/bin/python ]; then
  /app/venv/bin/python /app/src/app/main.py
elif [ -f /app/venv/bin/python3 ]; then
  /app/venv/bin/python3 /app/src/app/main.py
else
  echo "Python executable not found!"
  exit 1
fi

# Mantener el contenedor corriendo
tail -f /var/log/cron.log
