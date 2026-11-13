import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from controllers.sistema import Sistema
from models.pagamento import Pagamento
from models.carrinho import Carrinho

def configurar_estilo():
    style = ttk.Style()
    # Define o tema clam, que permite personalizar diversos aspectos visuais
    style.theme_use('clam')
    # Armazena o código da cor de fundo
    cor_fundo_claro = '#e0f7fa'
    # Armazena a cor de fundo principal
    cor_fundo_principal = '#b2ebf2'
    '''Define a cor de fundo e a fonte padrão dos componentes ttk'''
    style.configure('.', background=cor_fundo_principal, 
                    font=('Helvetica', 10))
    '''Configura os rótulos, definindo o fundo, cor do texto e tamanho da fonte'''
    style.configure('TLabel', background=cor_fundo_principal, 
                    foreground='#004d40', font=('Helvetica', 12))
    # Cria um estilo personalizado para os títulos da aplicação
    style.configure('Titulo.TLabel', font=('Helvetica', 18, 'bold'), 
                    foreground='#006064')
    # Configura os frames, definindo a cor de fundo e o tipo de borda
    style.configure('TFrame', background=cor_fundo_claro, 
                    relief='groove')
    # Define a aparência inicial dos botões personalizados
    style.configure('Custom.TButton', background='#00bcd4', foreground='white',
                    font=('Helvetica', 10, 'bold'), padding=10, 
                    relief='raised', borderwidth=5)
    # Define como o botão personalizado deve aparecer em diferentes estados
    style.map('Custom.TButton', 
              background=[('active', '#0097a7'), ('pressed', '#006978')],#Altyera a cor de fundo ao passar o mouse
              foreground=[('active', 'white'), ('pressed', 'white')],#Define cor do texto quando o botão está ativo
              relief=[('pressed', 'sunken'), ('!pressed', 'raised')],
              #Deixa a borda com aparência pressionada quando clicada
              )
    # Define a aparência dos botões utilizados em ações de alerta
    style.configure('Alerta.TButton', background='#ffc107', foreground='black',
                    font=('Helvetica', 10, 'bold'), padding=10)
    # Altera a cor de fundo do botão de alerta quando ele está ativo
    style.map('Alerta.TButton', background=[('active', '#ffb300')])

'''Classe principal da interface.
Ela herda de tk.Tk, que representa a janela principal do programa'''
class AppGUI(tk.Tk):
    def __init__(self):
        # Inicializa a janela principal da classe Tkinter.
        super().__init__()
        self.title("Sistema de Mercado")
        self.geometry("800x600")
        # Inicializa as regras de negócio, produtos e controle do caixa
        self.sistema = Sistema()
        # Executa a função que configura os estilos da interface
        configurar_estilo()
        ''' Inicializa a variável que armazenará o tipo de usuário conectado.
        O valor None indica que ainda não há usuário autenticado'''
        self.usuario_logado = None
        # Cria um frame que servirá como área para organizar as telas
        self.container = ttk.Frame(self)
        # Posiciona o container no topo e permite que ocupe toda a área disponível
        self.container.pack(side="top", fill="both", expand=True)
        # Permite que a primeira linha do container se expanda verticalmente
        self.container.grid_rowconfigure(0, weight=1)
        # Permite que a primeira coluna do container se expanda horizontalmente
        self.container.grid_columnconfigure(0, weight=1)
        # Cria um dicionário para armazenar as diferentes telas da aplicação
        self.frames = {}
        # Percorre as classes que representam as telas do sistema
        for F in (LoginFrame, CaixaFrame, AdminFrame, RelatoriosFrame):
            '''Cria uma instância da tela atual dentro do container.
            O segundo argumento é a referência à janela principal'''
            frame = F(self.container, self)
            # Armazena a tela no dicionário, utilizando sua classe como chave
            self.frames[F] = frame
            '''Posiciona a tela na primeira linha e coluna do container.
            sticky="nsew" faz a tela ocupar todas as direções disponíveis'''
            frame.grid(row=0, column=0, sticky="nsew")
        # Exibe inicialmente a tela de login
        self.mostrar_frame(LoginFrame) 

    def mostrar_frame(self, cont):
        # Recupera do dicionário a instância correspondente à tela solicitada
        frame = self.frames[cont]
        # Verifica se a tela solicitada é a tela do operador de caixa
        if cont == CaixaFrame:
            # Atualiza a lista de produtos antes de exibir a tela do caixa
            frame.atualizar_produtos()

        # Coloca a tela selecionada na frente das demais telas
        frame.tkraise()

    # Define o método que verifica as credenciais informadas no login
    def realizar_login(self, username, password):
        # Verifica se o usuário informou o nome admin e a senha 123
        if username == "admin" and password == "123":
            # Registra que o usuário conectado possui perfil administrador
            self.usuario_logado = "admin"
            # Exibe a tela administrativa
            self.mostrar_frame(AdminFrame)
            messagebox.showinfo("Login", "Bem-vindo, Administrador")
            return True
        elif username == "caixa" and password == "123":
            # Registra que o usuário conectado é o operador de caixa
            self.usuario_logado = 'caixa'
            self.mostrar_frame(CaixaFrame)
            messagebox.showinfo("Login", "Bem-vindo, Operador do caixa")
            return True

        else:
            messagebox.showerror("Erro de login", "Usuário ou senha inválidos.")
            return False

    def logout(self):
        self.usuario_logado = None
        self.mostrar_frame(LoginFrame)

''' Tela de login'''
class LoginFrame(ttk.Frame):
    
    def __init__(self, parent, controller):

        # Inicializa o frame e aplica o estilo visual configurado
        super().__init__(parent, style='TFrame')
        # Armazena a referência à aplicação principal para acessar seus métodos
        self.controller = controller
        '''Cria um frame interno para agrupar os componentes de login.
        padding define o espaçamento interno em cada lado'''
        login_frame = ttk.Frame(self, style='TFrame', padding="20 20 20 20")
        '''Posiciona o frame no centro da tela'''
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        '''Cria o título da tela de login.
        grid posiciona o componente na linha 0, ocupando duas colunas'''
        ttk.Label(login_frame, text="Acesso ao Sistema", 
                  style='Titulo.TLabel').grid(row=0, column=0, columnspan=2, pady=10)
        '''Cria o rótulo que identifica o campo de usuário.
        sticky='w' alinha o texto à esquerda'''
        ttk.Label(login_frame, text="Usuário:").grid(row=1,column=0,padx=5,pady=5,sticky='w')
        # Cria o campo de entrada para digitar o nome de usuário
        self.user_entry = ttk.Entry(login_frame, width=30)
        # Posiciona o campo de usuário na primeira linha de entrada
        self.user_entry.grid(row=1,column=1,padx=5,pady=5)
        # Preenche o campo de usuário inicialmente com o texto caixa
        self.user_entry.insert(0, 'caixa')
        # Continuamos amanhã....

        # Cria o rótulo que identifica o campo de senha
        ttk.Label(login_frame, text="Senha:").grid(row=2,column=0, 
        padx=5, pady=5, sticky='w')
        '''Cria o campo de senha.
        show="*" substitui os caracteres digitados por asteriscos'''
        self.pass_entry = ttk.Entry(login_frame, show="*", width=30)
        '''Posiciona o campo de senha na segunda linha de entrada'''
        self.pass_entry.grid(row=2, column=1, padx=5, pady=5)
        # Preenche inicialmente o campo de senha com 123
        self.pass_entry.insert(0, '123')

        '''Cria o botão de entrar.
        command define o método executado quando o botão é clicado.
        style aplica a aparência personalizada do botão'''
        login_button = ttk.Button(login_frame, text="Entrar",
        command=self._login_click, style='Custom.TButton')

        # Posiciona o botão abaixo dos campos de usuário e senha
        login_button.grid(row=3, column=0, columnspan=2, pady=15)

        '''Associa a tecla Enter à tentativa de login.
        lambda permite chamar o método sem passar diretamente o evento'''
        self.bind('<Return>', lambda event: self._login_click())

    # Método executado quando o usuário tenta entrar no sistema
    def _login_click(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        # Solicita à aplicação principal que valida as credenciais 
        self.controller.realizar_login(username, password)

# Tela do operador de caixa (vendas)
class CaixaFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='TFrame')
        self.controller = controller
        # Inicializa a variável que armazenará o carrinho atual
        self.carrinho_atual = None
        # Cria um novo carrinho para iniciar a compra
        self._inicializar_carrinho()
        # Cria um componente Notebook, que permite organizar telas em abas
        self.notebook = ttk.Notebook(self)
        # Posiciona o Notebook e permite que ele ocupe o espaço disponível
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")
        # Cria a primeira aba, destinada à realização de vendas
        self.aba_venda = ttk.Frame(self.notebook, style='TFrame')
        # Adiciona a aba de vendas ao Notebook
        self.notebook.add(self.aba_venda, text="Nova venda")
        # Monta os componentes da aba de vendas
        self._setup_aba_venda(self.aba_venda)
        # Cria a segunda aba, destinada aos relatórios do caixa
        self.aba_relatorios_caixa = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.aba_relatorios_caixa, text="Relatórios")
        # Monta os componentes da aba de relatórios
        self._setup_aba_relatorios(self.aba_relatorios_caixa)

        # Cria o botão de sair e associa seu clique ao método logout
        logout_button = ttk.Button(self, text="Sair", command=controller.logout, 
        style='Alerta.TButton')
        # Posiciona o botão no canto inferior direito da tela
        logout_button.pack(side="bottom", anchor='e', padx=10, pady=10)

    # Define o método que cria um novo carrinho
    def _inicializar_carrinho(self):
        # Cria uma nova instância da classe Carrinho
        self.carrinho_atual = Carrinho()

        # Verifica se o componente visual do carrinho já foi criado
        if hasattr(self, 'listbox_carrinho'):
            # Remove todos os itens exibidos na lista do carrinho
            self.listbox_carrinho.delete(0, tk.END)
            # Atualiza o valor total apresentado na tela
            self.atualizar_total_carrinho()

    # Define o método responsável por montar a aba de vendas
    def _setup_aba_venda(self, parent_frame):
        # Define que a primeira coluna terá peso 2 na distribuição do espaço
        parent_frame.columnconfigure(0, weight=2)
        # Define que a segunda coluna terá peso 1 na distribuição do espaço
        parent_frame.columnconfigure(1, weight=1) 
        # Cria o frame que agrupará os componentes relacionados aos produtos
        frame_produtos = ttk.Frame(parent_frame, style='TFrame', padding="10")

        ''' Posiciona o frame de produtos na primeira coluna.
        sticky="nsew" permite que ele se expanda em todas as direções'''
        frame_produtos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Cria o título da seção de produtos disponíveis
        ttk.Label(frame_produtos, text="Produtos disponíveis:", 
        style='Titulo.TLabel').pack(pady=5)
        # Cria uma lista visual para exibir os produtos disponíveis
        self.listbox_produtos = tk.Listbox(frame_produtos, height=10, 
        font=('Courier', 10), bd=2, relief="sunken")

        # Posiciona a lista e permite que ela ocupe a lasgura disponível
        self.listbox_produtos.pack(fill="x", padx=5)
        # Associa o evento de seleção de um produto ao método corretamente 
        self.listbox_produtos.bind('<<ListboxSelect>>', self._selecionar_produto)
        # Cria um rótulo para identificar o campo de quantidade
        ttk.Label(frame_produtos, text="Quantidade:").pack(pady=5)
        # Cria o campo de entrada da quantidade desejada
        self.qtd_entry = ttk.Entry(frame_produtos, width=10)
        # Define 1 como a quantidade inicial
        self.qtd_entry.insert(0, '1')
        self.qtd_entry.pack(pady=5)

        ''' Cria o botão para adicionar o produto selecionado ao carrinho.
        0 método _adicionar_ao_carrinho será executado ao clicar.'''
        ttk.Button(frame_produtos, text="Adicionar ao Carrinho", 
        command=self._adicionar_ao_carrinho, style='Custom.TButton').pack(pady=10)
        # Cria o botão para remover uma unidade do item selecionado no carrinho
        ttk.Button(frame_produtos, text="Remover Item", 
        command=self._remover_do_carrinho, style='Alerta.TButton').pack(pady=5) 
        # Cria um frame para agrupar os componentes do carrinho
        frame_carrinho = ttk.Frame(parent_frame, style='TFrame', padding="10")
        # Posiciona o frame do carrinho na segunda coluna
        frame_carrinho.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        # Cria o título da seção do carrinho
        ttk.Label(frame_carrinho, text="Seu Carrinho:", style='Titulo.TLabel').pack(
            pady=5
        )         
        # Cria a lista visual dos produtos adicionados à compra
        self.listbox_carrinho = tk.Listbox(frame_carrinho, height=10, 
        font=('Courier', 10), bd=2, relief="sunken")
        # Posiciona a lista do carrinho na interface
        self.listbox_carrinho.pack(fill="x", padx=5)
        # Cria um rótulo que apresenta o valor total da compra
        self.label_total = ttk.Label(frame_carrinho, text="Total R$ 0.00", 
        font=('Helvetica', 14, 'bold'), foreground="#d32f2f")
        # Posiciona o rótulo do valor total
        self.label_total.pack(pady=10)

        # Cria o botão que abre a janela de pagamento
        ttk.Button(frame_carrinho, text="Finalizar compra", 
        command=self._finalizar_compra, style='Custom.TButton').pack(
            pady=15, fill='x'
        )          
        # Cria o botão que cancela a compra atual e devolve o estoque
        ttk.Button(frame_carrinho, text="Cancelar compra", 
        command=self._cancelar_compra, style='Alerta.TButton').pack(
            pady=5, fill='x'
        )

    # Define o método responsável por montar a aba de relatórios do caixa
    def _setup_aba_relatorios(self, parent_frame):
        # Cria o tótulo da seção de fechamento do caixa
        ttk.Label(parent_frame, text="Relatório do dia (caixa)", 
        style='Titulo.TLabel').pack(pady=20)
        # Exibe uma orientação sobre a geração do relatório diário
        ttk.Label(parent_frame, text="Este relatório é gerado pelo fechamento do dia",
        style='TLabel').pack(pady=5)
        # Cria um botão para registrar o fechamento do dia
        ttk.Button(parent_frame, text="Gerar fechamento do dia", 
        command=self._fechamento_dia, style='Custom.TButton').pack(pady=15)
        # Cria um rótulo inicialmente vazio para mostrar o resultado do fechamento
        self.fechamento_label = ttk.Label(parent_frame, text="", style='TLabel')
        # Posiciona o rótulo do resultado na interface
        self.fechamento_label.pack(pady=5)

    # Método que executa o fechamento diário do caixa
    def _fechamento_dia(self):
        try:
            self.controller.sistema.fechamento_dia()
            total_dia = self.controller.sistema.caixa.total_dia
            itens_vendidos = self.controller.sistema.caixa.itens_vendidos

            self.fechamento_label.config(
                text=f"Fechamento registrado:\n"
                     f"Total arrecadado R$ {total_dia:.2f}\n"
                     f"Itens vendidos: {itens_vendidos}\n"
                     f"O arquivo de relatório foi salvo."   
            )        
            messagebox.showinfo("Fechamento","Fechamento do dia e relatório salvo!")
        except Exception as e:
            messagebox.showerror("Erro",f"Erro ao realizar fechamento: {e}")

    def atualizar_produtos(self):
        # Limpa todos os produtos atualmente exibidos na lista
        self.listbox_produtos.delete(0, tk.END)
        # Percorre a lista de produtos atualmente exibidos na lista
        for produto in self.controller.sistema.produtos:
            '''Monta o texto de cada produto com nome, preço e estoque.
            <20 reserva um espaço de 20 caracteres para o nome.
            :5.f formata o preço com duas casas decimais'''
            texto =(
                f"{produto.nome:<20} "
                f"R$ {produto.preco:5.2f} "
                f"(Estoque: {produto.estoque})"
            )            
            # Insere o texto do produto na lista visual
            self.listbox_produtos.insert(tk.END, texto)

    def _adicionar_ao_carrinho(self):
        # Continuamos amanhã...
        try:
            # Recupera os índices dos itens selecionados na lista produtos
            selecao = self.listbox_produtos.curselection()

            # Verifica se nenhum produto foi selecionado
            if not selecao:
                # Informa que é necessário selecionar um produto
                messagebox.showerror("Erro","Selecione um produto da lista.")
                return

            # Obtém o índice do primeiro produto selecionado
            indice_produto = selecao[0]
            # Recupera o objeto Produto correspondente ao índice selecionado
            produto = self.controller.sistema.produtos[indice_produto]
            # Obtêm a quantidade digitada e converte o texto para inteiro
            quantidade = int(self.qtd_entry.get())

            if quantidade <= 0:
                raise ValueError("Quantidade deve ser maior que zero.")

            '''Adiciona o produto e a quantidade ao carrinho.
            A classe Carrinho também verifica a disponibilidade do estoque'''
            self.carrinho_atual.adicionar(produto, quantidade)
            messagebox.showinfo("Sucesso",f"{quantidade}x {produto.nome} adicionado(s)!")
            # Atualiza a lista visual dos produtos que estão no carrinho
            self.atualizar_visualizacao_carrinho()
            # Atualiza a lista de produtos para refletir o estoque atual
            self.atualizar_produtos()
            # Apaga o conteúdo do campo de quantidade
            self.qtd_entry.delete(0, tk.END)
            # Preenche novamente o campo com a quantidade padrão 1
            self.qtd_entry.insert(0, '1')
        except ValueError as e:
            messagebox.showerror("Erro de estoque/QTD", str(e))

        # Captura outros erros que não foram tratados anteriormente
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Define o método que remove uma unidade do produto selecionado no carrinho
    def _remover_do_carrinho(self):
        if self.carrinho_atual.vazio():
            messagebox.showinfo("Carrinho","O carrinho está vazio.")
            return

        selecao = self.listbox_carrinho.curselection()
        # Verifica se nenhum item foi selecionado
        if not selecao:
            messagebox.showerror("Erro", "Selecione um item no carrinho para remover")
            return

        # Obtém o índice do item selecionado no carrinho
        indice_carrinho = selecao[0]
        '''Converte os itens do carrinho em uma lista.
        Isso permite acessar um item pelo seu índice'''
        itens = list(self.carrinho_atual.listar_itens())
        # Recupera o produto e sua quantidade atual no carrinho
        produto, qtd_no_carrinho = itens[indice_carrinho]
        # Define que será removido apenas uma unidade do produto
        qtd_remover = 1
        try:
            self.carrinho_atual.remover(produto, qtd_remover)
            messagebox.showinfo("Sucesso", f"1x {produto.nome} removido(s) do carrinho.")
            # Atualiza a lista visual do carrinho
            self.atualizar_visualizacao_carrinho()
            # Atualiza a lista de produtos para refletir o estoque devolvido
            self.atualizar_produtos()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    # Define o método que recalcula e apresenta o total da compra
    def atualizar_total_carrinho(self):
        total = self.carrinho_atual.calcular_total()
        self.label_total.config(text=f"Total R$ {total:.2f}")

    # Define o método que atualiza a lista visual do carrinho
    def atualizar_visualizacao_carrinho(self):
        self.listbox_carrinho.delete(0, tk.END)

        # Percorre os produtos e suas qtd armazenadas no carrinho
        for produto, qtd in self.carrinho_atual.listar_itens():
            texto = (
                f"{qtd}x {produto.nome} "
                f"(R$ {produto.preco * qtd:.2f})"
            )                
            # Insere o produto formatado na lista visual do carrinho
            self.listbox_carrinho.insert(tk.END, texto)

        # Atualiza o valor total depois de atualizar os itens
        self.atualizar_total_carrinho()

    # Define o método chamado quando o usuário seleciona um produto
    def _selecionar_produto(self, event):
        self.qtd_entry.delete(0, tk.END)
        self.qtd_entry.insert(0, '1')

    # Define o método que cancela a compra atual
    def _cancelar_compra(self):
        '''Pergunta ao usuário se ele realmente deseja cancelar a compra.
        askyesno retorna True se o usuário confirmar''' 
        if not messagebox.askyesno(
            "Confirmar cancelamento",
            "Tem certeza que deseja cancelar esta compra? "
            "O estoque será devolvido"
        ):
            return

        # Cria uma lista com os produtos e quantidades que serão devolvidos
        itens_para_devolver = list(self.carrinho_atual.listar_itens())

        # Percorre todos os produtos que estão no carrinho
        for produto, qtd in itens_para_devolver:
            try:
                '''Remove do carrinho a quantidade total do produto.
                O método remover também devolve a quantidade ao estoque.'''
                self.carrinho_atual.remover(produto, qtd)

            except Exception as e:
                print(f"Erro ao devolver estoque de {produto.nome}: {e}")

        # Cria um novo carrinho vazio
        self._inicializar_carrinho()
        # Atualiza a lista de produtos no estoque
        self.atualizar_produtos()
        messagebox.showinfo("Cancelado", "Compra cancelada. Estoque devolvido.")

    # Define o método que inicia o processo de finalização da compra
    def _finalizar_compra(self):
        if self.carrinho_atual.vazio():
            messagebox.showerror("Erro", 
            "O carrinho está vazio para finalizar a compra.")
            return

        ''' Cria a janela de pagamento.
        Envia o carrinho, o objeto Caixa e a função que cria um novo carrinho'''
        PagamentoDialog(
            self,
            self.carrinho_atual,
            self.controller.sistema.caixa,
            self._inicializar_carrinho
        )                    

''' Janela de diálogo de pagamento
Define uma janela secundária para processar o pagamento da compra.
tk.Topleval permite criar uma janela à janela principal'''
class PagamentoDialog(tk.Toplevel):
    # Método construtor da janela de pagamento
    # master é a janela que originou o diálogo
    # carrinho contém os produtos da compra
    # caixa_manager representa o objeto responsável pelo caixa
    # callback_novo_carrinho é a função executada para iniciar outra compra
    def __init__(
        self,
        master,
        carrinho,
        caixa_manager,
        callback_novo_carrinho
    ):
        # Inicializa a janela secundária vinculada à janela principal
        super().__init__(master)
        self.title("Finalizar Pagamento")
        self.geometry("400x450")
        # Associa a janela secundária à janela principal
        self.transient(master)
        ''' Torna a janela modal, impedindo a interação com outras janelas da 
        aplicação enquanto este diálogo estiver ativo'''
        self.grab_set()
        # Armazena a referência ao carrinho atual
        self.carrinho = carrinho
        # Armazena a referência ao objeto responsável pelo caixa
        self.caixa_manager = caixa_manager
        # Armazena a função que será chamada para iniciar outro carrinho
        self.callback_novo_carrinho = callback_novo_carrinho
        # Calcula o valor original da compra, antes de descontos ou acréscimos
        self.total_bruto = carrinho.calcular_total()
        # Inicializa a variável que armazenará a descrição do pagamento
        self.forma_pagamento_str = ""
        # Inicializa a variável que armazenará o valor final a pagar
        self.valor_final = 0.0
        # Cria o frame principal da janela de pagamento
        self.frame_main = ttk.Frame(
            self, style='TFrame', padding="15"
        )
        # Faz o frame ocupar toda a área disponível da janela
        self.frame_main.pack(fill="both", expand=True)
        ttk.Label(
            self.frame_main,
            text="Pagamento",
            style='Titulo.TLabel'
        ).pack(pady=10)
        # Exibe o valor original da compra
        ttk.Label(
            self.frame_main,
            text=f"Total bruto R$ {self.total_bruto:.2f}",
            font=('Helvetica', 12)
        ).pack(pady=5)
        # Orienta o usuário a selecionar uma forma de pagamento
        ttk.Label(
            self.frame_main,
            text="Selecione a forma de pagamento:",
            font=('Helvetica', 12, 'bold')
        ).pack(pady=10)
        ''' Cria uma lista de opções de pagamento.
        Cada tupla contém um código numérico e uma descrição'''
        self.opcoes_pagamento = [
            (1, "Dinheiro/PIX - 10% de desconto"),
            (2, "Cartão de débito - 5% de desconto"),
            (3, "Cartão de crédito 1x - mesmo valor"),
            (4, "Cartão de crédito 2x - 5% de acréscimo"),
            (5, "Cartão de crédito 3x - 10% de acréscimo"),
            (6, "Cartão de crédito 4x - 15% de acréscimo")
        ]
        ''' Cria uma variável inteira para armazenar a opção escolhida.
        O valor inicial 0 significa que nenhuma opção foi selecionada'''
        self.var_opcao = tk.IntVar(self, value=0)
        # Percorre a lista de opções de pagamento
        for codigo, descricao in self.opcoes_pagamento:
            # Cria um botão de opção para cada forma de pagamento
            # Os botões compartilham a variável var_opcao
            # Assim, somente uma opção pode ficar selecionada por vez
            # Ao selecionar uma opção, o método de cálculo é executado
            rb = ttk.Radiobutton(
                self.frame_main,
                text=f"[{codigo}] {descricao}",
                variable=self.var_opcao,
                value=codigo,
                command=self._calcular_valor_final
            )
            # Posiciona o botão de opção alinhado à esquerda
            rb.pack(anchor='w', padx=5, pady=2)

        # Cria um rótulo para mostrar o valor final da compra
        self.label_valor_final = ttk.Label(
            self.frame_main,
            text="Valor final R$ 0.00",
            font=('Helvetica', 14, 'bold'),
            foreground='#004d40'
        )    
        # Posiciona o rótulo do valor final
        self.label_valor_final.pack(pady=10)
        # Cria o botão para confirmar o pagamento e gerar a nota fiscal
        self.btn_pagar = ttk.Button(
            self.frame_main,
            text="Pagar e emitir nota",
            command=self._processar_pagamento,
            style='Custom.TButton'
        )
        # Posiciona o botão e permite que ocupe toda a largura disponível
        self.btn_pagar.pack(pady=15, fill='x')
        # Seleciona inicialmente a opção 3, correpondente ao crédito em 1x
        self.var_opcao.set(3)
        # Calcula e apresenta o valor correspondente à opção inicial
        self._calcular_valor_final()

    # Define o método que calcula o valor de acordo com o pagamento escolhido
    def _calcular_valor_final(self):
        # Obtém o código da opção selecionada
        opcao = self.var_opcao.get()
        # Verifica se nenhuma opção de pagamento foi selecionada
        if opcao == 0:
            # Apresenta o valor inicial de zero no rótulo
            self.label_valor_final.config(text="Valor final R$ 0.00")
            return

        try:
            # Cria um objeto Pagamento com o valor bruto da compra
            pagamento = Pagamento(self.total_bruto)
            # Calcula o valor final e obtém a descrição da forma de pagamento
            valor_final, forma_pagamento_str = (
                pagamento.calcular_pagamento(opcao)
            )
            # Armazena o valor final calculado
            self.valor_final = valor_final
            # Armazena a descrição da forma de pagamento
            self.forma_pagamento_str = forma_pagamento_str
            # Atualiza a interface com o valor e a descrição do pagamento
            self.label_valor_final.config(
                text=(
                   f"Valor final R$ {valor_final:.2f} "
                   f"({forma_pagamento_str})" 
                )
            )
        except ValueError:
            self.label_valor_final.config(text="Opção inválida")

    # Define o método que registra o pagamento e gera a nota fiscal
    def _processar_pagamento(self):
        if self.var_opcao.get() == 0:
            messagebox.showerror("Erro", "Selecione uma forma de pagamento.")
            return

        # Inicia o tratamento de erros do processo de pagamento
        try:
            # Recupera o valor final calculado para a compra
            total_compra = self.valor_final
            # Calcula a quantidade total de unidades vendidas no carrinho
            itens_vendidos = self.carrinho.total_itens()
            ''' 1 - Registra a venda no objeto responsável pelo caixa.
            O valor contabilizado é o valor final, já com o desconto ou acréscimo'''
            self.caixa_manager.registrar_venda(
                total_compra, itens_vendidos
            )                
            ''' 2 - Obtém a data e a hora atuais.
            O formato utilizado permite criar nomes de arquivos únicos 
            para diferentes vendas realizadas em segundos distintos'''
            agora = datetime.datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )
            # Monta o nome do arquivo de nota fiscal usando a data e a hora
            filename = f"nota_{agora}.txt"

            ''' Abre o arquivo para escrita.
            '''
            with open(filename, "w", encoding="utf-8") as f:
                f.write("==== Nota fiscal ====\n")
                # Percorre os produtos e as quantidades do carrinho
                for produto, qtd in self.carrinho.listar_itens():
                    f.write(
                        f"{qtd}x {produto.nome} - "
                        f"R$ {produto.preco * qtd:.2f}\n"
                    )
                f.write(
                    f"Forma de pagamento: "
                    f"{self.forma_pagamento_str}\n"
                )    
                f.write(
                    f"Total a pagar R$ {total_compra:.2f}\n"
                )
                f.write("=======================\n")

            messagebox.showinfo(
                "Sucesso",
                f"Venda de R$ {total_compra:.2f} registrada! "
                f"Nota fiscal salva em: {filename}"
            )    
            ''' Executa a função que cria um novo carrinho vazio.
            Isso prepara a tela para uma nova compra'''
            self.callback_novo_carrinho()
            # Fecha a janela de pagamento
            self.destroy()

        except Exception as e:
            messagebox.showerror(
                "Erro",
                f"Erro ao processar pagamento/nota: {e}"
            )    

''' Tela administrativa.
classe que representa o painel administrativo'''
class AdminFrame(ttk.Frame):
    def __init__(self, parent, controller):
        # Inicializa o frame com o estilo visual configurado
        super().__init__(parent, style='TFrame')
        # Armazena a referência à aplicação principal
        self.controller = controller
        # Cria o título do painel administrativo
        ttk.Label(
            self,
            text="Painel administrativo - Controle de estoque",
            style='Titulo.TLabel'
        ).pack(pady=20)
        ''' Cria um botão para gerenciar o estoque.
        lambda permite executar a função somente quando o botão for clicado.
        Atualmente, o botão apenas exibe uma mensagem informativa'''
        ttk.Button(
            self,
            text="Gerenciar estoque",
            command=lambda: messagebox.showinfo(
                "Info",
                "Implementar gerenciamento de estoque."
            ), style='Custom.TButton'
        ).pack(pady=10, ipadx=20)
        # Cria um botão que abre a tela de relatórios de vendas.
        ttk.Button(
            self,
            text="Ver relatórios de vendas",
            command=lambda: controller.mostrar_frame(RelatoriosFrame),
            style='Custom.TButton'
        ).pack(pady=10, ipadx=20)
        # Cria o botão para sair da seção adminitrativa
        ttk.Button(
            self,
            text="Sair",
            command=controller.logout,
            style='Alerta.TButton'
        ).pack(side="bottom", anchor='e', padx=10, pady=10)

''' Tela de relatórios de vendas (Admin e Caixa)
Define a classe responsável por apresentar os dados de vendas'''
class RelatoriosFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='TFrame')
        # Armazena a referência à aplicação principal
        self.controller = controller
        # Cria o título da tela de relatórios
        ttk.Label(
            self,
            text="Relatórios de vendas",
            style='Titulo.TLabel'
        ).pack(pady=20)
        ''' Cria um rótulo com uma orientação inicial sobre os dados do caixa'''
        self.caixa_label = ttk.Label(
            self,
            text=(
                "Dados do caixa: \n"
                "(Realize um fechamento de caixa para atualizar)"
            ), style='TLabel'
        )
        # Posiciona o rótulo dos dados do caixa
        self.caixa_label.pack(pady=10)
        # Cria o botão para atualizar os valores exebidos no relatório
        ttk.Button(
            self,
            text="Atualizar dados do caixa",
            command=self._atualizar_caixa,
            style='Custom.TButton'
        ).pack(pady=10)
        ''' Cria o botão de voltar.
        Se o usuário conectado for administrador, volta ao painel adm.
        Caso contrário, retorna a tela do operador de caixa'''
        ttk.Button(
            self,
            text="Voltar",
            command=lambda: (
                controller.mostrar_frame(AdminFrame)
                if controller.usuario_logado == 'admin'
                else controller.mostrar_frame(CaixaFrame)
            ), style='Alerta.TButton'
        ).pack(
            side="bottom", anchor='e', padx=10, pady=10
        )
        # Atualiza os dados do caixa assim que a tela é criada
        self._atualizar_caixa()

    # Define método que consulta e apresenta os dados acumulados do caixa
    def _atualizar_caixa(self):
        # Obtém o total arrecadado registrado no objeto Caixa
        total = self.controller.sistema.caixa.total_dia
        # Obtém a quantidade de itens vendidos registrados no objeto Caixa
        itens = self.controller.sistema.caixa.itens_vendidos
        ''' Cria o texto inicial do relatório com o total arrecadado.'''
        texto = (
            f"Total Arrecadado (Desde o Inicio): R$ {total:.2f}\n"
        )
        # Acrescenta ao texto a quantidade total de itens vendidos
        texto +=(f"Total de itens vendidos (Desde o início): {itens}")
        # Atualiza o rótulo da tela com os dados mais recentes
        self.caixa_label.config(text=texto)

if __name__ == '__main__':
    try:
        app = AppGUI()
        app.mainloop()
    except Exception as e:
        print(f"Erro fatal na apliacação: {e}")
        print(
            "Verifique se a nova estrutura de pastas e os arquivos "
            "__init__.py foram criados corretamente"   
        )
