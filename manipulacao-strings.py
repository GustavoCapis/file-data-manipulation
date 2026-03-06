# strip()
# Remove espaços e quebras de linha do começo e do fim.
linha = "   Olá mundo \n"
print(linha.strip())

# count()
# Conta quantas vezes uma substring aparece.
texto = "Olá Olá Olá"
print(texto.count("Olá"))

# split()
# Quebra uma string em lista de palavras.
frase = "Eu amo programar"
palavras = frase.split()
print(palavras)
# Com separador
texto = "carro,moto,avião"
print(texto.split(","))

# join()
# Faz o contrário do split: junta lista em string.
lista = ["Python", "é", "legal"]
texto = " ".join(lista)
print(texto)
print("\n".join(lista))

# Exemplo em programas reais
texto = "Eu amo programar"

palavras = texto.split()
palavras_maiusculas = [p.upper() for p in palavras]

resultado = " ".join(palavras_maiusculas)

print(resultado)