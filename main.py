#Challenge 1
def print_fifth(arr):
  print(arr[4])

print_fifth([1, 2, 3, 4, 5, 6, 7, 8])

#Challenge 2
natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in natural_numbers:
  if (num % 2 == 1):
    print(num)
#Challenge 4
class Book:
  def __init__(self, title, author): 
    self.title = title
    self.author = author

book1 = Book("Dinosaur DNA", "Mariyln Easton")

class Catalog:
  books = [book1]
  def find_book(self, title):
    for book in self.books:
      if (title == book.title):
        return book.author
    return "not found"

c = Catalog()
print(c.find_book("Dinosaur DNA"))