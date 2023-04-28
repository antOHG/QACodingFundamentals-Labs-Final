
def_list_of_squares(n):
d = dict()
for i in range(i, n + 1):
  d[i] = i * i
return d

def test_list_of_squares():
  assert list_of_squares(1) == {1: 1}
  assert list_of_squares =={1: 1, 2:4, 3: 9, 4: 16, 5, 25}

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
    number_of_vowels = += 1
    return number_of_vowels

def test_vowels():
  assert vowels("xyz") == 0
  assert vowels("aeiou") == 5
  assert vowels("AEIOU") == 5
  assert vowels("hello world") == 3

def is_even(number):
  return number % 2 == 0

def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(0) == True
  assert is_even(-1) == False

def filter_even(numbers):
  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_number.append(number)
      return even_numbers

def test_filter_even():
  assert filter_even([1,2,3,4,5]): == [2 , 4]
  assert filter_even([-1, -2 , -3, -4, -5]) == [-2, -4] 