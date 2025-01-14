# Sentiment Analysis Program

## Descrição
Este programa analisa os sentimentos presentes em um conjunto de comentários, categorizando-os como **Positivos**, **Negativos** ou **Neutros**. 
A análise é realizada utilizando a biblioteca `VADER SentimentIntensityAnalyzer`, especializada em processar texto para identificar sentimentos.

## Funcionalidades
1. **Menu Interativo**:
   - Lista automaticamente os ficheiros presentes na pasta `input`.
   - Permite ao utilizador selecionar o ficheiro a ser analisado.

2. **Análise de Sentimento**:
   - Cada comentário é avaliado e classificado como Positivo, Negativo ou Neutro.

3. **Resultados Organizados**:
   - Cria um ficheiro CSV na pasta `output`, contendo os comentários classificados.
   - Gera um gráfico de barras em formato PNG mostrando a distribuição dos sentimentos.

4. **Nomes Personalizados**:
   - Os ficheiros de output começam com o nome do ficheiro de entrada, seguido por sufixos apropriados (e.g., `LojaA-classificacao.csv`, `LojaA-analise.png`).

## Estrutura de Pastas
- **input/**: Pasta onde devem ser colocados os ficheiros de comentários em formato `.txt` para análise.
- **output/**: Pasta onde os resultados da análise (gráfico e CSV) serão armazenados.

## Como Utilizar
1. Coloque os ficheiros de comentários em formato `.txt` na pasta `input`.
2. Execute o programa (main.py).
3. Escolha o ficheiro a ser analisado a partir do menu interativo.
4. Os resultados serão salvos automaticamente na pasta `output`.

## Exemplo de Output
- **CSV**: Contém a classificação de cada comentário.
- **PNG**: Gráfico de barras com a distribuição de sentimentos:

```
+------------+--------------+
| Sentimento | Número      |
+------------+--------------+
| Positivos  | 5            |
| Negativos  | 3            |
| Neutros    | 2            |
+------------+--------------+
```

## Requisitos
- Python 3.7 ou superior.
- Bibliotecas necessárias:
  - `matplotlib`
  - `vaderSentiment`

## Notas
- Certifique-se de que os ficheiros na pasta `input` estejam em formato `.txt` e com texto legível.
- O programa cria automaticamente as pastas `input` e `output` se não existirem.
