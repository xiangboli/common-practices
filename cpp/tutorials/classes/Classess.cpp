#include <iostream>
#include <sstream>
#include "Cat.h"

using namespace std;

int main(){
    string name = "Bob";
    int age =  32;

    stringstream ss;
    
    ss << "Name is: ";
    ss << name;
    ss <<  "Age is: ";
    ss << age;

    cout << ss.str() << endl;

    Cat cat;
    cat.jump();
    cat.speak();
    
    return 0;
}