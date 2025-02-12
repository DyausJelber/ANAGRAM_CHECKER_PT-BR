def eh_anagrama(word1, word2):

    # Converte as palavras para minúsculas para garantir q a comparação seja case-insensitive.
    word1 = word1.lower()
    word2 = word2.lower()

    # Se o comprimento da word1 for diferente do comprimento da word2, retorna False.
    if len(word1) != len(word2):
        return False

    # Ordena as letras das palavras e as compara. Se forem iguais, são anagramas.
    return sorted(word1) == sorted(word2)

def main():

    while True:  # Adiciona um loop infinito para repetir o processo.
        # Captura a entrada do usuário para as duas palavras.
        word1 = input("Digite a primeira palavra: ")
        word2 = input("Digite a segunda palavra: ")

        # Valida se as entradas são compostas apenas por letras. Caso contrário, exibe uma mensagem de erro.
        if not word1.isalpha() or not word2.isalpha():
            print("Por favor, digite apenas letras.")
            continue  # Retorna ao início do loop

        # Chama a função eh_anagrama para verificar se as palavras são anagramas e imprime o resultado.
        if eh_anagrama(word1, word2):
            print(f"As palavras {word1} e {word2} são anagramas!")
        else:
            print(f"As palavras {word1} e {word2} não são anagramas.")

# Verifica se o script está sendo executado diretamente e chama a função main.
if __name__ == "__main__":
    main()