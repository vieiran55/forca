import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import json

class JogoDaForca:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo da Forca")
        self.janela.geometry("700x700")
        
        # Variaveis que precisam ser in
        self.letras_utilizadas_texto = ""
        self.label_letras_utilizadas = None
        self.entrada_letra = None
        self.palavra_escolhida = []
        self.letras_adivinhadas = []
        self.erros = 0  # Contador de erros
            # Lista para armazenar tuplas de (palavra, dica)
        self.palavras_e_dicas = []
        

        
        
        #fotos do enforcado
        self.enforcado = r".\assets\imgs\forca.png"
        self.enforcado1 = r".\assets\imgs\forca1.png"
        self.enforcado2 = r".\assets\imgs\forca2.png"
        self.enforcado3 = r".\assets\imgs\forca3.png"
        self.enforcado4 = r".\assets\imgs\forca4.png"
        self.enforcado5 = r".\assets\imgs\forca5.png"

        self.imagem_enforcado = self.enforcado
        
        # Rótulo do jogo
        self.titulo = tk.Label(janela, text="Jogo da Forca", font=("Arial", 24))
        self.titulo.pack(pady=20)

        # Carregar a imagem da forca
        self.imagem_forca = Image.open(r".\assets\imgs\forquilha.png")
        self.imagem_forca = self.imagem_forca.resize((400, 300))
        self.imagem_forca = ImageTk.PhotoImage(self.imagem_forca)

        # Rótulo para exibir a imagem da forca
        self.label_forca = tk.Label(janela, image=self.imagem_forca)
        self.label_forca.pack()

        # Criar um botão para começar o jogo
        self.botao_comecar = tk.Button(janela, text="Começar", command=self.iniciar_jogo)
        self.botao_comecar.pack(pady=40)

    def iniciar_jogo(self):
        # Reinicialize o contador de erros
        self.erros = 0
        # Abrir o arquivo palavras
        # Abrir o arquivo JSON
        with open(r".\assets\database\palavras.json", "r", encoding="utf-8") as arquivo_json:
            dados = json.load(arquivo_json)
            
        escolha = random.choice(dados)
        self.palavra_revelada = list(escolha["palavra"])
        self.palavra_escolhida = list(escolha["palavra"].strip().lower())
        self.dica = escolha["dica"]
        
        # Escolhendo uma palavra aleatória
        self.palavra_dica = random.choice(self.dica)

        # Limpe a Janela Principal
        self.limpar_janela_principal(self.palavra_escolhida)

        # Rótulo do jogo
        self.titulo = tk.Label(self.janela, text="Jogo da Forca", font=("Arial", 24))
        self.titulo.pack(pady=20)
        
                        # Carregar a imagem da forca
        self.naforca = Image.open(self.imagem_enforcado)
        self.naforca = self.naforca.resize((150, 100))
        self.naforca = ImageTk.PhotoImage(self.naforca)

        # Rótulo para exibir a imagem da win
        self.label_naforca = tk.Label(janela, image=self.naforca)
        self.label_naforca.pack()

        

        palavra_com_underscores = ["_" for _ in self.palavra_escolhida]

        # Exiba as lacunas correspondentes à palavra escolhida
        self.label_palavra = tk.Label(self.janela, text=" ".join(palavra_com_underscores), font=("Arial", 20))
        self.label_palavra.pack(pady=20)
        
                # Campo de entrada para inserir as letras
        self.label_dica = tk.Label(self.janela, text=f"{self.dica}", font=("Arial", 12))
        self.label_dica.pack(pady=10)
        

        # Campo de entrada para inserir as letras
        self.entrada_letra = tk.Entry(self.janela, font=("Arial", 12))
        self.entrada_letra.pack(pady=10)

        # Função para validar a entrada (permitir apenas 1 caractere)
        def validar_entrada(event):
            novo_valor = self.entrada_letra.get()
            if len(novo_valor) > 1:
                self.entrada_letra.delete(1, 'end')  # Remova todos os caracteres além do primeiro
            return True

        # Configurar a validação da entrada usando o evento KeyRelease
        self.entrada_letra.bind("<KeyRelease>", validar_entrada)

        # Botão para confirmar a letra inserida
        botao_confirmar = tk.Button(self.janela, text="Confirmar Letra", command=self.processar_letra)
        botao_confirmar.pack(pady=10)

        # Rótulo para exibir as letras utilizadas
        self.label_letras_utilizadas = tk.Label(self.janela, text="Letras Utilizadas: " + self.letras_utilizadas_texto, font=("Arial", 12))
        self.label_letras_utilizadas.pack(pady=10)
    
    def tela_vitoria(self):
    # Limpe a Janela Principal
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Exibir mensagem de vitória
        label_vitoria = tk.Label(self.janela, text="Parabéns! Você Sabe Muito!", font=("Arial", 24))
        label_vitoria.pack(pady=20)
        
        palavraCorreta = ''.join(self.palavra_revelada)
        label_palavraCorreta = tk.Label(self.janela, text=f"A palavra correta era {palavraCorreta}", font=("Arial", 20))
        label_palavraCorreta.pack(pady=20)
        
                # Carregar a imagem da forca
        self.imagem_win = Image.open(r".\assets\imgs\win.png")
        self.imagem_win = self.imagem_win.resize((400, 300))
        self.imagem_win = ImageTk.PhotoImage(self.imagem_win)

        # Rótulo para exibir a imagem da win
        self.label_win = tk.Label(janela, image=self.imagem_win)
        self.label_win.pack()

        # Botão para jogar novamente
        botao_jogar_novamente = tk.Button(self.janela, text="Jogar Novamente", command=self.iniciar_jogo)
        botao_jogar_novamente.pack(pady=20)
        
    def tela_derrota(self):
    # Limpe a Janela Principal
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Exibir mensagem de vitória
        label_vitoria = tk.Label(self.janela, text="Que Vacilo! Você Perdeu", font=("Arial", 24))
        label_vitoria.pack(pady=20)
        
                        # Carregar a imagem da forca
        self.imagem_lose = Image.open(r".\assets\imgs\lose.png")
        self.imagem_lose = self.imagem_lose.resize((400, 300))
        self.imagem_lose = ImageTk.PhotoImage(self.imagem_lose)

        # Rótulo para exibir a imagem da lose
        self.label_lose = tk.Label(janela, image=self.imagem_lose)
        self.label_lose.pack()

        # Botão para jogar novamente
        botao_jogar_novamente = tk.Button(self.janela, text="Jogar Novamente", command=self.iniciar_jogo)
        botao_jogar_novamente.pack(pady=20)

    def processar_letra(self):
        letra = self.entrada_letra.get()
        #print("Letra Inserida:", letra)  # Adicione esta linha para verificar a letra inserida
        # Verifique se a entrada não está vazia e se a letra não foi utilizada
        if letra and letra not in self.letras_utilizadas_texto:

            # Verifique se a letra está na palavra escolhida
            if letra in self.palavra_escolhida:
                #print("Letra está na palavra escolhida")  # Adicione esta linha para verificar a condição

                # Atualize as lacunas da palavra com a letra correta
                nova_palavra = []
                for char in self.palavra_escolhida:
                    if char == letra or char in self.letras_utilizadas_texto:
                        nova_palavra.append(char)
                    else:
                        nova_palavra.append("_")
                self.label_palavra.config(text=nova_palavra)  # Atualize a label com a lista de caracteres
                #print("Palavra da Label:", self.label_palavra.cget("text"))  # Verifique a palavra da label após a atualização

                # Adicione a letra correta à lista de letras adivinhadas
                self.letras_adivinhadas.append(letra)
                #print("Letras Adivinhadas:", self.letras_adivinhadas)  # Verifique a lista de letras adivinhadas

                # Verifique se todas as letras foram adivinhadas
                if set(self.palavra_escolhida) == set(self.letras_adivinhadas):
                    # messagebox.showinfo("Parabéns!", "Você Adivinhou a palavra")
                    self.tela_vitoria()
                    self.letras_adivinhadas = []
                    # Reiniciar o jogo
            else:
                # A letra está incorreta()
                self.letra_incorreta()
                self.erros += 1  # Incrementar o contador de erros
                
                # Atualize a imagem do enforcado
                if self.erros <= 5:
                    nova_imagem_enforcado = Image.open(getattr(self, f'enforcado{self.erros}'))
                    nova_imagem_enforcado = nova_imagem_enforcado.resize((150, 100))
                    nova_imagem_enforcado = ImageTk.PhotoImage(nova_imagem_enforcado)
                    self.label_naforca.configure(image=nova_imagem_enforcado)
                    self.label_naforca.image = nova_imagem_enforcado

                # Verificar se o jogador atingiu o limite de erros (5 erros)
                if self.erros == 6:
                    self.tela_derrota()
                    self.letras_adivinhadas = []

            self.entrada_letra.delete(0, 'end')  # Limpe o campo de entrada

            # Atualizar as letras utilizadas
            self.letras_utilizadas_texto += letra + " "
            self.label_letras_utilizadas.config(text="Letras Utilizadas: " + self.letras_utilizadas_texto)
        else:
            # Exibir uma mensagem de erro ou feedback
            self.letra_invalida()
            #print("Entrada Inválida")



    # Função da letra inválida
    def letra_invalida(self):
        messagebox.showwarning("Aviso!", "Você ja usou essa letra!")

    def letra_incorreta(self):
        #print("Letra incorreta chamada")  # Adicione esta linha para verificar quando a função é chamada
        messagebox.showwarning("Aviso!", "Letra incorreta")

    def limpar_janela_principal(self, palavra_escolhida):
        self.letras_utilizadas_texto = ""  # Limpe a lista de letras utilizadas

        for widget in self.janela.winfo_children():
            widget.destroy()

        #print("Palavra escolhida:", palavra_escolhida)

if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoDaForca(janela)
    janela.mainloop()
