from utils.gerenciador_json import salvar_banco, carregar_banco
from models.dispositivo import Computador, Smartphone
from models.ordem_servico import OrdemServiço
import textwrap



def main():
    lista_atedimento = carregar_banco()
    
    while True:
        print(textwrap.dedent("""
        =======HardwareFlow - Gestão de OS============
        [1]\tAbrir Nova Ordem de Serviço
        [2]\tListar todas as Ordens
        [3]\tSalvar
        [0]\tSair
        """))
        opcao = input("Digite a opção que dejesar: ")

        if opcao =="1":
            try:
                cliente = input("Digite o nome do cliente: ")
                marca = input("Digite a marca do produto: ")
                modelo = input("Digite o modelo do aparelho: ")
                descricao = input("Qual o problema do aparelho: ")
                valor_base = float(input("Digite o valor do serviço: "))

                tipo_equipamento = input("Tipo (1- Computador / 2- Smartphone): ")

                if tipo_equipamento == "1":
                    tipo_pc = input("É Desktop ou Notebook? ")
                    dispositivo = Computador(marca, modelo, tipo_pc, valor_base)

                else:
                    trincando = input("A tela está trincada? (y/n): ").lower() == 'y'
                    dispositivo = Smartphone(marca, modelo, valor_base, trincando)

                nova_os = OrdemServiço(cliente, dispositivo, descricao)
                lista_atedimento.append(nova_os)
                print(f"\nOs de {cliente} aberto com sucesso!")
                
            except ValueError:
                print("\nErro: No valor do serviço, use apenas números (ex: 150.50)")

        elif opcao == "2":
            print("\n---------LISTA DE ORDENS-------")
            if not lista_atedimento:
                print("Nenhuma ordem foi encontrada!")

            else:
                for os in lista_atedimento:
                    print(os)


        elif opcao == "3":
            salvar_banco(lista_atedimento)
        
        elif opcao == "0":
            print("\nSaindo do sistema, até a próxima OS, Padrinho!")
            break

        else:
            print("\n Opção inválida! Tente novamente.")

if __name__=="__main__":
    main()