from draw_game import draw

values = list(range(1,10))

def input_values(player):
   valid = False
   while not valid:
      player_answer = input(f"Куда поставим {player}? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(values[player_answer-1]) not in "XO"):
            values[player_answer-1] = player
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(values):
   win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for item in win:
       if values[item[0]] == values[item[1]] == values[item[2]]:
          return values[item[0]]
   return False

def main(values):
    counter = 0
    win = False
    while not win:
        draw(values)
        if counter % 2 == 0:
            input_values("X")
        else:
            input_values("O")
        counter += 1
        if counter > 4:
           tmp = check_win(values)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw(values)

main(values)

