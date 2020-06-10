#include <iostream>
#include "Cat.h"

using namespace std;

Cat::Cat()
{
    cout << "Cat is created..." << endl;
    happy = true;
}

Cat::~Cat()
{
    cout << "Cat is destroyed..." << endl;
}

void Cat::speak()
{
    if (happy)
    {
        cout << "Meowww!!" << endl;
    }
    else
    {
        cout << "Ssss!!" << endl;
    }
}

void Cat::jump()
{
    cout << "jump!!" << endl;
}