#include <stdio.h>

int main(void)
{
	printf("202112713 이도윤 스마트시티공학부 과제1\n");

	float w;
	float h;
	float area;
	float area2;

	printf("삼각형의 밑변 입력 : ");
	scanf("%f", &w);
	printf("삼각형의 높이 입력 : ");
	scanf("%f", &h);

	area = w * h / 2;
	area2 = (w * h / 2) * (w * h / 2);

	printf("삼각형의 면적: %f\n", area);
	printf("삼각형 면적의 제곱:%f\n", area2);
	return 0;
}