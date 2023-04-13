function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  if (nums1.length === 1 && nums2.length === 1)
    return (nums1[0] + nums2[0]) / 2;

  const n1IsEven = nums1.length % 2 === 0;
  const n1Mid = nums1.length / 2;
  const n1Median = n1IsEven
    ? (nums1[n1Mid - 1] + nums1[n1Mid]) / 2
    : nums1[Math.floor(n1Mid)];

  const n2IsEven = nums2.length % 2 === 0;
  const n2Mid = nums2.length / 2;
  const n2Median = n2IsEven
    ? (nums2[n2Mid - 1] + nums2[n2Mid]) / 2
    : nums2[Math.floor(n2Mid)];

  // if (nums1.length === 1) {
  //   if (n1Median > n2Median) {
  //     return n1IsEven
  //       ? nums1[Math.floor(n1Mid)]
  //       : nums1[Math.floor(n1Mid)];
  //   } else {
  //     return findMedianSortedArrays(nums1, nums2.slice(n2Mid, nums2.length));
  //   }
  // }

  if (n1Median === n2Median) return n1Median;
  else if (n1Median > n2Median) {
    return findMedianSortedArrays(
      nums1.slice(0, (n1IsEven ? Math.floor(n1Mid) : Math.ceil(n1Mid)) + 1),
      nums2.slice(n2IsEven ? Math.ceil(n2Mid) : Math.floor(n2Mid), nums2.length)
    );
  } else {
    return findMedianSortedArrays(
      nums1.slice(
        n1IsEven ? Math.ceil(n1Mid) : Math.floor(n1Mid),
        nums1.length
      ),
      nums2.slice(0, (n2IsEven ? Math.floor(n2Mid) : Math.ceil(n2Mid)) + 1)
    );
  }
}

// console.log(findMedianSortedArrays([1, 3], [2]));
console.log(findMedianSortedArrays([1, 2], [3, 4]));
// console.log(findMedianSortedArrays([0, 0], [0, 0]));
