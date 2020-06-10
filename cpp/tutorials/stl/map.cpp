#include <iostream>
#include <map>
using namespace std;

void multiMap(){
    typedef multimap<string, int> MapType;
    MapType myMap;

    // insertion
    myMap.insert(pair<string, int>("test", 43));
    myMap.insert(pair<string, int>("test", 45));
    myMap.insert(pair<string, int>("other-test", 0));

    auto it = myMap.find("test");
    if (it != myMap.end())
        cout << "value for " << it->first << " is " << it->second << endl;
    else
        cout << "value not found" << endl;
}

void signleMap(){
    typedef map<string, int> MapType;
    MapType myMap;

    // insertion
    myMap.insert(pair<string, int>("test", 42));
    myMap.insert(pair<string, int>("other-test", 0));

    // search
    auto it = myMap.find("test");
    if (it != myMap.end())
        cout << "value for " << it->first << " is " << it->second << endl;
    else
        cout << "value not found" << endl;
}

int main()
{
    cout << "Single Map:" << endl;
    signleMap();
    cout << "Multi Map:" << endl;
    multiMap();
}