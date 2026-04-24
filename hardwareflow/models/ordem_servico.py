from .dispositivo import Dispositivo
import json
from datetime import datetime


class OrdemServico:
    def __init__(self, cliente: str, dispositivo: Dispositivo, descricao: str):
        self.cliente = cliente
        self.dispositivo = dispositivo
        self.descricao = descricao
        self.status = "Aberto"
        self.__valor_total = 0.0
        self.data_abertura = datetime.now()
        self.data_finalizacao = None

    def __str__(self):
     
        return (f"Cliente: {self.cliente} | Status: {self.status}\n"
                f"Aparelho: {self.dispositivo.marca} {self.dispositivo.modelo}\n"
                f"Descrição: {self.descricao}\n"
                f"Valor Base: R$ {self.dispositivo.valor_base_reparo:.2f}")

    def finalizando_ordem(self):
        self.__valor_total = self.dispositivo.calcular_reparo()
        self.status = "Finalizado"
        self.data_finalizacao = datetime.now()

    def to_dict(self):
        data_fim = self.data_finalizacao.strftime("%d/%m/%Y %H:%M") if self.data_finalizacao else None

        return {
            "cliente": self.cliente,
            "descricao": self.descricao,
            "status": self.status,
            "valor": self.__valor_total,
            "data_abertura": self.data_abertura.strftime("%d/%m/%Y %H:%M"),
            "data_finalizacao": data_fim,
            "dispositivo": {
                "tipo": self.dispositivo.__class__.__name__,
                "marca": self.dispositivo.marca,
                "modelo": self.dispositivo.modelo,
                "valor_base": self.dispositivo.valor_base_reparo,
                "extra": getattr(self.dispositivo, 'tipo', None) or getattr(self.dispositivo, 'tela_trincada', None)
            }
        }

    
    def salvar_json(self):

        nome_arquivo = f"os {self.cliente.lower().replace(' ', '_')}.json" 

        try:
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(self.to_dict(), arquivo, indent=4, ensure_ascii=False)
            print(f"Ordem de serviço de {self.cliente} salva em {nome_arquivo}!")
            
        except Exception as e:
            print(f"Erro inesperado ao salvar o arquivo: {e}")
            