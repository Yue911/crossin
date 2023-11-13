with open('report.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    print('======读取======')
    print(data)
    for i in range(len(data)):
        data[i] = data[i].replace('\n', '').split(' ')
    print('======处理======')
    print(data)

title = data[0] + ['总分', '平均分']
title.insert(0,'名次')
result = data[1:]
print('======title & result======')
print(title)
print(result)

for i in result:
    course = len(i) - 1
    total_score = 0
    for j in range(1,len(i)):
        total_score += int(i[j])
    average_score = round(total_score/course, 1)
    #i = i + [str(total_score), str(average_score)]
    i.extend([str(total_score), str(average_score)])
print('======加总分、均分======')
print(result)

#按总分排名
result = sorted(result, key=lambda x:x[-2], reverse=True)
k = 1
for i in result:
    i.insert(0, str(k))
    k += 1
print('======sorted======')
print(result)

#每科总分、均分
score_by_course = ['0', '平均']
student_num = len(result)
for i in range(2,13):
    total_by_course = 0
    for j in result:
        total_by_course += float(j[i])
    avg_by_course = round(total_by_course/student_num, 1)
    score_by_course.append(str(avg_by_course))
print('======科目均分行======')
print(score_by_course)

#替换不及格
for i in range(2, 13):
    for j in result:
        if float(j[i]) < 60:
            j[i] = '不及格'

result.insert(0, score_by_course)
result.insert(0, title)
print('======最终成绩单======')
print(result)

with open('result_midterm.txt', 'w', encoding='utf-8') as f_final:
    for l in result:
        line = ' '.join(l)
        f_final.write(line + '\n')