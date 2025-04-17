print("\n\nFashion Store\n")
restart = ('Y')
sum = 0

while restart != ('N','NO','n','no'):
    print("1.Buy Clothes")
    print("2.Checkout")
    option = int(input("\nEnter your option : "))


    if option == 1:
        print("The categories are as follows:")
        print("1. Bottoms")
        print("2. Tshirt/Tops/Shirts")
        print("3. Dress/Skirt")
        option1 = int(input("\nEnter your option: "))

        if option1 == 1:
            print("The following items are in stock:")
            print("1. Pants (all colours) - Rs500")
            print("2. Cargos (all colours) - Rs700")
            print("3. Leggings (all colour) - Rs400")
            print("4. Trousers (all colour) - Rs600")
            print("5. Shorts (all colour) - Rs400")
            option2 = int(input("\nEnter your option : "))

            if option2 == 1:
                print("Pants")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 500
                
            elif option2 == 2:
                print("Cargos")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 700
                
            elif option2 == 3:
                print("Leggings")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 400
                
            elif option2 == 4:
                print("Trousers")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 600
                
            elif option2 == 5:
                print("Shorts")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 400
                        
        elif option1 == 2:
            print("The following items are in stock:")
            print("1. Tshirt - Rs300")
            print("2. Crop top - Rs300")
            print("3. Shirts - Rs600")
            print("4. Party tops - Rs600")
            option3 = int(input("\nEnter your option : "))

            if option3 == 1:
                print("Tshirt")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 300
                
            elif option3 == 2:
                print("Crop top")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 300
                    
            elif option3 == 3:
                print("Shirts")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 600
                
            elif option3 == 4:
                print("Party tops")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 600

        elif option1 == 3:
            print("The following items are in stock:")
            print("1. Long dress - Rs800")
            print("2. Short dress - Rs600")
            print("3. Skirt - Rs500")
            print("4. Long skirt - Rs700")
            option4 = int(input("\nEnter your option : "))

            if option4 == 1:
                print("Long dress")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 800
                
            elif option4 == 2:
                print("Short dress")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 600
                
            elif option4 == 3:
                print("Skirt")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 500
                
            elif option4 == 4:
                print("Long skirt")
                qunatity = int(input("Enter quantity:"))
                colour_l = []
                size_l = []
                sum = sum + 700

                for q in range(quantity):
                    colour = str(input("\nColour : "))
                    colour_l.append(colour)             
                    size  = str(input("\nSize  : "))
                    size_l.append(size)

    elif option == 2:
        print("Your total bill is :",sum)
        address = input("Enter address:")
        print("Thank you for shopping your items will arrive at your doorstep in 2/3 working days, we only except cash on delivery")
        exit(0)

                
restart = str(input("\nDid you forgot something? y/n: "))
if restart in ('y','YES','yes','Yes'):
    restart = ('Y')
else :
    x = 0
    print("\nTotal Items : ",quantity)
    for p in range(1,quantity+1):
        print("Quantity : ",q)
        print("Colour : ", colour_l[x])
        print("Size  : ", size_l[x])
        x += 1
