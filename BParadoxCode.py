import random

numbers = random.choices(range(1,366), k =23)
print(numbers)
is_duplicates = len(numbers) != len(set(numbers))
if is_duplicates == True:
    print("There are duplicate birthdays in the list! This is an example of the birthday paradox being proven true!")
elif is_duplicates == False:
    print("There are no duplicate birthdays in the list.")
    
#How many times were there duplicate results? Try to run the code 10 times and note the results. 
#Are there not more duplicates than you would expect?
                                                                     
