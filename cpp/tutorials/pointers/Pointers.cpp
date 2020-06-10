#include <iostream>
using namespace std;

int main()
{
    int nVlaue = 8;
    int *p = &nVlaue;
    int **pp;
    pp = &p;
    cout << "nValue address: " << &nVlaue << endl;
    cout << "p address: " << p << endl;
    cout << "p value: " << *p << endl;
    cout << "pp address: " << pp << endl;
    cout << "pp value: " << *pp << endl;
    cout << "pp value's value: " << **pp << endl;

    string texts[] = {"one", "two", "three"};
    string *pText = texts;

    for (int i=0; i<sizeof(texts)/sizeof(string); i++, pText++)
    {
        cout << pText << ": " << *pText <<" " << flush;
    }

    cout << endl;

    string *pElement = texts;
    string *pEnd = &texts[2];

    while (true)
    {
        cout << *pElement << " " << flush;
        if(pElement == pEnd)
        {
            break;
        }
        pElement++;
    }

    cout << endl;

    char msg[] = "hello";
    char msg2[] = {'h', 'e', 'l', 'l', 'o'};

    for(int i=0; i<sizeof(msg2); i++)
    {
        cout << i << " : " << msg2[i] << endl;
    }

    char *msg3 = msg;
    while (*msg3)
    {
        cout << *msg3 << flush;
        msg3++;
    }

    

    return 0;
}