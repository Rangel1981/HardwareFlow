import customtkinter as ctk
from models.dispositivo import Computador, Smartphone
from models.ordem_servico import OrdemServico
from utils.gerenciador_json import salvar_banco, carregar_banco

class HardwareApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("HardwareFlow Pro - Gestão de OS")
        self.geometry("1000x600")
        
        # Carregar dados iniciais
        self.lista_atendimentos = carregar_banco()

        # Configuração de Grid (2 colunas: Form e Lista)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- FRAME ESQUERDO: FORMULÁRIO ---
        self.frame_form = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.frame_form.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.label_titulo = ctk.CTkLabel(self.frame_form, text="Nova Ordem de Serviço", font=("Roboto", 20, "bold"))
        self.label_titulo.pack(pady=(20, 30))

        # Campos de Entrada
        self.entry_cliente = ctk.CTkEntry(self.frame_form, placeholder_text="Nome do Cliente", width=250)
        self.entry_cliente.pack(pady=10)

        self.entry_marca = ctk.CTkEntry(self.frame_form, placeholder_text="Marca", width=250)
        self.entry_marca.pack(pady=10)

        self.entry_modelo = ctk.CTkEntry(self.frame_form, placeholder_text="Modelo", width=250)
        self.entry_modelo.pack(pady=10)

        self.entry_valor = ctk.CTkEntry(self.frame_form, placeholder_text="Valor Base (R$)", width=250)
        self.entry_valor.pack(pady=10)

        self.option_tipo = ctk.CTkOptionMenu(self.frame_form, values=["Computador", "Smartphone"], width=250)
        self.option_tipo.pack(pady=10)

        self.btn_salvar = ctk.CTkButton(self.frame_form, text="Abrir OS", command=self.criar_os, fg_color="green", hover_color="#006400")
        self.btn_salvar.pack(pady=30)

        # --- FRAME DIREITO: LISTAGEM ---
        self.frame_lista = ctk.CTkFrame(self)
        self.frame_lista.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        self.label_lista = ctk.CTkLabel(self.frame_lista, text="Ordens Registradas", font=("Roboto", 18))
        self.label_lista.pack(pady=10)

        self.txt_lista = ctk.CTkTextbox(self.frame_lista, width=600, height=450)
        self.txt_lista.pack(padx=20, pady=10)
        
        self.btn_atualizar = ctk.CTkButton(self.frame_lista, text="Salvar no Banco (JSON)", command=self.persistir_dados)
        self.btn_atualizar.pack(pady=10)

        self.atualizar_lista_visual()

    def criar_os(self):
        try:
            # Captura dados
            cliente = self.entry_cliente.get()
            marca = self.entry_marca.get()
            modelo = self.entry_modelo.get()
            valor = float(self.entry_valor.get())
            tipo = self.option_tipo.get()

            # Lógica de POO (Instanciação)
            if tipo == "Computador":
                disp = Computador(marca, modelo, "Desktop", valor)
            else:
                disp = Smartphone(marca, modelo, valor, False) # Padrão sem tela trincada

            nova_os = OrdemServico(cliente, disp, "Reparo Geral")
            self.lista_atendimentos.append(nova_os)
            
            self.atualizar_lista_visual()
            self.limpar_campos()
            print(f"OS de {cliente} criada com sucesso!")

        except ValueError:
            print("Erro: Valor inválido!")

    def atualizar_lista_visual(self):
        self.txt_lista.delete("0.0", "end") # Limpa a caixa de texto
        for os in self.lista_atendimentos:
            self.txt_lista.insert("end", f"{os}\n" + "-"*50 + "\n")

    def persistir_dados(self):
        salvar_banco(self.lista_atendimentos)
        print("Dados persistidos no database.json")

    def limpar_campos(self):
        self.entry_cliente.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_modelo.delete(0, 'end')
        self.entry_valor.delete(0, 'end')