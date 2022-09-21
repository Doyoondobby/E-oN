#include <stdio.h>

int main(void)
{
    printf("스마트시티공학부 202112713 이도윤 과제4\n");

    int size;
    char ch;

    printf("컵의 크기와 색깔을 입력하시오(크기,색깔): ");
    scanf("%d , %c",&size, &ch);

    switch (ch)
    {
    case 'G':
        printf("이 컵은 Green 색상으로");
        break;
    case 'B':
        printf("이 컵은 Blue 색상으로");
        break;
    default:
        printf("생산되지 않는 컵 색상입니다.\n");
        break;
    }
    if (size > 0)
        if (100 < size)
            printf(" Large 사이즈입니다.\n");
   
        else
            printf(" Small 사이즈입니다.\n");

    else
        printf("존재하지 않는 컵 용량입니다.\n");

    return 0;
}



