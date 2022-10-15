# spotifyETLproject

In this project we create a quick ETL process using an API to pull data from a server to create an appealing database that can be used for analytical purposes. 

With this project you will see some interesting aspects of what a data engineering project looks like. Not only will we create a ETL process but also schedule a DAG process with Apache airflow, which will keep running your code to pull data for your database.

We're using the Python programming language for the bulk of this project along with many libraries such as:
`SQLITE3`,
`PANDAS`,
`AIRFLOW`.

I have decided to highlight those three specifically because they are the our bread and butter for this project. Without these our project would be a lot tricker to program, but not to worry, all of these  tools are free for anyone to start using them at any time.

The ideia behind the project is to pull data from a website (EXTRACT), once it's been pulled said data will be transformed, meaning that we will only get the parts we want from the data dump our server provides (for this project we will use spotify's API), after the data has been pulled and treated we will load it into our database. After creating this algorithm, we will schedule a job for it on Apache airflow which will allow us to pull data daily from the source.
