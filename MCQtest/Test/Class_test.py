from Student.TestManager import TestManager
from Test.TestUtil import Test_Util


class Class_test:
    def __init__(self):
        self.test_manager = TestManager()
        self.test_util = Test_Util()


    def Candiate_area(self):
        try:
            score=0
            candidate_Id = self.test_util.get_candidate_id()

            self.test_manager.register_student()
            ques_data = self.test_manager.get_questions()
            answer_data = self.test_manager.conduct_test(ques_data)
            score = self.test_manager.assesment(ques_data,answer_data)
            self.test_manager.display_result(score,candidate_Id)
        except Exception as e:
            raise e

if __name__ == "__main__":
    test_class = Class_test()
    option = input("Please select your choice : \n1.Candidate Area \n2.Exit\n")
    print(option)
    if option == "1":
        try:
            test_class.Candiate_area()
        except Exception as e:
            raise e
    elif option == "2":
        exit()





