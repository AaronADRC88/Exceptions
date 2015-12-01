__author__ = 'aferreiradominguez'
class meuFaio(Exception):
    def __init__(self,valor):
        self.valor=valor
    def __str__(self):
        return "Error"+str(self.valor)

resultado=9

try:
    if resultado>10:
        raise meuFaio(10)
except meuFaio as e :
    print(e)
else:
    print("resul < q dez")
finally:
    print("final do analise")