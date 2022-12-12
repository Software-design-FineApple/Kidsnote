import sys


class Director():

    def __init__(self, user):

        self.user = user

        pass

    def manageKindergartenName(self):

        data = self.get_from_db('check_name')

        self.give_data_to_sys('check_name', data)

        self.show_from_sys('check_name', data)

        data = self.get_from_db('change_name')

        self.give_data_to_sys('change_name', data)

        self.show_from_sys('change_name', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)

        print('manageKindergartenName : invoked by', self.user)

        pass

    def manageTeacherList(self):

        data = self.get_from_db('check_teacher_list')

        self.give_data_to_sys('check_teacher_list', data)

        self.show_from_sys('check_teacher_list', data)

        data = self.get_from_db('change_teacher_list')

        self.give_data_to_sys('change_teacher_list', data)

        self.show_from_sys('change_teacher_list', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)

        print('manageTeacherList : invoked by', self.user)

        pass

    def manageDirector(self):

        data = self.get_from_db('check_director')

        self.give_data_to_sys('check_director', data)

        self.show_from_sys('check_director', data)

        data = self.get_from_db('change_director')

        self.give_data_to_sys('change_director', data)

        self.show_from_sys('change_director', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)

        print('manageDirector : invoked by', self.user)

        pass

    def get_from_db(self, meaning):

        pass

    def show_from_sys(self, meaning, data):

        pass

    def give_data_to_sys(self, meaning, data):

        pass
