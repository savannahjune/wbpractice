digit_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def word_numbers(input):
  input = str(input)
  strings = ['']
  for char in input:
    letters = digit_map.get(char, '')
    strings = [string+letter for string in strings for letter in letters]
  return strings

print word_numbers(456)

def word_numbers(input):
  input = str(input)
  strings = ['']
  combo = []
  for char in input:
    letters = digit_map.get(char, '')
    for string in strings:
      strings.append(string)
      for letter in letters:
        combo.append(letter)
  return combo

print word_numbers(456)

