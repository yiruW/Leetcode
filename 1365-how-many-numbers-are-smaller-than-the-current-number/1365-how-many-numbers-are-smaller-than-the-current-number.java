class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] res = Arrays.copyOf(nums, nums.length);
        Arrays.sort(res);
        for(int i=0; i<res.length; i++){
            if(!map.containsKey(res[i])){
                map.put(res[i], i);
            }
        }
        for(int i=0; i<res.length; i++){
            res[i] = map.get(nums[i]);
        }
        return res;
    }
}