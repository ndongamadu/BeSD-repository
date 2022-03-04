from pandas.io import sql
import yaml
from sqlalchemy import create_engine


def getDBConf():
    host = "host"
    db = "db"
    user = "user"
    password = "passer"
    with open('config/dbConfig.yml') as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)
        host = conf["hostname"]
        db = conf["dbname"]
        user = conf["username"]
        password = conf["password"]
    return host, db, user, password
