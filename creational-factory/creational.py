from abc import ABC, abstractmethod


# Interface notificacao
class Notificacao(ABC):  # ABC é para indicar uma classe abstrata em python
    @abstractmethod  # Indica metodo abstrato
    def enviar(self) -> str:
        pass


# Criando os dois tipos de notificações existentes
class NotificacaoEmail(Notificacao):
    def enviar(self) -> str:
        return "Enviando notificação por Email"


class NotificacaoSMS(Notificacao):
    def enviar(self) -> str:
        return "Enviando notificação por SMS"


# Criando os Criadores das notificações
class CriadorNotificacao(ABC):  # Criador abstrato para ser implementado por outras classes
    @abstractmethod
    def criar_notificacao(self) -> Notificacao:
        pass

    def enviar_notificacao(self) -> str:
        notificacao = self.criar_notificacao()
        return f"Criador: O mesmo código do criador funcionou com {notificacao.enviar()}"


# Criando os criadores especificos para cada caso.
class CriadorEmail(CriadorNotificacao):
    def criar_notificacao(self) -> Notificacao:
        return NotificacaoEmail()


class CriadorSMS(CriadorNotificacao):
    def criar_notificacao(self) -> Notificacao:
        return NotificacaoSMS()


# Dessa maneira é possivel deixar o código mais desacoplado de funcionalidades e fazer a função para cada tipo.

# Exemplo de uso
criador_email = CriadorEmail()
print(criador_email.enviar_notificacao())  # Output: Criador: O mesmo código do criador funcionou com Enviando notificação por Email

criador_sms = CriadorSMS()
print(criador_sms.enviar_notificacao())  # Output: Criador: O mesmo código do criador funcionou com Enviando notificação por SMS
