"""@package docstring
Script which will run daily @4am UK time and collect all daily updates for football fantasy dbs.

We will fetch and update :
    + player db ( current_price , transfers_in , transfers_out )
"""

import urllib, json
import requests
import argparse

from Player import Player

from MySQLLib import SimpleMysql

import logging

def parse_score_for_player(data) :
	player = Player ( playerId 						= data["id"]														,
									  name 								= data["first_name"] + " "+ data["second_name"]	,
									  webName 						= data["web_name"] 											,
									  teamId 							= data["team_code"] 										,
									  news								= data["news"]													,
									  chanceThis					= data["chance_of_playing_this_round"]	,
									  chanceNext					= data["chance_of_playing_next_round"]	,
									  totalPoints 				= data['total_points'] 									,
									  transfersIn 				= data["transfers_in"]									,
									  transfersOut 				= data["transfers_out"]									,
									  currentValue 				= data['now_cost'] 											,
									  minutes							= data["minutes"]												,		
										goalsScored					= data["goals_scored"]									,
										assists							= data["assists"]												,	
										cleanSheets					= data["clean_sheets"]									,
										goalsConceeded			= data["goals_conceded"]								,
										ownGoals						= data["own_goals"]											,
										penaltiesSaved			= data["penalties_saved"]								,
										penaltiesMissed			= data["penalties_missed"]							,
										yellows							= data["yellow_cards"]									,	
										reds								= data["red_cards"]											,		
										saves								= data["saves"]													,		
										bonus 							= data["bonus"]													,		
										bps 								= data["bps"]				
									)
	return player
	

def init_players_data( json_data ):
	totalPlayers = len( json_data[ "elements" ] )
	for x in range( 0, totalPlayers ):
		player = parse_score_for_player( json_data["elements"][x]) 
		# in the first time we need to update all the dbs with the data so far
		player.insertStats()
		#update scores db for each history fixture
		#player.insertScores()'''


def update_scores():
	# fetch played GWs so far
	# compare with the length of the fixtureHistory
	# if different get the tail of the list [or as a security get the last N elements based on the length difference]
	# update the DB with these data
	for x in range(1, 2):
		logging.info('update data for %s' , str(x))
		player = parse_score_for_player(15) 
		# in the first time we need to update all the dbs with the data so far
		player.updateStats()
		#update scores db for each history fixture
		player.updateScores()



if __name__ == "__main__" :
	# parse arguments
	#   first_time will fetch all the data up the current date
	#		update means it will update for the new gameweeks only
	##########################################################
	logging.basicConfig(filename='fantasydevbackend.log',level=logging.DEBUG)
	parser = argparse.ArgumentParser()
	parser.add_argument("-i" ,"--init", action="store_true" , help="init databases")
	args = parser.parse_args()	
	
	### get response into an object
	url = "https://fantasy.premierleague.com/drf/bootstrap-static" 
	response = requests.get(url) #urllib.urlopen(url)
	json_data = response.json()

	## we should save the existing api json file as our back up on our S3 instance
	## TODO - save the json of the day on our S3 instance


	if ( args.init ) :
		init_players_data( json_data )
	#elif (args.update_type == "update") :
		#update_scores()



