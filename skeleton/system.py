from survey import Survey
from manageKindergarten import ManageKindergarten
from manageChildren_staff import ManageChildren_staff
from bus_staff import Bus_staff
from director import Director
from manageChildren_staff import ManageChildren_staff
from bus_staff import Bus_staff
from manageChildren import ManageChildren
from bus import Bus
import sys
import os


class System():
    def __init__(self, n):
        self.user = self.check_user(n)
        self.survey = Survey(self.user)
        if self.user == 'Teacher':
            self.manageKindergarten = ManageKindergarten(self.user)
            self.manageChildren_staff = ManageChildren_staff(self.user)
            self.bus = Bus_staff(self.user)
        elif self.user == 'Director':
            self.manageKindergarten = ManageKindergarten(self.user)
            self.director = Director(self.user)
            self.manageChildren_staff = ManageChildren_staff(self.user)
            self.bus = Bus_staff(self.user)
        else:
            self.manageChildren = ManageChildren(self.user)
            self.bus = Bus(self.user)
            pass

    def check_user(self, n):
        if n == 1:
            return 'Parent'
        elif n == 2:
            return 'Teacher'
        else:
            return 'Director'

    def chatOnline(self):
        data = self.get_from_db('request_all_user_list')
        self.show_from_sys('request_all_user_list', data)
        data = self.get_from_db('request_chat_history')
        self.show_from_sys('request_chat_history', data)
        data = self.get_from_db('save_message')
        self.show_from_sys('save_message', data)
        print('User List : Minsu, Juhyeok, Mingyu, Jungjoong (this is example)\n')
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('chatOnline : invoked by', self.user)
        pass

    def replyCounselling(self):
        data = self.get_from_db('request_history')
        self.show_from_sys('request_history', data)
        self.send_reply()
        data = self.get_from_db('save_reply')
        self.show_from_sys('save_reply', data)
        print('Survey List : Survey1, Survey2 (this is example) \n')
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('replyCounselling : invoked by', self.user)
        pass

    def reserveCounselling(self):
        data = self.get_from_db('request_teacher_list')
        self.show_from_sys('request_teacher_list', data)
        self.send_counseling_reserve()
        data = self.get_from_db('save_counselling_reserve')
        self.show_from_sys('save_counselling_reserve', data)
        print('User List : Minsu, Juhyeok, Mingyu, Jungjoong (this is example)\n')
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('reserveCounselling : invoked by', self.user)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def send_reply(self):
        pass

    def send_counseling_reserve(self):
        pass
