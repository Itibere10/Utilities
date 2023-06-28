import string
import random

def gerar_senha(qtd_upper,qtd_lower,qtd_ponct,qtd_number):
  for x in range(qtd_upper):
    r1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(qtd_upper))
  for x in range(qtd_lower):
    r2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(qtd_lower))
  for x in range(qtd_ponct):
    r3 = ''.join(random.choice(string.punctuation) for _ in range(qtd_ponct))
  for x in range(qtd_number):
    r4 = ''.join(random.choice(string.digits) for _ in range(qtd_number))

  senha = r1+r2+r3+r4
  lista = list(senha)
  random.shuffle(lista)
  senha = ''.join(lista)
  return senha

saida = gerar_senha(6,6,6,6)
print(saida)
