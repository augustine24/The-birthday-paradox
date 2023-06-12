#Hello! Please visit https://www.online-python.com and copy/paste the below code starting from import random onwards into the main.py code section 
#you will find on the website. There will be  After that use the Run button which is next to the Share button, both of which are below the section 
#where the raw code is supposed to be.
#Once that's done, below both of those sections there will be an output which tells you the answer to the million dollar question:
#If you randomly put 23 people in a room, will any of them share a birthday?
#The answer in that instance of the generated 23 people, will be showed to you and explained. Enjoy!

import random

numbers = random.choices(range(1,366), k =23)
#random.choices randomizes choices from range, and range(1,366) gives me a choice from 1 - 365 which corresponds to the days in a year.
#k=23 is put to return the amount of random numbers from 1 - 365 that will be extracted from that range, which will become the list known as 
#numbers
print(numbers)
is_duplicates = len(numbers) != len(set(numbers))
#This statement tests if the number of different values in the list numbers are equivalent to the amount of total number values.
#If they differ, then there was a duplicate value in the list, otherwise they'd both be 23.
if is_duplicates == True:
    print("There are duplicate birthdays in the list! This is an example of the birthday paradox being proven true!")
elif is_duplicates == False:
    print("There are no duplicate birthdays in the list.")
    
#How many times were there duplicate results? Try to run the code 10 times and note the results. 
#Are there not more duplicates than you would expect?
                                                                     
