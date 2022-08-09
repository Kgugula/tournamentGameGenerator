
### TOURNAMENT GAME GENERATOR

''' This program can schedule games that teams will play in an end of year tournament.
    This program is only responsible for the first round of the tournmanet.
    The first game outputted will contain the team with the most regular season wins vs. least
    regular season wins, the second game will contain the team with the second most regular
    season win vs.second least regular season wins etc. Home team of each matchup is the team with the least wins of the two, if there is
    a tie in wins the program will choose a team at random
    '''

## Assumptions

''' Assume there will always be an even number of teams
    User input will always be the correct type (i.e. ask for a number
    it will always be of type int '''

# Ask user to input the number of teams
# Going to start with a while loop to keep running an input function
# Constraints: number of teams has to be greater than 2

number_of_teams_complete = False


while not number_of_teams_complete:
    number_of_teams = int(input("Enter the number of teams in the tournament: "))
    if number_of_teams >= 2:
        break
    print("The minimum number of teams is 2, try again.")
    number_of_teams_complete = False

# Need to gather the teams names corresponding to the number of teams
# Storing names in list

# Initialize list

team_names = []

# Counter to hold the number associated with the team (for the input prompt)
# When counter is greater than number of teams - end while loop
# Start at 1 b/c can't be team #0

counter = 1

while counter <= number_of_teams:
    teamName = input(f"Enter the name for team #{counter}: ")
    tempName_check = teamName.split() # To check if they entered more than two words (put input into list, separated by whitespace)
    
    if len(teamName) < 2:   # First constraint (can't be two characters)
        print("Team names must have at least 2 characters, try again.")
         
    elif len(tempName_check) > 2: # Second constraint (can't be more than two words) 
        print("Team names may have at most 2 words, try again.")

    else:
        team_names.append(teamName)
        counter += 1

# Gather how many games were played by each team
# Complete variable set to 'False" until contrainst is not breached
# In this case user has to enter int that is greater than the number of teams less one - constraint on PE assignment - each team must play each other at least once

not_complete = True

while not_complete:
    games_played_each_team = int(input('Enter the number of games played by each team: '))
    if games_played_each_team >= (number_of_teams - 1):
        break
    else:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        not_complete = True


# Need to collect and store the number of wins per team
# Putting a while loop inside for loop
# Need user to input number of wins for each team (want an input function for each iterable, hence the for loop)
# Need to keep track of wins - going to make a list of tuples containing (teamName, wins)
# Also need to be mindful of constraints:

''' wins per team can't be negative, and it can't be more than the number
    of games they played -  just a side note but there could be more
    intricate functionality here e.g. every team can't have the same number
    of wins if they played each other. Right now that is not built in'''

tournamentRecords = []

for team in team_names:

    while True:
        number_of_wins = int(input(f"Enter the number of wins team {team} had: ")) 
        if number_of_wins < 0:
            print("The minimum number of wins is 0, try again")
        elif number_of_wins > games_played_each_team:
            print(f"The maximum number of wins is {games_played_each_team}, try again.")
        else:
            tournamentRecords.append((team, number_of_wins))
            break # end while loop, go to next iterable

# With team names and their respective records (no. of wins) stored in a list of tuples
# I can sort the list based on the second element in the tuples i.e. wins

print("Generating the games to be played in the first round of the tournament...")

# Sort the list of tuples - store in a new variable

sorted_tournamentRecords = sorted(tournamentRecords, key= lambda x : x[1], reverse=True)

# First for loop just grabbing the team names from the sorted list above. Just need to grab the names since it was sorted based on wins

sorted_teamNames = []

for item in sorted_tournamentRecords:
    sorted_teamNames.append(item[0]) # grabbing first element from each tuple i.e. team name


# Opted to use a while loop
# Seems a bit 'brute force' but 'while' the sorted list is more than two, I will take the first
# and last elements (away vs. home) and print out the results - deleting the two teams after I do so

while len(sorted_teamNames) >= 2:

    homeTeam = sorted_teamNames[-1]
    awayTeam = sorted_teamNames[0]
    
    print(f"Home: {homeTeam} VS Away: {awayTeam}")

    sorted_teamNames.remove(homeTeam)
    sorted_teamNames.remove(awayTeam)
    









