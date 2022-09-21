#include <stdio.h>
int main(void)
{
	printf("202112713_이도윤_스마트시티공학부_과제2\n");

	double light_speed = 300000;
	double distance = 149600000;
	double time;

	time = distance / light_speed;
	time = time / 60.0;

	printf("빛의 속도는 5fkm/s\n", light_speed);
	printf("태양과 지구와의 거리 %fkm \n", distance);
	printf("도달시간은 %f초\n", time);

	int minute;
	int second;

	second = ("%f", time);
	minute = second / 60;
	second = second % 60;

	printf("도달시간은 %d분 %d초\n", minute, second);

	return 0;

}