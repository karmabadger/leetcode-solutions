impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n == 0 {
            return 0;
        } else if n == 1 {
            return 1;
        }

        let mut cache1 = 0;
        let mut cache2 = 1;
        for _ in 2..n {
            let tmp = cache1 + cache2;
            cache1 = cache2;
            cache2 = tmp;
        }

        return cache1 + cache2;
    }
}
