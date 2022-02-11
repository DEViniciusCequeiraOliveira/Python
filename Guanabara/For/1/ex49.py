num = int(input("Qual tabuada você deseja? "))

print("-"*12)

for n in range(1,11):
    print(f"{num} X {n:2} = {num * n:2}")