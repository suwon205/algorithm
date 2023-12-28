var dict = {
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
};

function isNumber(char) {
  var numericPattern = /^[0-9]$/;
  return numericPattern.test(char);
}

function solution(s) {
  var answer = '';
  var idx = 0;

  while (idx < s.length) {
    if (isNumber(s[idx])) {
      answer += s[idx];
      idx += 1;
    } else {
      for (let ed = idx + 1; ed <= s.length; ed++) {
        var temp = s.slice(idx, ed);
        if (dict[temp] !== undefined) {
          answer += dict[temp];
          idx = ed;
          break;
        }
      }
    }
  }

  return parseInt(answer);
}
