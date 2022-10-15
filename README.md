# Spotify ETL project

In this project we create a quick ETL process using an API to pull data from a server to create an appealing database that can be used for analytical purposes. 

With this project you will see some interesting aspects of what a data engineering project looks like. Not only will we create a ETL process but also schedule a DAG process with Apache airflow, which will keep running your code to pull data for your database.

We're using the Python programming language for the bulk of this project along with many libraries such as:
`SQLITE3`,
`PANDAS`,
`AIRFLOW`.

I have decided to highlight those three specifically because they are our bread and butter for this project. Without these our project would be a lot tricker to program, but not to worry, all of these  tools are free for anyone to start using them at any time.

The ideia behind the project is to pull data from a website (EXTRACT), once it's been pulled said data will be transformed (TRANSFORM), meaning that we will only get the parts we want from the data dump our server provides (for this project we will use spotify's API), after the data has been pulled and treated we will load (LOAD) it into our database. After creating this algorithm, we will schedule a job for it on Apache airflow which will allow us to pull data daily from the source.

This project requires you to use this API (RECENTLY_PLAYED_TRACKS):
`https://api.spotify.com/v1/me/player/recently-played`

Now along with the source code within this repo you should be able to create your ETL, have fun!
