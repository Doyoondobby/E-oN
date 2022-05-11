import sys
from library import service

def fun1():
    print('1. 도서 추가하기 \n')
    
def fun2():
    print('2. 도서 검색하기 \n')

def fun3():
    print('3. 도서 정보 수정하기 \n')

def fun4():
    print('4. 도서 삭제하기 \n')

def fun5():
    print('5. 현재 도서 목록 출력 \n')

def fun6():
    print('6. 프로그램 나가기 \n')





while True:
    a= service()
    print(' 1. 도서 추가하기 ')
    print(' 2. 도서 검색하기 ')
    print(' 3. 도서 정보 수정하기 ')
    print(' 4. 현재 도서 목록 출력 ')
    print(' 5. 저장하기 ')
    print(' 6. 나가기')

    num = int(input('선택 : '))

    if num == 0:
        print(' 프로그램 종료 ')
        sys.exit()
    elif num == 1:
        a.add()
    elif num == 2:
        a.find()
    elif num == 3:
        a.modify()
    elif num == 4:
        a.show()
    elif num == 5:
        a.save()
    elif num == 6:
        fun6()
    else:
        print('{}는 없는 번호'.format(num))
