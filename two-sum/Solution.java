import java.util.Map;
import java.util.HashMap;

public class Solution {

    /* time: O(n), space: O(n) */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> dictionary = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (dictionary.containsKey(target - nums[i])) {
                int j = dictionary.get(target - nums[i]);
                return new int[] { i, j };
            } else {
                dictionary.put(nums[i], i);
            }
        }
        return new int[] { -1, -1 };
    }

}