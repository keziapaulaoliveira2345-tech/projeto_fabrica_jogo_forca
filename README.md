
# 🎯 Jogo da Forca

Bem-vindo ao **Jogo da Forca**, um divertido jogo em Python onde o jogador tenta adivinhar uma palavra secreta, letra por letra, com até **6 erros permitidos**.

---

## 🕹️ Como Jogar

1. Execute o script `forca.py`.
2. Uma palavra secreta será selecionada aleatoriamente a partir de um arquivo de palavras.
3. Tente adivinhar a palavra **uma letra por vez**.
4. Você tem **6 chances** para errar antes de perder o jogo.
5. O jogo termina quando você:

   * Acerta todas as letras da palavra → **Você ganha!** 🏆
   * Comete 6 erros → **Você perde!** 💀

---

## 💻 Executando o Jogo

Certifique-se de ter **Python 3.x** instalado no seu computador.

```bash
# Clone o repositório
git clone <URL_DO_REPOSITORIO>

# Entre na pasta do projeto
cd forca

# Execute o jogo
python forca.py
```

> ⚠️ **Atenção:** Atualize o caminho do arquivo `palavras_forca.txt` dentro da função `carrega_palavra_secreta()` para o diretório correto no seu computador.

---

## 🛠️ Funcionalidades

* Seleção aleatória de palavras a partir de um arquivo de texto.
* Contador de erros do jogador (até 6).
* Interface em linha de comando simples e intuitiva.
* Mensagens de vitória e derrota.

---

## 📂 Estrutura do Projeto

```
forca/
│
├── forca.py               # Código principal do jogo
├── palavras_forca.txt     # Lista de palavras secretas
└── README.md              # Documentação do projeto
```

---

## 🔧 Melhorias Futuras

* Adicionar **categorias de palavras** (animais, frutas, países, etc.).
* Implementar **interface gráfica** com `Tkinter` ou `PyGame`.
* Registrar **pontuação e histórico de jogos**.

---

## 👩‍💻 Sobre o Projeto

Este projeto é um ótimo exercício para praticar:

* Estruturas de repetição (`while`, `for`)
* Condicionais (`if/else`)
* Manipulação de arquivos (`open`, `read`, `close`)
* Funções em Python
* Lógica de jogos

