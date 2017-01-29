import unittest
import json
from getPlayersScore import *

class GetPlayersScore ( unittest.TestCase ) :
    def setUp( self ):
        with open('test_data.json') as json_file:
            self.json_data =  json.load( json_file )   

    def test_PlayerWithId2( self ) :
        data    = self.json_data["elements"][1]
        player  = parse_score_for_player( data) 
        self.assertEqual( data["id"]                                , 
                          player.playerId                           )
        self.assertEqual( data["first_name"] + data["second_name"]  , 
                          player.name                               )
        self.assertEqual( data["web_name"]                          , 
                          player.webName                            )      
        self.assertEqual( data["team_code"]                         ,
                          player.teamId                             )       
        self.assertEqual( data["news"]                              ,
                          player.news                               )  
        self.assertEqual( data["chance_of_playing_this_round"]      ,
                          player.chanceThis                         )  
        self.assertEqual( data["chance_of_playing_next_round"]      ,
                          player.chanceNext                         )       
        self.assertEqual( data['total_points']                      ,
                          player.totalPoints                        )  
        self.assertEqual( data["transfers_in"]                      ,
                          player.transfersIn                        )           
        self.assertEqual( data["transfers_out"]                     ,
                          player.transfersOut                       )  
        self.assertEqual( data['now_cost']                          ,
                          player.value                              )           
        self.assertEqual( data["minutes"]                           ,
                          player.minutes                            )               
        self.assertEqual( data["goals_scored"]                      ,
                          player.goalsScored                        )  
        self.assertEqual( data["assists"]                           ,
                          player.assists                            )          
        self.assertEqual( data["clean_sheets"]                      ,
                          player.cleanSheets                        ) 
        self.assertEqual( data["goals_conceded"]                    ,
                          player.goalsConceeded                     )  
        self.assertEqual( data["own_goals"]                         ,
                          player.ownGoals                           )           
        self.assertEqual( data["penalties_saved"]                   ,
                          player.penaltiesSaved                     )  
        self.assertEqual( data["penalties_missed"]                  ,
                          player.penaltiesMissed                    )  
        self.assertEqual( data["yellow_cards"]                      ,
                          player.yellows                            )  
        self.assertEqual( data["red_cards"]                         ,
                          player.reds                               )           
        self.assertEqual( data["saves"]                             ,
                          player.saves                              )  
        self.assertEqual( data["bonus"]                             ,
                          player.bonus                              )  
        self.assertEqual( data["bps"]                               ,
                          player.bps                                )  

if __name__ == '__main__':
    unittest.main()          
                                    
