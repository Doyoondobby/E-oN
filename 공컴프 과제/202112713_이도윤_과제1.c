#include <stdio.h>

int main(void)
{
	printf("202112713 �̵��� ����Ʈ��Ƽ���к� ����1\n");

	float w;
	float h;
	float area;
	float area2;

	printf("�ﰢ���� �غ� �Է� : ");
	scanf("%f", &w);
	printf("�ﰢ���� ���� �Է� : ");
	scanf("%f", &h);

	area = w * h / 2;
	area2 = (w * h / 2) * (w * h / 2);

	printf("�ﰢ���� ����: %f\n", area);
	printf("�ﰢ�� ������ ����:%f\n", area2);
	return 0;
}