import time

dats = ['Quiz0.dat', 'Quiz1.dat', 'Quiz2.dat', 'Quiz3.dat', 'Quiz4.dat', 'Quiz5.dat', 'Quiz6.dat', 'Quiz7.dat',
        'Quiz8.dat']
# x = 0
for x in dats:

    y = str(x)
    print(y)
    print(x)
    # message_txt = open('Quiz = []
    # x = 0
    #
    # # Quiz_list = [Quiz]
    # dats = ['Quiz0.dat', 'Quiz1.dat', 'Quiz2.dat', 'Quiz3.dat', 'Quiz4.dat', 'Quiz5.dat', 'Quiz6.dat', 'Quiz7.dat',
    #         'Quiz8.dat', 'Quiz9.dat', 'Quiz10.dat']
    # # x = 0
    # for x in dats:
    #
    #     y = str(x)
    #     print(y)
    #     print(x)
    #     # message_txt = open('Quiz' + y + '.dat', 'r')
    #     # img_sms = message_txt.readlines()
    #     # Quiz.append(img_sms)
    #     # x = x + 1
    #     print('X is ' + y)
    #     print('Loop 1')
    #     # message_txt.close()
    #     # Quizzes  End
    #
    #     # Python program to count the number of lines in a text file
    #     # Opening a file
    #
    #     # 'Quiz' + y + '.dat', 'r'
    #     message_txt = open(x)
    #     Counter = 0
    #     # Reading from file
    #     Content = message_txt.read()
    #     CoList = Content.split("\n")
    #
    #     for i in CoList:
    #         if i:
    #             Counter += 1
    #             print('loop 2')
    #
    #     print("This is the number of lines in the file")
    #     print(Counter)
    #
    #     message_txt.close()
    #     # Counting End
    #
    #     file = open(x, 'r')
    #     c = int(Counter)
    #
    #     reading = file.readlines()
    #     print('this is the reading ')
    #     print(reading)
    #     #  Read end
    #     print('loop 3')
    #
    #     #  Start looping to access read lines
    #     b = 0
    #     while b < c:
    #         # k = int(a)
    #         print(b)
    #         # print(reading[a])
    #         Question = reading[b]
    #         b = b + 1
    #         # End count
    #
    #         print('The Question is here below')
    #         print(Question)
    #
    #         # Question = 'This is substitute question'
    #
    #         msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    #         msg_box.send_keys(Question)
    #         msg_box.send_keys(Keys.SHIFT + Keys.ENTER)
    #         msg_box.send_keys("Hallo, Shift Enter worked. ***End***")
    #         msg_box.send_keys(Keys.SHIFT + Keys.ENTER)
    #
    #         #  button.click()
    #
    #         z = str(b)
    #
    #         # y = y + 1
    #
    #         # defining this for breaks in the code, its too fast
    #         # In need ot a time delay
    #         # x = x + 1
    #         # time.sleep(3)
    #
    #         print('loop 4')
    #         file.close()Quiz' + y + '.dat', 'r')
    # img_sms = message_txt.readlines()
    # Quiz.append(img_sms)
    # x = x + 1
    print('X is ' + y)
    print('Loop 1')
    # message_txt.close()
    # Quizzes  End

    # Python program to count the number of lines in a text file
    # Opening a file

    # 'Quiz' + y + '.dat', 'r'
    message_txt = open(x)
    Counter = 0
    # Reading from file
    Content = message_txt.read()
    CoList = Content.split("\n")

    for i in CoList:
        if i:
            Counter += 1
            print('loop 2')

    print("This is the number of lines in the file")
    print(Counter)

    message_txt.close()
    # Counting End

    file = open(x, 'r')
    c = int(Counter)

    reading = file.readlines()
    print('this is the reading ')
    print(reading)
    #  Read end
    print('loop 3')

    #  Start looping to access read lines
    b = 0
    while b < c:
        # k = int(a)
        print(b)
        # print(reading[a])
        Question = reading[b]
        b = b + 1
        # End count

        print('The Question is here below')
        print(Question)

        # Question = 'This is substitute question'

        # msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        # msg_box.send_keys(Question)
        # msg_box.send_keys(Keys.SHIFT + Keys.ENTER)
        # msg_box.send_keys("Hallo, Shift Enter worked")

        #  button.click()

        z = str(b)

        # y = y + 1

        # defining this for breaks in the code, its too fast
        # In need ot a time delay
        # x = x + 1
        # time.sleep(3)

        print('loop 4')
        file.close()
    print("Question sent is = " + y)
    # msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    # msg_box.send_keys(Keys.ENTER)
