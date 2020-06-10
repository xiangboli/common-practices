#include <iostream>
using namespace std;

struct Node{
    int data;
    Node* next;
    Node(int data): data(data), next(nullptr){}
};

class LinkedList{
private:
    Node *head;
public:
    LinkedList(){head = nullptr;}

    void insertNode(int value){
        Node *tmp = new Node(value);
        if (head == nullptr){
            head = tmp;
        } else {
            tmp->next = head;
            head = tmp;
        }
    }
    void deleteNode(int value){
        if (head->data == value){
            head = head->next;
            delete 
        }

        Node *node = head;
        while (node->next != nullptr){
            if (node->next->data == value){
                next_node = node->next;
                node->next = node->next->next;
                delete 
                break;
            }
            node = node->next;
        }
    }
    void display(){
        Node *node = head;
        while (node != nullptr){
            cout << node->data << endl;
            node = node->next;
        }
    }
};

int main(){
    LinkedList ll;
    ll.insertNode(1);
    ll.insertNode(3);
    ll.insertNode(2);
    ll.display();
    ll.deleteNode(3);
    ll.display();

    return 0;
}


