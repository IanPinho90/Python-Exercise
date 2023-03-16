NomeIan = 'Ian: '
NascimentoIan = 2007
MêsIan = 1
DiaIan = 1
NomeAnna = 'Anna: '
NascimentoAnna = 2006
MêsAnna = 4
DiaAnna = 17
AnoAtual = 2023
def CalculoIdade(NascimentoIan, AnoAtual):
    Idade = AnoAtual - NascimentoIan
    return Idade
Idade = CalculoIdade(NascimentoIan,AnoAtual)
IdadeAnna = CalculoIdade(NascimentoAnna,AnoAtual)
print( NomeIan + 'Idade ' + str(Idade))
print( NomeAnna + 'Idade ' + str(IdadeAnna))

print('Aniversário Anna:', DiaAnna,MêsAnna,AnoAtual)
print('Aniversário Ian:', DiaIan,MêsIan,AnoAtual)



