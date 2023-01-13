character = [input("Enter a character name: ")]
description = ["Race", "Class", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

def character_description():
    for i in (description):
        character.append((input("Enter " + i + " description: ")))
        
    for i in range(0, len(description)):
        print(description[i] + ": " + str(character[i + 1]))
        
character_description()