import sys
input = sys.stdin.readLine

N, K = map(int, input().split())
arr = list(map(int, input().split()))


def quick_sort(arr, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우
            arr[right], arr[pivot] = arr[pivot], arr[right]

    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr[K-1])
