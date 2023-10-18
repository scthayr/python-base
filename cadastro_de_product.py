#!/usr/bin env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

produto = {
    "nome": "Smart TV",
    "cores": ["preto", "cinza"],
    "preco": 3500,
    "dimensao": {
        "altura": 12.1,
        "largura": 122.0,
    },
    "em_estoque": True,
    "codigo": 57689,
    "codebar": None, 
}

cliente = {
    "nome": "Thaina"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"A cliente {compra['cliente'] ['nome']}"
    f" comprou {compra ['quantidade']} {compra['produto'] ['nome']}"
    f" e pagou o total de {total_compra}"
)
