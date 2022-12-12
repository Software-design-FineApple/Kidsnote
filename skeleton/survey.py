import system
import sys


class Survey():
    def __init__(self, user):
        self.user = user
        pass

    def reply_survey(self):
        data = self.get_from_db('survey_history')
        self.give_data_to_sys('survey_history', data)
        self.show_from_sys('survey_history', data)
        data = self.get_from_db('survey_content')
        self.give_data_to_sys('survey_content', data)
        self.show_from_sys('survey_content', data)
        data = self.get_from_db('save_answer')
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('replySurvey : invoked by', self.user)
        pass

    def create_survey(self):
        data = self.get_from_db('survey_history')
        self.give_data_to_sys('survey_history', data)
        self.show_from_sys('survey_history', data)
        data = self.get_from_db('all_user_info')
        self.give_data_to_sys('all_user_info', data)
        self.show_from_sys('all_user_info', data)
        data = self.get_from_db('create_survey')
        print('User List : Minsu, Juhyeok, Mingyu, Jungjoong (this is example)\n')
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('createSurvey : invoked by', self.user)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass
