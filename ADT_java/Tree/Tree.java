package Tree;

public interface Tree<Key extends Comparable<Key>, Value> {
    public Value get(Key key);
    public void put(Key key, Value value);
    public boolean search(Key key);
    public int size();
    public boolean isEmpty();
}