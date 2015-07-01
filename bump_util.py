"""
bump_util.py
@author: Suyash Kumar
Common Bumper Pool Functions/Utilities 
"""

from parsing import * # Import parse functions


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
        Dict with win values and dates for all games played by playerOne against playerTwo (in that perspective only)
    """
       
    p1Data=playerData[playerOne]
    returnData={'win':[],'date':[]} # From Player One's perspective
    for i in xrange(0,len(p1Data['games'])):
    	if (p1Data['opponent'][i]==playerTwo):
    		returnData['win'].append(p1Data['games'][i])
    		returnData['date'].append(p1Data['dates'][i])
    return returnData



if __name__ == '__main__':
    playerData=parse.parse('parsing/master.csv')
    print playerCompare('Josh','Suyash',playerData)

