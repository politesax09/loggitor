import re

# TODO: De momento esta hecho solo para SYSLOG, habrá que probar con los demás ficheros después
# TODO: Refactorizar para usar config.yml e integrar correctamente con el resto del codigo
def parse_log(line):
# Parse a log line using the correct pattern for each log format selected in "config.yml".

    # line1 = "2025-11-13T17:39:47.120672+00:00 ubuntu systemd[1]: Started session-10.scope - Session 10 of User elmonje."
    pattern = re.compile(r'^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2}))\s+(?P<host>[^\s]+)\s+(?P<service>[A-Za-z0-9_\-@./]+)(?:\[(?P<pid>\d+)\])?:\s*(?P<message>.*)$')
    m = pattern.match(line)
    if m:
    #     print("Linea 1 >>")
    #     print("timestamp:", m.group("timestamp"))
    #     print("host:",      m.group("host"))
    #     print("service:",   m.group("service"))
    #     print("pid:",       m.group("pid"))
    #     print("message:",   m.group("message"))
        return (m.group("timestamp"), m.group("host"), m.group("service"), m.group("pid"), m.group("message"))
    return None


