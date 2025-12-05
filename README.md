Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma

Este proyecto implementa una arquitectura de CI/CD híbrida para el servicio "Docs Registry API". El objetivo es demostrar la gestión segura de pipelines combinando GitHub-hosted runners (para tareas ligeras) y Self-hosted runners (para tareas de infraestructura local).

## Demos de Sprints

* **Sprint 1 (API + CI Hosted):**  https://1drv.ms/f/c/fdb226ef3c2e079a/IgC5dM3Il_PJQIdvL1Os1OYPAewzYsQ0gu6cKer4Xm440QI?e=kPgmcA

* **Sprint 2 (Self-hosted runner + build/scan):** https://1drv.ms/f/c/fdb226ef3c2e079a/IgDEEeuIV_wpRqjahXv3j7hHAW9fVQRgpbRoINibczd-0o4

* **Sprint 3 (Agregar):**

* **Sprint 4 (Agregar):**


## Documentación de Riesgos y Mitigaciones en self-hosted runners

Para la integración continua (CI), se requiere un servidor de ejecución (Self-Hosted Runner) encargado de procesar los trabajos definidos. Cada disparador (trigger) configurado (como un push a main o un Pull Request) inicia una instancia en este servidor que clona el repositorio y ejecuta los comandos definidos en los archivos .yaml dentro de .github/workflows/. Al utilizar un repositorio público con runners propios, la infraestructura queda expuesta a colaboradores externos, introduciendo riesgos como los siguientes.

RIESGOS:

1.    Obtención de Secretos: Un atacante puede imprimir variables de entorno o acceder a archivos de configuración no encriptados para robar tokens de api o claves de bases de datos.

2.    Inyección de Malware y Persistencia: Dado que el runner es persistente, un script malicioso puede instalar software espía o modificar el código fuente local para infectar futuros despliegues legítimos.

3.    Uso de Recursos de dudosa procedencia: "Colaboradores" maliciosos pueden aprovechar la potencia de cómputo del servidor para realizar otros servicios como minar criptomonedas o utilizar el ancho de banda de la red para lanzar ataques a terceros, actuando el runner como un nodo de una botnet (estos serían "servicios de dudosa procedencia").

4.    Ataques de Denegación de Servicio (DoS): Se pueden lanzar bucles infinitos intencionales para saturar el host del runner, impidiendo que el equipo de desarrollo pueda ejecutar sus pipelines correctamente.

MITIGACIONES

1.    Mitigación de colaboradores no deseados, aprobación obligatoria para colaboradores externos: Para evitar que colaboradores maliciosos ejecuten código arbitrario usando Pull Requests desde forks, se ha configurado la regla de requerir aprobación por un colaborador oficial antes de la ejecución, en la configuración del repositorio.

2.    Mitigación de ejecución de servicios externos, uso de entornos efímeros (Contenedores Docker): Para mitigar la persistencia de malware, los jobs se ejecutan dentro de contenedores Docker aislados. Al finalizar el job, el contenedor se destruye junto con cualquier archivo modificado o proceso malicioso, garantizando un entorno limpio para la siguiente ejecución.

3.    Mitigación de acceso de recursos privados, uso de Privilegios: El runner se ejecuta bajo un usuario del sistema operativo con permisos limitados (non-root), restringiendo su capacidad de instalar software a nivel global. Además, se restringe la red para mitigar conexiones no deseadas y se aplican reglas de firewall para bloquear el acceso del runner a la red interna sensible (bases de datos locales, por ejemplo), permitiendo únicamente la comunicación necesaria con GitHub.

4.    Mitigación DoS, Configuración de Timeouts: Para evitar ataques DoS se establecen timeouts estrictos (por ejemplo 2 minutos o según el pipeline lo requiera) para detener automáticamente cualquier proceso que exceda el tiempo esperado.
