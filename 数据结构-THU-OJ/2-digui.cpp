#include<iostream>
using namespace std;

//2.最大公约数(Divisor)
int want(int i, int j);
int main()
{
	long int a, b;
	long int r=1;
	cin >> a >> b;

	cout << want(a, b) << endl;
	
	return 0;
}

int want(int i, int j)
{
	if (i == j)
	{
		return i;
	}
	else if (i < j)
	{
		j = j - i;
	}
	else
	{
		i = i - j;
	}
	want(i, j);
}


