# Bot para sinais da Blaze Double

Script para ler os últimos resultados da blaze, verificar se bate com a estratégia e enviar sinal no Telegram.
## Instalação

Use o GIT para clonar o repositório:
```bash
git clone https://github.com/samuelrizzo/blaze-double-bot
```
Crie o ambiente virtual com o Python
```bash
python -m venv venv - para Windows
python3 -m venv venv - para Linux
```

Ative o ambiente virtual com:
```bash
source venv/bin/activate - para Linux

cd venv/bin
activate
para Windows
```
Instale os requerimentos com o pip

```bash
pip install -r requirements.txt
```

## Utilização:

```bash
python3 main.py - para Linux
python main.py - para Windows
```
#### Para alterar configurações:
Abra o arquivo estratégias.json e altere
```json
[
    {
        "colors": ["P", "P"],
        "cor": "🛑",
        "name": "Padrão PP",
        "mensagem": "SINAL ENCONTRADO\nENTRAR EM VERMELHO\nPADRAO PP"
    },    
    {
        "colors": ["V", "V"],
        "cor": "⚫️",
        "name": "Padrão VV",
        "mensagem": "SINAL ENCONTRADO\nENTRAR EM PRETO\nPADRAO VV"
    }
]

```
Você pode adicionar mais padrões e alterar a mensagem para ser enviada
#### Arquivo .env:

```json
TELEGRAM_TOKEN=
TELEGRAM_CHAT_ID=
BLAZE_API_URL=https://blaze.com/api/roulette_games/recent
ANALISANDO=False
MARTINGALE=2
```
