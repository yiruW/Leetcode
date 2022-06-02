/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    let res = [];
    function isvalid(row, col, board){
        // col check
        for(var i=0; i<row; i++){
            if(board[i][col] === 'Q') return false;
        }
        for(var i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
            if(board[i][j] === 'Q') return false;
        }
        for(var i=row-1, j=col+1; i>=0 && j<n; i--, j++){
            if(board[i][j] === 'Q') return false;
        }
        return true;
    }
    function transToArray(board){
        let chessBoard = [];
        board.forEach(row => {
            let str = ''
            row.forEach(val => {
                str += val
            })
            chessBoard.push(str);
        })
        return chessBoard;
    }
    function backTracking(row, board){
        if(row === n){
            res.push(transToArray(board));
            return;
        }
        for(let col=0; col<n; col++){
            if(isvalid(row, col, board)){
                board[row][col] = 'Q';
                backTracking(row + 1, board);
                board[row][col] = '.'
            }
        }
    }
    let chessBoard = new Array(n).fill([]).map(() => new Array(n).fill('.'));
    backTracking(0, chessBoard);
    return res;
};