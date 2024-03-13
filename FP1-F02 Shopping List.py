#Dictionaries
shopping_list = {'apples':4}

#Variables
progress = True


#Main code here

print("Lets create a shopping list!")
while progress == True:
    choice = int(input("""1 = Add Item
2 = Remove Item
3 = View
4 = Quit
What would you like to do? """))
    
    if choice == 1:
        new_item = input("what would you like to add?")
        item_price = float(input("how much does that cost? $"))
        shopping_list[new_item] = item_price
    
    elif choice == 2:
        removed_item = input("what would you like to remove?")
        while removed_item not in shopping_list:
            print("That was not in the list. Try again.")
            removed_item = input("what would you like to remove?")
        shopping_list.pop(removed_item)
        
        
        
    elif choice == 3:
        print("Your list contains:")
        for i, v in shopping_list.items():
            print(i, "which costs $", v)
        pointless = input("hit enter to coninue")
            
        
    elif choice == 4:
        print("Quit")
        progress = False
    
    else:
        print("that was not an option")
    
    