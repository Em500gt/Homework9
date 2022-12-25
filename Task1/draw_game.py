import emoji

def draw(values):
   print(emoji.emojize(':black_small_square:' * 13))
   for i in range(3):
      print(emoji.emojize(':black_small_square:'), values[0 + i * 3], emoji.emojize(':black_small_square:'), values[1 + i * 3], emoji.emojize(':black_small_square:'), values[2 + i * 3], emoji.emojize(':black_small_square:'))
      print(emoji.emojize(':black_small_square:' * 13))