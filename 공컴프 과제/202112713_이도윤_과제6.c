#include <windows.h>
#include <stdio.h>
#include <math.h>
#define PI 3.141592
double rad(double degree)
{
    return PI * degree / 180.0;
}
int main(void)
{
    printf("202112713_이도윤_스마트시티공학부_과제6\n");
    printf("sin함수는 빨간색, cos함수는 파란색으로 출력했습니다.");

    int degree, x, y;
    double radian, result;
    HWND hwnd = GetForegroundWindow();
    HDC hdc = GetWindowDC(hwnd);
    for (degree = 0; degree <= 720; degree++)
    {
        result = sin(rad((double)degree));
        x = degree + 30;
        y = 200 - (int)(100.0 * result);
        SetPixel(hdc, x, y, RGB(255, 0, 0));
    }
    for (degree = 0; degree <= 720; degree++)
    {
        result = cos(rad((double)degree));
        x = degree + 30;
        y = 200 - (int)(100.0 * result);
        SetPixel(hdc, x, y, RGB(0, 0, 255));
    }
    return 0;
}