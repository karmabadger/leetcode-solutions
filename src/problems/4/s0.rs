impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        recur(nums1, nums2)
    }
}

fn recur(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
    if nums1.len() == 1 && nums2.len() == 1 {
        (nums1[0] + nums2[0]) as f64 / 2
    }

    let mid1 = nums1.len() / 2;
    let mod1 = nums1.len() % 2;
    let med1 = if mod1 == 0 {
        (nums1[mid1] + nums1[mid1 - 1]) as f64 / 2
    } else {
        nums1[mid1] as f64
    };

    let mid2 = nums2.len() / 2;
    let mod2 = nums2.len() % 2;
    let med2 = if mod2 == 0 {
        (nums2[mid2] + nums2[mid2 - 1]) as f64 / 2
    } else {
        nums2[mid2] as f64
    };

    if med1 == med2 {
        med1
    } else if med1 > med2 {
        recur(&nums1[..mid1 + mod1].to_vec(), &nums2[mid2..].to_vec())
    } else {
        recur(&nums1[mid1..].to_vec(), &nums2[..mid2 + mod2].to_vec())
    }
}
