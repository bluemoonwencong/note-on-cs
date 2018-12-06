#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
/*
	char input1[8];
	char input2[8];
	cin >> input1;
	cin >> input2;
	cout << "1:" << input1 << " 2:" << input2 << endl;
	
	//cout << time2num(input2) - time2num(input1) << endl;

*/
	int h1, m1, s1, h2, m2, s2, result;
	scanf_s("%d:%d:%d %d:%d:%d", &h1, &m1, &s1, &h2, &m2, &s2);
	//cout << h1 << m1 << s1 << h2 << m2 << s2 << endl;
	//cout << h2 * 3600 + m2 * 60 + s2 << endl;
	//cout << h1 * 3600 + m1 * 60 + s1 << endl;
	result = h2 * 3600 + m2 * 60 + s2 - h1 * 3600 - m1 * 60 - s1;
	if (result < 0)
	{
		result += 24 * 3600;
	}
	printf_s("%d\n", result);
	
	//system("pause");
	return 0;
}


