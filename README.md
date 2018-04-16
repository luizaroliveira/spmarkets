# SP Markets

SP Markets is a python restful API made to get, post, update and search São Paulo open markets in an SQL database and can serve as barebone structure base to any restful API alike.

The project run un a virtual envorinment and has a setup script to install its necessary packages.
The API documentation, thechnologies used and setup instrucions are listed below.

#### Documentation
For documentation, open the ***docs*** directory, located right at the root of the repository.

#### Frameworks, libs and database used

   * [Flask] - A lightweight barebones framework for building python APIs.
  Chosen for being fast and using only the resources needed by the API.
  *Besides the SQLite, all other components used for this project are small addons to this framework, wicht is very extensible*.

  * [SQLite] - Embeded lightweight SQL database.
  Chosen for its ease of use and portability for this project. It is based on a single file, natively compatible with all versions of python and the database can be posted on the project repository and be ready for testing. Also, the DB engine can be easily changed in a single line of configuration, without having to change any code, thanks to the ORM engine used.

  * [Flask-SQLAlchemy] - SQL Object-Relational Mapping framework.
  Makes ORM simple and manageable, while it can also manage all the work if we need to change the database used, by just having to change a connection string. It's stable, powerful and compatible with SQLite, Postgresql, MySQL, Oracle, MS-SQL, Firebird, Sybase and others.

  * [Flask-Restless] - Python framework for creating simple restful APIs.
  Chosen for being just enough to build the requested API in a reliable and simple way, while even providing additional functionality, like pagination and a more advanced search mechanism.

#### Testing
For this API, there are 9 unit tests to show how to handle testing within the API structure.

To Run the tests, install the envoronment (explained below) activate the envoronment and run tests.py
```sh
$ source venv/bin/activate
$ python tests.py
```

Some tests may be meant to err and will generate error messages. Its ok, as long as the assert methods get the desired values and don't fail.
##### Desired result
----------------------------------------------------------------------
Ran 9 tests in #.#s

OK

##### Test cases
  1. **test_0_get**: Get request at /api/feiras.
  Must return status 200 - Ok.
  2. **test_1_post_new_market**: Post a new market, using id -9999.
  Must return status 201 - Created.
  3. **test_2_get_by_id**: Get request for id -9999.
  Request response data must not be empty.
  4. **test_3_post_new_market_bad_request**: Bad Post for a new market, using id -9998.
  Must return status 400 - Bad Request.
  5. **test_4_search_by_name_equals**: Search markets for with name "VILA MEDEIROS".
  There must be at least one result and its *nome_feira* must be == "VILA MEDEIROS"
  6. **test_5_search_by_district_like**: Search markets by district, looking for matches *like* "%MADALENA%"
  There must be at least one result and its *district* must have "MADALENA" somewhere in the text.
  7. **test_6_update**: Update market "*bairro*" field.
  Must return status 200 - Ok.
  8. **test_7_bad_update**: Tries to update market id and fails.
  Must return status 400 - Bad Request.
  9. **test_8_delete_by_id**: Delete market with id -9999.
  Must return status 204 - No Content.

# Setup
To run the project it's necessary to run the setup.sh script at least once, it will create the environment and install the necessary packages, given the pre-requisites below are met.

> The environment setup script is meant to run on a linux system. For windows users, a python2.7 or any python3.x virtual environment must be created first, activated and then the packages can be installed through pip using the requirements.txt file.

#### Pre-requisites
For the setup script and API to run, the following software must be present.
  - **Python2.7** (originally built to run on python3, but totally compatible with 2.7. So, let's stick with 2.7 for better compatibility with most systems.)
  - **pip**
  - **virtualenv**

#### Setup and how to run
  - Run setup.sh: installs the environment.
  - Run app.sh: Activates the environment and run the app.py.
That's it! The API will be running on the port 5000 of the localhost. ex.: localhost:5000/api/feira

#### Database Import
The database was imported using *importer.py*.
The CSV file containing the data is inside the data folder.

To reimport the data:
```sh
$ rm feiras.db
$ source venv/bin/activate
$ python importer.py
$ deactivate
```

#### Logging
Logs will be generated in a DSV format, saved in the file log.txt, delimited by "|" (pipe)

Log fields:
  * time
  * level
  * method
  * URI
  * query
  * return status

Log line example:
* 2018-04-12 16:14:16,506 | INFO | GET | http://localhost:5000/api/feira | q={%22filters%22:[{%22name%22:%22distrito%22,%20%22op%22:%20%22like%22,%20%22val%22:%20%22VILA%%22}]} | 200


   [Flask]: <http://flask.pocoo.org/>
   [SQLite]: <https://www.sqlite.org/index.html>
   [Flask-SQLAlchemy]: <http://flask-sqlalchemy.pocoo.org/2.3/>
   [Flask-Restless]: <https://flask-restless.readthedocs.io/en/stable/>

