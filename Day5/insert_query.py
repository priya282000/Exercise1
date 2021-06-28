""" Insert values into database """
import json
import logging
from mysql_connection import Connection


class InsertQuery():
    """ Insert query class """
    def insert_request(self, fname, mname, lname, dob, gender, nationality, city, state, pincode, qualification, salary, pan):
        """ Insert query """
        con = Connection().connectdb()
        my_cursor = con.cursor()
        query = "insert into request_info (firstname, middlename, lastname, dob, gender, nationality, " \
                "current_city, state, pincode, qualification," \
                "salary, pan_number) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vals = (fname, mname, lname, dob, gender, nationality, city, state, pincode, qualification, salary, pan)
        my_cursor.execute(query, vals)
        con.commit()

    def insert_response(self, response, reason, flag):
        """ Insert response table """
        con = Connection().connectdb()
        my_cursor = con.cursor()
        query1 = "select max(id) from request_info"
        my_cursor.execute(query1)
        max_id = my_cursor.fetchone()
        max_id = int(max_id[0])
        dictionary = {"cust_id": max_id, "response": response, "reason": reason}
        x = json.dumps(dictionary)
        y = json.loads(x)
        logging.info(x)
        res = y['response']
        rea = y['reason']
        if flag == 0:
            query = "insert into response_info(cust_id, response) values (%s,%s)"
            vals = (max_id, res)
            my_cursor.execute(query, vals)
        else:
            query = "insert into response_info(cust_id, response, reason) values (%s,%s,%s)"
            vals = (max_id, res, rea)
            my_cursor.execute(query, vals)
        con.commit()
