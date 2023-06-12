import sys

n = int(sys.stdin.readline())
books_list = dict()

for i in range(n):
    book = sys.stdin.readline().strip()
    books_list[book] = book.get(book, 0) + 1

result = sorted(books_list.items(), key=(lambda x: (-x[1], x[0])))
print(result[0][0])
