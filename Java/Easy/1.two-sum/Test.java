public class Test {

    public static void main(String[] args){    
        int[] nums={2,3,-2,-3};
        int target = 5; 
        int[] result = new Solution().twoSum(nums, target);
        System.out.println("result: " + result[0] + "," + result[1]);
    }

}