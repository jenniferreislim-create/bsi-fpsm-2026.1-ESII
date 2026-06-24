from dataclasses import dataclass


@dataclass
class Item:
    """Entidade de domínio: um item do pedido."""
    nome: str
    preco: float
    qtd: int = 1

        # TODO: retornar preço × quantidade
    def subtotal(self) -> float:
           return self.preco * self.qtd
