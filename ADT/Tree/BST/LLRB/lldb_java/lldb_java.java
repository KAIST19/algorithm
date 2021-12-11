package lldb_java;

public class lldb_java {
	public static void main(String args[]) {
		String test = "S E A R C H E X A M P L E"; 
        String[] keys = test.split(" "); 
        RedBlackBST<String, Integer> st = new RedBlackBST<String, Integer>();
        for (int i = 0; i < keys.length; i++) {
            st.put(keys[i], i); 
            System.out.println("i = " + i + ", height = " + st.height() + ", size = " + st.size());
            }

        System.out.println("size = " + st.size());
        System.out.println();

        System.out.println("Testing keys()");
        System.out.println("--------------------------------");
        for (int i=0; i<keys.length; i++) 
            System.out.println(keys[i] + " " + st.get(keys[i])); 
        System.out.println();
    }
}

class RedBlackBST<Key extends Comparable<Key>, Value> {

    private static final boolean RED   = true;
    private static final boolean BLACK = false;

    private Node root;     // root of the BST
    private int n;         // number of key-value pairs in BST

    // BST helper node data type
    private class Node {
        private Key key;           // key
        private Value val;         // associated data
        private Node left, right;  // links to left and right subtrees
        private boolean color;     // color of parent link

        public Node(Key key, Value val, boolean color) {
            this.key = key;
            this.val = val;
            this.color = color;
        }
    }

   /***************************************************************************
    *  Standard BST search.
    ***************************************************************************/

    // return value associated with the given key, or null if no such key exists
    public Value get(Key key) {
        return get(root, key);
    }
    public Value get(Node x, Key key) {
        while (x != null) {
            int cmp = key.compareTo(x.key);
            if      (cmp < 0) x = x.left;
            else if (cmp > 0) x = x.right;
            else              return x.val;
        }
        return null;
    }

    // is there a key-value pair in the symbol table with the given key?
    public boolean contains(Key key) {
        return get(key) != null;
    }


   /***************************************************************************
    *  Red-black tree insertion.
    ***************************************************************************/

    public void put(Key key, Value val) {
        root = insert(root, key, val);
        root.color = BLACK;
    }

    private Node insert(Node h, Key key, Value val) { 
        if (h == null) {
            n++;
            return new Node(key, val, RED);
        }

        int cmp = key.compareTo(h.key);
        if      (cmp < 0) h.left  = insert(h.left,  key, val); 
        else if (cmp > 0) h.right = insert(h.right, key, val); 
        else              h.val   = val;

        // fix-up any right-leaning links
        if (isRed(h.right) && !isRed(h.left))      h = rotateLeft(h);
        if (isRed(h.left)  &&  isRed(h.left.left)) h = rotateRight(h);
        if (isRed(h.left)  &&  isRed(h.right))     flipColors(h);

        return h;
    }

   /***************************************************************************
    *  Red-black tree helper functions.
    ***************************************************************************/

    // is node x red (and non-null) ?
    private boolean isRed(Node x) {
        if (x == null) return false;
        return x.color == RED;
    }

    // rotate right
    private Node rotateRight(Node h) {
        
        Node x = h.left;
        h.left = x.right;
        x.right = h;
        x.color = h.color;
        h.color = RED;
        return x;
    }

    // rotate left
    private Node rotateLeft(Node h) {
        
        Node x = h.right;
        h.right = x.left;
        x.left = h;
        x.color = h.color;
        h.color = RED;
        return x;
    }

    // precondition: two children are red, node is black
    // postcondition: two children are black, node is red
    private void flipColors(Node h) {
        
        h.color = RED;
        h.left.color = BLACK;
        h.right.color = BLACK;
    }


   /***************************************************************************
    *  Utility functions.
    ***************************************************************************/
    // return number of key-value pairs in symbol table
    public int size() {
        return n;
    }

    // is the symbol table empty?
    public boolean isEmpty() {
        return n == 0;
    }

    // height of tree (1-node tree has height 0)
    public int height() { return height(root); }
    private int height(Node x) {
        if (x == null) return -1;
        return 1 + Math.max(height(x.left), height(x.right));
    }
    
   
}