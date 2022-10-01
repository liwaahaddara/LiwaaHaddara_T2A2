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

## **_AFL ERD Entity Relationships Explained_**

- **CLUBS:**

  - Each club is identified by its primary key (in this case, the _'club_id'_)

  - Each club has a **1-to-many relationship** with **_PLAYERS,_** **_COACHES_** & **_DOCTORS_** (each club can have one or more player/coach/doctor, but each player/coach/doctor belongs to only a single club). A connection is established by having the _club_id_ be used as a foreign key attribute for each **PLAYERS**, **COACHES** and **DOCTORS** entry.

- **COACHES:**

  - Each coach has the primary identifier _'coach_id'_

  - Each coach works for a single **CLUB** (uses the _'club_id'_ as a foreign key attribute to establish a connection)

- **DOCTORS:**

  - Each doctor has the primary identifier _'doctor_id'_

  - Each doctor works for a single **CLUB** (uses the _'club_id'_ as a foreign key attribute to establish a connection)

- **PLAYERS:**

  - Each player entry is identified by its primary key attribute (the _'player_id_)

  - Each player belongs to only one **CLUB** (connected through the foreign key attribute _'club_id'_)

  - Each player also has a connection to the **STATS** entity (in this case, a _one-to-one relationship_). The **STATS** primary identifier (the _'set_of_stats_id'_ attribute) is used as a foreign key attribute in each **PLAYERS** entry (since each AFL player needs to have their own statistical data available for viewing)

## **_Mangament of the API Webserver Project_**

- Using Trello cards to track the creation of the API (through planning, designing and code implementation documentation)

- Task Allocation/Tracking Location:
  [Trello Link](https://trello.com/invite/b/ayqBiMcF/902b058cdd87a611e0b692466e0d934b/t2a2-webserver-api-project)
