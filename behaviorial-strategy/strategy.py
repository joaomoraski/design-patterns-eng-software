from abc import ABC, abstractmethod


# Interface de pagamento
class Pagamento(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor: float, tipo: str) -> str:
        pass


# Diferentes tipos de pagamento
class PagamentoCartao(ABC):
    def realizar_pagamento(self, valor: float, tipo: str) -> str:
        return f"Pagou {valor} com o método {tipo} parcelado"


class PagamentoPix(ABC):
    def realizar_pagamento(self, valor: float, tipo: str) -> str:
        return f"Pagou {valor} com o método {tipo} a vista"


# Classe compra
class Compra:
    def __init__(self, pagamento: Pagamento):
        self.pagamento = pagamento

    def set_forma_pagamento(self, pagamento: Pagamento):
        self.pagamento = pagamento

    def executar_pagamento(self, valor: float, tipo: str) -> str:
        return self.pagamento.realizar_pagamento(valor, tipo)


# Exemplo de execução
compra = Compra(PagamentoCartao())
print("Pagando: ", compra.executar_pagamento(5, "Cartão"))  # Output: Pagando:  Pagou 5 com o método Cartão parcelado

compra = Compra(PagamentoPix())
print("Pagando: ", compra.executar_pagamento(5, "Pix"))  # Output: Pagando:  Pagou 5 com o método Pix a vista
