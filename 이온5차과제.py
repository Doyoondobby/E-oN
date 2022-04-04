def solution(arr1,arr2):
    
    # arr1은 slicing-sort-select 할 배열, arr2는 arr1을 조작할 변수(i, j, k)가 담긴 배열
    
    i=arr2[0]   # arr2 배열의 첫번째 요소를 변수 i에 담음 (i: 슬라이싱을 시작할 변수)
    j=arr2[1]   # arr2 배열의 두번째 요소를 변수 i에 담음 (j: 슬라이싱을 끝마칠 변수)
    k=arr2[2]   # arr2 배열의 세번째 요소를 변수 k에 담음
                # (k: 슬라이싱이 끝난 배열에서 원하는 값을 선택하기 위한 변수)
    if i>j: # 슬라이싱을 시작할 값은 슬라이싱을 끝마칠 값보다 클 수 없음(ex. 5번째부터 2번째까지는 불가능)
        print("범위 지정이 잘못되었습니다: i>j")    #error1
    else : # len(array)>k>=0
        if k<0: # 음수 번째는 존재할 수 없음
            print("추출값은 음수가 될 수 없습니다.") #error2
        elif k>(j-i+1) or k<0:   # 슬라이싱을 통해 만들어진 배열의 길이(요소의 총 갯수)내에서 선택해야 함
            print("추출값이 범위를 벗어났습니다.")   #error3
        else :    
            array=arr1[i-1:j] # arr1을 i부터 j까지 슬라이싱 한 배열을 변수 array에 담음
            #array=sorted(arr1[i-1:j])    #오름차순으로 정렬(방법 1)
                                            
            for i in range(len(array)-1):    #오름차순으로 정렬(방법 2)
                for j in range(len(array)-i-1): 
                    if(array[j]>array[j+1]):    
                        temp=array[j]  
                        array[j]=array[j+1]
                        array[j+1]=temp
                
            k=array[k-1]    # 배열의 인덱스는 0부터 시작하므로 k-1번째가 원하는 값이 됨
            print("[",k,"]")    # 출력 형태 조작

solution([1,5,2,6,3,7,4], [1, 4, 3])
solution([1,5,2,6,3,7,4], [4, 4, -1]) #error2
solution([1,5,2,6,3,7,4], [1, 7, 3])
solution([1,5,2,6,3,7,4], [1, 5, 7]) #error3
