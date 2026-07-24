# Analysis of Algorithms — Quick Reference

## Why analyze algorithms?
To compare solutions objectively (independent of hardware/language) and
predict how an algorithm will scale as input size `n` grows.

## Asymptotic Notation
| Notation | Meaning                               |
|----------|----------------------------------------|
| O(f(n))  | Upper bound — worst case               |
| Ω(f(n))  | Lower bound — best case                |
| Θ(f(n))  | Tight bound — average/typical case     |

## Time Complexity Cheat Sheet (this week's algorithms)

| Algorithm       | Best        | Average     | Worst       | Space     |
|-----------------|-------------|-------------|-------------|-----------|
| Linear Search   | O(1)        | O(n)        | O(n)        | O(1)      |
| Binary Search   | O(1)        | O(log n)    | O(log n)    | O(1)      |
| Bubble Sort     | O(n)        | O(n²)       | O(n²)       | O(1)      |
| Quick Sort      | O(n log n)  | O(n log n)  | O(n²)       | O(log n)  |
| Merge Sort      | O(n log n)  | O(n log n)  | O(n log n)  | O(n)      |

## Key takeaways
- **Binary Search requires a sorted array** — that's the tradeoff for
  going from O(n) to O(log n).
- **Bubble Sort** is easy to understand but impractical for large `n`;
  useful mainly as a teaching example.
- **Quick Sort** is usually the fastest in practice (good cache
  locality, in-place), but its O(n²) worst case can occur on
  already-sorted or adversarial input with a poor pivot choice.
- **Merge Sort** guarantees O(n log n) even in the worst case, at the
  cost of O(n) extra memory — a classic time/space tradeoff.
- **Space complexity matters too**, not just time — always note the
  extra memory an algorithm needs beyond the input itself.
