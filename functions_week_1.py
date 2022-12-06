import numpy as np
import os

def open_current_file(current_day: str)-> list:
    """Reads the file of the day, and returns it as a list.

    Args:
        current_day (str): Day of the advent.

    Returns:
        list: List containing the input of the day.
    """    
    filename = 'dag_' + str(current_day) + '.txt'
    with open(os.path.join('input', filename)) as f:
        text = f.readlines()

    text = [line.replace('\n', '') for line in text]    
    return text

#############################################
# Day 1
#############################################

def calc_calories(text: list):
    """Calculates the calories an elf has in their backpack.

    Args:
        text (list): List containing the input of the day.
    """    
    current_calories = 0
    highest_calories = 0
    for line in text:
        if not line:
            highest_calories = max(highest_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    print(f"Highest calories: {highest_calories}") #70369


def calc_highest_3_calories(text: list): 
    """Calculates the sum of the calories that the three elves with the highest 
    calories in their backpack have.

    Args:
        text (list): List containing the input of the day.
    """    
    highest_3_calories = [0, 0, 0]
    current_calories = 0

    for line in text:
        if not line:
            highest_3_calories[0] = max(highest_3_calories[0], current_calories)
            highest_3_calories.sort()
            current_calories = 0
        else:
            current_calories += int(line)

    print(f"Highest 3 calories: {highest_3_calories}. Their sum is {sum(highest_3_calories)}")


#############################################
# Day 2
#############################################

def rps(opponent: str, player: str)-> int:
    """Calculates RPS scores based on what the opponent plays.
    Playing scissors is optimal.

    Args:
        opponent (str): Move of the opponent.
        player (str): Move of the player.

    Returns:
        int: Resulting score of the two moves.
    """    
    # Win
    if player == 'X' and opponent == 'C' or player == 'Y' and opponent == 'A' or player == 'Z' and opponent == 'B':
        score = 6
    # Draw
    elif player == 'X' and opponent == 'A'or player == 'Y' and opponent == 'B' or player == 'Z' and opponent == 'C':
        score = 3
    # Lose
    elif player == 'X' and opponent == 'B'or player == 'Y' and opponent == 'C' or player == 'Z' and opponent == 'A':
        score = 0

    if player == 'X':
        score += 1
    elif player == 'Y':
        score += 2
    elif player == 'Z':
        score += 3
    return score

def rps_2(tactic: str, player: str):
    """Calculates RPS scores based on whether you should win, draw, or lose.
    Playing scissors is still optimal.

    Args:
        tactic (str): Move of the opponent.
        player (str): Move of the player.

    Returns:
        int: Resulting score of the two moves.
    """     
    # Rock
    if player == 'X' and tactic == 'B' or player == 'Y' and tactic == 'A' or player == 'Z' and tactic == 'C':
        score = 1
    # Paper
    elif player == 'X' and tactic == 'C' or player == 'Y' and tactic == 'B' or player == 'Z' and tactic == 'A':
        score = 2
    # Scissors
    elif player == 'X' and tactic == 'A' or player == 'Y' and tactic == 'C' or player == 'Z' and tactic == 'B':
        score = 3

    if player == 'X':
        score += 0
    elif player == 'Y':
        score += 3
    elif player == 'Z':
        score += 6
    return score

def get_rps_score(text: list, rps_style: bool = 1):
    """Get the rps scores of either rps 1 or rps 2.

    Args:
        text (list): List containing the input of the day.
        rps_style (bool, optional): Which rps score to calculate. Defaults to 1.
    """    
    total_score = 0
    for line in text:
        opponent, player = line.split()
        if rps_style: # Unoptimal if statement, but clearer
            total_score += rps(opponent, player)
        else:
            total_score += rps_2(opponent, player)

    print(f"The total score is {total_score}")

#############################################
# Day 3
#############################################

def share_an_item(text: list)->list:
    """Determines which item is shared between rucksacks.

    Args:
        text (list): List containing the input of the day.

    Returns:
        list: List of items that are shared between rucksacks.
    """    
    shared_items = []
    for line in text:
        line_length = int(len(line)/2)
        rucksack_1 = line[:line_length]
        rucksack_2 = line[line_length:]

        for item_type in rucksack_1:
            if item_type in rucksack_2:
                shared_items.append(item_type)
                break # Shared item found, no repeats happen
    return shared_items


def calculate_priority(shared_items: list)-> int:
    """Calculates the total priority of the shared items.

    Args:
        shared_items (list): List containing the shared items between rucksacks.

    Returns:
        int: The sum over all priority values.
    """    
    total_sum = 0
    for letter in shared_items:
        if letter.islower():
            total_sum += ord(letter)-96
        elif letter.isupper():
            total_sum += ord(letter)-38
    return total_sum

def group_share(text: list):
    """Determines which item is shared in the group. The total priority 
    is then calculated.

    Args:
        text (list): List containing the input of the day.
    """    
    shared_items = []
    group_amount = int(len(text)/3)
    for idx in range(group_amount):
        rucksack_1 = text[idx*3]
        rucksack_2 = text[idx*3+1]
        rucksack_3 = text[idx*3+2]

        # Duplicate forloop, can be a function of itself
        for item_type in rucksack_1:
            if item_type in rucksack_2 and item_type in rucksack_3:
                shared_items.append(item_type)
                break # Shared item found, no repeats happen

    print(f"The total priority is {calculate_priority(shared_items)}")

#############################################
# Day 4
#############################################

def get_characters(line: list)-> tuple:
    """Get the minimum and maximum number for both sides.

    Args:
        line (list): Specific line in the list containing the input of the day.

    Returns:
        tuple: Two lists containing the minimum and maximum value of their respective character.
    """    
    char_1, char_2 = line.split(',')
    char_1_min, char_1_max = char_1.split('-')
    char_2_min, char_2_max = char_2.split('-')
    char_1_min, char_1_max, char_2_min, char_2_max = int(char_1_min), int(char_1_max), int(char_2_min), int(char_2_max)
    return [char_1_min, char_1_max], [char_2_min, char_2_max]

def get_amount_of_pairs_1(text: list):
    """Gets the amount of pairs.

    Args:
        text (list): List containing the input of the day.
    """    
    amount = 0
    for line in text:
        char_1, char_2 = get_characters(line)

        if char_1[0] <= char_2[0] and char_1[1] >= char_2[1] or char_2[0] <= char_1[0] and char_2[1] >= char_1[1]:
            amount += 1

    print(f"The amount of pairs is {amount}")

def get_amount_of_pairs_2(text: list):
    """Gets the amount of pairs, but different.

    Args:
        text (list): List containing the input of the day.
    """    
    amount = 0
    for line in text:
        char_1, char_2 = get_characters(line)
        char_1_range = np.arange(char_1[0], char_1[1]+1, 1)
        char_2_range = np.arange(char_2[0], char_2[1]+1, 1)
        overlapping_elements = [number for number in char_1_range if number in char_2_range]
        if overlapping_elements:
            amount += 1

    print(f"The amount of pairs is {amount}")


#############################################
# Day 5
#############################################
def get_crates(text: list, p: bool = True)-> tuple[list, list, list]:
    """Get the crates in a better readable format, split the
    text in placements and instructions.

    Args:
        text (list): List containing the input of the day.
        p (bool, optional): Boolean to print the crate layout. Defaults to True.

    Returns:
        tuple[list, list, list]: A list containing the crates in their specified order,
                                 A list containing the initial placements of the crates,
                                 A list contaiing the instructions given.
    """    

    crates = [[] for _ in range(9)]
    placements = text[:9]
    instructions = text[10:]
    if p:
        for line in text[:9]:
            print(line)

    placements.reverse()
    for line_of_crates in placements:
        for idx, character in enumerate(line_of_crates):
            if character.isalpha():
                crate_placement = int(idx/4)
                crates[crate_placement].append(character)
    return crates, placements, instructions

def get_instructions(instructions: list)-> list:
    """Take the numbers from each line (strings) and keep them together
    for further followup.

    Args:
        instructions (list): A list containing the instructions for moving
        the crates.

    Returns:
        list: An instruction list containing only numbers.
    """    
    instruct_list = []
    for instruction in instructions:
        temp_list = []
        word_list = instruction.split()
        for word in word_list:
            if word.isnumeric():
                temp_list.append(int(word))
        instruct_list.append(temp_list)
    return instruct_list    

def follow_instructions_1(crates: list, instruct_list: list):
    """Use the instruct list data to change the crate positions.

    Args:
        crates (list): A list containing the position of each crate.
        instruct_list (list): A list containing three numbers per instruction.

    Returns:
        _type_: The new position of the crates
    """    
    for instructs in instruct_list:
        amount = instructs[0]
        initial_loc = instructs[1]-1
        new_loc = instructs[2]-1
        for i in range(amount):
            crates[new_loc].append(crates[initial_loc][-1])
            crates[initial_loc].pop()
    return crates

def follow_instructions_2(crates: list, instruct_list: list):
    """Use the instruct list data to change the crate positions.
    A different strategy for moving crates has been chosen.

    Args:
        crates (list): A list containing the position of each crate.
        instruct_list (list): A list containing three numbers per instruction.

    Returns:
        _type_: The new position of the crates
    """    
    for instructs in instruct_list:
        amount = instructs[0]
        initial_loc = instructs[1]-1
        new_loc = instructs[2]-1
        
        crates[new_loc].extend(crates[initial_loc][-amount:])
        crates[initial_loc] = crates[initial_loc][:-amount]
    return crates


#############################################
# Day 6
#############################################

def find_marker(text: list, distinct_characters: int = 4):
    """Checks for each sequence if it exists of only distinct characters.

    Args:
        text (list): List containing the input of the day.
        distinct_characters (int, optional): Value that states how long the sequence should be. Defaults to 4.
    """    
    line = text[0]
    sequence_of_characters = line[:distinct_characters]
    for idx, letter in enumerate(line[distinct_characters:]):
        sequence_of_characters = sequence_of_characters[1:] + letter
        duplicates = [sequence_of_characters.count(part) for part in sequence_of_characters]
        if sum(duplicates) == distinct_characters:
            print(f"The sequence is: {sequence_of_characters}, the new letter is: {letter}")
            break

    print(f"The amount of characters is {idx+distinct_characters+1}")  


#############################################
# Day 7
#############################################

