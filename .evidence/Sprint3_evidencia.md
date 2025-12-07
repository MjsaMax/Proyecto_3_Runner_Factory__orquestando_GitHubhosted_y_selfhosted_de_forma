
Evidencia del Sprint 2: https://1drv.ms/f/c/fdb226ef3c2e079a/IgD3ZGQyo0UsRYUcbwu_V7vUAXUyZ-0B4XjErhAvuT7EwIE?e=GOVUMJ
## Historia 1: Implementación del Pipeline de Despliegue Local (deploy_local.yml)

ID: #38

Descripción: Se requiere crear el archivo de flujo de trabajo deploy_local.yml para automatizar el despliegue de la aplicación en el entorno de infraestructura propia. Este pipeline debe orquestar la ejecución de la aplicación, verificar su estado y asegurar que el entorno quede limpio post-ejecución.

Tareas:

	Configurar el job para que se ejecute en un runner etiquetado como self-hosted.

	Definir el paso de levantamiento de infraestructura (usando docker compose up o manifiestos de K8s).

	Implementar un Smoke Test que valide la disponibilidad del servicio (por ejemplo curl -f http://localhost:PUERTO/health).

Criterios de Aceptación:

	El pipeline se ejecuta exitosamente en el runner local.

	La aplicación responde con código 200 al endpoint /health.

	Documentarlo en .evidence/

EVIDENCIA: Ubicados en .evidence/cleanup_log.txt , ‎.evidence/deploy_log.txt , .evidence/execution_log_deploy.txt , .evidence/smoke_test.txt

Responsable(s): Serrano Max
