function solution(strings, n) {
    return (
        strings.sort((a,b) => {
            if(a[n]==b[n]){
                return (a>b)-(a<b);
            } else {
                return (a[n]>b[n])-(a[n]<b[n]);
            }
        })
    )
}

function solution(strings, n) {
    return(
        strings.sort((a,b) => a[n]==b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n]) )
    )
 }


 def solution(strings, n):
 return sorted(sorted(strings), key=lambda x : x[n])