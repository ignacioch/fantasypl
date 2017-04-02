from MySQLLib import SimpleMysql
import logging

class Player:
    #init
    def __init__(   self                ,
                    playerId            ,
                    name                ,
                    webName             ,
                    news                ,
                    chanceThis          ,
                    chanceNext          ,
                    teamId              ,
                    transfersIn         ,
                    transfersOut        ,
                    totalPoints         ,
                    currentValue        ,
                    minutes             ,
                    goalsScored         ,
                    assists             ,
                    cleanSheets         ,
                    goalsConceeded      ,
                    ownGoals            ,
                    penaltiesSaved      ,
                    penaltiesMissed     ,
                    yellows             ,
                    reds                ,
                    saves               ,
                    bonus               ,
                    bps                 ,
                    position
                ):

        self.playerId          = playerId
        self.name              = name
        self.webName           = webName
        self.news              = news
        self.chanceThis        = chanceThis
        self.chanceNext        = chanceNext
        self.teamId            = teamId
        self.transfersIn       = transfersIn
        self.transfersOut      = transfersOut
        self.totalPoints       = totalPoints
        self.value             = currentValue
        self.minutes           = minutes
        self.goalsScored       = goalsScored
        self.assists           = assists
        self.cleanSheets       = cleanSheets
        self.goalsConceeded    = goalsConceeded
        self.ownGoals          = ownGoals
        self.penaltiesSaved    = penaltiesSaved
        self.penaltiesMissed   = penaltiesMissed
        self.yellows           = yellows
        self.reds              = reds
        self.saves             = saves
        self.bonus             = bonus
        self.bps               = bps
        self.position          = position


    def insertStats(self , db) :
        # we need to decode the data in the format we need them
        # we need the following columns :
        #       p_id
        #       p_name
        #   p_team
        #   p_value
        #       p_last_gw
        #       p_last_gw_points
        #       p_total_score
        ##########################################################
        dt = {}
        dt['p_id'                       ]   = self.playerId
        dt['p_name'                     ]   = self.name
        dt['p_value'                    ]   = self.value
        dt['p_total_score'              ]   = self.totalPoints
        dt['p_web_name'                 ]   = self.webName.encode('utf8')
        dt["p_team_code"                ]   = self.teamId
        dt["p_news"                     ]   = self.news
        dt["p_chance_of_playing_this"   ]   = self.chanceThis
        dt["p_chance_of_playing_next"   ]   = self.chanceNext
        dt["p_transfers_in"             ]   = self.transfersIn
        dt["p_transfers_out"            ]   = self.transfersOut
        dt["p_minutes"                  ]   = self.minutes
        dt["p_goals_scored"             ]   = self.goalsScored
        dt["p_assists"                  ]   = self.assists
        dt["p_clean_sheets"             ]   = self.cleanSheets
        dt["p_goals_conceeded"          ]   = self.goalsConceeded
        dt["p_own_goals"                ]   = self.ownGoals
        dt["p_penalties_saved"          ]   = self.penaltiesSaved
        dt["p_penalties_missed"         ]   = self.penaltiesMissed
        dt["p_yellows"                  ]   = self.yellows
        dt["p_reds"                     ]   = self.reds
        dt["p_saves"                    ]   = self.saves
        dt["p_bonus"                    ]   = self.bonus
        dt["p_bps"                      ]   = self.bps
        dt["p_position"                 ]   = self.position

        db.insertOrUpdate( 'player' , # TABLE NAME
                            dt      , # data
                            'p_id'
                         )

        #logging.debug('Inserting data for player : %s ',str(self.name))    

    def insert_history_price( self , db ) :
        dt = {}
        dt['p_id'                       ]   = self.playerId
        dt['p_value'                    ]   = self.value
        db.insert( 'player_history_price' , # TABLE NAME
                    dt                      # data
                 )

