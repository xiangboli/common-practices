#include <iostream>
using namespace std;

void show1(string texts[], int n)
{
    for(int i=0; i<n; i++)
    {
        cout << texts[i] << endl;
    }
}

void show2(string *texts, int n)
{
    for(int i=0; i<n; i++, texts++)
    {
        cout << *texts << endl;
    }
}

int main()
{
    int value1 = 8;
    int &value2 = value1;
    value2 = 10;

    cout << value1 << endl;
    cout << value2 << endl;
    
    string texts[] = {"apple", "orange", "banna"};
    int size = sizeof(texts)/sizeof(string);
    //cout << size << endl;
    show2(texts, size);

    return 0;
}