#include <stdio.h>
int main(void)
{
	printf("����Ʈ��Ƽ���к� 202112713 �̵��� ����3\n");
	int c_temp;
	double f_temp;

	printf("�����µ��� �Է��Ͻÿ�:");
	scanf("%d", &c_temp);
	f_temp = (9.0 / 5.0 * c_temp + 32);
	printf("ȭ���µ��� %f�Դϴ�.\n", f_temp);

	return 0;

}