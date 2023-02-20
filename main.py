from scraper import pegarUltimosResultados
from mybot import enviarSinalTelegram, enviarWinLoss, enviarGale
from dotenv import load_dotenv
import os
import time
import json

load_dotenv()
with open("estrategias.json") as f:
    estrategias = json.load(f)

class Blaze:
    emAnalise = False
    qtdEntrada = 0
    resultado = []
    verificaResultado = []


    def reset(self):
        self.qtdEntrada = 0
        self.emAnalise = False


    def verificaMartingale(self):
        self.qtdEntrada += 1
        if self.qtdEntrada <= int(os.getenv("MARTINGALE")):
            enviarGale(self.qtdEntrada)
        else:
            enviarWinLoss(False)
            self.reset()


    def validaGreenLoss(self, resultado, cor):
        if resultado[0:1] == ['P'] and cor == '⚫️' or resultado[0:1] == ['V'] and cor == '🛑':
            enviarWinLoss(True)
            self.reset()
        elif resultado[0:1] == ['P'] and cor == '🛑' or resultado[0:1] == ['V'] and cor == '⚫️':
            self.verificaMartingale()
        elif resultado[0:1] == ['B']:
            enviarWinLoss(True)
            self.reset()


    def verificaEstrategias(self, cores):
        if self.emAnalise:
            self.validaGreenLoss(cores, self.cor_sinal)
        else:
            for estrategia in estrategias:
                padrao = estrategia['colors']
                if cores[:len(padrao)] == estrategia['colors']:
                    self.cor_sinal = estrategia['cor']
                    mensagem = estrategia['mensagem']
                    enviarSinalTelegram(self.cor_sinal, padrao, mensagem)
                    self.emAnalise = True
                    break


if __name__ == "__main__":
    blaze = Blaze()

    while True:
        resultado = pegarUltimosResultados()
        if resultado != blaze.verificaResultado:
            blaze.verificaResultado = resultado
            blaze.verificaEstrategias(resultado)
