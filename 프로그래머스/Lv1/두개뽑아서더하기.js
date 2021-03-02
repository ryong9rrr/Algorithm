js
function solution(numbers) {
    let num = new Set();
    for(var i=0; i<numbers.length; i++){
        for(var j=i+1; j<numbers.length; j++){
            num.add(numbers[i]+numbers[j]);
        }
    }
    return [...num].sort((a,b) => a-b)
}
python
def solution(numbers):
    result = set()
    for i in range(0, len(numbers)) :
        for j in range(i+1, len(numbers)) :
            result.add(numbers[i]+numbers[j])
            
    return sorted(list(result))