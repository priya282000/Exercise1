""" MySQL Connection code """
import mysql.connector
#pylint: disable=no-self-use
#pylint: disable=too-few-public-methods


class Connection():
    """ Connection code """
    def connectdb(self):
        """ Connect method """
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", port="3306",
                                    password="Padma2000!", database="myproject")
            return mydb
        except ConnectionError:
            print("Not Connected")
