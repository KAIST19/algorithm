package Tree.BST;
import Tree.*;

public class BST implements Tree {
    private class Node {
        Key key
    }
    /** Return true if the element is in the tree */
    public boolean search(Key key) {
        return search(key, root)
    }

    /** Insert element e into the binary tree*/
    public void insert(Key key);

    /** Inorder traversal from the root*/
    public void inorder();

    /** Postorder traversal from the root */
    public void postorder();

    /** Preorder traversal from the root */
    public void preorder();

    /** Get the number of nodes in the tree */
    public int getSize();

    /** Return true if the tree is empty */
    public boolean isEmpty();

    // helper
    private int compare(Node left, Node right) {
        if (left.key < left.right) return -1;
        if (left.key > left.right) return 1;
        return 0;
    }
}