#include<stdio.h>
int main(void)

{
    int scores[6] = { 0 };
    int i;

    for (i = 1; i < 6; i++)
    {
        printf("[%d]�л��� ������ �Է��Ͻÿ�:\n", i, &scores[i]);
        scanf("%d", &scores[i]);
    }
    for (i = 1; i < 6; i++)
    {
        printf("scores[%d]=%d\n", i, scores[i]);
    }

    return 0;

}