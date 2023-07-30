Node* merge(Node* l1,Node*l2)
{
if(l1==NULL)return l2;
if(l2==NULL)return l1;
Node* res=l1;
if(l1->data>l2->data)swap(l1,l2);
while(l1!=NULL && l2!=NULL)
{
    Node* temp=NULL;
    while(l1!=NULL && l1->data<=l2->data)
    {
        temp=l1;
        l1=l1->bottom;
    }
    temp->bottom=l2;
    swap(l1,l2);
}
return res;
}

Node* merge(Node* a, Node* b) {
    
    Node *temp = new Node(0);
    Node *res = temp; 
    while(a != NULL && b != NULL) {
        if(a->data < b->data) {
            temp->child = a; 
            temp = temp->child; 
            a = a->child; 
        }
        else {
            temp->child = b;
            temp = temp->child; 
            b = b->child; 
        }
    }
    
    if(a) temp->child = a; 
    else temp->child = b; 
    
    return res -> child; 
}

Node* flattenLinkedList(Node* head) 
{
	if(head == NULL || head->next == NULL){
		return head;
	}
	Node* left = head;
	Node* sorted = flattenLinkedList(head -> next);
	left->next = NULL;
	Node* ans = merge(left, sorted);
	return ans;
}

#include <queue>
struct mycomp {
    bool operator()(Node* a, Node* b)
    {
        return a->data > b->data;
    }
};
Node *flattenLinkedList(Node *head) {
    Node *pointer = head;
    Node *result = NULL;
    // Heap to store all the node value pair.
    priority_queue<Node*, vector<Node*>, mycomp> pq;
    // Push the head nodes.
    while (pointer) {
        pq.push(pointer);
        pointer = pointer->next;
    }
    // Add child nodes while popping out the minimum.
    while (!pq.empty()) {
        Node *temp = pq.top();
        pq.pop();
        // If the child of temp is not null add it to the heap.
        if (temp->child) {
            pq.push(temp->child);
        }
        if (!result) {
            result = temp;
            pointer = temp;
            pointer->next = nullptr;
        } else {
            pointer->child = temp;
            pointer = temp;
            pointer->next = nullptr;
        }
    }
    return result;
}