import sqlite3
from sqlalchemy.orm import sessionmaker
from datetime import date, datetime
import pandas as pd
import sqlalchemy
import requests
import json

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "YOUR_USER_ID_GOES_HERE"
TOKEN = "YOUR_TOKEN_GOES_HERE"

# Transform stage
def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Verify is the dataframe isn't empty.
    if df.empty:
        print("No songs were downloaded.")
        return False
    
    # Setting a primary key.
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")
    
    # Check for any null values.
    if df.isnull().values.any():
        raise Exception("Null valued found.")

    # Check that all timestamps are from the last 24 hrs.
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df["timestamp"].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != yesterday:
            raise Exception("At least one of the returned songs does not have a yesterday's time stamp.")
    return True

if __name__ == "__main__":
    # Create headers for request 
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "aplication/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    # Download all song
    r = requests.get('https://api.spotify.com/v1/me/player/recently-played', headers=headers)

    # Getting the request data into a json format
    data = r.json()
    
    # Building data structures to hold the data
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant data from our json object
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    # Building a dict to pass to pandas dataframe
    song_dictionary = {
        "song_name":song_names,
        "artist_name":artist_names,
        "played_at":played_at_list,
        "timestamp":timestamps,
    }

    song_df = pd.DataFrame(song_dictionary, columns=("song_name", "artist_name", "played_at", "timestamp"))

    # Creating the framework for database
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor()

    # Builiding our table
    query = '''
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(60),
        artist_name VARCHAR(60),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    '''

    cursor.execute(query)
    print("Database went through.")

    try:
        song_df.to_sql("my_played_tracks", engine, index=False, if_exists="append")
    except:
        print("Data already in DB.")

    conn.close()
    print("Connection closed successfully.")

# Airflow Scheduling