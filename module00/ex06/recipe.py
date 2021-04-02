cookbook={
            "sandwich": {
                "ingredients" : ["ham", "bread","cheese", "tomatoes"], 
                "meal" :"lunch", 
                "prep_time":10
            },
            "cake":{
                "ingredients" : ["flour", "sugar", "eggs"], 
                "meal": "dessert", 
                "prep_time":60},
            "salad":{
                "ingredients":["avocado", "arugula", "tomatoes", "spinach"], 
                "meal":"lunch", 
                "prep_time": 15}
          }
def menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print a cookbook")
    print("5: Quit")
    return

def print_recipe(recipe):
    #print(cookbook[recipe]['ingredients'])
    print("Recipe for {}:".format(recipe))
    print("Ingredients list:{}.".format(cookbook[recipe]['ingredients'])) 
    print("To be eaten for {}.".format(cookbook[recipe]['meal']))
    print("Takes {} minutes of cooking.".format(cookbook[recipe]['prep_time']))
    return
def print_cookbook():
    for item in cookbook.items():
        print("\n")
        print_recipe(item[0])
    return
def del_recipe(recipe):
    del cookbook[recipe]
    print("recipe for {} deleted.".format(recipe))
    return
def add_recipe(recipe, ing, m, prep_time):
    cookbook[recipe]={}
    cookbook[recipe]['ingredients']=ing
    cookbook[recipe]['meal']=m
    cookbook[recipe]['prep_time']=prep_time
    print("\n {} added successfully.".format(recipe))
    return

menu()
choix=input()
while 1:
    if choix=='5':
        print("Cookbook closed")
        break
    elif choix=='1':
        print("Add a recipe")
        recipe=input("Enter a recipe name :")
        ing = input("Enter the ingredients:")
        my_ing=[]
        my_ing = list(ing.split(' '))
        print(my_ing)
        meal=input("Enter the type of meal:")
        prep_time=input("Enter the preparation time in minutes:")
        add_recipe(recipe, my_ing, meal, prep_time)
        break
    elif choix=='2':
        recipe=input()
        del_recipe(recipe)
        break
    elif choix=='3':
        recipe=input()
        print_recipe(recipe)
        break
    elif choix=='4':
        print_cookbook()
        break
    else:
        print("\nThis option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
    choix=input()
