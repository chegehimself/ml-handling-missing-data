# Machine Learning

## Handling Missing Data with Python

### setup
- #### Make sure you have [postgresql](https://www.postgresql.org/download/) installed
- #### First, log into the default Postgres user with the following command:
    `sudo su - [user - your postgres user]`
- #### Download world database file
  ```
  wget http://pgfoundry.org/frs/download.php/527/world-1.0.tar.gz
  
  ```
 - #### Extract the gzipped archive and change the content directory
      ```
      tar xzvf world-1.0.tar.gz
      cd dbsamples-0.1/world
      ```
- #### Create a database to import the file structure into:
  ```
    createdb -T template0 worlddb
  ```
  
- #### Finally, we will use the .sql file as input into the newly created database:
    ```
    psql worlddb < world.sql
    ```
 ## Running the code
 Make sure to use python3 while running the code
 
 - install the dependencies in requirements in `requirements.txt`
 
    ```pip3 install -r requirements.txt``` - python3
 - To plot the graphs run the following command
    ```
    python3 run.py
    ```
 - Done!🥰