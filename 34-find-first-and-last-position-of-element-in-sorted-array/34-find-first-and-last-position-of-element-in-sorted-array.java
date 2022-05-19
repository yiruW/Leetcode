class Solution {
    public int[] searchRange(int[] nums, int target) {
        int index = binarySearch(nums, target);
        if(index == -1){
            return new int[] {-1, -1};
        }
        int left = index, right = index;
        while(left > 0 && nums[left - 1] == nums[index]){
            left --;
        }
        while(right < nums.length - 1 && nums[right + 1] == nums[index]){
            right ++;
        }
        return new int[] {left, right};
    }
    
    public int binarySearch(int[] nums, int target){
        if (nums.length < 1 || target < nums[0] || target > nums[nums.length-1]){
            return -1;
        }
        int left = 0, right = nums.length-1;
        while(left <= right){
            int mid = left + ((right - left) >>1);
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                right = mid-1;
            }else{
                left = mid +1;
            }
        }
        return -1;
    }
}