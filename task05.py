matn = input("So'z kiriting: ")
teskari_matn = ""
index = len(matn) - 1

while index >= 0:
    teskari_matn += matn[index]
    index -= 1 
print(f"Natija: {teskari_matn}")