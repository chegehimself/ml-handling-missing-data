import psycopg2


class DBConnection(object):
    """ creates connection to the database """

    def __init__(self):
        self.db = psycopg2.connect(host='localhost', user='jameschege', dbname='worlddb', port=5432)

    def db_instance(self):
        return self.db
