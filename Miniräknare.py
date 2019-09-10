print("Välkommen till min miniräknare")
try:
    num1 = int(input("Mata in tal här: "))
except:
    print("Du måste skriva in en siffra")
    num1 = 0
try:
    num2 = int(input("Mata in ett till tal här: "))
except:
    print("Du måste skriva in en siffra")
    num2 = 0
#summa = int(num1) + int(tal2)
#print("Summan är:" +str(summa))

operator = input("Ange operator")
if operator == "+":
    total = num1+ num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/":
    try:
        total = num1 / num2
    except ZeroDivisionError:
        exit("Det går ej att dela med 0!")
else:
    print("FEL")

print("total är:", total)

