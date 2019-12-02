import psycopg2


class DBConnection(object):
    """ creates connection to the database """

    def __init__(self):
        """
        host:- db host
        user:- your postgres user/ default user. Use "postgres" if your default user is postgres
        dbname:- name of the db where you imported world database
        port:- the database port. For psycopg2 the default port is 5432
        """
        self.db = psycopg2.connect(host='localhost', user='postgres', dbname='worlddb', port=5432)

    def db_instance(self):
        """
        :return: database instance
        """
        return self.db
