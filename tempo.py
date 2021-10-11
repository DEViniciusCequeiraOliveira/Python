tempo = int(input("Quantos segundos? "))

dias = tempo // 86400
rest_dias = tempo % 86400 

horas = rest_dias // 3600
rest_horas = rest_dias % 3600

minutos = rest_horas // 60
rest_segundos = rest_horas % 60

segundos = rest_segundos % 60

print(f"{dias} dias {horas} horas {minutos} minutos {segundos} segundos")