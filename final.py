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
                    print('Too small, please try again.')
                elif num > answer:
                    print('Too big, please try again.')
                else:
                    print('Bingo! You have guessed {} times.'.format(times))
                    break
            else:
                print('You have to enter a number between 1-100.')
        except ValueError:
            print('You have to enter a integer!')
    return times

def score(user_history, user, total_round, total_avg, min_times):
    user_history[user] = [user, str(total_round), str(total_avg), str(min_times)]
    result = [' '.join(user_history[key]) + '\n' for key in user_history]

    try:
        with open('game_users.txt', 'w', encoding='utf-8') as f:
            f.writelines(result)
    except:
        f = open('game_score.txt', 'w', encoding='utf-8')
        f.writelines(result)
        f.close()

def play():
    user = input('Please enter your Name: ')
    user_history = {}

    with open('game_users.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '').split(' ')
        # print(data)
        for j in data:
            user_history[j[0]] = j

        if user in user_history:
            total_round = int(user_history[user][1])
            total_avg = float(user_history[user][2])
            min_times = int(user_history[user][3])
        else:
            total_round = 0
            total_avg = 0.00
            min_times = 0

        print('{}, You have played {} rounds, the average time of guessing is {}, the minimum time of guessing is {}. Let\'s start the game!'.format(
                user, total_round, total_avg, min_times))
        _round = 1
        _round_time = 0
        times = game()
        total_round += _round
        _round_time += times
        total_avg = round(((total_round-_round) * total_avg + _round_time) / total_round, 2)
        if user in user_history:
            min_times = min(min_times, times)
        else:
            min_times = times
        score(user_history, user, total_round, total_avg, min_times)

    while True:
        print('{}, You have played {} rounds, the average time of guessing is {}, the minimum time of guessing is {}. Let\'s start the game!'.format(
                user, total_round, total_avg, min_times))
        restart = input('Do you want to play again?("y" for yes and "e" for exit)')
        if restart.lower() == 'y':
            _round += 1
            total_round += 1
            times = game()
            _round_time += times
            total_avg = round(((total_round - _round) * total_avg + _round_time) / total_round, 2)
            min_times = min(min_times, times)
            score(user_history, user, total_round, total_avg, min_times)
        elif restart.lower() == 'e':
            print('Your score has been saved. Good bye~')
            break
        else:
            print('Please enter the right contents.')

if __name__ == "__main__":
    # new_game = play()
    play()