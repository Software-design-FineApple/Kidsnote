import os
import sys


def print_list(*args):
    args = list(args)
    for i in range(len(args)):
        print(i+1, '.', args[i], '\n')


def ui_parent(system):
    system = system
    os.system('clear')
    print_list('ManageChildren', 'Bus', 'ChatOnline', 'Counselling', 'Survey')
    n = int(sys.stdin.readline())
    if n == 1:
        ui_ManageChildren(system)
    elif n == 2:
        ui_Bus(system)
    elif n == 3:
        ui_ChatOnline(system)
    elif n == 4:
        ui_Counselling(system)
    else:
        ui_Survey(system)


def ui_ManageChildren(system):
    system = system
    os.system('clear')
    print_list('ViewAlbum', 'ViewHomework', 'ViewNotice',
               'ViewDevelopment', 'ViewAttendence', 'MonthlyReport', 'ViewHealth')
    n = int(sys.stdin.readline())
    if n == 1:
        system.manageChildren.viewAlbum()
    elif n == 2:
        system.manageChildren.viewHomework()
    elif n == 3:
        system.manageChildren.viewNotice()
    elif n == 4:
        system.manageChildren.viewDevelopment()
    elif n == 5:
        system.manageChildren.viewAttendence()
    elif n == 6:
        system.manageChildren.monthlyReport()
    else:
        system.manageChildren.viewHealth()


def ui_Bus(system):
    system = system
    os.system('clear')
    print_list('TrackBus')
    n = int(sys.stdin.readline())
    if n == 1:
        system.bus.trackBus()


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
        system.reserveCounselling()


def ui_Survey(system):
    system = system
    os.system('clear')
    print_list('Survey')
    n = int(sys.stdin.readline())
    if n == 1:
        system.survey.reply_survey()
