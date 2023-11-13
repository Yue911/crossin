import requests
def game():
    url = 'https://python666.cn/cls/number/guess/'
    r = requests.get(url)
    answer = int(r.text)

    times = 0
    while True:
        num = input('Please enter a number between 1-100: ')
        try:
            num = int(num)
            if 1 <= num <=100:
                times += 1
                if num < answer:
                    print('Too small')
                elif num > answer:
                    print('Too big!')
                else:
                    print('Bingo!')
                    break
            else:
                print('You have to enter a number between 1-100.')
        except ValueError:
            print('You have to enter a integer!')
    return times

def score(_round, times):
    user = input('Please enter your name to record your score: ')
    user_history = {}

    with open('game_users.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '').split(' ')
        #print(data)
        for j in data:
            user_history[j[0]] = j

        if user in user_history:
            total_round = int(user_history[user][1]) + _round
            total_times = int(user_history[user][1]) * int(user_history[user][2]) + times
            total_avg = round(total_times/total_round)
            min_times = min(int(user_history[user][3]), times)
            user_history[user] = [user, str(total_round), str(total_avg), str(min_times)]
        else:
            print('Hello, you are new to this game.')
            total_round = _round
            total_avg = round(times/_round)
            min_times = times
            user_history[user] = [user, str(total_round), str(total_avg), str(min_times)]

    with open('game_users.txt', 'w', encoding='utf-8') as f:
        result = [' '.join(user_history[key]) + '\n' for key in user_history]
        f.writelines(result)

def play():
    while True:
        _round = 0
        start = input('Do you want to start a new game?("y" for yes and "e" for exit)')
        print('Start:', start)
        if start.lower() == 'y':
            _round += 1
            times = game()
            score(_round, times)
        elif start.lower() == 'e':
            print('Good bye~')
            break
        else:
            print('Please enter the right contains.')

if __name__ == "__main__":
    new_game = play()