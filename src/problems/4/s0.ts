function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  let i1 = 0;
  let i2 = 0;

  const totalLength = nums1.length + nums2.length;
  let count = 0;
  if (totalLength % 2 === 0) {
    let res = 0;
    const mid = totalLength / 2;
    while (true) {
      if (count === mid) {
        if (i1 < nums1.length && i2 < nums2.length) {
          if (nums1[i1] < nums2[i2]) return (res + nums1[i1++]) / 2;
          else return (res + nums2[i2++]) / 2;
        } else if (i1 < nums1.length) return (res + nums1[i1++]) / 2;
        else return (res + nums2[i2++]) / 2;
      } else {
        if (i1 < nums1.length && i2 < nums2.length) {
          if (nums1[i1] < nums2[i2]) res = nums1[i1++];
          else res = nums2[i2++];
        } else if (i1 < nums1.length) res = nums1[i1++];
        else res = nums2[i2++];
      }
      count++;
    }
  } else {
    const mid = (totalLength - 1) / 2;
    while (true) {
      if (count === mid) {
        if (i1 < nums1.length && i2 < nums2.length) {
          if (nums1[i1] < nums2[i2]) return nums1[i1++];
          else return nums2[i2++];
        } else if (i1 < nums1.length) return nums1[i1++];
        else return nums2[i2++];
      } else {
        if (i1 < nums1.length && i2 < nums2.length) {
          if (nums1[i1] < nums2[i2]) i1++;
          else i2++;
        } else if (i1 < nums1.length) i1++;
        else i2++;
      }
      count++;
    }
  }
}

// console.log(findMedianSortedArrays([1, 3], [2]));
console.log(findMedianSortedArrays([1, 2], [3, 4]));
console.log(findMedianSortedArrays([0, 0], [0, 0]));
