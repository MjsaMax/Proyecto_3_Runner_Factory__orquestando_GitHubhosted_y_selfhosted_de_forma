
Evidencia del Sprint 1: VIDEO

Historia 1: Configuración del Self-Hosted Runner

ID: #16 ID_PULL_REQUEST: #20

Descripción: Instalar y registrar un agente "runner" de GitHub en la máquina local (o VM de laboratorio) para permitir la ejecución de trabajos que requieren acceso a infraestructura local (Docker).

Tareas:
 Descargar el paquete del runner de GitHub Actions para el sistema operativo local (Linux/Mac/Windows).
 Registrar el runner en el repositorio usando el token proporcionado por GitHub (Settings > Actions > Runners).
 Asignar las etiquetas (labels) obligatorias durante la configuración: self-hosted y local-docker.
 Iniciar el servicio del runner (interactivamente con ./run.sh o como servicio background).
 Verificar conexión sin usar credenciales externas (PATs).

Criterios de Aceptación:
 El runner aparece con estado "Idle" (Verde) en la configuración del repositorio en GitHub.
 El runner tiene visible la etiqueta personalizada local-docker.

EVIDENCIA: Ubicado en self-hosted.log ejecución de ./run.sh
``` bash
√ Connected to GitHub

Current runner version: '2.329.0'
2025-12-04 05:13:21Z: Listening for Jobs


```


Responsable(s): Serrano Max

Historia 1: Configuración del Self-Hosted Runner

ID: #19 ID_PULL_REQUEST: #21

Descripción:
Documentar los riesgos de seguridad inherentes al uso de self-hosted runners, específicamente en repositorios públicos o con múltiples colaboradores, y establecer las reglas para mitigarlos.

Tareas:

Actualizar sección en README.md.
Explicar el riesgo de persistencia: "Qué pasa si un PR malicioso se ejecuta en mi máquina" (acceso a red local, sistema de archivos, etc.).
Documentar estrategias de mitigación implementadas o recomendadas:
   Explicar buena práctica, uso de branch protection rules.
   Configuración de aprobación para colaboradores externos.
   Limpieza de entorno post-ejecución.

Criterios de Aceptación:

    El riesgo está explicado en README.md o implementado en un archivo (colocar en README.md la ubicación del archivo asociado).
    Se explican claramente al menos 2 riesgos y 2 mitigaciones.
EVIDENCIA:	[commit 2cf7af9ad8f1a5e66cb7f8622a7e028105bf6c0b](https://github.com/MjsaMax/Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma/pull/21/files)


Responsable(s): Serrano Max
