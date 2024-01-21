# You are at a vending machine. If you are hungry and want something salty or you are thirsty, get a drink. If you are hungry and want something sweet, get a chocolate bar
import sys





#######FUNCTIONS########
def handle_sweet_salty(user_salty, user_sweet):
   #if sweet/salty
   if user_salty == 'yes' and user_sweet == 'yes':
       print('Get some chips')
       handle_add_to_receipt('Chips', receipt)
       print('Get a chocolate bar')
       handle_add_to_receipt('Chocolate Bar', receipt)
   elif user_salty == 'yes':
       print('Get some chips')
       handle_add_to_receipt('Chips', receipt)
   elif user_sweet == 'yes':
       print("Get a chocolate bar")
       handle_add_to_receipt('Chocolate Bar', receipt)
   elif user_sweet == 'no' and user_salty == 'no':
       print('Come back when your hungry... :)')
       handle_add_to_receipt('None', receipt)





def handle_add_to_receipt(item, receipt): {
    receipt.append(item)
    
}

#######FUNCTIONS########










##main program
       
##list
receipt = []


# Welcome message
print("Welcome to the Vending Machine")
# Prompts
user_hungry = str(input('Are you HUNGRY?: ')).lower()
user_thirsty = str(input('Are you THIRSTY?: ')).lower()




#for both
if user_thirsty == 'yes' and user_hungry == 'yes':
   print('Get a drink')
   handle_add_to_receipt('Drink', receipt)

   #for hungry
   user_salty= str(input('Do you want something SALTY?: ')).lower()
   user_sweet = str(input('Do you want something SWEET: ')).lower()
   ##FUNCTION CALL##
   handle_sweet_salty(user_salty, user_sweet)



#if hungry
elif user_hungry == 'yes':
   user_salty= str(input('Do you want something SALTY?: ')).lower()
   user_sweet = str(input('Do you want something SWEET: ')).lower()
   ##FUNCTION CALL##
   handle_sweet_salty(user_salty, user_sweet)






#if thirsty
elif user_thirsty == 'yes':
   print('Get a drink')
   handle_add_to_receipt('Drink', receipt)


#if none
elif user_hungry == 'no' and user_thirsty == 'no':
    print('Come back when your hungry or thirsty... :)')
    handle_add_to_receipt('None', receipt)



# Display receipt
print("Receipt:", receipt)

# Pause before exiting
input("Press Enter to exit...")