class DB:
    def __init__(self, name, year, company, genre, author): #클래스의 내부 변수에 값 할당 객체에 셀프(자기자신)의
        self.name = name #이름은 이름이다.(이런식으로 책 한권한권 지정)
        self.year = year
        self.company = company
        self.genre = genre
        self.author = author # 여기까지 cpp의 생성자 느낌 

    def show_Book(self):
        print(self.name)
        print(self. author)
        print(self.year)
        print(self.company)
        print(self.genre)

    def get_book(self):
        return self.name+ " " + self.author+ " " + self.year+ " " + self.company+ " " + self.genre + "\n"


       