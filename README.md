# Loggitor

Monitor de logs y alertas en sistemas Linux. Es una herramienta sencilla y útil que recoge y muestra aletas sobre los logs de un sistema.

## Índice  
- [Loggitor](#loggitor)
  - [Índice](#índice)
  - [Acerca del proyecto](#acerca-del-proyecto)
  - [Funcionalidades](#funcionalidades)
  - [Tecnologías utilizadas](#tecnologías-utilizadas)
  - [Instalación](#instalación)

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
- Librerías: `socket`, `asyncio`, `pandas`, `Flask`, `FastAPI`, etc.  
- Base de datos: SQLite / PostgreSQL (si aplica)  
- Entorno: Linux / Docker (si aplica)  
- Otras: systemd service, cron job, etc.

## Instalación  
Instrucciones para instalar/configurar el proyecto localmente. Por ejemplo:  
```bash
git clone https://github.com/tu_usuario/tu_proyecto.git  
cd tu_proyecto  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  