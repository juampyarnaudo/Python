import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    #transformo el texto ingresado a minusculas
    user_option = user_option.lower()
    if not user_option in options:
        print('esa opción no es valida')
        return None, None

    #con el .choice le decimos que elija alguna de las opciones que ponemos en (options)
    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return(user_option,computer_option)
def check_rules(user_option,computer_option, user_wins, computer_wins):

  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera!')
      print('User gana!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Computadora gana')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra!')
      print('User gana!')
      user_wins += 1
    else:
      print('Tijera gana a Papel')
      print('Computadora gana')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel!')
      print('User Gana!')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('Computadora gana')
      computer_wins += 1
  return user_wins, computer_wins  

def check_winner(user_wins,computer_wins):
    if computer_wins == 2:
        print('El ganardor es la computadora')
        exit()
    if user_wins == 2:
        print('El ganardor fuiste tu!')
        exit()
    
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds =1

    while True:
        print('*' * 15)
        print('ROUND: ', rounds)
        print('*' * 15)
        rounds +=1
        #como retorna multiples opciones le ponemos la opcion de user y computer
        user_option, computer_option = choose_options()
        #ponemos user_wins, computer_wins = 
        #porque en la funcion check_rules se contabiliza cuantas veces gano c/u
        #y se va asignando a esas variables.
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        #en este caso no asina nada, por eso no le ponemos la variables antes.
        check_winner(user_wins,computer_wins)
        
        

run_game()
