from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Função que analisa o sentimento de um comentário
def analisar_sentimento(comentario):
    # Cria uma instância do analisador de sentimentos
    analyzer = SentimentIntensityAnalyzer()
    # Obtém a pontuação do sentimento (valor 'compound' indica a intensidade do sentimento)
    sentimento = analyzer.polarity_scores(comentario)['compound']

    # Classifica o sentimento com base na pontuação
    if sentimento > 0.1:
        return 'Positivo'  # Sentimento positivo
    elif sentimento < -0.1:
        return 'Negativo'  # Sentimento negativo
    else:
        return 'Neutro'  # Sentimento neutro
