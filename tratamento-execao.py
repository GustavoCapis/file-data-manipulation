# Uma exceção é um erro que acontece durante a execução do programa.

try:
    arquivo = open("teste.txt", "r")

except FileNotFoundError:
    print("Arquivo não encontrado")

except PermissionError:
    print("Sem permissão para abrir o arquivo")
    
# Python executa apenas o except que corresponde ao erro.

# Pegando a mensagem do erro
try:
    arquivo = open("teste.txt", "r")

except FileNotFoundError as erro:
    print("Erro:", erro)