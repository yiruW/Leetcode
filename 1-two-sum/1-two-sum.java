import java.util.HashSet; 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> arr = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int sub = target - nums[i];
            if(arr.containsKey(sub)){
                return new int[] {arr.get(sub), i};
            }
            arr.put(nums[i], i);
        }
        return null;
    }
}