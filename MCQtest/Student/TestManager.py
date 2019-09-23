from datetime import date

from Student.Candidate import Candidate
from Test.TestUtil import Test_Util


class TestManager:
    def __init__(self):
        self.test_util = Test_Util()

    def register_student(self):
        try:
            candidate = self.get_details_console()
            self.test_util.insert_student_details(candidate)
            print("Registered student "
              "successfully")
        except Exception as e:
            raise e

    def get_details_console(self):

        try:
            First_Name = input("Name: ")
            Suraname = (input("Surname: "))
            candidate = Candidate(First_Name,Suraname,date.today(), "0", "N")
            return candidate
        except Exception as e:
            print(e)

    def get_questions(self):
        data = self.test_util.generate_questions()
        ques_data=  self.test_util.get_questions(data)
        return ques_data

    def conduct_test(self,ques_data):
        answer_data = []
        for i in range(0, 3):
            print(i + 1, ".", ques_data[i][0][1], "\na.", ques_data[i][0][3], "\tb.", ques_data[i][0][4], "\tc.", ques_data[i][0][5], "\td.",
                  ques_data[i][0][6])
            answer = input()
            answer_data.append(answer)
        return answer_data

    def assesment(self,ques_data,answer_data):
        sum = 0
        for i in range(0, 3):
            if answer_data[i] == ques_data[i][0][2]:
                sum = sum + 10

            else:
                sum = 0
        return sum

    def display_result(self,score,last_candiadate_id):
        try:
            if score>20:
                status = "P"
                print("Congratualtions!")
            else:
                status = "F"
                print("Sorry, Better Luck Next time!")
            self.test_util.add_marks_to_db(score,last_candiadate_id,status)
        except Exception as e:
            raise e