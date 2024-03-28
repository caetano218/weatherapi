import requests


def obter_previsao_tempo(cidade, chave_api):
   #     url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=2ee9924492ede6bbcfa20a837ddce701&units=metric"
    chave = '2ee9924492ede6bbcfa20a837ddce701'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric"
    resposta = requests.get(url)
    print("Status code:", resposta.status_code)  # Adicionando mensagem de depuração

    dados = resposta.json()
    print("Resposta JSON:", dados)  # Adicionando mensagem de depuração

    if resposta.status_code == 200:
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        return temperatura, descricao
    else:
        return None, None


def main():
    cidade = input("Digite o nome da cidade: ")
    chave = '2ee9924492ede6bbcfa20a837ddce701'  # Substitua com sua chave da OpenWeatherMap
    temperatura, descricao = obter_previsao_tempo(cidade, chave)

    if temperatura is not None and descricao is not None:
        print(f"A temperatura em {cidade} é de {temperatura}°C com {descricao}.")
    else:
        print("Não foi possível obter a previsão do tempo para esta cidade.")


if __name__ == "__main__":
    main()

