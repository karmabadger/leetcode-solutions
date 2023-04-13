function lengthOfLongestSubstring(s: string): number {
  const charMap = new Uint32Array(256);
  // 2,147,483,647
  let begin = 0;
  let end = 0;

  let max = 0;

  while (end < s.length) {
    const charCode = s.charCodeAt(end);
    if (charMap[charCode] > 0) {
      begin = Math.max(begin, charMap[charCode]!);
    }
    charMap[charCode] = end + 1;
    max = Math.max(max, end - begin + 1);
    end++;
  }

  return max;
}

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
