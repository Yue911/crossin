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

def score(user_history, user, total_round, total_avg, min_times):                          #写入成绩
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
    user_history = {}                                                             #用字典保存原先数据，key为名字，编辑文件改为编辑字典

    with open('game_users.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '').split(' ')
        # print(data)
        for j in data:
            user_history[j[0]] = j

        if user in user_history:
            total_round = int(user_history[user][1])                             #第二列数据是总轮数round
            total_avg = float(user_history[user][3])                             #第四列是平均每轮猜的次数
            min_times = int(user_history[user][2])                               #第三列是最小猜对次数
            total_time = total_round * total_avg                                 #历史记录反算猜的总次数
        else:
            total_round = 0
            total_avg = 0.00
            min_times = 0
            total_time = 0

        print('{}, You have played {} rounds, the average time of guessing is {}, the minimum time of guessing is {}. Let\'s start the game!'.format(
                user, total_round, total_avg, min_times))
        _round = 1
        total_round += _round
        times = game()
        total_time += times
        total_avg = round(total_time / total_round, 2)
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
            total_time += times
            total_avg = round(total_time / total_round, 2)
            min_times = min(min_times, times)
            score(user_history, user, total_round, total_avg, min_times)
        elif restart.lower() == 'e':
            print('Your score has been saved. Good bye~')
            break
        else:
            print('Please enter the right contents.')

if __name__ == "__main__":
    play()