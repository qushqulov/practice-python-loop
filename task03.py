matn = input("Matn kiriting: ")

katta_harf_soni = 0

for harf in matn:
    if harf.isupper():  
        katta_harf_soni += 1

print(f"Siz kiritgan matnda {katta_harf_soni} ta katta harf bor.")