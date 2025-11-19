# Loggitor

Monitor de logs y alertas en sistemas Linux. Es una herramienta sencilla y útil que recoge y muestra aletas sobre los logs de un sistema.

## Índice  
- [Loggitor](#loggitor)
  - [Índice](#índice)
  - [Acerca del proyecto](#acerca-del-proyecto)
  - [Funcionalidades](#funcionalidades)
  - [Tecnologías utilizadas](#tecnologías-utilizadas)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Roadmap](#roadmap)

## Acerca del proyecto  
Aquí detalla:  
- el problema que resuelve,  
- para quién es,  
- cuál es su valor añadido (por qué sería útil).  

> Esta herramienta monitoriza los logs de un sistema Linux más comunes con el fin de detectar acciones peligrosas (como intentos fallidos de login, accesos denegados a recursos privilegiados, ...) y alertar vía email, Telegram o Slack mostrando la información necesaria para reaccionar.
> Está pensado para ayudar a administradores de sistemas en entornos pequeños.
> Es una herramienta muy ligera, rápida de instalar y utilizar y muy personalizable gracias a su sistema de opciones.

## Funcionalidades  
Lista de lo que hace el proyecto (bullets). Ejemplo:  
- Monitoreo en tiempo real de ficheros de log  
- Filtrado de eventos mediante expresiones regulares  
- Envío de alertas por correo/Telegram  
- Generación de reporte diario en formato CSV/JSON  
- Guardado en base de datos de eventos gestionados
- etc.
- 

## Tecnologías utilizadas  
- Python 3.13


## Instalación  


## Uso

## Estructura del proyecto
monitor_logs_project/
│– monitor_logs.py            # script principal (CLI)
│– config.yml                 # archivo de configuración
│– modules/
│    ├─ file_watcher.py       # módulo de “seguimiento de fichero”
│    ├─ parser.py             # módulo de parseo de registros del log y detección de patrones
│    ├─ alert_manager.py      # módulo que implementa distintas alertas (correo, Telegram, Slack)
│    ├─ storage.py            # módulo para registro de eventos detectados (podría ser SQLite o fichero)
│– tests/
│    ├─ test_parser.py
│    ├─ test_alert_manager.py
│– requirements.txt
│– README.md
│– LICENSE


## Roadmap
| Fase | Duración estimada | Hitos |
|------|-------------------|-------|
| 1 - Diseño y preparación                          | ~1-2 días | Definir patrones a detectar, seleccionar ficheros de log, configuración base, entorno virtual e inicializar repo Git.                 |
| 2 - Implementación básica de seguimiento y parser | ~3-4 días | Implementar file_watcher.py (leer fichero en tiempo real) y parser.py (regex simples y capturar eventos) y probar con un fichero log. |
| 3 - Alertas simples                               | ~2-3 días | Implementar alert_manager.py (alertas por email), módulo de config de alerta, pruebas flujo detección + alerta.                       |
| 4 - Persistencia de eventos y testing             | ~2-3 días | Implementar storeage.py (SQLite), guardar eventos sencillo, tests unitarios parser y alert_manager y, mejorar logging del sistema.    |
| 5 - Umbrales / agrupar alertas                    | ~2 días   | Lógica de umbral tipo de evento, alerta grave (cuando se supere umbral), hacerlo configurable en yaml.                                |
| 6 - Empaquetado + documentación                   | ~1-2 días | README preeliminar, documentar código, requirements.txt, diseñar empaquetado CLI o con setup.py (Docker??).                           |
| 7(bonus) - Dashboard web                          | ~3-4 días | Aplicación web pequeña (Flask o FastAPI): últimos eventos, gráficos sencillos KPIs y lista completa eventos. Documentar cosas nuevas. |
