PLACEHOLDER = "Name"

with open("./Input/Name/invited_names.txt") as file:
    inbound = file.read()
    l_name = inbound.split()

with open("./Input/Letter/starting_letter.txt") as file:
    l_main = file.read()

for item in l_name:
    raw = l_main.replace("Name",item)
    with open(f"Output/LoadOut/{item}.txt", mode="w") as file:
        file.write(raw) 
   

    


























