print("E-oN 3주차 과제 202112713 이도윤")
a = list( map( int, input("더할 숫자를 입력하세요.\n"). split(",")))
len(a)
b = 0
for i in range( len(a)):
    b=b+a[i]
print(b)
