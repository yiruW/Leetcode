/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    const row = grid.length;
    const column = grid[0].length;
    let res = 0;
    for(var i=0; i<row; ++i){
        for(var j=0; j<column; ++j){
            if(grid[i][j] === 1){
                res += 4;
                if(i>0 && grid[i-1][j]==1){
                    res -= 2;
                }
                if(j>0 && grid[i][j-1]==1){
                    res -= 2;
                }
            }
        }
    }
    return res;
};