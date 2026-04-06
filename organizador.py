import os
from pathlib import Path
import shutil

# === CONFIG ===
PASTA_ALVO = Path.cwd()  # pasta onde o script está

MAPA_PASTAS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
    "PDFs": [".pdf"],
    "Documentos": [".docx", ".doc", ".txt"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Áudios": [".mp3", ".wav"],
    "Vídeos": [".mp4", ".mkv", ".avi"],
}

def criar_pastas():
    for pasta in MAPA_PASTAS:
        (PASTA_ALVO / pasta).mkdir(exist_ok=True)

def descobrir_destino(extensao):
    for pasta, extensoes in MAPA_PASTAS.items():
        if extensao.lower() in extensoes:
            return pasta
    return None

def renomear_arquivo(pasta_destino, extensao):
    arquivos = list((PASTA_ALVO / pasta_destino).glob(f"*{extensao}"))
    numero = len(arquivos) + 1
    prefixos = {
        "Imagens": "IMG",
        "PDFs": "PDF",
        "Documentos": "DOC",
        "Planilhas": "XLS",
        "Áudios": "AUD",
        "Vídeos": "VID",
    }
    prefixo = prefixos.get(pasta_destino, "ARQ")
    return f"{prefixo}_{numero:03}{extensao}"

def organizar():
    for arquivo in PASTA_ALVO.iterdir():
        if arquivo.is_file():
            extensao = arquivo.suffix
            destino = descobrir_destino(extensao)

            if destino:
                novo_nome = renomear_arquivo(destino, extensao)
                caminho_destino = PASTA_ALVO / destino / novo_nome
                shutil.move(str(arquivo), str(caminho_destino))
                print(f"Movido: {arquivo.name} -> {destino}/{novo_nome}")

if __name__ == "__main__":
    criar_pastas()
    organizar()
    print("\n✅ Organização concluída!")