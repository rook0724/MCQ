import random
from DataHandler.DataBaseUtil import DataBaseUtil
from DataHandler.QueryConstants import queries

class Test_Util:
    def __init__(self):
        self.db_util = DataBaseUtil()

    def insert_student_details(self, candidate):
        try:
            sql_query = queries.insert_into_student % ( candidate.stu__first_name,candidate.stu_surname,candidate.stu_date,candidate.stu_score,candidate.stu_status)
            self.db_util.execute_command(sql_query)
        except Exception as e:
            raise e

    def generate_questions(self):
        list=[]
        try:
            while(len(list)<3):
                r=random.randint(1,10)
                if r  not in list:list.append(r)
            return list
            print("List",list)
        except Exception as e:
            print(e)

    def get_questions(self,list):
        x = []
        try:

            for i in range(0, 3):
                sql_query = queries.get_questions % list[i]
                data = self.db_util.execute_command(sql_query)
                x.append(data)
                    # print(x[i][0][0])
            return x
        except Exception as e:
            print(e)

    def get_candidate_id(self):
        try:
            Id = 0
            sql_query = queries. get_last_candidate_id
            data = self.db_util.execute_command(sql_query)
            Id = data[0][0]
            return Id+1
        except Exception as e:
            print(e)


    def add_marks_to_db(self,score,candidate_id,status):
        try:

            sql_query = queries.update_score % (score,status,candidate_id)
            data = self.db_util.execute_command(sql_query)
        except Exception as e:
            print(e)
