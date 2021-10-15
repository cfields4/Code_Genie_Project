print ('=====================================')
print ('Welcome to the Code Genie')
print ('-------------------------------------')

#Defines coding language choices
language_choices = ['Python', 'Java', 'Golang']
#Defines List of use options
use_options = {1:'Web', 2:'GUI', 3:'Automation'}
#Defines Dictionary of skill levels: 1=Beginner, 2=Experienced, 3=Wizard
skill_level = ['Beginner', 'Intermediate', 'Professional']

while True:
    learn_selection = input('Would you like to learn more about coding? (Y/N): ').capitalize()
    if learn_selection == 'Y':
        print('')
        print('What is your coding language of choice?')
        for num, choice in enumerate(language_choices, start = 1):
            print (int(num),"-",choice)
        print('')
        lang = int(input('Select the number for language to learn:'))
        if lang == 1:
            print('')
            print('Choose option for how you would like to use Python:')
            for key in use_options:
                print(key, "-", use_options[key])
            print('')
            py_options = int(input('Select the number for your use case:'))
            print('')
            print ('What is your skill level?:')
            for num, skill in enumerate(skill_level, start = 1):
                print(int(num),"-",skill)
            print('')
            skill = int(input('Select the number for your skill level:'))
            if skill == 1:
                print('https://www.python.org/about/gettingstarted/')
            elif skill == 2:
                print('https://realpython.com/python-web-applications/')
            elif skill == 3:
                print('https://learn-robotics.com/')
        elif lang == 2:
            print('')
            print('Choose option for how you would like to use Java:')
            for key in use_options:
                print(key, "-", use_options[key])
            print('')
            jav_options = int(input('Select the number for your use case:'))
            print('')
            print('What is your skill level?:')
            for num, skill in enumerate(skill_level, start = 1):
                print(int(num),"-",skill)
            print('')
            skill = int(input('Select the number for your skill level:'))
            if skill == 1:
                print('https://www.java-made-easy.com/java-for-beginners.html')
            elif skill == 2:
                print('https://www.udemy.com/java-for-intermediate-users/')
            elif skill == 3:
                print('https://www.udemy.com/advanced-java-programming/')
        elif lang == 3:
            print('')
            print('Choose option for how you would like to use Golang:')
            for key in use_options:
                print(key, "-", use_options[key])
            print('')
            go_options = int(input('Select the number for your use case:'))
            print('')
            print('What is your skill level?:')
            for num, skill in enumerate(skill_level, start=1):
                print(int(num),"-",skill)
            print('')
            skill = int(input('Select the number for your skill level:'))
            if skill == 1:
                print('https://www.udemy.com/google-go-programming-for-beginners/')
            elif skill == 2:
                print('https://golang.org/doc/articles/wiki/')
            elif skill == 3:
                print('https://www.oreilly.com/library/view/advanced-go-programming/9781788994880/')
                # print('\n')
        print('')
    else:
        print('Ok, goodbye!')
        print('=====================================')
        print('Thanks for using Code Genie!')
        print('-------------------------------------')
        exit()


