#include<iostream>
#include<cstdio>
#include<cstring>
#include<cctype>

//3.字母统计(Count)
using namespace std;
#define STR_LEN 4096

int main()
{
	char input[STR_LEN+1];
	cin.get(input, STR_LEN + 1);
	//cout << input << endl;
	//cout << char('A' + 1) << endl;

	int result[26];
	for (int i = 0; i < 26; i++)
	{
		result[i] = 0;
		//cout << result[i] << endl;
	}
	
	for (int i = 0; i < strlen(input); i++)
	{
		char c = input[i];
		if (isalpha(c))
		{
			//cout << toupper(c) - 'A' << endl;
			//cout << "before: " << result[toupper(c) - 'A'] << endl;
			result[toupper(c) - 'A']++;
			//cout << "after: " << result[toupper(c) - 'A'] << endl;
		}
	}


	for (int i = 0; i < 26; i++)
	{
		if (result[i] != 0)
		{
			cout << char('A' + i) << ": " << result[i] << endl;
		}
	}

	//system("pause");
	return 0;
}
