#include<iostream>
using namespace std;

//1.简单表达式(Expr)
int main()
{
	long int a, b;
	char op;
	cin >> a >> op >> b;
	switch (op)
	{
	case'+':
		cout << a + b << endl;
		break;
	case'-':
		cout << a - b << endl;
		break;
	case'*':
		cout << a * b << endl;
		break;

	};
	return 0;
}

