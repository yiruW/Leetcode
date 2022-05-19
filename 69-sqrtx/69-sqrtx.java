class Solution {
    public int mySqrt(int x) {
        if(x < 2){return x;}
        int left = 2, right = x/2;
        while(left <= right){
            int mid = left + ((right-left)>>1);
            long pow = (long) mid * mid;
            if(pow > x){
                right = mid -1;
            }else if(pow < x){
                left = mid +1;
            }else{
                return mid;
            }
        }
        return right;
    }
}