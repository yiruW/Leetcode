class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if(cost.length == 1){return cost[0];}
        int[] costAtP = new int[cost.length];
        costAtP[0] = cost[0];
        costAtP[1] = cost[1];
        for(int i=2; i<cost.length; i++){
            costAtP[i] = Math.min(costAtP[i-1], costAtP[i-2])+cost[i];
        }
        return Math.min(costAtP[cost.length-1], costAtP[cost.length-2]);
    }
}