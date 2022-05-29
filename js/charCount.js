exports.charCount = function(str) {
    // we split into a list so we can count and remove the spaces
    const splitted = str.replace(/\s/g,"").split("")
    let ocurrences = {}
    let sortable = []
    // build an object with number of ocurrences
    for (i of splitted) {
        ocurrences[i] = ocurrences[i] ? ocurrences[i] + 1 : 1
    }
    // push an array with [char,ocurrences] to be sortable
    for (let char in ocurrences){
        sortable.push([char,ocurrences[char]])
    }
    // sort by function with bigger first in value as primary sorting and alphabetical key as secondary
    let result = sortable.slice().sort(function(a,b){
        if (a[1] > b[1]) { return -1} 
        if (a[1] < b[1]) { return 1} 
        if (a[1] == b[1]) {
            if (a > b) {return 1}
            if (a < b) {return -1}
            if (a == b) {return 0}
        } 
    })
    
    return result
      
    
    
};
