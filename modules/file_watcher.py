import asyncio

# No puedo utilizar esta funcion porque cuando termina, el fichero se cierra y devuelve una
# referencia a un fichero vacio que intenta utilizar la funcion follow_file() pero falla porque
# el fichero ya esta cerrado.
# async def open_file(filename):
#     with open(filename, "r") as f:
#         return f

async def follow_file(filename):
    print('follow_file(): Ejecutando funcion...')
    with open(filename, "r") as file:
        file.seek(0, 2)     # -> Move 0 bytes (0) from the end of file (2)
        while True:
            line = file.readline()
            if not line:
                await asyncio.sleep(0.1)
                continue
            yield line      # Return values without quiting the function


# filename = "./tests/test_log.txt"
# filename = "./tests/test_syslog.txt"
# with open(filename, "r") as f:
#     for line in follow_file(f):
#         print(line.strip())