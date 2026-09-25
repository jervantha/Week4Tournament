#############################################
# Name: Jeremiah Thawm
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
teams = []

# Enter 6 different teams
for i in range(6):
    print("\nEnter information for Team", i + 1)

    name = input("Team name: ")
    wins = int(input("Wins: "))
    ties = int(input("Ties: "))
    losses = int(input("Losses: "))

    # Calculate points
    points = wins * 2 + ties

    # Store team information
    teams.append([name, wins, ties, losses, points])


# Display all 6 teams
print("\n--- TOURNAMENT STANDINGS ---")

for team in teams:
    print("Team name:", team[0],
          "Wins:", team[1],
          "Ties:", team[2],
          "Losses:", team[3],
          "Points:", team[4])


# Find the team with the most points
top_team = teams[0]

for team in teams:
    if team[4] > top_team[4]:
        top_team = team


# Display the team at the top of the standings
print("\n--- TOP OF THE STANDINGS ---")

print("Team name:", top_team[0],
      "Wins:", top_team[1],
      "Ties:", top_team[2],
      "Losses:", top_team[3],
      "Points:", top_team[4])
