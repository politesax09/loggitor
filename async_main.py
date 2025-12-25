import asyncio
from modules.file_watcher import follow_file
from modules.parser import parse_log

# async def test_async():
#     print('Hola asincrono...')
#     asyncio.sleep(1)
#     print('Hola 2 asincrono...')
#     asyncio.sleep(2)
#     print('Fin corrutina')


# async def main():
#     print('Ejecutando main()...')
#     # task = [test_async()]
#     tasks = [follow_file(await open_file("./tests/test_syslog.txt"))]
#     await asyncio.gather(*tasks)

# TODO: Implementar main() como arriba, con lista de corrutinas
async def main():
    print('Ejecutando main...')
    async for line in follow_file("./tests/test_syslog.txt"):
    # follow_file() es generador asincrono (por usar yield) asi que no se hace "await"
        print(line)
        print(await parse_log(line))

asyncio.run(main())