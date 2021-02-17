# Desafios operadores lógicos

# Confirmado os 2 trabvalhos: TV 50 + sorvete
# Confirmado apenas 1 trabalho:TV 32 + sorvete
# nenhum trabalho confirmado: fica em casa

trabalho_terca = True
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("TV50={} TV32={} Sorvete={} Saudável={}"
     .format(tv_50, tv_32, sorvete, mais_saudavel))
