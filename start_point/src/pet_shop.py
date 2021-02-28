# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) + cash
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] = get_pets_sold(pet_shop) + pets
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    
    for pet in pet_shop["pets"]:    
        if pet["breed"] == breed:
            breed_list.append(pet)
    
    return breed_list


def find_pet_by_name(pet_shop, pet_name):
    name_list = None

    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            name_list = pet
        
    return name_list


def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)  


def add_pet_to_stock(pet_shop, pet_name):
    pet_shop["pets"].append(pet_name)

def get_customer_cash(pet_shop):
    return pet_shop["cash"]


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


#OPTIONAL STUFF

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

