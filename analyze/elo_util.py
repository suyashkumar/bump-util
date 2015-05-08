# elo_util.py
# @author Suyash Kumar (suyashkumar)
# Utilities to calculate all players' ELO ranking. 
# Provides methods that can eventually be integrated 
# into parse.py but can currently be used standalone 
# to calculate current ELO rankings or ELO rankings 
# up to a certain point 
import math
'''
Calculates the ELO of all players. The 
input parameter file specifies the master ledger
file (unparsed). This method can be integrated into
the main parse method of parse.py in the future as 
it is essentially the same. 

K=32 for players with R<1010
K=24 for players with 1010<R<=1100
K=16 for players with R>1100
'''
rankedList=['Tyler','Kaighn','Will','Jorge','Henry','James','Shaunak','Adil','Jonah','Kaustav','Mehul','Jeremy','Brian','Emma','Eddie','Scoots','Mithun','Jacob','Jason','Lizzie','Alex','Murphy','Sanford','Ben','Lyon','Bryce','Josh','MattyP','Nick','Sahil','Rachel','Yitaek','Sachin','PapaBear','Graeme','Suyash']
def calculateElo(file):
	mFile=open(file,'r')
	# Skip first two lines in file
	mFile.readline();
	mFile.readline(); 
	currentDate="replace"
	playerElos={}
	# Loop through each line in file.
	for line in mFile:
		currentData=line.split(','); # Split at , delimiter
		# Update the current date if it needs to be changed
		if (len(currentData[2])>1 and currentData[2]!=currentDate):
			currentDate=currentData[2] # Update current date
		name=currentData[0].strip()
		playerOne=currentData[0].strip().split(" ")[0]
		playerTwo=currentData[1].strip()

		if (len(name.split(" "))>1):
			# Repeat games!
			repeat=int(name.split(" ")[1])
			print repeat , "Repeat Games"
			for i in xrange(0,repeat):
				updateElo(playerOne,playerTwo,playerElos, currentDate)
		
		else:
			updateElo(playerOne, playerTwo,playerElos, currentDate)
	return playerElos

		

def updateElo(playerOne,playerTwo,playerElos,currentDate):
	# Return if player not ranked
	if ((playerOne not in rankedList) or (playerTwo not in rankedList)):
		return

	# Add new players if required. 
	if (playerElos.get(playerOne) == None):
		# Add Player One with starting elo=1000. Dates are keys in eloHistory.
		# Only the latest elo of the day ends up sitting in eloHistory for a given
		# date. 
		playerElos[playerOne]={'currentElo':1000,'eloHistory':{}}
	if (playerElos.get(playerTwo) == None):
		playerElos[playerTwo]={'currentElo':1000,'eloHistory':{}}
	
	# Calculate Expected Win Chance for playerOne
	Ra=playerElos[playerOne]['currentElo']
	Rb=playerElos[playerTwo]['currentElo']
	Ea=1/(1+math.pow(10,((Rb-Ra)/400)))
	# Update player Elos
	deltaEloPlayerOne=getK(Ra)*(1-Ea)
	deltaEloPlayerTwo=getK(Rb)*(0-(1-Ea))
	print getK(Ra)

	playerElos[playerOne]['currentElo']=Ra+deltaEloPlayerOne
	playerElos[playerTwo]['currentElo']=Rb+deltaEloPlayerTwo
	# Update elo history for the given date
	playerElos[playerOne]['eloHistory'][currentDate]=Ra+deltaEloPlayerOne 
	playerElos[playerTwo]['eloHistory'][currentDate]=Rb+deltaEloPlayerTwo
	



'''
Returns appropiate K-factor for given input Elo
'''	
def getK(currentElo):
	if (currentElo<=1010):
		return 32
	elif ((currentElo>1010) and (currentElo<=1100)):
		return 24
	else:
		return 16 
 
		
if __name__=='__main__':
		
	playerElos=calculateElo('master.csv')
	#print playerElos
	players=playerElos.keys()
	for i in xrange(0,len(playerElos)-1):
		print players[i]
		print playerElos[players[i]]['currentElo']

