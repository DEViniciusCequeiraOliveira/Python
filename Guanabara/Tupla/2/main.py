serieA = ('Atletico-Mg', 'Fortaleza','Flamengo','Palmeiras','Bragantino','Internacional',
          'Corinthians ','Fluminense','América-MG','Cuiabá','Athletico-PR','Atlético-GO',
          'São Paulo','Ceará','Bahia','Juventude','Santos','Sport','Grêmio','Chapecoense')

print("Os 5 primeiros:")
for pos in range (0,5):
    print(f"{serieA[pos]}")

print("\nOs 4 últimos:")
for pos in range (16,20):
    print(f"{serieA[pos]}")

print("\nOs times em ordem alfabética:")
print(f"{sorted(serieA)}")

while