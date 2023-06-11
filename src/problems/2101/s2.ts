function maximumDetonation(bombs: number[][]): number {
  const neighbors: number[][] = new Array(bombs.length).fill(0).map(() => []);

  for (const [i, [x1, y1, r1]] of bombs.entries()) {
    for (const [j, [x2, y2, r2]] of bombs.entries()) {
      if (i !== j && dist2(x1, y1, x2, y2) <= r1 ** 2) neighbors[i].push(j);
    }
  }

  let max = 0;
  for (let i = 0; i < bombs.length; i++) {
    const visited = new Set<number>([i]);
    dfs(i, visited, neighbors);
    max = Math.max(max, visited.size);
  }

  return max;
}

const dist2 = (x1: number, y1: number, x2: number, y2: number): number =>
  (x1 - x2) ** 2 + (y1 - y2) ** 2;

function dfs(u: number, visited: Set<number>, neighbors: number[][]): void {
  for (const v of neighbors[u]) {
    if (!visited.has(v)) {
      visited.add(v);
      dfs(v, visited, neighbors);
    }
  }
}

function main() {
  console.log(
    maximumDetonation([
      [2, 1, 3],
      [6, 1, 4],
    ])
  );
  console.log(
    maximumDetonation([
      [1, 1, 5],
      [10, 10, 5],
    ])
  );
  console.log(
    maximumDetonation([
      [1, 2, 3],
      [2, 3, 1],
      [3, 4, 2],
      [4, 5, 3],
      [5, 6, 4],
    ])
  );
}

main();
