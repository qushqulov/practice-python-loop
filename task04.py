import random

kompyuter_soni = random.randint(1, 20)
urinishlar = 0

while True:
    taxmin = int(input("Sonni kiriting: "))
    urinishlar += 1
    
    if taxmin < kompyuter_soni:
        print("Kattaroq son ayting ⬆:")
    elif taxmin > kompyuter_soni:
        print("Kichikroq son ayting ⬇:")
    else:
        print(f"Topdingiz!  {urinishlar} ta urinishda topdingiz.")
        break