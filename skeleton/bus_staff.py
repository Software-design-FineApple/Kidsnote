from bus import Bus
import sys


class Bus_staff(Bus):
    def __init__(self, user):
        self.user = user
        pass

    def manageBus(self):
        data = self.get_from_db('upload_bus_data')
        self.give_data_to_sys('upload_bus_data', data)
        self.show_from_sys('upload_bus_data', data)
        print('입력하세요 : ')
        n = (sys.stdin.readline())
        print(n)
        print('manageBus : invoked by', self.user)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass
