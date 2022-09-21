#include<stdio.h>
int main(void)

{
    int scores[6] = { 0 };
    int i;

    for (i = 1; i < 6; i++)
    {
        printf("[%d]학생의 성적을 입력하시오:\n", i, &scores[i]);
        scanf("%d", &scores[i]);
    }
    for (i = 1; i < 6; i++)
    {
        printf("scores[%d]=%d\n", i, scores[i]);
    }

    return 0;

}