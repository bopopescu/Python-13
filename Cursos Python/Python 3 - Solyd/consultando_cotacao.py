import requests
import json

while True:
    requisicao = requests.get('http://api.promains.net.br/cotacao/v1/valores')
    cotacao = json.loads(requisicao.text)

    print(cotacao['valores']['USD']['valor'])