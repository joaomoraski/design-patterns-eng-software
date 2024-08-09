# Permite objetos com interfaces incompativeis trabalhem juntos

# Classe do sistema legado que precisa ser adaptada
class ServicoDeFreteLegado:
    def calcular_frete(self, peso: float, destino: str) -> float:
        # Lógica para calcular frete
        return peso * 0.5


# Interface que o sistema atual espera
class ServicoDeFrete:
    def obter_valor_frete(self, peso: float) -> float:
        pass


# Adaptador que faz a ponte entre o sistema legado e o novo
class FreteAdapter(ServicoDeFrete):
    def __init__(self, servico_legado: ServicoDeFreteLegado):
        self.servico_legado = servico_legado

    def obter_valor_frete(self, peso: float) -> float:
        # Tradução da chamada para o método esperado pelo sistema legado
        destino_padrao = "São Paulo"  # Supondo um destino padrão
        return self.servico_legado.calcular_frete(peso, destino_padrao)


# Exemplo de uso
servico_legado = ServicoDeFreteLegado()
adaptador = FreteAdapter(servico_legado)

# O cliente usa o adaptador como se fosse o serviço esperado
valor_frete = adaptador.obter_valor_frete(10.0)
print(f"Valor do frete: {valor_frete}")  # Output: Valor do frete: 5.0
