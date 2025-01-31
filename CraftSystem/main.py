import random

AMNT_OF_ITEMS_AS_STARTER = 5 # amount of items the user spawns with
CHANCE_FOR_EASY_MATERIALS = 65

# prototype : item = ["empty1", "empty2", "empty3", "empty4", "empty5", "empty6", "empty7", "empty8", "empty9"]
stick1 = ["empty1", "empty2", "empty3", "wood", "empty5", "empty6", "wood", "empty8", "empty9"]
stick2 = ["empty1", "empty2", "empty3", "empty4", "wood", "empty6", "empty7", "wood", "empty9"]
stick3 = ["empty1", "empty2", "empty3", "empty4", "empty5", "wood", "empty7", "empty8", "wood"]
wood_pickaxe = ["wood", "wood", "wood", "empty4", "stick", "empty6", "empty7", "stick", "empty9"]
wood_sword = ["empty1", "wood", "empty3", "empty4", "wood", "empty6", "empty7", "stick", "empty9"]
rock_pickaxe = ["rock", "rock", "rock", "empty4", "stick", "empty6", "empty7", "stick", "empty9"]
rock_sword = ["empty1", "rock", "empty3", "empty4", "rock", "empty6", "empty7", "stick", "empty9"]

# using a dictionary to interpret what each of these values mean to the user.

crafted_items = { # cant have lists as keys.
    "a stick" : stick1,
    "b stick" : stick2, # a, b and c sticks just because keys cant be the same in a dictionary!
    "c stick" : stick3,
    "wooden pickaxe" : wood_pickaxe,
    "wooden sword" : wood_sword,
    "rock pickaxe" : rock_pickaxe,
    "rock sword" : rock_sword
}

items_that_can_be_crafted = [stick1, stick2, stick3, wood_pickaxe, wood_sword, rock_pickaxe, rock_sword]

def items_to_craft():
    print("Following are the items you can craft :")
    index = 1
    displayed_stick = False
    for i in crafted_items:
        if i[2:len(i)] == "stick" and displayed_stick:
            continue
        elif i[2:len(i)] == "stick":
            print(f"{index}) {i[2:len(i)]}")
            displayed_stick = True
            index += 1
        else:
            print(f"{index}) {i}")
            index += 1 
        

def hunt_for_materials_without_pick(inventory, materials_list):
    inven = inventory
    overall_item_chance = CHANCE_FOR_EASY_MATERIALS
    selected_chance = random.randint(1, 100)
    if selected_chance < overall_item_chance:
        inv_keys = list()
        for i in inven:
            inv_keys.append(i)
        item_to_deduct = random.choice(inv_keys)
        amnt = random.randint(1, 2)
        print(f"# You were chased down by a bear due to slow material hunting!\n> On your way back, you dropped {item_to_deduct}.\n>Craft a pickaxe so you never loose items.")
        print(f"You had {item_to_deduct} with amount {inven[item_to_deduct]}")
        inven[item_to_deduct] = inven[item_to_deduct] - amnt
        print(f"Your {item_to_deduct} has been deducted by amount {inven[item_to_deduct]}")
        
    elif selected_chance >= CHANCE_FOR_EASY_MATERIALS:
        amnt = random.randint(1, 2)
        item_to_give = random.choice(materials_list)
        already_existing = False
        if amnt == 1:
            print("# You found a material!")
        else:
            print("# You found materials!")
        for i in inven:
            if item_to_give == i:
                already_existing = True
                print(f"You had {item_to_give} with amount {inven[item_to_give]}")
                inven[i] = inven[i] + amnt
                print(f"Now, you have {item_to_give} with amount {inven[item_to_give]}")
        
        if not already_existing:
            inven[item_to_give] = amnt
            print(f"You found {item_to_give} of {inven[item_to_give]}")
    return inven
        

def append_crafted_item(inventory, item):
    appended = False
    inven = inventory
    if inven is not None:
        if item is not None:
            if item not in inventory:
                if item == "stick" and appended == False: # we dont have to loop thru since it doesnt even exist in inven
                    inven[item] = 4
                    print(f"> You've crafted 4 of {item}!")
                    appended = True
                elif appended == False:
                    inven[item] = 1
                    print(f"> You've crafted 1 of {item}!")
                    appended = True
            elif item in inventory: # we have to loop in order to find it
                for i in inven:
                    if i == "stick" and appended == False:
                        inven[i] = inven[i] + 4
                        print(f"> You've crafted 4 more of already existing {item}!")
                        print(f"Total sticks: {inven[i]}")
                        appended = True
                    elif i == item and appended == False:
                        inven[i] = inven[i] + 1
                        print(f"> You've crafted one more of {item}!")
                        appended = True
                
    return inven

def hunt_for_materials(inventory, materials_list):
    limit_of_chances = len(materials_list) * 2 # roof of chances, from 1 to limit
    number_pool = list() # numbers already selected and wont be chosen again
    chances_of_materials = dict()
    for material in materials_list:
        random_chance = random.randint(1, limit_of_chances)
        if random_chance not in number_pool:
            chances_of_materials[material] = random_chance # each material gains its own chance
            number_pool.append(random_chance)
    # then a random chance will be used, if that chance is greater than a certain item, that item will be granted.
    # whatever number gets generated, if it has a number less than itself and a number greater than itself, 
    # it'll be decided randomly which item to choose, greater chance one or lesser chance one.
    while True:
        chance_to_recieve_material = random.randint(1, limit_of_chances)
        number_pool.append(chance_to_recieve_material)
        our_index_chance = int()
        for i in range(0, len(number_pool) - 1):
            if number_pool[i] == chance_to_recieve_material:
                our_index_chance = i
        
        if our_index_chance >> 0 and our_index_chance << limit_of_chances - 1:
            break
        else:
            continue
    
    sorted(number_pool) # after this, check whats behind our index chance and what is ahead?
    
    material_1_index = our_index_chance - 1
    material_2_index = our_index_chance + 1
    
    selected_materials = list()
    for item, chance in chances_of_materials.items():
        if chance == number_pool[material_1_index]:
            selected_materials.append(item)
        elif chance == number_pool[material_2_index]:
            selected_materials.append(item)

    amnt = random.randint(1, 3)
    final_material = random.choice(selected_materials)
    inven = inventory
    if final_material not in inven:
        inven[final_material] = amnt
        print(f"> You found {amnt} of {final_material}!")
    else:
        for item, amount in inven.items():
            if item == final_material:
                amount = amount + amnt # where amnt will be added to the already existing item.
                print(f"> You got {amnt} more of {final_material}!")
                print(f"> Before, you had {amount} of {item}.")
    return inven

def identify_crafted_item(table, items_list):
    items_list_values = []
    for _, list in items_list.items():
        items_list_values.append(list) # contains all lists stored in items list as values (LIST containing LISTS)
    
    target_limit = 0
    for _ in items_list:
        target_limit += 1
    table_no = 0
    should_be_zero = 0
    targetted_key = items_list_values[table_no]
    while table_no <= target_limit - 1:
        should_be_zero = 0
        targetted_key = items_list_values[table_no] # one targetted key at a time. each while loop iter goes thru 1 key.
        for _ in range(0, 8):
            if targetted_key[table_no] != table[table_no]:
                should_be_zero += 1
        
        if should_be_zero == 0:
            for i, v in items_list.items():
                if v == table:
                    return i
        table_no += 1

def crafting_match(table_items, future_crafts): # future crafts is a list containing lists
    target_limit = 0
    match_found = False
    items_to_craft_with = table_items
    tables_to_compare_with = future_crafts
    for _ in tables_to_compare_with:
        target_limit += 1
    table_no = 0 #table number is the TABLE thats pre-defined in a list (list in a list) to easily iterate over the lists inside a list
    targetted_table = tables_to_compare_with[table_no]
    while table_no <= target_limit-1:
        targetted_table = tables_to_compare_with[table_no] # to ensure that it just doesnt check with a single list of a list
        should_be_zero = 0 # if this isnt zero, it means that the current table doesnt match w/ the pre defined table
        for i in range(0, 8):
            if items_to_craft_with[i] != targetted_table[i]:
                should_be_zero += 1
        
        if should_be_zero == 0:
            match_found = True
            return targetted_table # a match has been found between our table and the pre  defind table
        elif should_be_zero > 0:
            should_be_zero = 0
            table_no += 1
            continue
    if not match_found:
        return None

def inventory_sweeper(inventory):
    inven = inventory
    sweep = False
    for item in inven:
        if type(item) is None or type(inven) is None:
            continue
        elif inven[item] == 0 or inven[item] == '0':
            sweep  = True
            del inven[item]
            return inven
    if sweep is False: #it means theres nothing to sweep.
        return inven # return the inven as it is. THIS avoids the return of NONE type.
        

def crafting_system(table, inventory):
    table_items = list()
    for item in table:
        table_items.append(item)
    
    # we want the user to enter in the item they want to put in the table
    while True:
        item_is_there = False
        position_in_table = False
        item = input("Enter the item to craft with : ")
        if item in inventory:
            if int(inventory[item]) >= 1:
                item_is_there = True
    
        if item_is_there is False:
            print("Enter the item name correctly.")
            continue
    # where to put it?
        place = input("Enter the position where you want your item to be at : ")
        if place.isdigit():
            place = int(place)
            if place <= 9:
                position_in_table = True
        
            if position_in_table is False:
                return None
            else:
                place -= 1
                value = table_items[place]
                if value[0:len(value)-1] != "empty":
                    print("# That spot is already occupied by one of your items. Select another one.")
                    continue
                table_items[place] = item
                inventory[item] = int(inventory[item]) - 1
                quit = input("Do you wish to exit the crafting menu? (Y/N) : ").capitalize()
                if quit[0] == "Y":
                    return table_items, inventory # return a new dictionary (inventory) as well that has deductions

    
        

def crafting_menu_represent(crafting_table):
    row_1 = list()
    row_2 = list()
    row_3 = list()
    items = list()
    for item in crafting_table:
        items.append(item) # converting keys to indexes that can be utilised for representation
    
    for i in range(0, 3):
        row_1.append(items[i])
    
    for i in range(3, 6):
        row_2.append(items[i])
    
    for i in range(6, 9):
        row_3.append(items[i])
    
    craft_representation = [row_1, row_2, row_3]
    for row in craft_representation:
        print(" ".join(row))
        
                

def menu():
    print("///////////////////")
    print("-- WELCOME TO THE CRAFT SYSTEM --")
    print("\t1) Craft\n\t2) Inventory\n\t3) Hunt For Materials\t(\"Caution\": Pickaxe Recommended)\n\t4) View items that can be crafted")
    user_input = input("Enter \"option number\" to view : ")
    return int(user_input)

def inventory_represent(inventory):
    print("\n\tYou have . . .")
    i = 1
    for item, val in inventory.items():
        if val > 1:
            print(f"{i}] {val} {item}(s)")
        else:
            print(f"{i}] {val} {item}")
        i += 1

def inventory_placer():
    inventory = dict()
    i = 0
    while i <= AMNT_OF_ITEMS_AS_STARTER:
        item = random.choice(items)
        amount_of_item = random.randint(2, 4)
        
        inventory[item] = amount_of_item # placing in inventory
        i += 1
    
    return inventory
items = ["rock", "wood", "paper", "grass", "string", "coal", "sapling"] # all the items user may start with
items_to_hunt = ["rock", "wood", "paper", "grass", "string", "gravel", "sock", "sapling", "plastic", "shoe lace", "pumpkin", "apple", "watermelon slice"]
items_to_hunt_without_pick = ["wood", "rock", "paper", "string", "grass"]

def main(): # tip : we can style the code in a menu type format like minecraft itself
    inventory = inventory_placer()
    newInventory = dict()
    crafting_table = {
        "empty1" : None,
        "empty2" : None,
        "empty3" : None,
        "empty4" : None,
        "empty5" : None,
        "empty6" : None,
        "empty7" : None,
        "empty8" : None,
        "empty9" : None
    }
    i = 0
    timer = 0
    while True:
        user_input = menu()
        
        match user_input:
            case 1:
                crafting_menu_represent(crafting_table)
                if i >= 1:
                    newInventory = inventory_sweeper(newInventory)
                crafting_table_items, newInventory = crafting_system(crafting_table, inventory)
                newInventory = inventory_sweeper(newInventory) # sweep after crafting
                crafting_menu_represent(crafting_table_items)
                matched_with = crafting_match(crafting_table_items, items_that_can_be_crafted)
                # following function identifies crafted item and places it in the inventory
                if matched_with is None:
                    print("# While crafting, you forgot the recipe / guide of how to craft an item.\n> Hence, you also forgot the materials that you put on the table. Sucks to be you!")
                elif matched_with is not None:
                    crafted_item = identify_crafted_item(matched_with, crafted_items)
                    if len(crafted_item) == 7: # removing a, b amd c thats additional from sticks
                        if crafted_item[2:len(crafted_item)] == "stick":
                            crafted_item = crafted_item[2:len(crafted_item)]
                    newInventory = append_crafted_item(newInventory, crafted_item)
                
                go_back = input("Do you want to go back to menu ? (Y/N): ")
                if go_back[0].capitalize() == "Y":
                    i += 1
                    continue
                else:
                    get_out = input("Do you want to exit the system ? (Y/N) : ")
                    if get_out[0].capitalize() == "Y":
                        i += 1
                        break
            case 2:
                if i == 0:
                    inventory_represent(inventory)
                elif i >= 1:
                    newInventory = inventory_sweeper(newInventory)
                    inventory_represent(newInventory)
                go_back = input("Do you want to go back to menu ? (Y/N): ")
                
                if go_back[0].capitalize() == "Y":
                    continue
                else:
                    get_out = input("Do you want to exit the system ? (Y/N) : ")
                    if get_out[0].capitalize() == "Y":
                        break
            case 3:
                has_pickaxe = False
                for item in newInventory:
                    if item[len(item)-3:len(item)] == "axe":
                        has_pickaxe = True
                if has_pickaxe:
                    hunt_for_materials(newInventory, items_to_hunt)
                elif has_pickaxe == False:
                    print("Craft something to hunt first or take the difficult way to hunting?")
                    go_back = input("Do you want to hunt the difficult way ? \"You will loose inventory items\" (Y/N): ")
                    if go_back[0].capitalize() == "Y":
                        if timer == 0:
                            newInventory = hunt_for_materials_without_pick(inventory, items_to_hunt_without_pick)
                            newInventory = inventory_sweeper(newInventory)
                            timer += 1
                        elif timer != 0:
                            newInventory = inventory_sweeper(newInventory)
                            newInventory = hunt_for_materials_without_pick(newInventory, items_to_hunt_without_pick)
                            timer += 1
                
                go_back = input("Do you want to go back to menu ? (Y/N): ")
                if go_back[0].capitalize() == "Y":
                    continue
                else:
                    get_out = input("Do you want to exit the system ? (Y/N) : ")
                    if get_out[0].capitalize() == "Y":
                        break
            case 4:
                items_to_craft()
                go_back = input("Do you want to go back to menu ? (Y/N): ")
                if go_back[0].capitalize() == "Y":
                    continue
                else:
                    get_out = input("Do you want to exit the system ? (Y/N) : ")
                    if get_out[0].capitalize() == "Y":
                        break
            case _:
                print("Invalid option. Try again!")
if __name__ == "__main__":
    main()
