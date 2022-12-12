class Bus():
    def __init__(self, user):
        self.user = user
        pass

    def trackBus(self):
        data = self.get_bus_location()
        self.give_data_to_sys('trackBus', data)
        self.show_from_sys('trackBus', data)
        print('Bus list : Bus1, Bus2 (this is example)\n')
        print('trackBus : invoked by', self.user)
        pass

    def get_bus_location(self):
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass
