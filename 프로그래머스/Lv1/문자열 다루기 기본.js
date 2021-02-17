function solution(s) {
  let rS = s.replace(/ /g, "");

  if (rS.length == 4 || rS.length == 6) if (parseInt(s) == +s) return true;

  return false;
}

/* python

def solution(s):
    
    rS = s.replace(" ","")
    if len(rS) == 4 or len(rS) == 6 :
        if s.isdigit() :
            return True
    return False
*/
