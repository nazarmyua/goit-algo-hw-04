from task_2.src.merge_k_lists import merge_k_lists


def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Merged list:", merged_list)


if __name__ == "__main__":
    main()
