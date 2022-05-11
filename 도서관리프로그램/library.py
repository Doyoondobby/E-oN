import os
import book_DB



class service:
    def __init__(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')#폴더 안에만 있으면 파일 이름으로 파일 실행 가능
        f = open(my_file,'r')
        book_List = f.readlines()
        self.book_List = []
        for i in range(0,len(book_List)):
            self.book_List.append(book_DB.DB(book_List[i].split()[0],
                                        book_List[i].split()[1],
                                        book_List[i].split()[2],
                                        book_List[i].split()[3],
                                        book_List[i].split()[4]))

    def show(self): #도서 목록 출력
        for book in self.book_List:#이터레이터(Iterator) for문으로 list에 있는거 하나씩 가져옴
            book.show_Book()

    def add(self): #도서 추가
        new_book = str(input("추가할 도서의 세부정보를 입력:")).split()
        self.book_List.append(book_DB.DB(new_book[0],
                                         new_book[1],
                                         new_book[2],
                                         new_book[3],
                                         new_book[4]))
                                         
    def delete_book(self): #도서 삭제
        self.show()
        delete_index = int(input("삭제할 도서를 선택하세요:"))
        self.book_List.pop(delete_index).show_Book() #pop :pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
        print("이 삭제되었습니다.")

    def modify_book(self):
        self.show()
        modify_index = int(input("수정할 도서를 선택하세요:"))
        modify_book = str(input("수정할 도서의 세부정보를 입력:")).split()
        self.book_List.pop(modify_index).show_Book()
        self.book_List.append(book_DB.DB(modify_book[0],
                                         modify_book[1],
                                         modify_book[2],
                                         modify_book[3],
                                         modify_book[4]))
        print("==================수정완료====================")

    def find(self):
        find_index = int(input("검색할 방법을 선택하세요:(1.도서명, 2.저자,3.출판연도,4.출판사, 5장르"))
        find_text=str(input("검색어를 입력하게요: "))
        for book in self.book_List:
            if find_index==1:
                if find_text in book.name:
                    book.show_Book()
            if find_index==2:
                if find_text in book.author:
                    book.show_Book()
            if find_index==3:
                if find_text in book.year:
                    book.show_Book()
            if find_index==4:
                if find_text in book.company:
                    book.show_Book()
            if find_index==5:
                if find_text in book.genre:
                    book.show_B1
                    book()


    def save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')#폴더 안에만 있으면 파일 이름으로 파일 실행 가능
        f = open(my_file,'w')
        for book in self.book_List:
            f.write(book.get_book())

        
