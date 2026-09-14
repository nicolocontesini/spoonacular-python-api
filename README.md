# spoonacular-python-api
A Python program that filters Spoonacular recipes by cuisine, ingredients, and macros, generating an instant shopping list.
The tool simulates a recipe-finder App/website, which gets a list of cuisine, ingredients, macros from a .csv file (user_input.csv), formatted as a dictionary.
To get a list of recipes fulfilling the user preferences, I followed these steps:

- Reported API parameters, using the csv.DictReader method. Note: thanks to the function "user_friendly", user can ignore parameters they don't care about simply typing "none" or leaving blank space (respectively, for string and numeric parameters).

- Working with list indexing, the code gets a random bunch of recipes. Note: I decided to use this functionality to become familiar with indexing (see list like "dishes" and  variable like "dish")

- The program lets users choose the one they prefer, and automatically the list of ingredients and quantities is printed in "shoppinglist.csv". Note: I preferred the "a" (append) function over the "w" (which actually overwrites) to preserve past queries.

Through this tool I gained hands-on experience with several core concepts:

- Data Sanitization: Writing robust parsing functions to convert loose user inputs into valid HTTP request parameters.

- File I/O handling to commit changes to other files.

- API integrations.

Author: Nicolò Contesini

Language: Python

Time spent: 7hrs

