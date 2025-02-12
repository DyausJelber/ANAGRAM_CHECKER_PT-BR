import tkinter as tk
from tkinter import messagebox

# O main.py só roda no terminal. Então eu criei uma nova file para praticar usando o Tkinter dessa vez.
# Assim como o main.py usei (isalhpa) para validar se as entradas são apenas letras.
# Eu resolvi manter o loop de maneira diferente. O loop só ocorrerá se o resultado for True.
# No main.py o loop acontecia sempre, mesmo que o resultado fosse True ou False.

def anagram_verifier():
    word1 = input1.get().lower()
    word2 = input2.get().lower()
# As entradas do usuário.
    if not word1.isalpha() or not word2.isalpha():
        messagebox.showerror("Erro", "Por favor, digite apenas letras.")
        return
# Valida se as palavras são compostas apenas de letras. Se houver número aparece uma mensagem de erro.
    if len(word1) != len(word2):
        messagebox.showinfo("Resultado", f"As palavras {word1} e {word2} não são anagramas já que as duas tem comprimentos diferentes.")
        return
# Se as palavras não tiverem o mesmo comprimento o resultado será False.
    messagebox.showinfo("Resultado", f"As palavras {word1} e {word2} são anagramas!" if sorted(word1) == sorted(
        word2) and input1.delete(0, tk.END) == input2.delete(0, tk.END)
# Limpa os campos de entrada para uma nova verificação.
    else f"As palavras {word1} e {word2} não são anagramas.")
#Se os resultados forem False. Manterá as entradas intactas para o usuario corrigir.

# Configuração da janela
window = tk.Tk()
window.title("Verificador de Anagramas")
window.geometry("250x190")

# Elementos da interface
tk.Label(window, text="Digite a primeira palavra: ").pack(pady=5)
input1 = tk.Entry(window)
input1.pack(pady=5)

tk.Label(window, text="Digite a segunda palavra: ").pack(pady=5)
input2 = tk.Entry(window)
input2.pack(pady=5)

tk.Button(window, text="Verificar", command=anagram_verifier).pack(pady=10)

window.mainloop()