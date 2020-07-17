class ChattyBot:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def greet(self):
        print('Hello! My name is {}\nI was created in {}'.format(self.name, self.year))

    def remind_name(self):
        print('Please, remind me your name.')
        name = input()
        print('What a great name you have, ' + name + '!')

    def guess_age(self):
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5 and 7.')

        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

        print("Your age is " + str(age) + "; that's a good time to start programming!")

    def count(self):
        print('Now I will prove to you that I can count to any number you want.')
        for i in range(int(input()) + 1):
            print('{}!'.format(i))

    def test(self):
        print("Let's test your programming knowledge.")
        correct_answer = False
        while not correct_answer:
            print("Which's the number one programming language?")
            print('1. Python.')
            print('2. Typescript.')
            print('3. Scala.')
            print('4. C++.')
            answer = int(input())
            if answer != 1:
                print('Please, try again')
            else:
                correct_answer = True
        print('Completed, have a nice day!')

    def end(self):
        print('Congratulations, have a nice day!')


if __name__ == '__main__':
    my_bot = ChattyBot('Aid', '2020')
    my_bot.greet()  # change it as you need
    my_bot.remind_name()
    my_bot.guess_age()
    my_bot.count()
    my_bot.test()
    my_bot.end()
