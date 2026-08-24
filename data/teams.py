from nba_api.stats.static import teams
import pandas as pd

nba_teams = teams.get_teams()

# columns: id, full_name, abbreviation, nickname (mascot), city, state
teams_df = pd.DataFrame(nba_teams)

# add all the arenas
arenas = {
    "ATL": "State Farm Arena",
    "BOS": "TD Garden",
    "BKN": "Barclays Center",
    "CHA": "Spectrum Center",
    "CHI": "United Center",
    "CLE": "Rocket Arena",
    "DAL": "American Airlines Center",
    "DEN": "Ball Arena",
    "DET": "Little Caesars Arena",
    "GSW": "Chase Center",
    "HOU": "Toyota Center",
    "IND": "Gainbridge Fieldhouse",
    "LAC": "Intuit Dome",
    "LAL": "Crypto.com Arena",
    "MEM": "FedExForum",
    "MIA": "Kaseya Center",
    "MIL": "Fiserv Forum",
    "MIN": "Target Center",
    "NOP": "Smoothie King Center",
    "NYK": "Madison Square Garden",
    "OKC": "Paycom Center",
    "ORL": "Kia Center",
    "PHI": "Xfinity Mobile Arena",
    "PHX": "Mortgage Matchup Center",
    "POR": "Moda Center",
    "SAC": "Golden 1 Center",
    "SAS": "Frost Bank Center",
    "TOR": "Scotiabank Arena",
    "UTA": "Delta Center",
    "WAS": "Capital One Arena"
}
teams_df["arena"] = teams_df["abbreviation"].map(arenas)

teams_df.to_csv("nba_teams.csv", index=False)


