function solution(arr, divisor) {
    const result = [];
    
    for(var i =0; i<arr.length; i++){
        if(arr[i]%divisor == 0) {
            result.push(arr[i]);
        }
    }
    
    if (result.length == 0) {
        result.push(-1)
    }
    
    return result.sort((a,b) => a-b);
    
}

// filter

function solution(arr, divisor) {
    const result = arr.filter(x => x%divisor==0).sort((a,b) => a-b);
    
    return result.length==0 ? [-1] : result;
}

// python

def solution(arr, divisor):
    answer = sorted([x for x in arr if x % divisor == 0])
    return [-1] if len(answer) == 0 else answer