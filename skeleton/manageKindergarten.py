import sys


class ManageKindergarten():

    def __init__(self, user):

        self.user = user

        self.schedule = Schedule(self.user)

        self.childrenlist = ChildrenList(self.user)

        self.invite = Invite(self.user)

        self.manageclass = ManageClass(self.user)

        pass


class Schedule():

    def __init__(self, user):

        self.user = user

        pass

    def manageSchedule(self):

        data = self.get_from_db('check_schedule')

        self.give_data_to_sys('check_schedule', data)

        self.show_from_sys('check_schedule', data)

        data = self.get_from_db('change_schedule')

        self.give_data_to_sys('change_schedule', data)

        self.show_from_sys('change_schedule', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)

        print('manageSchedule : invoked by', self.user)

        pass

    def get_from_db(self, meaning):

        pass

    def show_from_sys(self, meaning, data):

        pass

    def give_data_to_sys(self, meaning, data):

        pass


class ChildrenList():

    def __init__(self, user):

        self.user = user

    def manageList(self):

        data = self.get_from_db('check_children_list')

        self.give_data_to_sys('check_children_list', data)

        self.show_from_sys('check_children_list', data)

        data = self.get_from_db('change_list')

        self.give_data_to_sys('change_list', data)

        self.show_from_sys('change_list', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)

        print('manageList : invoked by', self.user)

        pass

    def get_from_db(self, meaning):

        pass

    def show_from_sys(self, meaning, data):

        pass

    def give_data_to_sys(self, meaning, data):

        pass


class Invite():

    def __init__(self, user):

        self.user = user

    def inviteParents(self):

        data = self.send_message()

        self.get_from_db('store_message', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)

        print('inviteParents : invoked by', self.user)

        pass

    def get_from_db(self, meaning, data):

        pass

    def send_message(self):

        pass

    def give_data_to_sys(self, meaning, data):

        pass


class ManageClass():

    def __init__(self, user):

        self.user = user

    def manageClass(self):

        data = self.get_from_db('check_class')

        self.give_data_to_sys('check_class', data)

        self.show_from_sys('check_class', data)

        data = self.get_from_db('change_class')

        self.give_data_to_sys('change_class', data)

        self.show_from_sys('change_class', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('ManageClass : invoked by', self.user)

        pass

    def get_from_db(self, meaning):

        pass

    def show_from_sys(self, meaning, data):

        pass

    def give_data_to_sys(self, meaning, data):

        pass
