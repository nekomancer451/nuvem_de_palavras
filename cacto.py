import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# Carrega a máscara (certifique-se de que "cacto2.png" está em alta resolução)
mask = np.array(Image.open("cacto2.png"))

# Lista de expressões
palavras = [
    "ôxe", "caçar conversa", "paia", "lapois", "aí dentro", "migué", "égua",
    "estribado","lá ele", "aperreio", "fuleiragem", "vixe", "pagar sapo", "tá ca peste", "ficar bestando",  
    "meu rei", "arreado", "frescar", "na doida", "armaria", "kiu!", "esparroso", 
    "apombalado", "peba", "só quer ser as pregas", "tá com a gota serena", "tabacudo", 
    "pirangueiro", "dispense", "galalau", "vou chegar", "barril", "tô na bruxa",
    "fazer munganga", "buliçoso", "boy", "boe", "de rocha",  "vôti", 
    "cambito", "morgado", "mangar", "tá com a bexiga lixa", "avexado"
    "tá com a bubônica", "torar", "traquino", "massa", "brocado", "o raio", "triscar",
]

# Dicionário de frequências
frequencias = {expressao: 120 for expressao in palavras}

# Paleta de cores
cores = [
    "#3A5F0B", "#6B8E23", "#A0522D", "#8B4513", "#D2B48C",
    "#9ACD32", "#556B2F", "#BDB76B", "#CD853F", "#FFD700"
]

cores_palavras = {}

def cor_aleatoria(palavra, font_size, position, orientation, random_state, **kwargs):
    if palavra not in cores_palavras:
        cores_palavras[palavra] = random.choice(cores)
    return cores_palavras[palavra]

# Gera a nuvem de palavras com qualidade máxima (600 DPI - 7020 × 9900 pixels)
wordcloud = WordCloud(
    background_color="white",
    max_words=2000,
    mask=mask,
    contour_width=2,
    collocations=False,
    font_path=None,
    color_func=cor_aleatoria,
    width=7020,  # 600 DPI largura para folha A3
    height=9900,  # 600 DPI altura para folha A3
    scale=2  # Multiplica a densidade para garantir mais nitidez
).generate_from_frequencies(frequencias)

# Salva a imagem em alta resolução para impressão
wordcloud.to_file("wordcloud_A3_600dpi.png")

# Exibe a imagem (opcional)
plt.figure(figsize=(19.2, 27.5))  # Mantém a proporção A3
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
