# ANAGRAM_CHECKER_PT-BR
 Meu primeiro repositorio!


# Verificador de Anagramas

Este projeto contém dois programas para verificar se duas palavras são anagramas. Um deles é uma versão para terminal (`main.py`) que na época eu estava aprendendo, e o outro é uma versão do mesmo com interface gráfica (`anagram_gui.py`) de quando eu estava praticando.

---

## 📁 Estrutura do Projeto

```
ANAGRAM_CHECKER_PT-BR/
├── main.py              # Programa de terminal e versão inicial
├── anagram_gui.py       # Programa com interface gráfica e um pouco mais polido

```

---

## 🖥️ `main.py` (Terminal)

### **Descrição:**
Este programa roda no terminal e verifica se duas palavras são anagramas. Ele solicita que o usuário insira duas palavras e valida se elas contêm apenas letras. O programa repete o processo indefinidamente até ser interrompido manualmente.

### **Como Executar:**
1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta do projeto no terminal.
3. Execute o comando:
   ```bash
   python main.py
   ```

### **Funcionalidades:**
- Valida se as entradas são apenas letras.
- Verifica se as palavras têm o mesmo comprimento.
- Compara as palavras ordenadas para determinar se são anagramas.
- Loop infinito para repetir o processo.

---

## 🖼️ `anagram_gui.py` (Interface Gráfica)

### **Descrição:**
Este programa oferece uma interface gráfica (GUI) usando Tkinter para verificar anagramas. O usuário insere duas palavras em campos de texto, e o programa exibe o resultado em uma caixa de mensagem.

### **Como Executar:**
1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta do projeto no terminal.
3. Execute o comando:
   ```bash
   python anagram_gui.py
   ```

### **Funcionalidades:**
- Interface gráfica amigável.
- Valida se as entradas são apenas letras.
- Verifica se as palavras têm o mesmo comprimento. Caso não tenham, o usuário será avisado.
- Compara as palavras ordenadas para determinar se são anagramas.
- Limpa os campos de entrada quando o resultado for TRUE, permitindo repetir o processo sem fechar a janela.
- Mantem as palavras se o resultado for FALSE, permitindo que o usuário corrija se digitou errado e tente outra vez.

---

## 📋 Requisitos

- Python 3.x
- Biblioteca Tkinter (já vem com o Python)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✉️ Contato

Se tiver dúvidas ou sugestões, entre em contato:  
- **Nome:** [João Elber]  
- **Email:** [joaoelberflu18@gmail.com]  
- **GitHub:** [DyausJelber]

---

