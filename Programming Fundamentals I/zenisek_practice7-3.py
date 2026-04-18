def total_list(numbers):
    total = sum(numbers)
    return total

def main():
    listone = [5, 2, 9, 1, 7]
    listtwo = [3, 8, 6, 4, 0]

    combined_list = listone +listtwo
    combined_list.sort()

    total = total_list(combined_list)

    print("Sorted List:", combined_list)
    print("Total:", total)
    print("Max:", max(combined_list))
    print("Min:", min(combined_list))

if __name__ == "__main__":
    main()