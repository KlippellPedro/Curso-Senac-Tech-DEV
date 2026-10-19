import tkinter as tk
"""Rodar o comando no ctrl+j: pip install tkinter"""
"""
tkinter é uma biblioteca para a criação de interface grafica (janelas). Com ele conseguimos criar botões, caixas de texto, menus e etc.
"""
from tkinter import messagebox
"""
Importa o módulo messagebox para exibir uma caixa de diálogo
"""
class Cadastro:
    def __init__(self, master):
        """O master é a janela principal (root) passada como parâmetro. Dentro do construtor vamos moontar os elementos da tela"""
        self.nome=""
        self.sobrenome=""
        self.idade=0

        self.label_nome=tk.Label(master, text="Nome:")
        """Label= rótulo de texto fixo na tela. Cria um rótulo de texto. O master informa qual janela este rótulo pertence"""
        self.label_nome.pack()
        """Método pack() é um gerenciador de layout que organiza e exibe o rótulo na janela"""
        self.entry_nome=tk.Entry(master)
        """Entry = caixa de entrada de texto (onde o usuario digita alguma coisa). Cria uma caixa de texto"""
        self.entry_nome.pack()

        """Vamos criar o rótulo para o sobrenome"""
        self.label_sobrenome=tk.Label(master,text="Sobrenome:")
        self.label_sobrenome.pack()
        self.entry_sobrenome=tk.Entry(master)
        self.entry_sobrenome.pack()

        """Vamos criar o rótulo para idade"""
        self.label_idade=tk.Label(master,text="Idade:")
        self.label_idade.pack()
        self.entry_idade=tk.Entry(master)
        self.entry_idade.pack()

        """Criar um botão"""
        self.botao_salvar=tk.Button(master, text="Salvar dados", command=self.coletar_dados)
        """Cria um botão com o texto salvar dados.
        O parâmetro command, associa o botão a um método da classe coletar_dados"""
        self.botao_salvar.pack(pady=5)
        """Exibe o botão e adiciona um espaço vertical (padding) de 5px"""
        self.botao_exibir=tk.Button(master, text="Exibir dados", command=self.exibir_dados)
        self.botao_exibir.pack(pady=5)

    def coletar_dados(self):
        self.nome=self.entry_nome.get()
        """Captura o texto digitado na caixa, usando o método get()"""
        self.sobrenome=self.entry_sobrenome.get()
        """A idade precisa ser convertida para numero inteiro, pois o get() sempre retorna string"""
        try:
            self.idade =int(self.entry_idade.get())
            """Tenta converter o texto da idade em numero"""
        except ValueError:
            """Caso o usuario digite algo que não seja numero, a exeção é capturada"""
            messagebox.showerror("Erro", "Por favor, digite um número válido para idade.")
            self.idade= 0 # Retorna a idade pra 0
            return
        
        """Verifica se todos os campos foram preenchidos corretamente"""
        if self.nome and self.sobrenome and self.idade >0:
            # Mostra a caixa de diálogo de sucesso
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            self.limpar_campo()
        else:
            """Caso algum campo esteja vazio, mostra uma menssagem de aviso"""
            messagebox.showwarning("Aviso", "Preencha todos os campos antes de salvar")
    
    def exibir_dados(self):
        """Exibe os dados cadastrados em uma janela pop-up"""
        if self.nome and self.sobrenome and self.idade > 0:
            # Cria a mensagem a ser exibida
            mensagem= f"Nome completo: {self.nome} {self.sobrenome}\nIdade: {self.idade} anos"
            messagebox.showinfo("Dados cadastrados", mensagem)
        else:
            messagebox.showwarning("Aviso", "Nenhum dado valido foi salvo ainda.")
        
    def limpar_campos(self):
        """Limpar os campos de texto após salvar os dados"""
        self.entry_nome.delete(0,tk.END)
        self.entry_sobrenome.delete(0,tk.END)
        self.entry_idade.delete(0,tk.END)
        """Método delete, apaga o conteudo de um campo de entrada. Is parâmetros (0, tk.END) indicam que o texto será apagado do início (indice 0) até o fim"""
    
if __name__ == "__main__":
    # Criação da janela principal
    root= tk.Tk() # Cria a janela principal da interface
    root.title("Sistema de cadastro")
    root.geometry("300x250")# Define o tamanho da janela
    
    """Criado o objeto da classe Cadastro e passando a janela principal (root) como argumento"""
    app= Cadastro(root)

    """Inicia o loop principal da interface. Este método mantém a janela ativa e executando as interações do usuario como cliques e digitações. O programa só termina quando a janela é fechada"""
    root.mainloop()