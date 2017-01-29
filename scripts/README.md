Scripts that will run on the background (mostly).

## parse_player_data.py
We are parsing https://fantasy.premierleague.com/drf/bootstrap-static once a day (after 3am UK time) to check each players current data. These include :

+ elements[]
    + id
    + photo
    + web_name , first_name , second_name
    + news
    + chance_of_playing_this_round , chance_of_playing_next_round
    + team , where team codes are shown here : 
        + 3 , Arsenal
    + transfers_in , transfers_out
    + now_cost  ( a value of 54 means 5.4 )
    + total_points 
    + minutes , goals_scored , assists , clean_sheets , goals_conceded, own_goals, penalties_saved, penalties_missed , yellow_cards, red_cards , saves, bonus , bps 

# Databases description

Basic databases are :
+ players, for storing our players data
+ players_stats , for storing our players overall stats
+ players_history_price, for storing our player price per day
+ users, for storing our users
+ fantasy_teams, for storing the ids of the teams we follow
+ fantasy_teams_following, for storing which teams each users follows
+ teams , for the teams codes

**user**

| Column        | Type          | Notes | Comments |
| ------------- |:-------------:| -----:| :------- |
| user_id       | INT           | PK    | user_id  | 
| name          | STRING        |       | full name   | 
| tbd           | tbd           |       | tbc once we know methods of login |

**players**

This will contain players active data.

| Column        | Type          | Notes | Comments |
| ------------- |:-------------:| -----:| :------- |
| player_id     | INT           | PK    | player_id coming from fpl web site |
| name          | STRING        | | first_name + web_name from  api json |
| photo         | STRING        | | url abbrevation to get the photo |
| web_name      | STRING        | | | 
| news          | STRING        | | news field of json api | 
| chance_pl_this| INT           | | chance of playing this round field of json api | 
| chance_pl_next| INT           | | chance of playing next round field of json api |
| team          | INT | FK | team id - foreign key to teams table |
| transfers_in  | INT | | |
| transfers_out | INT | | |
| now_cost      | INT | | /10 gives the value in M |
| total points  | INT | | |

**players_data**

This will contain players stats data accumulated for the whole season.

| Column        | Type          | Notes | Comments |
| ------------- |:-------------:| -----:| :------- |
| player_id     | INT           | PK    | player_id coming from fpl web site |








