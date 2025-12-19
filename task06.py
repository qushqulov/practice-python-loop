matn = input("Matnni kiriting: ")

gaplar_soni = 0

for belgi in matn:
    
    if belgi == "." or belgi == "!" or belgi == "?":
        gaplar_soni += 1


print(f"Kiritilgan matnda {gaplar_soni} ta gap bor.")