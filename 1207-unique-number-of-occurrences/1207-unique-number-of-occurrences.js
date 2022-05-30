/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let map = new Map();
    arr.forEach(x => {
        map.set(x, (map.get(x) || 0) +1);
    })
    return map.size === new Set(map.values()).size;
};