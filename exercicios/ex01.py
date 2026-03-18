# Situação-problema
# Você foi contratado por uma empresa para desenvolver um script em Python que automatize a organização de arquivos de texto. A tarefa envolve ler o conteúdo de arquivos, processar essas informações, escrever em novos arquivos e tratar exceções que possam surgir, como arquivos inexistentes ou falta de permissões.

# Tarefa
# Implemente um script em Python que realize as seguintes operações:

# 1. Leia o conteúdo de um arquivo de texto.
# 2. Escreva o conteúdo lido em um novo arquivo, adicionando uma linha de cabeçalho.
# 3. Trate possíveis exceções durante as operações, exibindo mensagens informativas ao usuário.

def processar_arquivo(origem, destino):
    try:
        with open(origem, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    except PermissionError:
        print("Sem permissão para acessar arquivo.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return
    
    try:
        with open(destino, "w", encoding="utf-8") as f:
            f.write("CABEÇALHO\n")
            f.write(conteudo)
        print("Arquivo processado com sucesso!")
    except PermissionError:
        print("Sem permissão para escrever.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return
        
        
def main():
    import os

    origem = "projeto/arquivo_origem.txt"
    destino = "projeto/arquivo_destino.txt"
    
    processar_arquivo(origem,destino)
    
if __name__ == "__main__":
    main()
    