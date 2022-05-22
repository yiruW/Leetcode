class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.length;
        int column = obstacleGrid[0].length;
        int[][] path = new int[row][column];
        for(int i=0; i<row; i++){
            if (obstacleGrid[i][0] == 1) break;
            path[i][0] = 1;
        }
        for(int i=0; i<column; i++){
            if (obstacleGrid[0][i] == 1) break;
            path[0][i] = 1;
        }
        for(int i=1; i<row; i++){
            for(int j=1; j<column; j++){
                if(obstacleGrid[i][j] == 0){
                    path[i][j] = path[i-1][j] + path[i][j-1];
                }
            }
        }
        return path[row-1][column-1];
    }
}