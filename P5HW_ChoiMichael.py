# Michael Choi
# 11-21-24
# P5HW
# This program creates a game where the user can create soccer teams and match them against each other.  AI was used in its creation

import random
import time

def main():
    teamList = []
    run_again = "yes"
    # Display Menu
    while run_again.lower() == "yes":
        print("Menu:")
        print("1) Create a Team")
        print("2) View Teams")
        print("3) Play a Game")
        print("4) Exit")
        num = input("Pick an option to continue: ")
        print()
        match num:
            case "1":
                answer1 = "yes"
                while answer1.lower() == "yes":
                    # Store each team in a list
                    teamList.append(create_team())
                    print()
                    answer1 = input("Do you want to create another team? ")
                    print()
            case "2":
                display_teams(teamList)
                print()
            case "3":
                if len(teamList) < 2:
                    print("You need at least two teams to play a game!")
                else:
                    play_game(teamList)
                    print()
            case "4":
                print("Thanks for playing!")
                print("Game is closing.")
                run_again = "no"
            case _:
                num = print("Invalid entry. Please try again: ")
                print()

    
# Create a team with its Name, Attacking, Midfield, and Defensive score
def create_team():
    name = input("Enter the name of your team: ")
    attack = int(input("Enter the attacking score of your team: "))
    while attack < 1 or attack > 99:
        attack = int(input("Invalid score. Please enter a score between 1-100: "))
    midfield = int(input("Enter the midfield score of your team: "))
    while midfield < 1 or midfield > 99:
        attack = int(input("Invalid score. Please enter a score between 1-100: "))
    defense = int(input("Enter the defensive score of your team: "))
    while defense < 1 or defense > 99:
        attack = int(input("Invalid score. Please enter a score between 1-100: "))
# Store each team in a dictionary
    teamDict = {
        "Name": name,
        "Attack": attack,
        "Midfield": midfield,
        "Defense": defense
        }
    return teamDict
    print(f"Team {name} has been created!")
    print()

        
# Display all created teams with their stats
def display_teams(character_list): 
    print()
    print("\nTeams:")
    if len(character_list)> 0:
        for dict, team in enumerate(character_list, start=1):
                print(f"{dict}. {team['Name']} - Attack: {team['Attack']}, Midfield: {team['Midfield']}, Defense: {team['Defense']}")
    else:
        print("No teams have been created yet.")
    print()

# Logic of the game
def play_game(x):
   # Let the user choose two teams
    display_teams(x)
    team1_index = int(input("Enter the number of the first team: ")) - 1 # can't get good code to validate responses
    team1 = x[team1_index]
    team2_index = int(input("Enter the number of the second team: ")) - 1
    team2 = x[team2_index]
    
    print(f"\n{team1['Name']} vs {team2['Name']}")
    
    # Base scoring probabilities influenced by stats
    team1_attack_strength = (team1["Attack"] + team1["Midfield"]) / 2
    team2_defense_strength = (team2["Defense"] + team2["Midfield"]) / 2
    team2_attack_strength = (team2["Attack"] + team2["Midfield"]) / 2
    team1_defense_strength = (team1["Defense"] + team1["Midfield"]) / 2

    # Initialize goals to 0
    team1_goals = 0
    team2_goals = 0

    # Create total team strength variables
    team1_strength = team1["Attack"] + team1["Midfield"] + team1["Defense"]
    team2_strength = team2["Attack"] + team2["Midfield"] + team2["Defense"]
    strength_difference = abs(team1_strength - team2_strength)

    # Simulation starts
    print("\nThe match begins!\n")
    total_duration = 15  # Total game duration in seconds
    halftime_duration = total_duration // 2
    update_interval = 2  # Update interval in seconds

    # Simulate the game with live updates
    current_time = 0
    halftime_displayed = False

    while current_time < total_duration:
        # Adjust the scoring probabilities dynamically during the game based on team strengths
        if strength_difference < 10:
            # Teams are closely matched, more randomness
            team1_scoring_prob = random.uniform(0.35, 0.65)  # Randomized chance for close teams
            team2_scoring_prob = random.uniform(0.35, 0.65)
        elif strength_difference >= 15 and strength_difference < 25:
            # One team has a moderate advantage
            team1_scoring_prob = team1_attack_strength / (team1_attack_strength + team2_defense_strength) * 1.2
            team2_scoring_prob = team2_attack_strength / (team2_attack_strength + team1_defense_strength) * 0.8
        elif strength_difference >= 25:
            # One team has a significant advantage
            team1_scoring_prob = team1_attack_strength / (team1_attack_strength + team2_defense_strength) * 1.5
            team2_scoring_prob = team2_attack_strength / (team2_attack_strength + team1_defense_strength) * 0.5
        else:
            # Default balanced probability
            team1_scoring_prob = team1_attack_strength / (team1_attack_strength + team2_defense_strength)
            team2_scoring_prob = team2_attack_strength / (team2_attack_strength + team1_defense_strength)

        # Team 1 scores if the random number is less than its scoring probability
        if random.random() < team1_scoring_prob:
            team1_goals += 1
            print(f"Goal! {team1['Name']} scores! Current score: {team1['Name']} {team1_goals} - {team2_goals} {team2['Name']}")

        # Team 2 scores if the random number is less than its scoring probability
        elif random.random() < team2_scoring_prob:
            team2_goals += 1
            print(f"Goal! {team2['Name']} scores! Current score: {team1['Name']} {team1_goals} - {team2_goals} {team2['Name']}")

        # Halftime check
        if not halftime_displayed and current_time >= halftime_duration:
            print(f"\nHalftime! Current score: {team1['Name']} {team1_goals} - {team2_goals} {team2['Name']}")
            time.sleep(3)
            print("Second half starts!\n")
            halftime_displayed = True

        # Pause for update interval
        time.sleep(update_interval)
        current_time += update_interval

    # Display results
    print(f"\nFinal Score:")
    print(f"{team1['Name']} {team1_goals} - {team2_goals} {team2['Name']}")

    # Determine winner
    if team1_goals > team2_goals:
        print(f"{team1['Name']} wins!\n")
    elif team2_goals > team1_goals:
        print(f"{team2['Name']} wins!\n")
    else:
        print("It's a draw!\n")

if __name__ == "__main__":
    main()
