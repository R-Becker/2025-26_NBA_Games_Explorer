from flask import Flask, render_template
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/games")
def games():
    response = (
        supabase
        .table("games")
        .select("*")
        .limit(20)
        .execute()
    )

    print("RESPONSE:", response)
    print("DATA:", response.data)
    print("NUMBER OF ROWS:", len(response.data))

    game_list = response.data

    return render_template("games.html", games=game_list)



if __name__ == "__main__":
    app.run(debug=True)