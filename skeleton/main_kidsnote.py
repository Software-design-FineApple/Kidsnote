import sys
import os
import ui_parent
import ui_teacher
import ui_director
from system import System


def main():
    print('로그인 화면입니다. 약식으로 진행\n1 . 학부모\n2 . 교직원\n3 . 원장\n')
    n = int(sys.stdin.readline())
    system = System(n)
    if n == 1:
        ui_parent.ui_parent(system)
    elif n == 2:
        ui_teacher.ui_teacher(system)
    else:
        ui_director.ui_director(system)


main()
