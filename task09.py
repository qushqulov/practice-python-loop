import random

maxfiy_pin = random.randint(1000, 9999)


urinishlar_soni = 0
maksimal_imkoniyat = 7

print("---  PIN kod ochish o'yini ---")
print(f"Kompyuter 4 xonali PIN o'yladi. Sizda {maksimal_imkoniyat} ta imkoniyat bor.")

while urinishlar_soni < maksimal_imkoniyat:
    taxmin = int(input(f"\n{urinishlar_soni + 1}-urinish. PINni kiriting: "))
    urinishlar_soni += 1  
    if taxmin == maxfiy_pin:
        print(f"Tabriklaymiz, topdingiz! PIN: {maxfiy_pin}")
        print(f"Siz buni {urinishlar_soni} ta urinishda bajardingiz.")
        break  
    elif taxmin > maxfiy_pin:
        print(" Juda katta son!")
    else:
        print(" Juda kichik son!")


else:
    print("\n Afsuski, imkoniyatlaringiz tugadi.")
    print(f"Bloklandingiz! To'g'ri PIN {maxfiy_pin} edi.")