/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    const wordSet = new Set(wordList);
    if(wordSet.length == 0 || !wordSet.has(endWord)) return 0;
    const visitMap = new Map();
    const queue = [];
    queue.push(beginWord);
    visitMap.set(beginWord, 1);
    
    while(queue.length != 0){
        let word = queue.shift();
        let path = visitMap.get(word);
        for(let i=0; i<word.length; i++){
            for(let c = 97; c<=122; c++){
                let newWord = word.slice(0,i) + String.fromCharCode(c) + word.slice(i+1);
                if(newWord == endWord) return path+1;
                if(wordSet.has(newWord) && !visitMap.has(newWord)){
                    visitMap.set(newWord, path+1);
                    queue.push(newWord);
                }
            }
        }
    }
    return 0;
};