import java.util.Arrays;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        
        int left = 0;
        int right = people.length - 1;
        int boats = 0;
        
        while (left <= right) {
            // If the lightest and heaviest person fit together
            if (people[left] + people[right] <= limit) {
                left++;
            }
            // Heaviest person always gets a boat
            right--;
            boats++;
        }
        
        return boats;
    }
}