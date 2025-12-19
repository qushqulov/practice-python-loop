eng_katta = None

print("5 ta son kiriting:")

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    
    if eng_katta is None or son > eng_katta:
        eng_katta = son

print(f"Siz kiritgan sonlar ichida eng kattasi: {eng_katta}")