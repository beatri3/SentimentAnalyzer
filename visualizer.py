import matplotlib.pyplot as plt

# Função que gera um gráfico de barras para a distribuição de sentimentos
def gerar_grafico(contagem, nome_base):
    # Cria o gráfico de barras com os dados de sentimentos
    plt.figure(figsize=(10, 6))
    plt.bar(contagem.keys(), contagem.values(), color=['green', 'red', 'gray'])
    plt.xlabel('Tipo de Sentimento')  # Rótulo no eixo X
    plt.ylabel('Número de Comentários')  # Rótulo no eixo Y
    plt.title('Distribuição de Sentimentos nos Comentários')  # Título do gráfico

    # Guarda o gráfico gerado como uma imagem PNG na pasta output
    plt.savefig(f'output/{nome_base}-analise.png')
    plt.close()  # Fecha o gráfico para libertar memória
