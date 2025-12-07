#!/bin/bash

echo "[INFO] Iniciando limpieza de recursos del runner..."

if [ -f "docker-compose.yml" ]; then
    echo " -> Bajando servicios definidos en docker-compose..."
    docker compose down -v --remove-orphans || true

else
    echo " [WARN] No se encontró docker-compose.yml, saltando paso específico"
fi

echo  " -> Eliminando contenedores detenidos.-.."
docker container prune -f

echo  " -> Eliminando imágenes huérfanas (dangling)"
docker image prune -f

echo  " -> Eliminando redes no utilizadas..."
docker network prune -f

echo "[SUCCESS] El entorno Docker está limpio y listo para el siguiente job."
