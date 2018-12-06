#include<iostream>
using namespace std;

int main()
{
	long int a, b;
	long int r=1;
	cin >> a >> b;

	while (r)
	{
		r = a % b;
		a = b;
		b = r;
	}

	cout << a << endl;
	
	return 0;
}

