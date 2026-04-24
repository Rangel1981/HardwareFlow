import json
import os
from datetime import datetime
from models.dispositivo import Computador, Smartphone
from models.ordem_servico import OrdemServico

CAMINHO_BD = "database.json"

def salvar_banco(lista_ordens):
    dados = [os.to_dict() for os in lista_ordens]
    with open(CAMINHO_BD, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_banco():
    if not os.path.exists(CAMINHO_BD):
        return []
    
    try:
        with open(CAMINHO_BD, "r", encoding="utf-8") as f:
            dados_brutos = json.load(f)
        
        lista_objetos = []
        for item in dados_brutos:
            disp_data = item['dispositivo']
            if disp_data['tipo'] == "Computador":
                dispositivo = Computador(disp_data['marca'], disp_data['modelo'], disp_data['extra'], disp_data['valor_base'])
            else:
                dispositivo = Smartphone(disp_data['marca'], disp_data['modelo'], disp_data['valor_base'], disp_data['extra'])

            nova_os = OrdemServico(item['cliente'], dispositivo, item['descricao'])
            nova_os.status = item['status']
            nova_os.data_abertura = datetime.strptime(item['data_abertura'], "%d/%m/%Y %H:%M")
            
            lista_objetos.append(nova_os)
            
        return lista_objetos
    except Exception as e:
        print(f"Erro ao carregar banco: {e}")
        return []