"""Ponto de entrada do pipeline: deve correr tudo, de ponta a ponta, com `python main.py`
(no Colab: `!python main.py`).

Este ficheiro e o resultado FINAL do projeto: desenvolvam nos notebooks e consolidem aqui.
Os nomes das funcoes abaixo sao apenas uma sugestao; podem organizar como preferirem,
desde que o codigo esteja em funcoes com docstrings.
"""
from parametros import PARAMETROS


def obter_dados_cidade(nome, latitude, longitude, data_inicio, data_fim):
    """Pede a API os dados diarios de uma cidade. Deve ter timeout e tratar erros.

    Se ja existir uma resposta em data/raw/ para a mesma cidade e periodo,
    reutiliza-a em vez de repetir o pedido a API.
    """
    raise NotImplementedError


def carregar_e_limpar_dados_internos(caminho):
    """Le o ficheiro interno e trata nulos, duplicados, tipos, datas e nomes de cidade."""
    raise NotImplementedError


def juntar_fontes(meteorologia, consumo):
    """Junta as duas fontes por cidade e data."""
    raise NotImplementedError


def calcular_variaveis(dados):
    """Cria as variaveis derivadas."""
    raise NotImplementedError


def validar_dados(dados):
    """Validacoes de qualidade com `assert` e mensagens claras (minimo 3)."""
    # Exemplo do estilo esperado (adaptem e acrescentem):
    # assert not dados.duplicated(["data", "cidade"]).any(), "Existem linhas duplicadas por cidade e data"
    raise NotImplementedError


def gerar_relatorio(dados, caminho_saida):
    """Gera o relatorio (Excel ou HTML) com a data na nomenclatura do ficheiro."""
    raise NotImplementedError


def main():
    # TODO: ligar as funcoes acima pela ordem certa
    raise NotImplementedError("Pipeline por implementar")


if __name__ == "__main__":
    main()
