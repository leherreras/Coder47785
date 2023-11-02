import os
import json
import logging
from calculadoras.basica import suma

# Registro
# TODO 1. verificar si existe el acrhivo
# logging.error(os.path.exists("main.py"))
# si existe leer el arvhivo y cargar la data como diccionario
# si no existe crear un diccionario vacio
# TODO 2. agregar el usuario al diccionario
# TODO 3. guardar la informacion en el archivo

# leer la informacion


# verificar el usuario con contraseña
logging.basicConfig(level=logging.DEBUG)
logging.debug("este es mi mensaje inicial")
logging.info("este es mi mensaje inicial")
logging.warning("este es un warning")
logging.error(os.path.exists("main.py"))

user = {}
user["luis"] = "123"
di_str = json.dumps(user)
try:
    logging.info("estoy escribiendo un archivo")
    with open("archivo.trd", "w") as f:
        f.write(di_str)
except:
    logging.error("se ejecuto un error")
