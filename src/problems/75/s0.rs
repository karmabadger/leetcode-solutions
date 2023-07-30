impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut counts = [0, 0, 0];
        for num in nums.iter_mut() {
            counts[*num as usize] += 1;
        }

        let [r, g, b] = counts;
        for i in 0..counts[0] {
            nums[i] = 0;
        }

        let end = r + g;
        for i in r..r + g {
            nums[i] = 1;
        }

        let end2 = end + b;
        for i in end..end2 {
            nums[i] = 2;
        }
    }
}
