matn = input("Matn kiriting: ").lower()
unlilar = "aeiou"
count = 0

for harf in matn:
    if harf in unlilar:
        count += 1
print(f"Unli harflar soni: {count}")