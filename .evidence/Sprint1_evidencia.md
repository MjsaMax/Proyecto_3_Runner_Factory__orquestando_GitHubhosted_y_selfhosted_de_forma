
Historia 1: Configuración Inicial del Repositorio y Entorno

ID: #1 ID_PULL_REQUEST: #6

Descripción:

Inicializar el repositorio con la estructura básica de carpetas y dependencias necesarias para Python/FastAPI.

Tareas:

Crear repositorio en GitHub con rama main.
Crear estructura de carpetas: app/, tests/ y .evidence/ (esta última es obligatoria para el curso).
Crear archivo .gitignore para Python.
Crear requirements.txt o pyproject.toml incluyendo fastapi, uvicorn, pytest, ruff (o flake8).

Criterios de Aceptación:

    El repo existe y tiene las carpetas creadas.
    La carpeta .evidence/ existe (aunque esté vacía, debe existir un .gitkeep).

EVIDENCIA: [COMMIT](https://github.com/MjsaMax/Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma/commit/bbaf1f529ddbd422b6cf512770268c03c5023001)

Responsable(s): Serrano Max

Historia 2: Implementar "Docs Registry API"

ID: #2 ID_PULL_REQUEST: #2

Descripción:

Implementar el microservicio backend básico utilizando el framework FastAPI  con los endpoints requeridos para listar y consultar documentos simulados.

Tareas:

Crear archivo app/main.py.
Configurar FastAPI moviendo la documentación automática (Swagger) a /swagger para liberar la ruta /docs.
Implementar endpoint GET /health (status check).
Implementar endpoint GET /docs (debe devolver una lista ficticia de documentos con ID, nombre y tipo).
Implementar endpoint GET /docs/{id} (debe devolver detalles de un documento específico o 404 si no existe).

Criterios de Aceptación:

    La API corre localmente con uvicorn app.main:app --reload.
    Los 3 endpoints (/health, /docs, /docs/{id}) devuelven JSON válido

EVIDENCIA: execution_log.txt

```bash
INFO:     Will watch for changes in these directories: ['/home/walter/DesarrolloSoftware/PC5/Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [11573] using StatReload
INFO:     Started server process [11575]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


Historia 3: Pruebas Unitarias (Unit Tests)

ID: #3 ID_PULL_REQUEST: #8

Descripción:

Crear tests automatizados para asegurar que la API responde correctamente.

Tareas:

Configurar pytest.
Escribir un test para verificar que /health devuelve 200 OK.
Escribir tests básicos para /docs y /docs/{id}.

Criterios de Aceptación:

    Al ejecutar pytest, todos los tests pasan en verde.

Responsable(s): Serrano Max

EVIDENCIA: test_main.log

```bash
==================================================== test session starts =====================================================
platform linux -- Python 3.12.3, pytest-9.0.1, pluggy-1.6.0
rootdir: /mnt/c/Users/Max--/Documents/projects/repos/Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma
plugins: anyio-4.12.0
collected 4 items

tests/test_main.py ....                                                                                                [100%]

===================================================== 4 passed in 4.96s ======================================================
```
Historia 4: Pipeline de CI: ci_hosted.yml

ID: #4 

Descripción:

Configurar un workflow de GitHub Actions que corra en la infraestructura de GitHub (no en la máquina local aún) para validar la calidad del código.

Tareas:

- Crear archivo .github/workflows/ci_hosted.yml.
- Configurar runs-on: ubuntu-latest (GitHub-hosted).
- Job 1: Linting (usar ruff, flake8 o black).
- Job 2: Testing (ejecutar pytest).

Criterios de Aceptación:

    El pipeline se dispara automáticamente al crear un Pull Request.
    El pipeline aparece en verde en la pestaña "Actions" de GitHub.

Responsable(s): Aaron Davila Santos



**Log de ejecución local (Pre-validación):**

```bash
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.0.1, pluggy-1.6.0
rootdir: /home/aaron/UNI/DesarrolloSoftware/Proyecto_3_Runner_Factory
plugins: anyio-4.12.0
collected 4 items

tests/test_main.py ....                                                  [100%]

============================== 4 passed in 0.20s ===============================