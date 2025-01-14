import os
from file_handler import ler_comentarios, listar_arquivos_input, guardar_classificacao
from sentiment_analyzer import analisar_sentimento
from visualizer import gerar_grafico
import config

# Função que analisa os comentários e gera gráficos e ficheiros CSV
def analisar_comentarios(ficheiro):
    # Listas para armazenar os comentários classificados
    positivos = []
    negativos = []
    neutros = []

    # Lê os comentários do ficheiro
    comentarios = ler_comentarios(ficheiro)

    # Para cada comentário, analisa o sentimento
    for comentario in comentarios:
        comentario = comentario.strip()  # Remove espaços em branco no início e fim
        if comentario:  # Se o comentário não estiver vazio
            sentimento = analisar_sentimento(comentario)  # Analisa o sentimento
            # Adiciona o comentário à lista correspondente
            if sentimento == 'Positivo':
                positivos.append(comentario)
            elif sentimento == 'Negativo':
                negativos.append(comentario)
            else:
                neutros.append(comentario)

    # Conta a quantidade de comentários de cada tipo
    contagem = {
        'Positivos': len(positivos),
        'Negativos': len(negativos),
        'Neutros': len(neutros)
    }

    # Obtém o nome base do ficheiro (sem a extensão)
    nome_base = os.path.basename(ficheiro).split('.')[0]

    # Gerar o gráfico de análise
    gerar_grafico(contagem, nome_base)

    # Guardar a classificação em CSV
    guardar_classificacao(nome_base, positivos, negativos, neutros)

    # Informa o utilizador de onde os ficheiros foram guardados
    print(f"Os ficheiros '{nome_base}-analise.png' e '{nome_base}-classificacao.csv' foram guardados na pasta 'output'.")

# Função que cria um menu interativo para o utilizador selecionar o ficheiro
def menu_interativo():
    # Lista todos os ficheiros na pasta 'input'
    ficheiros = listar_arquivos_input(config.INPUT_DIR)

    # Verifica se existem ficheiros na pasta 'input'
    if not ficheiros:
        print("Nenhum ficheiro encontrado na pasta 'input'. Adicione ficheiros de texto e execute novamente.")
        return

    # Exibe os ficheiros disponíveis para análise
    print("\nFicheiros disponíveis na pasta 'input':")
    for i, ficheiro in enumerate(ficheiros, 1):
        print(f"{i}. {ficheiro}")

    # Permite ao utilizador selecionar um ficheiro para análise
    while True:
        try:
            # Lê a escolha do utilizador e verifica se é válida
            escolha = int(input("\nSelecione o número do ficheiro para análise: "))
            if 1 <= escolha <= len(ficheiros):
                ficheiro_escolhido = os.path.join(config.INPUT_DIR, ficheiros[escolha - 1])
                print(f"Ficheiro selecionado: {ficheiros[escolha - 1]}")
                # Chama a função de análise de comentários
                analisar_comentarios(ficheiro_escolhido)
                break  # Sai do loop após a análise
            else:
                print("Por favor, selecione um número válido.")
        except ValueError:
            print("Entrada inválida. Insira o número correspondente ao ficheiro desejado.")

# Função principal que executa o programa
if __name__ == "__main__":
    menu_interativo()  # Chama a função de menu interativo
