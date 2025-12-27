# Sorting Algorithm Performance Benchmark

This repository contains a simple benchmark comparing the execution time of three sorting algorithms:

- **Insertion Sort**
- **Merge Sort**
- **Timsort**

The goal is to demonstrate how algorithmic complexity impacts performance as input size increases.

---

## Benchmark Results

All measurements were taken in seconds (s).

| Array Size | Insertion Sort | Merge Sort | Timsort |
|-----------:|---------------:|-----------:|--------:|
| 100        | 0.000103 s     | 0.000077 s | 0.000005 s |
| 10,000     | 1.450095 s     | 0.014094 s | 0.000744 s |
| 20,000     | 6.004114 s     | 0.030297 s | 0.001578 s |
| 30,000     | 13.952351s     | 0.051523 s | 0.002688 s |

---

## Analysis

- **Insertion Sort** shows acceptable performance only for very small arrays. Its quadratic time complexity (O(n²)) makes it impractical for larger datasets.
- **Merge Sort** scales much better due to its O(n log n) complexity, remaining efficient even as the array size grows.
- **Timsort**, a hybrid algorithm used in many standard libraries, significantly outperforms both alternatives. It leverages existing order in the data and has excellent real-world performance.

---

## Conclusion

For non-trivial data sizes, **Timsort** is the preferred choice, followed by **Merge Sort**. **Insertion Sort** should be limited to educational purposes or very small datasets.