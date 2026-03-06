# Criar diretório
import os

os.mkdir("meu_diretorio")

# Remover diretório
import os

os.rmdir("meu_diretorio")

# Listar diretório
os.scandir()
# Cada item retornado pelo scandir() é um objeto DirEntry.

for entrada in os.scandir("meu_diretorio"):
    
    print("Nome:", entrada.name)
    print("Caminho:", entrada.path)

    if entrada.is_file():
        print("É um arquivo")

    if entrada.is_dir():
        print("É um diretório")

    print("------")


#OSError: é um erro genérico do sistema operacional.

#Então você pode verificar o número do erro usando: erro.errno
import errno

try:
    os.rmdir("meu_diretorio")

except OSError as erro:
    if erro.errno == errno.ENOTEMPTY:
        print("Diretório não está vazio")