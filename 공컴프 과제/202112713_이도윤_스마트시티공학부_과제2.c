#include <stdio.h>
int main(void)
{
	printf("202112713_�̵���_����Ʈ��Ƽ���к�_����2\n");

	double light_speed = 300000;
	double distance = 149600000;
	double time;

	time = distance / light_speed;
	time = time / 60.0;

	printf("���� �ӵ��� 5fkm/s\n", light_speed);
	printf("�¾�� �������� �Ÿ� %fkm \n", distance);
	printf("���޽ð��� %f��\n", time);

	int minute;
	int second;

	second = ("%f", time);
	minute = second / 60;
	second = second % 60;

	printf("���޽ð��� %d�� %d��\n", minute, second);

	return 0;

}