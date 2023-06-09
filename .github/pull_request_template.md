## Revisión de Pull Request
Antes de fucionar los cambios su petición debe cumplir con los siguientes cambios:

-  [ ] Estructura de PR valida.
-  [ ] Commits validos.
-  [ ] Código valido.

## Ejemplo de un PR valido
El PR debe contener los siguientes elmentos como minimo:

1. Descripción

  [Describir aquí los cambios realizados en este Pull Request.]


2. Problema solucionado 

  Resuelve el issues [id del issues]


3. Notas adicionales

  [Cualquier otra información o contexto relevante que pueda ser útil para revisar este Pull Request.]

## Commits validos
Un commit valido debe estar en ingles y debe seguir el estandar de [conventional commits](https://www.conventionalcommits.org/es/v1.0.0/). A continuación se explican los prefijos a utilizar:


-  build: Usado cuando se realiza una actualización o cambio en la configuración del entorno de construcción, como un cambio en el archivo de configuración de construcción.

-  chore: Se utiliza para cambios menores en el código que no están relacionados con una característica o corrección de error. Esto podría incluir tareas de mantenimiento, actualización de dependencias, etc.

-  ci: Utilizado cuando se realizan cambios en la configuración o automatización del sistema de integración continua.

-  docs: Usado cuando se realiza una actualización o cambio en la documentación del código, como agregar una descripción de una función o actualizar un archivo README.

-  feat: Utilizado cuando se agrega una nueva característica al código.

-  fix: Utilizado cuando se corrige un error o fallo en el código.

-  perf: Se utiliza cuando se realiza una mejora de rendimiento en el código.

-  refactor: Utilizado cuando se realiza una modificación en el código que no agrega ni elimina funcionalidad, pero mejora su estructura o legibilidad.

-  revert: Se utiliza cuando se revierte un commit previo.

-  style: Utilizado cuando se realizan cambios en la apariencia o estilo del código, como la eliminación de un espacio en blanco o la corrección de la indentación.

-  test: Usado cuando se agregan o actualizan pruebas en el código.

Ejemplos de commits validos:

-  docs: update README

-  chore (users): adds model migrations

-  chore (project_settings): Add CORS setting

-  feat (users): Add user profile functionality

## Código valido
Se concidera un código valido aquel donde las variables, funciones, componentes, etc, estan definidas en ingles.
