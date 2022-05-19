class Solution {
    public boolean isPerfectSquare(int num) {
        if(num == 1){return true;}
        if(num < 4){return false;}
        int left = 2, right = num/2;
        while(left <= right){
            int mid = left + ((right-left)>>1);
            long pow = (long) mid * mid;
            if(pow == num){
                return true;
            }else if(pow > num){
                right = mid -1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }
}