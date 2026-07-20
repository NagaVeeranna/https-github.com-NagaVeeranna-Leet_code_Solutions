 class Solution {
    public boolean isHappy(int n) {
        int tortoise = n;
        int hare = getNext(n);
        
        while (hare != 1 && tortoise != hare) {
            tortoise = getNext(tortoise);
            hare = getNext(getNext(hare));
        }
        
        return hare == 1;
    }

    private int getNext(int n) {
        int totalSum = 0;
        while (n > 0) {
            int d = n % 10;
            n = n / 10;
            totalSum += d * d;
        }
        return totalSum;
    }
}