import os
import sys


def print_list(*args):
    args = list(args)
    for i in range(len(args)):
        print(i+1, '.', args[i], '\n')


def ui_director(system):
    system = system
    os.system('clear')
    print_list('ManageChildren', 'Bus', 'ChatOnline',
               'Counselling', 'Survey', 'ManageKindergarten', 'Director')
    n = int(sys.stdin.readline())
    if n == 1:
        ui_ManageChildren(system)
    elif n == 2:
        ui_Bus(system)
    elif n == 3:
        ui_ChatOnline(system)
    elif n == 4:
        ui_Counselling(system)
    elif n == 5:
        ui_Survey(system)
    elif n == 6:
        ui_ManageKindergarten(system)
    else :
        ui_D(system)


def ui_ManageChildren(system):
    system = system
    os.system('clear')
    print_list('ManageAlbum', 'ManageHomework', 'ManageNotice',
               'ManageDevelopment', 'ManageAttendence', 'MonthlyReport', 'ManageHealth')
    n = int(sys.stdin.readline())
    if n == 1:
        system.manageChildren_staff.manageAlbum()
    elif n == 2:
        system.manageChildren_staff.manageHomework()
    elif n == 3:
        system.manageChildren_staff.manageNotice()
    elif n == 4:
        system.manageChildren_staff.manageDevelopment()
    elif n == 5:
        system.manageChildren_staff.manageAttendence()
    elif n == 6:
        system.manageChildren.monthlyReport()
    else:
        system.manageChildren_staff.manageHealth()


def ui_Bus(system):
    system = system
    os.system('clear')
    print_list('ManageBus')
    n = int(sys.stdin.readline())
    if n == 1:
        system.bus.manageBus()


def ui_ChatOnline(system):
    system = system
    os.system('clear')
    print_list('ChatOnline')
    n = int(sys.stdin.readline())
    if n == 1:
        system.chatOnline()


def ui_Counselling(system):
    system = system
    os.system('clear')
    print_list('Counselling')
    n = int(sys.stdin.readline())
    if n == 1:
        system.replyCounselling()


def ui_Survey(system):
    system = system
    os.system('clear')
    print_list('Survey')
    n = int(sys.stdin.readline())
    if n == 1:
        system.survey.create_survey()


def ui_ManageKindergarten(system):
    system = system
    os.system('clear')
    print_list('ManageSchedule', 'Children List', 'Invite Parents', 'Manage Class')
    n = int(sys.stdin.readline())
    if n == 1:
        system.manageKindergarten.schedule.manageSchedule()
    elif n == 2:
        system.manageKindergarten.childrenlist.manageList()
    elif n == 3:
        system.manageKindergarten.invite.inviteParents()
    elif n == 4:
        system.manageKindergarten.manageclass.manageClass()
    else:
        pass

def ui_D(system):
    system = system
    os.system('clear')
    print_list('Change Kindergarten Name', 'TeacherList', 'Manage Director')
    n = int(sys.stdin.readline())
    if n == 1:
        system.director.manageKindergartenName()
    elif n == 2:
        system.director.manageTeacherList()
    elif n == 3:
        system.director.manageDirector()
    else:
        pass
