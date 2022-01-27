import java.util.Map;
import java.util.HashMap;

public class Solution {

    private Map<Integer, Integer> dictionary = new HashMap<>();

    /*time: O(n), space: O(n)*/
    public int[] twoSum(int[] nums, int target) {
        initDictionary(nums);
        return compute(nums, target);
    }

    private void initDictionary(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            dictionary.put(nums[i], i);
        }
    }

    private int[] compute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int numberToFind = (target - nums[i]);
            if (dictionary.containsKey(numberToFind)) {
                int j = dictionary.get(numberToFind);
                if (j == i) {
                    continue;
                }
                return new int[] { i, j };
            }
        }
        return new int[] { -1, -1 };
    }

}