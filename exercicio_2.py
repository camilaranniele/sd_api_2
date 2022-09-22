import requests


def get_address():
    print("Escolha umas das opções: \n"
          "[1] - CEP\n"
          "[2] - Nome do logradouro")
    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        cep = (input("Digite o cep: "))
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        endereco = response.json()["logradouro"]
        bairro = response.json()["bairro"]
        cidade = response.json()["localidade"]
        uf = response.json()["uf"]
        formated_cep = '{}-{}'.format(cep[:5], cep[5:])
        return f"{endereco} - {bairro}, {cidade} - {uf}, {formated_cep}"
    elif opcao == 2:
        uf = input("Digite o uf: ")
        cidade = input("Digite a cidade: ")
        logradouro = input("Digite o nome da rua: ")
        url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'
        response = requests.get(url)
        bairro = response.json()[0]["bairro"]
        cep = response.json()[0]['cep']
        return f"{logradouro} - {bairro}, {cidade} - {uf}, {cep}"
    else:
        return 'Opção inválida'


print(get_address())