class LRUCache {
public:
    int LRU_capacity = 0;
    class Node {
    public:
        int key;
        int val;
        Node* prev;
        Node* next;

        Node(int key, int value) {
            this->key = key;
            this->val = value;
            this->prev = NULL;
            this->next = NULL;
        }
    };
    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);
    unordered_map<int, Node*> mpp;
    LRUCache(int capacity) {
        LRU_capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }
    void addNode(Node* newNode) {
        Node* temp = head->next;
        newNode->next = temp;
        newNode->prev = head;
        head->next = newNode;
        temp->prev = newNode;
    }
    void deleteNode(Node* delNode) {
        Node* prevv = delNode->prev;
        Node* nextt = delNode->next;
        prevv->next = nextt;
        nextt->prev = prevv;
    }

    int get(int key) {
        if (mpp.find(key) != mpp.end()) {
            Node* resNode = mpp[key];
            int ans = resNode->val;
            mpp.erase(key);
            deleteNode(resNode);
            addNode(resNode);
            mpp[key] = head->next;
            return ans;
        }
        return -1;
    }

    void put(int key, int value) {
        if (mpp.find(key) != mpp.end()) {
            Node* curr = mpp[key];
            mpp.erase(key);
            deleteNode(curr);
        }
        if (mpp.size() == LRU_capacity) {
            mpp.erase(tail->prev->key);
            deleteNode(tail->prev);
        }
        addNode(new Node(key, value));
        mpp[key] = head->next;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */