# blaze-double-bot
Robô em Python que extrai os últimos resultados do jogo Double da Blaze e envia sinais no Telegram

Para adicionar mais estratégias é só alterar o arquivo estrategias.json, adicionando:
,
{
        "colors": ["V", "V"],
        "cor": "⚫️",
        "name": "Padrão VV",
        "mensagem": "SINAL ENCONTRADO\nENTRAR EM PRETO\nPADRAO VV"
    }
]

EXEMPLO DO ARQUIVO .ENV:

TELEGRAM_TOKEN=
TELEGRAM_CHAT_ID=-
BLAZE_API_URL=https://blaze.com/api/roulette_games/recent
ANALISANDO=False
MARTINGALE=2