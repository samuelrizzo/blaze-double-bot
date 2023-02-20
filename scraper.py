import requests
import json
from dotenv import load_dotenv
import os

def pegarUltimosResultados():
    load_dotenv()
    BLAZE_URL = os.getenv("BLAZE_API_URL")
    r = requests.get(BLAZE_URL) 
    resultados = [i['roll'] for i in json.loads(r.content)]
    cores = converterEmCores(resultados)
    return cores

def converterEmCores(resultados):
    cores = []
    for valor in resultados:
        if valor == 0:
            cores.append("B")
        elif valor >= 1 and valor <= 7:
            cores.append("V")
        elif valor >= 8 and valor <= 14:
            cores.append("P")
    return cores