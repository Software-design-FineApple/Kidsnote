from manageChildren import ManageChildren
import sys


class ManageChildren_staff(ManageChildren):
    def __init__(self, user):
        self.user = user
        pass

    def manageAlbum(self):
        data = self.get_from_db('album_data')
        self.give_data_to_sys('album_data', data)
        self.show_from_sys('album_data', data)
        data = self.get_from_db('user_data')
        self.give_data_to_sys('user_data', data)
        self.show_from_sys('user_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageAlbum : invoked by', self.user)
        pass

    def manageHomework(self):
        data = self.get_from_db('homework_data')
        self.give_data_to_sys('homework_data', data)
        self.show_from_sys('homework_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageHomework : invoked by', self.user)
        pass

    def manageNotice(self):
        data = self.get_from_db('notice_data')
        self.give_data_to_sys('notice_data', data)
        self.show_from_sys('notice_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageNotice : invoked by', self.user)
        pass

    def manageDevelopment(self):
        data = self.get_from_db('development_data')
        self.give_data_to_sys('development_data', data)
        self.show_from_sys('development_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageDevelopment : invoked by', self.user)
        pass

    def manageAttendance(self):
        data = self.get_from_db('child_data')
        self.give_data_to_sys('child_data', data)
        self.show_from_sys('child_data', data)
        data = self.get_from_db('attendance_data')
        self.give_data_to_sys('attendance_data', data)
        self.show_from_sys('attendance_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageAttendence : invoked by', self.user)
        pass

    def manageHealth(self):
        data = self.get_from_db('child_data')
        self.give_data_to_sys('child_data', data)
        self.show_from_sys('child_data', data)
        data = self.get_from_db('temperature_data')
        self.give_data_to_sys('temperature_data', data)
        self.show_from_sys('temperature_data', data)
        data = self.get_from_db('diet_data')
        self.give_data_to_sys('diet_data', data)
        self.show_from_sys('diet_data', data)
        data = self.get_from_db('dosing_data')
        self.give_data_to_sys('dosing_data', data)
        self.show_from_sys('dosing_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageHealth : invoked by', self.user)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass
