import os
import csv

# Função que lê os comentários de um ficheiro de texto
def ler_comentarios(ficheiro):
    # Abre o ficheiro de comentários e lê todas as linhas
    with open(ficheiro, 'r', encoding='utf-8') as f:
        return f.readlines()

# Função que guarda a classificação dos sentimentos num ficheiro CSV
def guardar_classificacao(nome_base, positivos, negativos, neutros):
    # Cria e escreve os resultados num ficheiro CSV
    with open(f'output/{nome_base}-classificacao.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Tipo', 'Comentário'])  # Escreve o cabeçalho

        # Escreve os comentários classificados nas respetivas categorias
        for tipo, lista in zip(['Positivos', 'Negativos', 'Neutros'], [positivos, negativos, neutros]):
            for comentario in lista:
                writer.writerow([tipo, comentario])  # Escreve cada comentário e o seu tipo

# Função que lista todos os ficheiros de entrada na pasta especificada
def listar_arquivos_input(diretorio):
    return [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
