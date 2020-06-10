#include <iostream>
using namespace std;

struct DNode{
    int data;
    DNode *pre;
    DNode *next;
    DNode(int data): data(data), pre(nullptr), next(nullptr){};
};

class DoubleLinkedList {
private:
    DNode *head, *tail;
public:
    DoubleLinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    void insertNode(int value){
        DNode *node = new DNode(value);
        if (head == nullptr){
            
        }
    }

    void appendNode(int value){

    }
}