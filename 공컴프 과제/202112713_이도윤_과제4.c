#include <stdio.h>

int main(void)
{
    printf("����Ʈ��Ƽ���к� 202112713 �̵��� ����4\n");

    int size;
    char ch;

    printf("���� ũ��� ������ �Է��Ͻÿ�(ũ��,����): ");
    scanf("%d , %c",&size, &ch);

    switch (ch)
    {
    case 'G':
        printf("�� ���� Green ��������");
        break;
    case 'B':
        printf("�� ���� Blue ��������");
        break;
    default:
        printf("������� �ʴ� �� �����Դϴ�.\n");
        break;
    }
    if (size > 0)
        if (100 < size)
            printf(" Large �������Դϴ�.\n");
   
        else
            printf(" Small �������Դϴ�.\n");

    else
        printf("�������� �ʴ� �� �뷮�Դϴ�.\n");

    return 0;
}



