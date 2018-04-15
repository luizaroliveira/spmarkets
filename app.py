from flask import Flask, request
import logging
from flask_restless import APIManager
from models import db, Feira

# Setting up the app, using configurations from the specified python file.
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Creating and adding log handler for the app. Won't log to file if debug mode is activated.
if not app.debug:
    logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')


# handler to log info after every request
@app.after_request
def log_request_info(response):
    data = [
        request.method,
        request.base_url,
        request.query_string.decode(),
        str(response.status_code)
    ]

    logging.info(' | '.join(data))
    return response


# Initializing the database ORM
db.init_app(app)


# Initializing REST manager
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Feira, results_per_page=1000, methods=['GET', 'POST', 'DELETE', 'PATCH'])

if __name__ == '__main__':
    app.run()
