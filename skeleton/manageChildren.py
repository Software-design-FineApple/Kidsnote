class ManageChildren():
    def __init__(self, user):
        self.user = user
        pass

    def viewattendance(self):
        data = self.get_from_db('attendance')
        self.give_data_to_sys('attendance', data)
        self.show_from_sys('attendance', data)
        print('viewAttendence : invoked by', self.user)
        pass

    def monthlyReport(self):
        data = self.get_from_db('monthlyReport')
        self.give_data_to_sys('monthlyReport', data)
        self.show_from_sys('monthlyReport', data)
        print('monthlyReport : invoked by', self.user)
        pass

    def viewHealth(self):
        data = self.get_from_db('viewTemperature')
        self.give_data_to_sys('viewTemperature', data)
        self.show_from_sys('viewTemperature', data)
        data = self.get_from_db('viewDiet')
        self.give_data_to_sys('viewDiet', data)
        self.show_from_sys('viewDiet', data)
        data = self.get_from_db('viewDosing')
        self.give_data_to_sys('viewDosing', data)
        self.show_from_sys('viewDosing', data)
        print('viewHealth : invoked by', self.user)
        pass

    def viewAlbum(self):
        data = self.get_from_db('album_data')
        self.give_data_to_sys('album_data', data)
        self.show_from_sys('album_data', data)
        print('viewAlbum : invoked by', self.user)
        pass

    '''def shareAlbum(self):
        result = self.upload_sns(data)
        self.give_data_to_sys('sharing_completed', data)
        self.show_from_sys('sharing_completed', data)
        pass'''

    def viewHomework(self):
        data = self.get_from_db('homework_data')
        self.give_data_to_sys('homework_data', data)
        self.show_from_sys('homework_data', data)
        print('viewHomework : invoked by', self.user)
        pass

    def viewNotice(self):
        data = self.get_from_db('notice_data')
        self.give_data_to_sys('notice_data', data)
        self.show_from_sys('notice_data', data)
        print('viewNotice : invoked by', self.user)
        pass

    def viewDevelopment(self):
        data = self.get_from_db('development_data')
        self.give_data_to_sys('development_data', data)
        self.show_from_sys('development_data', data)
        print('viewDevelopment : invoked by', self.user)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def upload_sns(self, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass
