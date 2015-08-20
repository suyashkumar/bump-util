"""
bump_util.py
@author: Suyash Kumar
Common Bumper Pool Functions/Utilities 
"""

from parsing import * # Import parse functions
from elo import elo_util

#Loads stored playerData in json format, returns dict
#of player data

#@param path The (string) filepath to the json file
#@returns playerData dict with loaded player data
def jsonLoad(path):
    """
    Loads stored playerData in json format, returns dict of player data  
    Args:
        path: The filepath (String) to the json file
    Returns: 
        playerData dict with loaded player data
    """
    with open(path, 'rb') as fp:
    	playerData = json.load(fp)
    return playerData

def playerCompare(playerOne, playerTwo, playerData):
    """
    Returns a dict of win values and dates comparing playerOne to playerTwo (from playerOne's perspective) 
    Args:
        playerOne:  String name (key) for first player
        playerTwo:  String name (key) for second player 
        playerData: the dict holding all player data  
    Returns: 
        returnData: Dict with win values and dates for all games played by playerOne against playerTwo (in that perspective only)
    """
       
    p1Data=playerData[playerOne]
    returnData={'win':[],'date':[]} # From Player One's perspective
    for i in xrange(0,len(p1Data['games'])):
    	if (p1Data['opponent'][i]==playerTwo):
    		returnData['win'].append(p1Data['games'][i])
    		returnData['date'].append(p1Data['dates'][i])
    return returnData #TODO: include elohistory in this dict, tab this over to save iterations

def singleInfo(player, playerData, csvPath):
    """
    Returns playerData information for the given player along with full elo history
    Args:
        player:     the player "key" string
        playerData: playerData dict holding parsed data for all players
        csvPath:    path to the data csv (currently for elo history calculation 
    Returns:
        returnData: dict holding playerData and eloHistory for player. 
    """
    pData=playerData[player] # Get information for this player
    playerElos=elo_util.calculateElos(csvPath) # Recalc all Elos TODO: will be replaced by database read allowing for periodic recalcs 
    pElo=elo_util.getFullEloHistory(playerElos,player) # Get ELO history for this player
    returnData={'pData':pData, 'pElo':pElo} # Return dictionary holding player info
    return returnData


if __name__ == '__main__':
    playerData=parse.parse('parsing/master.csv')
    print playerCompare('Josh','Suyash',playerData)

