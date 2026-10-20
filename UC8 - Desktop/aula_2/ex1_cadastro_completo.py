import tkinter as tk
from tkinter import messagebox

class Cadastro:
    def __init__(self, master):
        self.master=master
        self.master.title("Sistema de cadastro TabajaraCorp")
        self.master.geometry("800x700")

        self.nome_valor=""
        self.sobrenome_valor=""
        self.idade_valor=""
        self.endereco_valor=""
        self.bairro_valor=""
        self.cidade_valor=""
        self.uf_valor=""
        self.sexo_valor=""
        self.telefone_valor=""
        self.email_valor=""
        self.rg_valor=""
        self.cpf_valor=""

        """tk.StringVar() é uma classe especial do tkinter que armazena uma string e pode ser vinculada a widgets de entrada (Entry, Label e etc) Quando o conteúdo do widgets muda, 
        a variável também muda automaticamente"""

        self.nome= tk.StringVar()
        self.sobrenome= tk.StringVar()
        self.idade= tk.StringVar()
        self.endereco= tk.StringVar()
        self.bairro= tk.StringVar()
        self.cidade= tk.StringVar()
        self.uf= tk.StringVar()
        self.sexo= tk.StringVar(value="Feminino")
        self.telefone= tk.StringVar()
        self.email= tk.StringVar()
        self.rg= tk.StringVar()
        self.cpf= tk.StringVar()

        """Labels e campos de entrada. Cria um label (rótulo) e uma Entry (caixa de entrada) para nome. O parâmetro textvariable vincula a entrada á variavel tkStringVar"""

        tk.Label(master, text="Nome:").pack()
        tk.Entry(master, textvariable=self.nome).pack()

        tk.Label(master, text="Sobreome:").pack()
        tk.Entry(master, textvariable=self.sobrenome).pack()

        tk.Label(master, text="Idade:").pack()
        tk.Entry(master, textvariable=self.idade).pack()

        tk.Label(master, text="Endereço:").pack()
        tk.Entry(master, textvariable=self.endereco).pack()

        tk.Label(master, text="Bairro:").pack()
        tk.Entry(master, textvariable=self.bairro).pack()

        tk.Label(master, text="Cidade:").pack()
        tk.Entry(master, textvariable=self.cidade).pack()

        # Cria uma lista de estados do Brasil
        estados= [
            "AC", "AL", "AP", "AM","BA","CE","DF","ES","GO","MA","MT","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]
        tk.Label(master, text="Estado (UF):").pack()
        self.uf.set(estados[0])
        # Define o valor inicial do campo UF como o primeiro estado da lista
        tk.OptionMenu(master, self.uf, *estados).pack()
        """tk.OptionMenu cria um menu suspenso. O primeiro parâmetro é a janela. O segundo é a variavel tk.StringVar associada e o * desempacota a lista de estados 
        para que cada item se torne  uma opção do menu"""

        tk.Label(master, text="Sexo:").pack()
        tk.Radiobutton(master, text="Masculino", variable=self.sexo, value="Masculino").pack
        tk.Radiobutton(master, text="Feminino", variable=self.sexo, value="Feminino").pack

        tk.Label(master, text="Telefone:").pack()
        tk.Entry(master, textvariable=self.telefone).pack()

        tk.Label(master, text="Email:").pack()
        tk.Entry(master, textvariable=self.email).pack()

        tk.Label(master, text="RG:").pack()
        tk.Entry(master, textvariable=self.rg).pack()

        tk.Label(master, text="CPF:").pack()
        tk.Entry(master, textvariable=self.cpf).pack()

        tk.Button(master, text="Salvar dados", command=self.salvar_dados).pack(pady=10)
        tk.Button(master, text="Exibir dados", command=self.exibir_dados).pack(pady=10)
    
    def salvar_dados(self):
        """Salva os dados digitados nos atributos da classe. Exibe mandagem de confirmação e limpa os campos de entrada"""

        """O método get() é usado para obter o valor atual da variavel tk.StringVar. Os valores dos campos de ntradas são copiados para os atributos normais da calsse"""
        self.nome_valor= self.nome.get()
        self.sobrenome_valor= self.sobrenome.get()
        self.idade_valor= self.idade.get()
        self.endereco_valor= self.endereco.get()
        self.bairro_valor= self.bairro.get()
        self.cidade_valor= self.cidade.get()
        self.uf_valor= self.uf.get()
        self.sexo_valor= self.sexo.get()
        self.telefone_valor= self.telefone.get()
        self.email_valor= self.email.get()
        self.rg_valor= self.rg.get()
        self.cpf_valor= self.cpf.get()

        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        """Limpa os campos para nova digitação"""
        self.nome.set("")
        self.sobrenome.set("")
        self.idade.set("")
        self.endereco.set("")
        self.bairro.set("")
        self.cidade.set("")
        self.uf.set("")
        self.sexo.set("")
        self.telefone.set("")
        self.email.set("")
        self.rg.set("")
        self.cpf.set("")

    # Método para exibir os dados
    def exibir_dados(self):
        """Abrir uma janela e exibir todos os dados salvos"""
        janela_dados= tk.Toplevel(self.master)
        """tk.Toplevel() cria uma nova janela que sobrepõe a pricipal"""
        janela_dados.title("Dados do usuário")
        janela_dados.geometry("600x500")

        tk.Label(janela_dados, text=f"Nome completo: {self.nome_valor}{self.sobrenome_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"Idade: {self.idade_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"Endereço: {self.endereco_valor}, Bairro: {self.bairro_valor}, Cidade: {self.cidade_valor}, Estado: {self.uf_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"Sexo: {self.sexo_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"Telefone: {self.telefone_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"Email: {self.email_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"RG: {self.rg_valor}").pack(anchor="w", padx=10, pady=5)
        tk.Label(janela_dados, text=f"CPF: {self.cpf_valor}").pack(anchor="w", padx=10, pady=5)

if __name__ == "__main__":
    root =tk.Tk() # Criar uma janela principal da aplicação
    app = Cadastro(root) # Cria um objeto da classe cadastro
    root.mainloop()
    """Inicia o loop principal e mantém a janela aberta e interativa"""