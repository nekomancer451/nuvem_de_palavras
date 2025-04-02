import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# Carrega a máscara (certifique-se de que "cacto2.png" existe e tenha resolução adequada)
mask = np.array(Image.open("cacto2.png"))

# Lista de expressões (com espaços, sem underscores)
palavras = [
    "estribado", "lapois", "pagar sapo", "vou chegar", "barril", "lá ele", "tô na bruxa", 
    "meu rei", "areado", "frescar", "na doida", "armaria", "égua", "kiu!", "esparroso", 
    "apombalado", "peba", "paia", "só quer ser as pregas", "ficar com a gota", "tabacudo", 
    "pirangueiro", "aperreio", "dispense", "caçar conversa", "ficar bestando", "galalau", 
    "fazer munganga", "buliçoso", "boy", "boe", "de rocha", "tá ca peste", "vôti", 
    "cambito", "fuleiragem", "morgado", "mangar", "migué", "ôxe", "tá com a bexiga lixa", 
    "tá com a bubônica", "torar", "traquino", "vixe", "massa", "brocado", "o raio", "triscar"
]

# Cria um dicionário de frequências (todas com a mesma frequência para este exemplo)
frequencias = {expressao: 100 for expressao in palavras}

# Paleta de cores (tons de verde, marrom e amarelo)
cores = [
    "#3A5F0B", "#6B8E23", "#A0522D", "#8B4513", "#D2B48C",
    "#9ACD32", "#556B2F", "#BDB76B", "#CD853F", "#FFD700"
]

cores_palavras = {}

def cor_aleatoria(palavra, font_size, position, orientation, random_state, **kwargs):
    if palavra not in cores_palavras:
        cores_palavras[palavra] = random.choice(cores)
    return cores_palavras[palavra]

# Gera a nuvem de palavras com resolução 4K (3840x2160 pixels)
wordcloud = WordCloud(
    background_color="white",
    max_words=1000,
    mask=mask,
    contour_width=0,
    collocations=False,
    font_path=None,
    color_func=cor_aleatoria,
    width=3840,   # Largura em pixels para 4K
    height=2160,  # Altura em pixels para 4K
    scale=1       # Ajuste se necessário
).generate_from_frequencies(frequencias)

# Salva a imagem gerada em 4K
wordcloud.to_file("wordcloud_4k.png")

# Exibe a imagem (opcional)
plt.figure(figsize=(19.2, 10.8))  # Tamanho em polegadas para aproximar 4K em dpi=200 (ajuste se necessário)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
