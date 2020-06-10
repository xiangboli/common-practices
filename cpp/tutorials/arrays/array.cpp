#include <iostream>
using namespace std;

int main(){
    int values[] = {4, 2, 3, 1};

    for(int i=0; i<sizeof(values)/sizeof(int); i++){
        cout << values[i] << " " << flush;
    }

    cout << endl;

    string animals[][3] = {
        {"fox", "dog", "cat"},
        {"mouse", "squirrel", "parrot"}
    };

    for(int i=0; i<sizeof(animals)/sizeof(animals[0]); i++){
        for(int j=0; j<sizeof(animals[0])/sizeof(string); j++){
            cout << animals[i][j] << " " << flush;
        }
        cout << endl;
    }

    return 0;
}