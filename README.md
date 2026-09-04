# NBA Schedule Web Application

> **Project Status: Work in Progress**

This project is currently under active development.

The goal of this project is to build a full-stack web application that allows users to browse and filter NBA games from the **2025–26 NBA season**.

I started this project as a way to apply and expand my experience with Python, SQL, databases, APIs, data processing, and web development by building a complete application around real NBA data.

---

## Project Overview

The NBA Schedule Web Application allows users to view games from the 2025–26 NBA season and search the schedule using filters.

Current filters include:

- NBA team
- Start date
- End date

Rather than simply displaying a static CSV file, the project follows a complete data pipeline. NBA data is collected and processed with Python, stored in a PostgreSQL database using Supabase, queried through a Flask backend, and displayed through a web interface.

### Current Technology Stack

- **Python** — data collection, processing, and backend development
- **nba_api** — NBA game and team data
- **Pandas** — data transformation and CSV creation
- **Supabase / PostgreSQL** — database storage and querying
- **Flask** — backend web framework
- **HTML** — webpage structure
- **CSS** — webpage styling
- **Jinja** — dynamically rendering database results in HTML

---

## How the Project Works

The project can be summarized as the following pipeline:

**NBA Data → Python → Pandas → CSV → Supabase/PostgreSQL → Flask → Web Interface**

### 1. Collecting NBA Game Data

The first step was obtaining a complete dataset for the 2025–26 NBA regular season.

Using the nba_api Python package, I retrieved the league game log for the season.

The API returns game information from each team's perspective. This means that the original data contains multiple records associated with the same NBA game.

To create a dataset that would work better for the application, I transformed the API response so that **each row represents one game**.

For each unique game ID, the program:

1. Finds the two teams associated with the game.
2. Determines the home and away teams using the matchup information.
3. Extracts the team IDs, names, abbreviations, scores, and game date.
4. Combines the information into a single game record.

The resulting dataset contains **1,230 regular-season games**.

---

### 2. Handling Neutral-Site Games

While processing the game data, I discovered that not every game followed the standard home/away format used by the API.

For most games:

- vs. identifies the home team.
- @ identifies the away team.

A small number of games did not follow this structure.

Instead of removing these games from the dataset, I added a neutral_site field.

Standard games are marked:

False

while games that do not follow the normal home/away structure are marked:

True

This allowed me to preserve the complete schedule while still identifying games that require different handling.

---

### 3. Creating Team Data

I created a second data-processing script for NBA team information.

Using nba_api, I collected information including:

- Team ID
- Full team name
- Abbreviation
- Nickname
- City
- State

I also added each team's home arena to the dataset.

This creates a separate source of team information that can be incorporated into additional features as the application develops.

---

### 4. Creating the Datasets

After processing the API responses with Pandas, the data scripts export the results into two CSV files:

- nba_2025_26_games.csv
- nba_teams.csv

The CSV files provide a processed version of the raw API data and also make it easier to inspect and verify the data before using it in the application.

The data collection scripts and generated datasets are stored separately from the web application in the "data/" directory.

---

### 5. Database Storage

After processing the NBA game data, I imported it into **Supabase**, which provides a PostgreSQL database for the application.

Instead of having Flask read directly from the CSV every time the website loads, game information is retrieved from the database.

This allows the application to perform database queries based on the filters selected by the user.

Supabase credentials are stored using environment variables rather than being included directly in the source code.

---

### 6. Flask Backend

The web application is built using Flask.

The Flask application currently contains routes for:

- "/" — application home page
- "/games" — schedule and filtering page

When a user submits filters on the games page, Flask reads the selections from the URL query parameters.

The backend then builds a Supabase query based on the selected filters.

For example, if a team is selected, the query searches for games where that team appears as either the home or away team.

Date selections can also be used to limit results to games within a particular range.

The matching records are returned from Supabase and passed from Flask to the HTML template.

---

### 7. Web Interface

The frontend currently uses HTML, CSS, and Jinja templates.

The schedule page displays each game's:

- Date
- Away team
- Score
- Home team

The page also provides controls for filtering the schedule by team and date range.

The current frontend is functional but is still in an early stage of development. Improving the design and overall user experience is one of the next major areas of the project.

---

## Project Structure

```text
nba-schedule/
│
├── data/
│   ├── games.py
│   ├── teams.py
│   ├── nba_2025_26_games.csv
│   └── nba_teams.csv
│
├── flask/
│   ├── app.py
│   │
│   ├── static/
│   │   └── style.css
│   │
│   └── templates/
│       ├── index.html
│       └── games.html
│
├── .gitignore
├── requirements.txt
└── README.md
```

### `data/`

Contains the data collection and processing portion of the project.

**`games.py`**  
Retrieves 2025–26 NBA regular-season game data using `nba_api`, transforms the API response into one record per game, identifies unusual or neutral-site games, and exports the processed dataset.

**`teams.py`**  
Retrieves NBA team information using `nba_api`, adds arena information, and creates the team dataset.

**`nba_2025_26_games.csv`**  
Processed game dataset generated by `games.py`.

**`nba_teams.csv`**  
Processed team dataset generated by `teams.py`.

### `flask/`

Contains the web application.

**`app.py`**  
Runs the Flask application, connects to Supabase, processes schedule filters, queries the database, and passes game data to the HTML templates.

**`templates/`**  
Contains the Jinja/HTML templates used to build the application's webpages.

**`static/`**  
Contains the CSS used to style the application.

### Other Files

**`requirements.txt`**  
Lists the Python packages and versions required to run the project.

**`.gitignore`**  
Prevents environment files, virtual environments, and other files that should not be committed from being included in the repository.

---

## Installation

To install the Python dependencies used by the project, run:

```bash
pip install -r requirements.txt
```

The current dependencies are:

```text
Flask==3.1.3
nba_api==1.11.4
pandas==3.0.5
python-dotenv==1.2.3
supabase==2.31.0
```

The Flask application also requires Supabase environment variables.

These credentials are intentionally **not included in this repository**.

---

## Current Features

- Complete 2025–26 NBA regular-season game dataset
- 1,230 games stored as individual game records
- NBA team metadata
- NBA arena information
- Neutral-site game identification
- Pandas data-processing pipeline
- Supabase/PostgreSQL database integration
- Flask backend
- Dynamic schedule rendering
- Team filtering
- Start-date filtering
- End-date filtering
- Basic web interface
- Environment-variable configuration for database credentials

---

## Planned Features

This project is still under development.

Some of the features and improvements I plan to work on include:

- Improve the overall UI and styling
- Improve the schedule layout
- Add additional game filters
- Improve handling and display of neutral-site games
- Incorporate additional team and arena information
- Improve navigation between pages
- Add pagination or another method for efficiently browsing the complete schedule
- Improve error handling
- Make the website responsive for different screen sizes
- Deploy the application so it can be accessed online

Additional features may be added as the project develops.

---

## What I Have Learned

One of my main goals with this project was to move beyond working with Python, SQL, and web development as separate concepts and better understand how they can work together in a complete application.

Through this project, I have gained experience with:

- Retrieving real-world data from an API
- Exploring and understanding unfamiliar API responses
- Cleaning and transforming data with Pandas
- Converting team-level records into game-level records
- Identifying and handling edge cases in real-world data
- Organizing data around the needs of an application
- Working with PostgreSQL through Supabase
- Querying a database from Python
- Protecting credentials using environment variables
- Building routes with Flask
- Using URL query parameters for filtering
- Passing backend data into Jinja templates
- Dynamically displaying database results in HTML
- Organizing a project into separate data-processing and web-application components

The hardest part throughout this project has been learning the frontend aspect of creating a web application. 

With more learning and practice, I plan to have a much better understanding of html and flask.

Most importantly, the project has helped me better understand the full path that data takes through an application:

**collection → processing → storage → querying → presentation**

---

## Project Status

**Currently in Development**

This repository represents the current state of the project and it will continue to change as I add new features, and improve the user interface.

The current version demonstrates the project's core pipeline:

**Collect NBA data → Transform the data → Store it in PostgreSQL → Query it with Flask → Display it to the user**

My next major focus is improving the frontend and expanding the schedule-browsing and filtering functionality.
