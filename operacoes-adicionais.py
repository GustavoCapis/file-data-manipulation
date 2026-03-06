# Remover arquivos
import os

os.remove("teste.txt")
#Se estiver em outro lugar:
os.remove("pasta/teste.txt")

# Renomear arquivos
# Parâmetros: os.rename(origem, destino)
os.rename("arquivo_antigo.txt", "arquivo_novo.txt")


# Sobrescrever arquivos
os.replace("arquivo1.txt", "arquivo2.txt")