impl Solution {
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        neighbors = vec![vec![]; bombs.len()];

        for i in 0..bombs.len() {
            for j in 0..bombs.len() {
                if i != j && dist2(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2] * bombs[i][2]] {
                    neighbors[i].push(j);
                }
            }
        }

        let mut max = 0;
        for i in 0..bombs.len() {
            let mut visited = HashSet::new();
            visited.insert(i);
            dfs(i, visited, bombs);
            max = max.max(visited.len());
        }

        max
    }
}

fn dist2(x1: i32, y1: i32, x2: i32, y2: i32) -> i32 {
    (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
}

fn dfs(u: i32, visited: HashSet<i32>, bombs: Vec<Vec<i32>>) {
    for v in neighbors[u] {
        if !visited.contains(v) {
            visited.insert(v);
            dfs(v, visited, bombs);
        }
    }
}
