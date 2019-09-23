import pymysql;
from DataHandler.QueryConstants import queries


class DataBaseUtil:
    def __init__(self):
        pass

    def get_data_base_connection(self):
        try:
            db_connection = pymysql.connect(
                "localhost","root", "Sai@123","MCQ")
            return db_connection
        except Exception as e:
            raise e
    def close_data_base_connection(self, db_connection):
        try:
            db_connection.close()
        except Exception as e:
            raise e

    def execute_command(self,sql_query):
        db_connection = self.get_data_base_connection()
        try:
            cursor = db_connection.cursor()
            cursor.execute(sql_query)
            row = cursor.fetchall()
            db_connection.commit()
        except Exception as e:
            raise e
        finally:
            self.close_data_base_connection(db_connection)
        return row