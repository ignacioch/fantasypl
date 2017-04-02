"""FindOppTransfers

Example
-------

Parameters
----------
x : type
   Description of parameter `x`.

"""
import argparse
import itertools
from MySQLLib import SimpleMysql

db = SimpleMysql (  db ='fantasydb'     ,
                    host = 'ignatiosch-london.comctnyap4ze.eu-west-2.rds.amazonaws.com',
                    user = 'ignch'      ,
                    passwd = 'p2nas0qe' ,
                    autocommit = True   ,
                    charset='utf8'      ,
                    use_unicode=True
                 )

player_values = db.getAll( 'player', order=["p_id", "ASC"])


def getAllSubteams( original_team , transfers_made ) :
    list_possible_teams = list( itertools.combinations( original_team , 15 - transfers_made))
    print list_possible_teams
    return list_possible_teams


def getTeamsToParse( ) :
    return [ 4 ] #[1,2,3,4]
    # demo data , 1: Graham , 2 : Chio , 3 : Kats , 4 : Nacho
    # later on this should come from the db


def getCurrentTeamPlayers( teamId ) :
    if ( teamId == 1) :
        return [
            100 , # Hennessey
            125 , # Baines
            132 , # Funes Mori
            98  , # Valencia
            412 , # Nyom
            321 , # Pieters
            368 , # Siggurdson
            48  , # King
            398 , # Alli
            462 , # Lanzini
            97  , # Costa
            143 , # Lukaku
            239 , # Aguero
            155 , # Snodgrass
            54    # Heaton
        ]
    elif ( teamId == 2 ) :
        return [
            340 , # PIckford
            55  , # Lowton
            321 , # Pieters
            436 , # McAuley
            48  , # King
            464 , # Antonio
            402 , # Son
            394 , # Eriksen
            500 , # Llorente
            239 , # Aguero
            143 , # Lukaku
            54  , # Heaton
            344 , # Van Aanholt
            203 , # Coutinho
            431 , # Evans
        ]
    elif ( teamId == 3 ) :
        return [
            188 , # Mignolet
            297 , # Fonte
            78  , # Cahill
            126 , # Coleman
            212 , # Mane
            48  , # King
            134 , # Barkley
            12  , # Sanchez
            468 , # Carroll
            143 , # Lukaku
            500 , # Llorente
            100 , # Hennessey
            384 , # Walker
            633 , # Ollson
            462 , # Lanzini
        ]
    elif ( teamId == 4 ) :
        return [
            54  , # Heaton
            340 , # Pickford
            561 , # Alonso
            438 , # Brunt
            152 , # Robertson
            362 , # Amat
            98  , # Valencia
            12  , # Sanchez
            468 , # Carroll
            143 , # Lukaku
            97  , # Costa
            212 , # Mane
            394 , # Eriksen
            48  , # King
            368 , # Siggurdson
        ]
    else :
        return []

def fetchLiveTeamData( teamId ) :
    if ( teamId == 1) :
        return ( 1038 , 0 )
    elif ( teamId == 2 ) :
        return ( 1031 , 0 )
    elif ( teamId == 3 ) :
        return ( 1017 , 0 )
    elif ( teamId == 4 ) :
        return (1063 , 1 ) # suppose that I did :
    else :
        return ( 0 ,0 )

def getTeamValue( candidate ) :
    tv = 0
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    #cur = db.cursor()
    # Use all the SQL you like
    #cur.execute("SELECT * FROM player")

    # print all the first cell of all the rows
    #for row in cur.fetchall():
    #   print row[0]
    #print player_values
    for player in candidate :
        print 'Get team value for player ' + str(player)
        print player_values[player - 1]
        tv += player_values[player - 1].p_value
    return tv

def findPlayersWithValue ( value ) :
    players = []
    for player in player_values :
        if  player.p_value == value :
            players.append( player )
    return players

def getTransfersForTeamId ( teamId ) :
    print 'Parsing data for team ' + str(teamId)
    getCurrentTeamPlayers( teamId )
    ( current_tv , transfers_made ) = fetchLiveTeamData( teamId )
    current_team_players = getCurrentTeamPlayers( teamId )
    print current_team_players
    list_possible_teams = getAllSubteams( current_team_players , transfers_made )
    # get current live team value
    for candidate in list_possible_teams :
        print candidate
        # get value of candidate team missing x players
        candidate_tv = getTeamValue ( candidate )
        print candidate_tv
        # find players from the db that add up to this number
        print 'Looking for players with a value of ' + str( current_tv - candidate_tv )
        possible_transfers = findPlayersWithValue( current_tv - candidate_tv )
        print possible_transfers
        # filter data out
        break

if __name__ == "__main__" :
    # parse arguments
    #   -i , --id  is the user id we want to find the opponents
    #############################################################
    '''logging.basicConfig(filename='findTransfers.log',level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" ,"--id" , help="fpl id")
    args = parser.parse_args()'''

    monitoredTeams =  getTeamsToParse()
    for team in monitoredTeams :
        getTransfersForTeamId( team )



