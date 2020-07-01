#include<bits/stdc++.h>

using namespace std;

class HashNode {
    private:
    string key;
    string value;
    HashNode *next;

    public:
    HashNode(string key, string value) {
        this->key = key;
        this->value = value;
        this->next = NULL;
    }

    string getValue() {
        return value;
    }
};

class HashKey {
    public:
    long hash(string key) {
        return 100 + key[0];
    }
};

class HashMap {
    private:
    size_t size;
    HashNode **table;
    HashKey hk;

    public:
    HashMap(size_t size) {
        table = new HashNode*[size];
    }

    ~HashMap() {
            delete [] table;
    }

    string get(string key) {
        long hash = hk.hash(key);
        HashNode *h = table[hash];
        return h->getValue();
    }

    void put(string key, string value)
    {
        long hash = hk.hash(key);
        table[hash] = new HashNode(key, value);
    }
};

int main()
{
    HashMap *hm = new HashMap(1024);
    hm->put("mykey", "avalue");
    cout << hm->get("mykey") << endl;

    return 0; 
}