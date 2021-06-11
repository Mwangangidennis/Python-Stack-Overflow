# Quizzes Beginning
Quiz = []
x = 0
y = str(x)

# Quiz_list = [Quiz]
while x < 10:
    message_txt = open('Quiz' + y + '.dat', 'r')
    img_sms = message_txt.readlines()
    # print(img_sms)
    Quiz.append(img_sms)
    x = x + 1
    y = str(x)
    print(x)
    # print(Quiz)

# Quiz1.close()
# print(Quiz)
# print(Quiz[1])
# Quizzes  End
