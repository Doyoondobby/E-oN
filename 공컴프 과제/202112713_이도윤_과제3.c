#include <stdio.h>
int main(void)
{
	printf("스마트시티공학부 202112713 이도윤 과제3\n");
	int c_temp;
	double f_temp;

	printf("섭씨온도를 입력하시오:");
	scanf("%d", &c_temp);
	f_temp = (9.0 / 5.0 * c_temp + 32);
	printf("화씨온도는 %f입니다.\n", f_temp);

	return 0;

}