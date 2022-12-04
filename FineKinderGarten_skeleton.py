class System():
    def __init__(self):
        self.user = self.check_user()
        self.survey = Survey(self.user)
        if self.user == 'Teacher':
            self.managekindergarten = ManageKindergarten()
            self.managechildren = ManageChildren_staff()
            self.bus = Bus_staff()
        elif self.user == 'Director':
            self.managekindergarten = ManageKindergarten()
            self.director = Director()
            self.managechildren = ManageChildren_staff()
            self.bus = Bus_staff()
        else:
            self.managechildren = ManageChildren()
            self.bus = Bus()
            pass

    def check_user():
        pass

    def chatOnline(self):
        data = self.get_from_db('request_all_user_list')
        self.show_from_sys('request_all_user_list', data)
        data = self.get_from_db('request_chat_history')
        self.show_from_sys('request_chat_history', data)
        data = self.get_from_db('save_message')
        self.show_from_sys('save_message', data)
        pass

    def replyCounselling(self):
        data = self.get_from_db('request_history')
        self.show_from_sys('request_history', data)
        self.send_reply()
        data = self.get_from_db('save_reply')
        self.show_from_sys('save_reply', data)

    def reserveCounselling(self):
        data = self.get_from_db('request_teacher_list')
        self.show_from_sys('request_teacher_list', data)
        self.send_counseling_reserve()
        data = self.get_from_db('save_counselling_reserve')
        self.show_from_sys('save_counselling_reserve', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def send_reply(self):
        pass
    
    def send_counseling_reserve(self):
        pass

class Bus():
    def __init__(self):
        pass

    def trackBus(self):
        data = self.get_bus_location()
        self.give_data_to_sys('trackBus', data)
        self.show_from_sys('trackBus', data)
        pass

    def get_bus_location():
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class Bus_staff(Bus):
    def __init__(self):
        super.__init__()
        pass

    def manageBus(self):
        data = self.get_from_db('upload_bus_data')
        self.give_data_to_sys('upload_bus_data', data)
        self.show_from_sys('upload_bus_data', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass


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
            pass

        def create_survey(self):
            data = self.get_from_db('survey_history')
            self.give_data_to_sys('survey_history', data)
            self.show_from_sys('survey_history', data)
            data = self.get_from_db('all_user_info')
            self.give_data_to_sys('all_user_info', data)
            self.show_from_sys('all_user_info', data)
            data = self.get_from_db('create_survey')
            pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class Director():
    def __init__(self):
        pass

    def manageKindergartenName(self):
        data = self.get_from_db('check_name')
        self.give_data_to_sys('check_name', data)
        self.show_from_sys('check_name', data)
        data = self.get_from_db('change_name')
        self.give_data_to_sys('change_name', data)
        self.show_from_sys('change_name', data)
        pass

    def manageTeacherList(self):
        data = self.get_from_db('check_teacher_list')
        self.give_data_to_sys('check_teacher_list', data)
        self.show_from_sys('check_teacher_list', data)
        data = self.get_from_db('change_teacher_list')
        self.give_data_to_sys('change_teacher_list', data)
        self.show_from_sys('change_teacher_list', data)
        pass

    def manageDirector(self):
        data = self.get_from_db('check_director')
        self.give_data_to_sys('check_director', data)
        self.show_from_sys('check_director', data)
        data = self.get_from_db('change_director')
        self.give_data_to_sys('change_director', data)
        self.show_from_sys('change_director', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class ManageChildren():
    def __init__(self):
        pass

    def viewattendance(self):
        data = self.get_from_db('attendance')
        self.give_data_to_sys('attendance', data)
        self.show_from_sys('attendance', data)
        pass

    def monthlyReport(self):
        data = self.get_from_db('monthlyReport')
        self.give_data_to_sys('monthlyReport', data)
        self.show_from_sys('monthlyReport', data)
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
        pass

    def viewAlbum(self):
        data = self.get_from_db('album_data')
        self.give_data_to_sys('album_data', data)
        self.show_from_sys('album_data', data)
        pass

    def shareAlbum(self):
        result = self.upload_sns(data)
        self.give_data_to_sys('sharing_completed', data)
        self.show_from_sys('sharing_completed', data)
        pass

    def viewHomework(self):
        data = self.get_from_db('homework_data')
        self.give_data_to_sys('homework_data', data)
        self.show_from_sys('homework_data', data)
        pass

    def viewNotice(self):
        data = self.get_from_db('notice_data')
        self.give_data_to_sys('notice_data', data)
        self.show_from_sys('notice_data', data)
        pass

    def viewDevelopment(self):
        data = self.get_from_db('development_data')
        self.give_data_to_sys('development_data', data)
        self.show_from_sys('development_data', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def upload_sns(self, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class ManageChildren_staff(ManageChildren):
    def __init__(self):
        super.__init__()
        pass

    def manageAlbum(self):
        data = self.get_from_db('album_data')
        self.give_data_to_sys('album_data', data)
        self.show_from_sys('album_data', data)
        data = self.get_from_db('user_data')
        self.give_data_to_sys('user_data', data)
        self.show_from_sys('user_data', data)
        pass

    def manageHomework(self):
        data = self.get_from_db('homework_data')
        self.give_data_to_sys('homework_data', data)
        self.show_from_sys('homework_data', data)
        pass

    def manageNotice(self):
        data = self.get_from_db('notice_data')
        self.give_data_to_sys('notice_data', data)
        self.show_from_sys('notice_data', data)
        pass

    def manageDevelopment(self):
        data = self.get_from_db('development_data')
        self.give_data_to_sys('development_data', data)
        self.show_from_sys('development_data', data)
        pass

    def manageattendance(self):
        data = self.get_from_db('child_data')
        self.give_data_to_sys('child_data', data)
        self.show_from_sys('child_data', data)
        data = self.get_from_db('attendance_data')
        self.give_data_to_sys('attendance_data', data)
        self.show_from_sys('attendance_data', data)
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
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class ManageKindergarten():
    def __init__(self):
        self.schedule = Schedule()
        self.childrenlist = ChildrenList()
        self.invite = Invite()
        self.manageclass = ManageClass()
        pass


class Schedule():
    def __init__(self):
        pass

    def manageSchedule(self):
        data = self.get_from_db('check_schedule')
        self.give_data_to_sys('check_schedule', data)
        self.show_from_sys('check_schedule', data)
        data = self.get_from_db('change_schedule')
        self.give_data_to_sys('change_schedule', data)
        self.show_from_sys('change_schedule', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class ChildrenList():
    def __init__(self):
        pass

    def manageList(self):
        data = self.get_from_db('check_children_list')
        self.give_data_to_sys('check_children_list', data)
        self.show_from_sys('check_children_list', data)
        data = self.get_from_db('change_list')
        self.give_data_to_sys('change_list', data)
        self.show_from_sys('change_list', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class Invite():
    def __init__(self):
        pass

    def inviteParents(self):
        data = self.send_message()
        self.get_from_db('store_message', data)
        pass

    def get_from_db(self, meaning, data):
        pass

    def send_message(self):
        pass

    def give_data_to_sys(self, meaning, data):
        pass

class ManageClass():
    def __init__(self):
        pass

    def manageClass(self):
        data = self.get_from_db('check_class')
        self.give_data_to_sys('check_class', data)
        self.show_from_sys('check_class', data)
        data = self.get_from_db('change_class')
        self.give_data_to_sys('change_class', data)
        self.show_from_sys('change_class', data)
        pass

    def get_from_db(self, meaning):
        pass

    def show_from_sys(self, meaning, data):
        pass

    def give_data_to_sys(self, meaning, data):
        pass