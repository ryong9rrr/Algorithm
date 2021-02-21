function solution(arr) {
  const ans = [];

  for (var i = 0; i < arr.length - 1; i++) {
    if (arr[i] != arr[i + 1]) ans.push(arr[i]);
  }
  ans.push(arr[arr.length - 1]);

  return ans;
}

/*py

def solution(arr):
    ans = []
    
    for i in range(len(arr)-1) :
        if(arr[i] != arr[i+1]) :
            ans.append(arr[i])
    
    ans.append(arr[-1])
    
    return ans

*/
