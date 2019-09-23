class queries:
    show_all_questions = "select * from questionnaire"
    get_questions = "select * from questionnaire where q_id ='%s'"
    insert_into_student = "insert into candidates (First_name, Surname,Exam_date,Score,Status) values('%s','%s','%s','%s','%s')"
    update_score ="update candidates set score = '%s', status = '%s' where Candidate_ID = '%s'"
    get_last_candidate_id = "select candidate_id from candidates order by candidate_id desc limit 1"

