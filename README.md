# **API Webserver Project (T2-A2) - Liwaa Haddara**

(Created in September, 2022)

## **_API Chosen (Problem Identification and Why)_**

- I've chosen to create an AFL (the Australian Football League) API that acts as a tool for retrieving important AFL-related statistics

- Being the major professional sporting league of Australia, the AFL receives a lot of data input to officially document any changes in the league (such as player additions and delistings, club changes, staff changes, etc)

- Having a massive fanbase (comprised of MILLIONS across the country) creates a massive demand to want to know all the latest official information surrounding a certain AFL club

- Creating this API provides (the fans, coteries, staff members, and more) an easily accessible way to retrieve any of this information at the touch of a button!

## **_Database Chosen (PostgreSQL) and Why_**

- I've chosen to use **_PostgreSQL_** as a Database Managment System (DBMS), mainly due to the following:

1. **Data Integrity:** It provides our data integrity through key constraints and regulation of added data, so we can forget about invalid records!

2. **Disaster Recovery & Reliability:** Includes sophisticated replication options to keep our data safe.

3. **Data Types:** Has support for all mainstream/needed data types, including _documents, geometry, primitives, structures, etc_

4. **Performance:** Contains multiple features (such as powerful indexing methods, parallelisation of read queries, multiversion concurrency control, and many more) that boost and optimise the performance of a DBMS.

5. **Text Search & Internalisation:** Supports international character sets, and so enables full-text search, thereby speeding up a finding process (since it also integrates case-sensitive and accent-insensitive collations)

## **_Key Functionalities and Benefits when using an ORM_**

- There are many popular ORM's (**Object Relational Mappers**) available for use when using a DBMS such as PostgreSQL in Python, including _Django, Storm, **SQLAlchemy** (the ORM I will be using for this project), and many more_

- Plenty of benefits arrive at a programmer's fingertips with the use of an ORM (such as SQLAlchemy), since it practically hides away all the boilet plate tasks that come when creating a functional API, and that includes:

  1. Connecting to a Database Server

  2. Sanitising any potential parameters

  3. Generating the required queries

  4. Fetching data and (if necessary) serialising it

  5. Localisation

- As you can see, ORM's eliminate A LOT of potential hassles for us and have us focus primarily on creating a functioning database that works as intended

## **_ERD (& ERD Modelling of the AFL API)_**

![Image of the AFL API ERD](./docs/AFL%20API%20ERD.jpg)
![Image of the modelling of the AFL API ERD](./docs/AFL%20API%20ERD%20Modelling.jpg)

## **_AFL ERD Entity Relationships & Database Implementations Explained_**

- **CLUBS:**

  - Each club is identified by its primary key (in this case, the _'club_id'_)

  - Each club has a **1-to-many relationship** with **_PLAYERS,_** **_COACHES_** & **_DOCTORS_** (each club can have one or more player/coach/doctor, but each player/coach/doctor belongs to only a single club). A connection is established by having the _club_id_ be used as a foreign key attribute for each **PLAYERS**, **COACHES** and **DOCTORS** entry.

  - When a club is removed from the database, its **PLAYERS (and subsequently STATS), COACHES & DOCTORS** entries are automatically removed from the database (due to the _cascading delete_ option being enabled in each of these relationships) to ensure all present information inside the database is sanitised

- **COACHES:**

  - Each coach has the primary identifier _'coach_id'_

  - Each coach works for a single **CLUB** (uses the _'club_id'_ as a foreign key attribute to establish a connection)

- **DOCTORS:**

  - Each doctor has the primary identifier _'doctor_id'_

  - Each doctor works for a single **CLUB** (uses the _'club_id'_ as a foreign key attribute to establish a connection)

- **PLAYERS:**

  - Each player entry is identified by its primary key attribute (the _'player_id_)

  - Each player belongs to only one **CLUB** (connected through the foreign key attribute _'club_id'_)

  - Each player also has a connection to the **STATS** entity (in this case, a _one-to-one relationship_). The **PLAYERS** primary identifier (the _'player_id'_ attribute) is used as a foreign key attribute in each **STATS** entry (since each AFL player needs to have their own statistical data available for viewing)

- **STATS:**

  - Each stats entry belongs to a single **PLAYER** entry. This is implemented by using the **PLAYER** model primary*key (\_player_id*) as a foreign key attribute for the **STATS** model

  - A stats entry is automatically removed when its respective player entry is deleted from the database (the _cascading delete_ option is enabled in the player-stats relationship to ensure any irrelevant data is removed to keep the database sanitised)

## **AFL API Endpoints Documentation:**

### All methods present in the API are implemented strictly using HTTP methods (that result in the **C.R.U.D, or Create, Read, Update, & Delete** operations), and each operation is further explained below.

(**NOTE:** every Model's Endpoints are located in their respective 'Controller' files)

#### The **'GET' HTTP method (used to _READ/RETRIEVE_ entries)**

1. _@clubs.route("/clubs", methods=["GET"])\_

- Executes the 'get_clubs()' function, which retrieves all the football Club entries that are currently present in the database

2. _@clubs.route("/clubs/<int:id>", methods=["GET"])\_

- Executes the 'get_club(id)' function, which retrieves the football Club entry connected to the provided 'id' if it's present in the database.
- Otherwise it returns an error message saying that the requested club entry doesn't exist

3. _@coaches.route("/coaches", methods=["GET"])\_

- Executes the 'get_coaches()' function, which retrieves all the Coach entries that are currently present in the database

4. _@coaches.route("/coaches/<int:id>", methods=["GET"])\_

- Executes the 'get_coach(id)' function, which retrieves the Coach entry connected to the provided 'id' if it's present in the database.
- Otherwise it returns an error message saying that the requested Coach entry doesn't exist

5. _@doctors.route("/doctors", methods=["GET"])\_

- Executes the 'get_doctors()' function, which retrieves all the Doctor entries that are currently present in the database

6. _@doctors.route("/doctors/<int:id>", methods=["GET"])\_

- Executes the 'get_doctor(id)' function, which retrieves the Doctor entry connected to the provided 'id' if it's present in the database.
- Otherwise it returns an error message saying that the requested Doctor entry doesn't exist

7. _@players.route("/players", methods=["GET"])\_

- Executes the 'get_players()' function, which retrieves all the Player entries that are currently present in the database

8. _@players.route("/players/<int:id>", methods=["GET"])\_

- Executes the 'get_player(id)' function, which retrieves the Player entry connected to the provided 'id' if it's present in the database.
- Otherwise it returns an error message saying that the requested Player entry doesn't exist

9. _@stats.route("/stats", methods=["GET"])\_

- Executes the 'get_stats()' function, which retrieves all the Stat entries that are currently present in the database

10. _@stats.route("/stats/<int:id>", methods=["GET"])\_

- Executes the 'get_stat(id)' function, which retrieves the Player entry connected to the provided 'id' if it's present in the database.
- Otherwise it returns an error message saying that the requested Player entry doesn't exist

#### The **'POST' HTTP method (used to _CREATE_ entries)**

1. _@clubs.route("/clubs", methods=["POST"])\_

- Executes the 'new_club()' function, which uses the provided football Club data to create a new Club entry in the database

2. _@coaches.route("/coaches", methods=["POST"])\_

- Executes the 'new_coach()' function, which uses the provided Coach data to create a new Coach entry in the database

3. _@doctors.route("/doctors", methods=["POST"])\_

- Executes the 'new_doctor()' function, which uses the provided Doctor data to create a new Doctor entry in the database

4. _@players.route("/players", methods=["POST"])\_

- Executes the 'new_player()' function, which uses the provided Player data to create a new Player entry in the database

5. _@stats.route("/stats", methods=["POST"])\_

- Executes the 'new_stat()' function, which uses the provided Stat data to create a new Stat entry in the database

#### The **'PUT' HTTP method (used to _UPDATE_ entries)**

1. _@clubs.route("/clubs/<int:id>", methods=["PUT"])\_

- Executes the 'update_club(id)' function, which uses the provided football Club data to update an existing Club entry in the database.

- Otherwise it returns an error message saying that the provided 'club_id' parameter doesn't match any existing entries

2. _@coaches.route("/coaches/<int:id>", methods=["PUT"])\_

- Executes the 'update_coach(id)' function, which uses the provided football Coach data to update an existing Coach entry in the database.

- Otherwise it returns an error message saying that the provided 'coach_id' parameter doesn't match any existing entries

3. _@doctors.route("/doctors/<int:id>", methods=["PUT"])\_

- Executes the 'update_doctor(id)' function, which uses the provided football Doctor data to update an existing Doctor entry in the database.

- Otherwise it returns an error message saying that the provided 'doctor_id' parameter doesn't match any existing entries

4. _@players.route("/players/<int:id>", methods=["PUT"])\_

- Executes the 'update_player(id)' function, which uses the provided football Player data to update an existing Player entry in the database.

- Otherwise it returns an error message saying that the provided 'player_id' parameter doesn't match any existing entries

5. _@stats.route("/stats/<int:id>", methods=["PUT"])\_

- Executes the 'update_stat(id)' function, which uses the provided football Stat data to update an existing Stat entry in the database.

- Otherwise it returns an error message saying that the provided 'stat_id' parameter doesn't match any existing entries

#### The **'DELETE' HTTP method (used to _DELETE_ entries)**

1. _@clubs.route("/clubs/<int:id>", methods=["DELETE"])\_

- Executes the 'delete_club(id)' function, which uses the provided 'id' parameter data to delete an existing Club entry in the database.

- Otherwise it returns an error message saying that the provided 'id' parameter doesn't match any existing entries

2. _@coaches.route("/coaches/<int:id>", methods=["DELETE"])\_

- Executes the 'delete_coach(id)' function, which uses the provided 'id' parameter data to delete an existing Coach entry in the database.

- Otherwise it returns an error message saying that the provided 'id' parameter doesn't match any existing entries

3. _@doctors.route("/doctors/<int:id>", methods=["DELETE"])\_

- Executes the 'delete_doctor(id)' function, which uses the provided 'id' parameter data to delete an existing Doctor entry in the database.

- Otherwise it returns an error message saying that the provided 'id' parameter doesn't match any existing entries

4. _@players.route("/players/<int:id>", methods=["DELETE"])\_

- Executes the 'delete_player(id)' function, which uses the provided 'id' parameter data to delete an existing Player entry in the database.

- Otherwise it returns an error message saying that the provided 'id' parameter doesn't match any existing entries

5. _@stats.route("/stats/<int:id>", methods=["DELETE"])\_

- Executes the 'delete_stat(id)' function, which uses the provided 'id' parameter data to delete an existing Stat entry in the database.

- Otherwise it returns an error message saying that the provided 'id' parameter doesn't match any existing entries

## **Third-party Services Used in the Webserver API**

(NOTE: referring to the specific pip packages installed here and their purpose)

### **_flask_**

- Used the 'flask' module to install the following packages:
  - Flask (used a microweb framework to create our App to run our dynamic routes, commands, etc)
  - Blueprint
  - request (used to load any provided user data in order to manipulate said data to our liking)
  - jsonify (used to convert given user data into a JSON object so it can be formatted correctly for viewing, as JSON is an industry standard)

### **_flask_sqlalchemy_**

- Used to install the following packages:
  - SQLALchemy (used as an ORM to connect us to our PostgreSQL database, complete the 'boiler-plate' tasks for us in the background)

### **_flask_marshmallow_**

- Used to install the following packages:
  - Marshmallow (used to serialise our data, automatically create our primary_keys, and to design our schemas to be able to choose what we would like to display to the user)

## **_Management of the API Webserver Project_**

- Using Trello cards to track the creation of the API (through planning, designing and code implementation documentation)

- Task Allocation/Tracking Location:
  [Trello Link](https://trello.com/invite/b/ayqBiMcF/902b058cdd87a611e0b692466e0d934b/t2a2-webserver-api-project)
