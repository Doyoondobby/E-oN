#include <stdio.h>
int main(void)
{
	printf("202112713_����Ʈ��Ƽ���к�_�̵���_9������\n");
	int i = 3000;
	int* p = NULL;
	int t = 10;
	int *pi = &i;

	p = &i;
	printf("i = %d\n", i); 
	printf("&i = %u\n\n", &i); 
	printf("p = %u\n", p); 
	printf("*p = %d\n", *p); 

	printf("t = %d, pi = %p\n", i, pi);
	(*pi)++;
	printf("t = %d, pi = %p\n", i, pi);
	printf("t = %d, pi = %p\n", i, pi);
	*pi++;
	printf("t = %d, pi = %p\n", i, pi);

	return 0;
}