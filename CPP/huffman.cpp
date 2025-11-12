#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// Structure to represent each node of the Huffman tree
struct HuffmanNode {
    int data;       // frequency of the character
    char c;         // the character itself
    HuffmanNode *left, *right; // pointers to left and right child nodes

    // Constructor to easily create new nodes
    HuffmanNode(int d, char ch) {
        data = d;
        c = ch;
        left = right = nullptr;
    }
};

// Comparator for the priority queue (min-heap based on frequency)
struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        // return true if a has higher frequency (so smaller freq stays on top)
        return a->data > b->data;
    }
};

// Function to print the Huffman code recursively
void printCode(HuffmanNode* root, string s) {
    if (!root) return;  // base condition: null node

    // If it's a leaf node (no left/right) and a valid character
    if (!root->left && !root->right && isalpha(root->c)) {
        cout << root->c << ": " << s << endl; // print character and its code
        return;
    }

    // Traverse left with '0' and right with '1'
    printCode(root->left, s + "0");
    printCode(root->right, s + "1");
}

int main() {
    int n;
    cout << "Enter number of characters: ";
    cin >> n;

    vector<char> chars(n);  // store characters
    vector<int> freq(n);    // store their frequencies

    // Input characters and their frequencies
    for (int i = 0; i < n; i++) {
        cout << "Enter character " << (i + 1) << ": ";
        cin >> chars[i];
        cout << "Enter frequency of '" << chars[i] << "': ";
        cin >> freq[i];
    }

    // Min-heap priority queue (lowest frequency node on top)
    priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> pq;

    // Step 1: Create a leaf node for each character and push into PQ
    for (int i = 0; i < n; i++) {
        pq.push(new HuffmanNode(freq[i], chars[i]));
    }

    // Step 2: Combine two smallest nodes until one node remains
    while (pq.size() > 1) {
        // Remove two nodes with smallest frequencies
        HuffmanNode *x = pq.top(); pq.pop();
        HuffmanNode *y = pq.top(); pq.pop();

        // Create new internal node with combined frequency
        HuffmanNode *f = new HuffmanNode(x->data + y->data, '-');
        f->left = x;
        f->right = y;

        // Push the new node back into the queue
        pq.push(f);
    }

    // Step 3: The remaining node is the root of Huffman tree
    cout << "\nHuffman Codes:\n";
    printCode(pq.top(), "");  // print codes by traversing the tree

    return 0;
}
