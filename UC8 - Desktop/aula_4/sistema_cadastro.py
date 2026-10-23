import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, ttk
"""Import PhotoImage para trabalhar com imagens e ttk para widgets mais modernos"""
class Cadastro:
    def __init__(self,master):
        """Construtor da classe master e a janela principal da interface Tkinter"""
        self.master=master
        self.master.title("Sistemas de cadastro TabajaraCorp")
        self.master.geometry("950x850")
        self.master.configure(bg="#fdf5e6")
        """Define a cor de fundo da janela como pérola"""
        #Logo Principal
        self.imagem_logo=PhotoImage(file="logosenac.png")
        tk.Label(self.master,image=self.imagem_logo,bg="#fdf5e6").pack(pady=15)
        """Cria um rótulo para exibir a imagem da logo na janela principal"""
        self.nome_valor=""
        self.sobrenome_valor=""
        self.idade_valor=""
        self.endereco_valor=""
        self.cidade_valor=""
        self.bairro_valor=""
        self.uf_valor=""
        self.sexo_valor=""
        self.telefone_valor=""
        self.email_valor=""
        self.rg_valor=""
        self.cpf_valor=""

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

        """Frame principal para organizar os campos. Cria um frame, que é um cantêiner para agrupar outros widgets"""
        self.frame=tk.Frame(master,bg="#fdf5e6", padx=25, pady=25)
        self.frame.pack(fill="both",expand=True)
        """.pack com fill e expand faz com que o frame preencha todo o espaço disponivel na janela"""
        # Função auxiliar para criar Label+Entry
        def criar_campo(texto,variavel,linha):
            """Cria um label com formatação de forte e cor e alinhamento á esquerda"""
            tk.Label(self.frame,text=texto, font=("Arial",12,"bold"),fg="#333333",bg="#fdf5e6", anchor="w").grid(row=linha,column=0,sticky="w",pady=8)
            """Cria uma Entry com formatação de fonte,largura e borda"""
            tk.Entry(self.frame,textvariable=variavel,font=("Arial",12), width=35, relief="solid",bd=2).grid(row=linha,column=1,pady=8,padx=5)
        """Chama a função auxiliar para criar cada par de campo e rótulo"""
        criar_campo("Nome:", self.nome,0)
        criar_campo("Sobrenome:", self.sobrenome,1)
        criar_campo("Idade:", self.idade,2)
        criar_campo("Endereço:", self.endereco,3)
        criar_campo("Bairro:", self.bairro,4)
        criar_campo("Cidade:", self.cidade,5)
        estados= ["AC", "AL", "AP", "AM","BA","CE","DF","ES","GO","MA","MT","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]
        tk.Label(self.frame,text="Estados (UF):", font=("Arial",12,"bold"),fg="#333333",bg="#fdf5e6").grid(row=6,column=0,sticky="w",pady=8)
        self.uf.set(estados[0])  # Define o valor inicial do Combobox como o primeiro estado da lista
        self.cambo_uf=ttk.Combobox(self.frame,textvariable=self.uf,values=estados,font=("Arial",12),width=33,state="readonly")
        self.cambo_uf.grid(row=6,column=1,sticky="w",pady=8)
        tk.Label(self.frame,text="Sexo:", font=("Arial",12,"bold"),fg="#333333",bg="#fdf5e6").grid(row=7,column=0,sticky="w",pady=8)
        """Cria um frame para agrupar os RadioButtons"""
        sexo_frame=tk.Frame(self.frame,bg="#fdf5e6")
        sexo_frame.grid(row=7,column=1,sticky="w",pady=8)
        """Cria os RadioButtons. indicatorn=0 e relief=raised dão a eles uma aparência de botão"""
        tk.Radiobutton(sexo_frame,text="Masculino",variable=self.sexo,value="Masculino",font=("Arial",12),bg="#fdf5e6",indicatoron=0,relief="raised",width=12).pack(side="left",padx=5)
        tk.Radiobutton(sexo_frame,text="Feminino",variable=self.sexo,value="Feminino",font=("Arial",12),bg="#fdf5e6",indicatoron=0,relief="raised",width=12).pack(side="left",padx=5)
        criar_campo("Telefone:", self.telefone,8)
        criar_campo("Email:", self.email,9)
        criar_campo("RG:", self.rg,10)
        criar_campo("CPF:", self.cpf,11)

        """Botão de ação com layout aprimorado"""
        self.btn_frame=tk.Frame(self.frame,bg="#fdf5e6", pady=25)
        self.btn_frame.grid(row=12,column=0,columnspan=2)
        """Cria o botão salvar dados com estilo aprimorado (cor,fonte e borda)"""
        tk.Button(self.btn_frame,text="Salvar dados",command=self.salvar_dados,font=("Arial",12,"bold"),bg="#4CAF50",fg="white",width=18,relief="raised",bd=4).pack(side="left",padx=12)
        """Cria o botão exibir cadastro com estilo aprimorado (cor,fonte e borda)"""
        tk.Button(self.btn_frame,text="Exibir cadastro",command=self.exibir_cadastro,font=("Arial",12,"bold"),bg="#2196f3",fg="white",width=18,relief="raised",bd=4).pack(side="left",padx=12)
    
    def salvar_dados(self):
        """Salva os dados do cadastro em variáveis de instância"""
        self.nome_valor=self.nome.get()
        self.sobrenome_valor=self.sobrenome.get()
        self.idade_valor=self.idade.get()
        self.endereco_valor=self.endereco.get()
        self.bairro_valor=self.bairro.get()
        self.cidade_valor=self.cidade.get()
        self.uf_valor=self.uf.get()
        self.sexo_valor=self.sexo.get()
        self.telefone_valor=self.telefone.get()
        self.email_valor=self.email.get()
        self.rg_valor=self.rg.get()
        self.cpf_valor=self.cpf.get()

        messagebox.showinfo("Sucesso","Cadastro salvo com sucesso!")

        # Limpa os campos
        self.nome.set("")
        self.sobrenome("")
        self.idade.set("")
        self.endereco.set("")
        self.bairro.set("")
        self.cidade.set("")
        self.uf.set("")
        self.sexo.set("Feminino")
        self.telefone.set("")
        self.email.set("")
        self.rg.set("")
        self.cpf.set("")

    def exibir_cadastro(self):
        """Exibe os dados do cadastro em uma nova janela"""
        janela_resultado=tk.Toplevel(self.master)
        janela_resultado.title("Dados do usuário")
        janela_resultado.geometry("750x650")
        janela_resultado.configure(bg="#fdf5e6")

        """Logo maior no topo centralizado .subsample() reduz a imagem para metade do tamanho original"""
        logo_red=self.imagem_logo.subsample(2,2)
        tk.Label(janela_resultado,image=logo_red,bg="#fdf5e6").pack(pady=15)
        """tkCanvas é um widget que pode ser usado para desenhar ou conter outros widgets"""
        canvas=tk.Canvas(janela_resultado, bg="#fdf5e6",highlightthickness=0)
        """rkScrollbar cria uma barra de rolagem, orient=vertical define a direção"""
        scrollbar=tk.Scrollbar(janela_resultado, orient="vertical", command=canvas.yview)
        """Cria um frame dentro do canvas para conter os dados"""
        scroll_frame=tk.Frame(canvas,bg="#fdf5e6")
        """O método .bind() associa a uma dunção <configure> é o evento de redimensionamento do widget. A função lembda redimensiona a área de rolagem do canvas para caber todo o conteúdo do frame"""
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        """Cria a janela dentro do canvas. O conteúdo do scroll_frame será exibido aqui"""
        canvas.create_window((0,0), window=scroll_frame, anchor="nw")
        """Configura o canvas para usar a barra de rolagem para o movimento na vertical"""
        canvas.configure(yscrollcommand=scrollbar.set)
        """Posiciona o canvas e a barra de rolagem na janela"""
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        """Função para criar fram de dado"""

        def criar_frame_dado(texto):
            """Criar um frame com borda sólida e padding interno"""
            frame=tk.Frame(scroll_frame,bg="white",bd=1,relief="solid",padx=10,pady=5)
            """Empacota o fmrae, fazendo preencher a largura horizontal"""
            frame.pack(fill="x",pady=5,padx=20)
            tk.Label(frame,text=texto,font=("Arial",12,"bold"),bg="white").pack(anchor="w")
        """Exibe os dados em frame separados. Chama a função auxiliar para cada dado do cadastro, organizado-os em frames distintos"""
        criar_frame_dado(f"Nome Completo: {self.nome_valor} {self.sobrenome_valor}")
        criar_frame_dado(f"Idade: {self.idade_valor}")
        criar_frame_dado(f"Endereço: {self.endereco_valor}, Bairro: {self.bairro_valor}, Cidade: {self.cidade_valor}, UF: {self.uf_valor}")
        criar_frame_dado(f"Sexo: {self.sexo_valor}")
        criar_frame_dado(f"Telefone: {self.telefone_valor}")
        criar_frame_dado(f"Email: {self.email_valor}")
        criar_frame_dado(f"RG: {self.rg_valor}")
        criar_frame_dado(f"CPF: {self.cpf_valor}")

        """Mantém a referência da imagem para não desaparecer. O python pode colocar no lixo e remover a imagem da memoria se não houver referência a ela. [
        Ao atribuir a imagem a um atributo da janela, garantimos que ela permaneça na memória enquanto a janela estiver aberta."""
        janela_resultado.logo_red=logo_red


if __name__=="__main__":
    root=tk.Tk()
    app=Cadastro(root)
    root.mainloop()