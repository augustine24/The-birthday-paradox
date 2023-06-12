#Hello! Please visit https://www.online-python.com and copy/paste the below code starting from import random onwards into the main.py code section 
#you will find on the website. There will be  After that use the Run button which is next to the Share button, both of which are below the section 
#where the raw code is supposed to be.
#Once that's done, below both of those sections there will be an output which tells you the answer to the million dollar question:
#If you randomly put 23 people in a room, will any of them share a birthday?
#The answer in that instance of the generated 23 people, will be showed to you and explained. Enjoy!

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
                                                                     
