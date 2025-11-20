import time

# TODO: Implementar ASYNCIO o THREADING para hacer asincrona tareas de seguimiento de ficheros

def follow_file(file):
    file.seek(0, 2)     # -> Move 0 bytes (0) from the end of file (2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line      # Return values without quiting the function


filename = "./tests/test_log.txt"
with open(filename, "r") as f:
    for line in follow_file(f):
        print(line.strip())