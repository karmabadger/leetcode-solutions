function convert(s: string, numRows: number): string {
  if (numRows === 1) return s;
  const zigLen = numRows - 2;
  const numPacks = Math.ceil(s.length / (numRows + zigLen));

  const res = new Array(s.length).fill("");
  let count = 0;
  for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < numPacks; j++) {
      if (count >= s.length) return res.join("");
      res[count++] = s[i + j * (numRows + zigLen)];
      if (i === 0 || i === numRows - 1) continue;
      for (let k = 0; k < zigLen; k++) {
        if (count >= s.length) return res.join("");
        res[count++] = s[i + j * (numRows + zigLen) + numRows + k];
      }
    }
  }

  return res.join("");
}

console.log(convert("PAYPALISHIRING", 3));
// console.log(convert("PAYPALISHIRING", 4));
// console.log(convert("A", 1));
