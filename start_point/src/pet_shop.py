


def get_pet_shop_name(pet_shop):
    return pet_shop["name"] 


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount_of_cash):
    pet_shop["admin"]["total_cash"] += amount_of_cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number):
    pet_shop["admin"]["pets_sold"] += number

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    found_pets = [] 
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            found_pets.append(pet)
    return found_pets
   
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            return pet 

def remove_pet_by_name(pet_shop, name):
    found_pet = ""
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            found_pet = pet

    pet_shop["pets"].remove(found_pet)        

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount 

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

 # --- OPTIONAL ---

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True 
    return False

# These are 'integration' tests so we want multiple asserts.

# def sell_pet_to_customer(pet_shop, pet, customer):
    # if customer["cash"] >= pet["price"]:
    #     customer["cash"] -= pet["price"]
    #     pet_shop["admin"]["total_cash"] += pet["price"]
    #     pet_shop["admin"]["pets_sold"] += 1
    #     pet_shop["pets"].remove(pet)
    #     customer["pets"].append(pet)

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None:
        return

    if customer_can_afford_pet(customer,pet):
        remove_customer_cash(customer,pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)













# def test_add_or_remove_cash__add(get_total_cash):
#         test_add_or_remove_cash__add("Sir Percy")
#         return get_total_cash("Sir Percy")







# def test_pets_sold(gets_pets_sold):
#         return gets_pets_sold("Chamelot of pets")


