import csv

players=[]
Shark=[]
Dragons=[]
Raptors=[]

def readCSV():
    '''
    parses the csv file
    '''
    with open('soccer_players.csv', newline='') as csvfile:
        player = csv.DictReader(csvfile, delimiter=',')
        rows = list(player)
        for row in rows[0:19]:
            players.append(row)

def checkPlayer(player, team):
    '''
    Chek to see if the experience level for each team is even or not and if
    another player can be added
    @param player - details of the player
    @param team - a list of players on the team
    @return boolean - true if the player can be added to team based on Experience
                      false if the player can't be added to team based on Experience
    '''
    exp = player['Soccer Experience']
    countE = 0
    for p in team:
        if p['Soccer Experience'] == exp:
            countE += 1
    if countE < 3:
        return True
    else:
        return False

def createTeam():
    '''
    Split players up into teams
    '''
    for player in players:
        if checkPlayer(player, Shark):
            Shark.append(player)
        elif checkPlayer(player, Dragons):
            Dragons.append(player)
        elif checkPlayer(player, Raptors):
            Raptors.append(player)

def createTeamTxt():
    '''
    Starts the process to write the details of each team
    '''
    with open('teams.txt', 'w') as teamsFil:
        writeTeamTxt('Shark', Sharks, teamsFile)
        writeTeamTxt('Dragons', Dragons, teamsFile)
        writeTeamTxt('Raptors', Raptors, teamsFile)

def writeTeamTxt(teamName, team, teamsFile):
    '''
    Writes to the team.txt with the team name and player's info
    @param teamName - the name of the teams
    @param team - a list of soccer_players
    @param teamsFile - the opened file of teams.txt
    '''
    playerInfo = "{}, {}, {}\n"
    teamsFile.write(teamName+'\n========================\n')
    for player in team:
        teams.write(playerInfo.format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))
    teamsFile.write()

def createWelcomeLetter():
    '''
    This function is used to start the process of creating welcome letters
    '''
    writeTeamWelcomeLetter('Shark', Shark, '5', '00')
    writeTeamWelcomeLetter('Dragons', Dragons, '5', '30')
    writeTeamWelcomeLetter('Raptors', Raptors, '6', '00')

def writeTeamWelcomeLetter(teamName, team, hour, minute):
    '''
    Writes individual letter to each player's Guardian
    @param teamName - the name of the team.
    @param tema - a list of all the players for that team
    @param hour - the hour of day practice starts
    @param minute - the minute of the hours practice stars
    '''
    letter = "Dear {},\n Your child's, {}, team is {}. Practice starts on Monday, August 1, 2017 at {}:{} PM"
    for player in team:
        name = player['Name'].lower()
        nameSplit = name.split(' ')
        fileName = '_'.join(nameSplit)+'.txt'
        with open(fileName, 'w') as welcome:
            welcome.write(letter.format(player['Guardian Name(s)'],
                                        player['Name'],
                                        'Raptors', hour, minue))


if __name__ == '__main__':
    '''
    This is the main function
    '''
    readCSV()
    createTeam()
    createTeamTxt()
    createWelcomeLetter()
