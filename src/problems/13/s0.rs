impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        // total = 0
        // last_val = matchRoman(s[0])
        // cur_val = 0
        // for c in s[1:]:
        //     cur_val = matchRoman(c)
        //     if cur_val > last_val:
        //         total -= last_val
        //     else:
        //         total += last_val
        //     last_val = cur_val

        // total += last_val
        // return total

        let s_chars = s.chars();
        let mut total = 0;
        let mut last_val = matchRoman(
    }
}

fn matchRoman(c: &char) -> i32 {
    match c {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000,
        _ => 0,
    }
}
