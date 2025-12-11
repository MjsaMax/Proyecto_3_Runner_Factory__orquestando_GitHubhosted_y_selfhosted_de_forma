
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

Historia 2: Desarrollo del Script de Limpieza y Mantenimiento de Recursos

**ID:** #39

Descripción:
Para garantizar la estabilidad del servidor y evitar conflictos entre ejecuciones consecutivas (o saturación de disco), se implementó un script dedicado (bash) que gestiona la limpieza profunda de recursos utilizados por el runner self-hosted al finalizar el despliegue.

Tareas:
* Crear el script scripts/cleanup_runner.sh para la eliminación de contenedores y volúmenes huérfanos asociados al despliegue.
* Incluir comandos de mantenimiento para limpiar imágenes temporales o "dangling images" 
* Implementar manejo de errores (flags condicionales) para asegurar que el script no falle el pipeline si no encuentra recursos para borrar.
* Integrar la ejecución del script dentro del workflow deploy_local.yml utilizando la condicional if: always() para garantizar la limpieza incluso si el despliegue falla.

Criterios de Aceptación:
* El script libera espacio en disco eliminando artefactos no utilizados tras la ejecución.
* El script puede ejecutarse múltiples veces sin generar errores críticos (idempotencia).
* El entorno de Docker queda en un estado "limpio" listo para el siguiente job.
* Documentarlo en .evidence/.

**EVIDENCIA:** Ubicados en .evidence/cleanup_runner_log.txt (Log de ejecución y espacio liberado), scripts/cleanup_runner.sh (Código fuente) y la integración en .github/workflows/deploy_local.yml.

**Responsable(s):** Poma Walter

---

## Historia 3: Documentación de Protocolos de Seguridad del Runner

**ID:** #40

Descripción:
Documentar los protocolos de seguridad para la administración del Self-Hosted Runner. Este documento guía el mantenimiento de la integridad del servidor y mitiga riesgos de persistencia o fuga de información, complementando las medidas técnicas implementadas en el pipeline.

Tareas:
* Crear el documento `docs/RUNNER_SECURITY.md` con checklist de verificación.
* Documentar la política de Logs: Persistencia, ubicación y rotación.
* Documentar la estrategia de Aislamiento: Ejecución rootless y limpieza de contenedores.
* Documentar el procedimiento de Reset: Pasos para desvincular y limpiar el runner en caso de compromiso.

Criterios de Aceptación:
* El documento `RUNNER_SECURITY.md` existe en el repositorio en la carpeta `docs/`.
* El checklist cubre explícitamente logs, aislamiento y procedimientos de reset.
* La documentación es clara y ejecutable.

**EVIDENCIA:** [Documento de Seguridad (RUNNER_SECURITY.md)](../docs/RUNNER_SECURITY.md)

**Responsable(s):** Davila Aaron