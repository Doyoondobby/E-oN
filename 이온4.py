print("이온 4주차 과제 202112713 이도윤")

a=list(map(int,input("오름차순 정렬할 숫자를 입력하세요\n:").split(" ")))   #list와 map함수를 이용하여 정렬할 숫자들을 입력받음.

for i in range(len(a)-1):    #list a의 개수(길이)만큼 반복 비교함. index의 시작은 0부터 시작하므로 len(a)-1
    for j in range(len(a)-i-1): #마지막수는 비교대상(오른쪽 수)가 없어 -1을 함.
        if(a[j]>a[j+1]):    #list a의 j 번째 수가 j+1번째 수보다 클 경우 if문 실행함. 
            temp=a[j]   #j와 j+1을 바꾸기 위해 빈공간(temp)을 생성함.
            a[j]=a[j+1]
            a[j+1]=temp
        #print(a) 오름차순 되어가는 과정 확인
            
print(a)    #결과출력
