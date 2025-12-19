asl_parol = "python1234"

for i in range(1, 4): 
    parol = input(f"{i}-urinish. Parolni kiriting: ")
    
    
    if parol == asl_parol:
        print("Xush kelibsiz! ")
        break  
    else:
        
        if i < 3:
            print("Xato! Yana urinib ko'ring.")
        else:
            print("Bloklandiz! ")