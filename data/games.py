from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

# object from nba_api library
game_log = leaguegamelog.LeagueGameLog(
    season="2025-26",
    season_type_all_star="Regular Season",
    player_or_team_abbreviation="T"  # sorted by team
)

games_log = game_log.get_data_frames()[0]   # convert into dataframe

all_games = []

for game_id in games_log["GAME_ID"].unique():

    game = games_log[games_log["GAME_ID"] == game_id]

    home = game[game["MATCHUP"].str.contains("vs.", na=False)]
    away = game[game["MATCHUP"].str.contains("@", na=False)]

    # Normal game
    if len(home) == 1 and len(away) == 1:

        all_games.append({
            "game_id": game_id,
            "game_date": home.iloc[0]["GAME_DATE"],

            "home_team_id": home.iloc[0]["TEAM_ID"],
            "home_team": home.iloc[0]["TEAM_NAME"],
            "home_team_abbr": home.iloc[0]["TEAM_ABBREVIATION"],
            "home_score": home.iloc[0]["PTS"],

            "away_team_id": away.iloc[0]["TEAM_ID"],
            "away_team": away.iloc[0]["TEAM_NAME"],
            "away_team_abbr": away.iloc[0]["TEAM_ABBREVIATION"],
            "away_score": away.iloc[0]["PTS"],

            "neutral_site": False
        })

    # Neutral-site / unusual matchup
    else:
        team1 = game.iloc[0]
        team2 = game.iloc[1]

        all_games.append({
            "game_id": game_id,
            "game_date": team1["GAME_DATE"],

            "home_team_id": team1["TEAM_ID"],
            "home_team": team1["TEAM_NAME"],
            "home_team_abbr": team1["TEAM_ABBREVIATION"],
            "home_score": team1["PTS"],

            "away_team_id": team2["TEAM_ID"],
            "away_team": team2["TEAM_NAME"],
            "away_team_abbr": team2["TEAM_ABBREVIATION"],
            "away_score": team2["PTS"],

            "neutral_site": True
        })

games = pd.DataFrame(all_games)
games.to_csv("nba_2025_26_games.csv", index=False) # convert to csv