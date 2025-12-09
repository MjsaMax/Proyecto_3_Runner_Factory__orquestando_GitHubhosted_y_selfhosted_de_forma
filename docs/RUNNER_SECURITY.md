# Protocolos de Seguridad y Administración del Self-Hosted Runner

Este documento define las políticas operativas para garantizar la seguridad, integridad y disponibilidad del Self-Hosted Runner utilizado en el proyecto Runner Factory.

## 1. Checklist de Verificación Diario
El administrador del runner debe realizar las siguientes verificaciones antes de habilitar el servicio para el equipo:

- [ ] **Estado del Servicio:** Verificar que el servicio del runner esté activo y escuchando (`./svc.sh status`).
- [ ] **Espacio en Disco:** Asegurar que hay al menos 20% de espacio libre para evitar fallos en builds grandes (`df -h`).
- [ ] **Procesos Huérfanos:** Comprobar que no hay contenedores de Docker "zombis" de ejecuciones anteriores (`docker ps -a`).
- [ ] **Conectividad:** Verificar que el runner tiene salida a GitHub y no hay bloqueos de firewall inesperados.

## 2. Política de Logs
Para mantener la trazabilidad de las operaciones sin comprometer el almacenamiento:

* **Ubicación:** Los logs de ejecución del runner se almacenan localmente en la carpeta `_diag/` dentro del directorio de instalación del agente.
* **Persistencia:** Se mantendrán los logs de los últimos **7 días**.
* **Rotación:** GitHub Actions rota automáticamente algunos logs, pero se recomienda ejecutar un script de limpieza semanal para eliminar archivos `Worker_*.log` antiguos que ya no sean relevantes.
* **Auditoría:** En caso de fallo de seguridad, los logs no deben ser borrados hasta finalizar el análisis forense.

## 3. Estrategia de Aislamiento
Para mitigar el riesgo de que un job malicioso afecte al sistema operativo host:

* **Ejecución en Contenedores:** Todos los jobs de CI/CD que requieran compilación o ejecución de código no confiable deben correr dentro de contenedores Docker (usando `container:` en el workflow o pasos `docker run`).
* **Usuario sin Privilegios:** El agente del runner **NO** debe correr como `root`. Debe ejecutarse bajo un usuario dedicado del sistema operativo con permisos limitados.
* **Red:** El runner no debe tener acceso a la red interna de producción, solo salida a internet (HTTPS puerto 443) hacia GitHub y acceso al socket de Docker.

## 4. Procedimiento de Reset (Compromiso del Runner)
En caso de sospecha de intrusión, persistencia de malware o corrupción del entorno, seguir estos pasos inmediatamente:

1. **Detener el servicio:**
   Ejecutar `./svc.sh stop` en la carpeta del runner.
2. **Aislar la máquina:**
   Desconectar el cable de red o deshabilitar la interfaz de red para evitar propagación.
3. **Limpieza profunda de Docker:**
   Ejecutar `docker system prune -a --volumes -f` para eliminar todos los contenedores, imágenes y volúmenes.
4. **Desvincular de GitHub:**
   Ir a la configuración del repositorio en GitHub (*Settings > Actions > Runners*) y forzar la eliminación del runner ("Force remove").
5. **Reinstalación:**
   Eliminar la carpeta del runner completamente y realizar una instalación limpia generando un nuevo token de registro.
