
import requests                #to add: -AI to generate a name of the meal, nutrients (range of nutrients into which randomly choose a qty)
import random                  #         based on what I have done today (workout, i.e.)  
import csv                     
                                


values = []
api_key = "a8efbe77e58f4a3cb2f122763ec18a08"

#reading CSV + indexing
def main():
    meal = input("What do you want to eat today? ").lower()
    with open("blacklist.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["query","user_input"])
        user_friendly(reader)
    while True:
        try:
            variable = requests.get("https://api.spoonacular.com/recipes/complexSearch?",
                                    params={"query":meal, "cuisine":"Italian", "apiKey": api_key}
                    ).json()
            loops(variable)
            break
        except IndexError:
            pass
   # loops(variable)
    

def user_friendly(r):
    for i, row in enumerate(r):
        if 1 <= i < 19:
            if row["user_input"].strip() == "":
                if "min" in row["query"]:
                    values.append("0")
                if "max" in row["query"]:
                    values.append("1000")
            else:
                values.append(row["user_input"].strip().replace(",", "&"))


def loops(api):
    recipes_number = []
    dishes = []
    ids = []
    ideas = 0
    for i in api["results"]:
            ideas=ideas + 1
    
        
    for i in range(ideas):
        recipes_number.append(i)

    rnd_k = random.choice(range(ideas))
    rnd_recipe = random.choices(recipes_number, k=rnd_k)  #I get a list of int

    for index in rnd_recipe:
        dish = api["results"][index]["title"]
        print(dish)
        dishes.append(dish)
        id = api["results"][index]["id"]
        ids.append(id)


    while True:
        choose_recipe = input("Which one would you like to try? ")
        if choose_recipe in dishes:
            break


    for id in ids:  #gets a list of ingredients
        shopping = requests.get(f"https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey={api_key}").json()

        for ingredient in shopping["ingredients"]:
            output = ""
            output = str(ingredient["amount"]["metric"]["value"]) + ingredient["amount"]["metric"]["unit"] + (" ") + ingredient["name"]
            
            
            with open("shoppinglist.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([output])

if __name__=="__main__":
    main()

