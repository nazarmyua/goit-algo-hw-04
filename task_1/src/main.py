import timeit
import numpy as np

from merge_sort import merge_sort
from insertion_sort import insertion_sort


def generate_array(size, min_val, max_val):
    return np.random.randint(min_val, max_val + 1, size).tolist()


def main():
    itterations = 2
    small_array = generate_array(100, 0, 100)
    middle_array = generate_array(10000, 0, 10000)
    large_array = generate_array(20000, 0, 20000)
    large2_array = generate_array(30000, 0, 30000)

    for arr in [small_array, middle_array, large_array, large2_array]:
        insertion_time = (
            timeit.timeit(lambda: insertion_sort(arr.copy()), number=itterations)
            / itterations
        )
        merge_time = (
            timeit.timeit(lambda: merge_sort(arr.copy()), number=itterations)
            / itterations
        )
        timsort_time = (
            timeit.timeit(lambda: sorted(arr.copy()), number=itterations) / itterations
        )

        print(
            f"Array ({len(arr)}): Insertion Sort: {insertion_time:.6f}s, Merge Sort: {merge_time:.6f}s, Timsort: {timsort_time:.6f}s"
        )


if __name__ == "__main__":
    main()
