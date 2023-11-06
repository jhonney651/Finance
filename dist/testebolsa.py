import requests ,json

# A URL do endpoint da API
url = "https://brapi.dev/api/quote/PETR4"

# Parâmetros da requisição
params = {
    'interval': '3mo',  # Intervalo entre os pontos de dados (3 meses)
    'token': 'oLfPSSfjC6na61bAF3cgZj',  # Seu token de autenticação
}

# Faz a requisição GET
response = requests.get(url, params=params)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrai os dados JSON da resposta
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
