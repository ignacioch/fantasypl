from MySQLLib import SimpleMysql
import logging

class Player:
	#init
	def __init__(	self						, 
								playerId				, 
								name 						, 
								webName     		,
								news 						,
								chanceThis 			,
								chanceNext			,
								teamId 					, 
								transfersIn			,
								transfersOut		,
								totalPoints			,
								currentValue 		,
								minutes					,
								goalsScored			,
								assists					,
								cleanSheets			,
								goalsConceeded	,
								ownGoals				,
								penaltiesSaved	,
								penaltiesMissed	,
								yellows					,
								reds						,
								saves						,
								bonus 					,
								bps
							):

		self.playerId 				= playerId
		self.name 						= name
		self.webName					= webName
		self.news 						= news 						
		self.chanceThis 			= chanceThis 	
		self.chanceNext				= chanceNext	
		self.teamId 					= teamId
		self.transfersIn			= transfersIn
		self.transfersOut			= transfersOut
		self.totalPoints 			= totalPoints
		self.value 						= currentValue
		self.minutes					= minutes
		self.goalsScored			= goalsScored
		self.assists					= assists
		self.cleanSheets			= cleanSheets
		self.goalsConceeded		= goalsConceeded
		self.ownGoals					= ownGoals
		self.penaltiesSaved		= penaltiesSaved
		self.penaltiesMissed	= penaltiesMissed
		self.yellows					= yellows
		self.reds							= reds
		self.saves						= saves
		self.bonus 						= bonus
		self.bps							= bps

		self.db = SimpleMysql ( db ='fantasydb',
														host = 'ignatiosch-london.comctnyap4ze.eu-west-2.rds.amazonaws.com',
														user = 'ignch',
														passwd = 'p2nas0qe' ,
														autocommit = True 	,
														charset='utf8',
                     				use_unicode=True
													)

	def insertStats(self) :
		# we need to decode the data in the format we need them
		# we need the following columns :
		#		p_id
		#		p_name
		#   p_team
		#  	p_value
		#		p_last_gw
		#		p_last_gw_points
		#		p_total_score
		##########################################################
		dt = {}
		dt['p_id'											] 	= self.playerId
		dt['p_name'										] 	= self.name
		dt['p_value'									] 	= self.value
		dt['p_total_score'						] 	= self.totalPoints
		dt['p_web_name'								]		= self.webName.encode('utf8')
		#unicode(self.webName, "utf-8")
		#self.webName.encode('utf8')
		dt["p_team_code"							] 	= self.teamId 					 							
		dt["p_news"										]		= self.news																
		dt["p_chance_of_playing_this"	]		= self.chanceThis		
		dt["p_chance_of_playing_next"	]		= self.chanceNext		
		dt["p_transfers_in"						]		= self.transfersIn 				
		dt["p_transfers_out"					]		= self.transfersOut			
		dt["p_minutes"								]		= self.minutes														
		dt["p_goals_scored"						]		= self.goalsScored					
		dt["p_assists"								]		= self.assists														
		dt["p_clean_sheets"						]		= self.cleanSheets					
		dt["p_goals_conceeded"				]		= self.goalsConceeded	
		dt["p_own_goals"							]		= self.ownGoals											
		dt["p_penalties_saved"				]		= self.penaltiesSaved	
		dt["p_penalties_missed"				]		= self.penaltiesMissed
		dt["p_yellows"								]		= self.yellows														
		dt["p_reds"										]		= self.reds															
		dt["p_saves"									]		= self.saves														
		dt["p_bonus"									]		= self.bonus 															
		dt["p_bps"										]		= self.bps 		
									
		self.db.insert('player'	, # TABLE NAME
										dt 				# data 			
									)
		
		#logging.debug('Inserting data for player : %s ',str(self.name))	

	def insertScores(self) :
		playedMatches = len(self.fixtureHistory)
		scoresData={}
		scoresData['p_id'] = self.playerId
		for i in range(0,playedMatches) :
			gw = i + 1
			gw_score = self.fixtureHistory[i][-1]
			scoresData['s_gw_'+str(gw)] = gw_score
		for i in range(playedMatches,39) :
			scoresData['s_gw_'+str(i)] = 0
		self.db.insert('Scores',		# TABLE NAME
										scoresData	# data
									)
		logging.debug('Scores : %s' , str(scoresData))	


	def updateStats(self) :
		# we need to update only for the data that changed
		# so we update the 
		#	   p_last_gw_points
		#		 p_last_gw
		#    p_total_score
		#		 p_value
		#    p_team [in case player has changed team]
		dt = {}
		dt['p_team'] = self.teamName
		dt['p_value'] = self.value
		dt['p_last_gw_points'] = self.fixtureHistory[-1][-1]
		dt['p_last_gw'] = self.lastPlayedGW
		dt['p_total_score'] = self.totalPoints
		logging.debug('Updating data for player : %s ',str(self.name))	
		logging.debug('New Data : %s',str(dt))
		self.db.update( table = 'PlayerStats' ,	# table
										data  = dt , # data
										where = ("p_id = %s",[self.playerId]) # where
									)

	def updateScores(self) :
		currentPlayer = self.db.getOne( table = 'Scores',
																		where = ("p_id = %s",[self.playerId])
																	)
		# update the scores only for the new GWs
		lastGW = currentPlayer['p_last_gw']
		# lastGW to currentGW need to be updated
		logging.debug("last gw updated is %s " , str(lastGW))
		logging.debug("about to update until GW %s", str(self.lastPlayedGW))

		for x in range(lastGW,self.lastPlayedGW):
			logging.debug("Updating Player Stats for GW %d ",x)




	def fetchAll(self) :
		print self.db.getAll('PlayerStats')

	#
	# getters 
	####################################

	def getFixtures(self) :
		return self.fixtureHistory
