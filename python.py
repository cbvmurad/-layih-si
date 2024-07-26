# Messages
NAME_MESSAGE = "Adinizi yaz: "
SURNAME_MESSAGE = "Soyadinizi yaz: "
EXPERINCE_QUIZ_MESSAGE = "tecrubeniz var mi? (yes/hə/no/yox): "
EXPERINCE_COUNT_MESSAGE = "nece il tecrubeniz var: "

# Requierements
REQ_EXPERIENCE_YEAR = 3

# Inputs
name = input(NAME_MESSAGE)
surname = input(SURNAME_MESSAGE)
experince_quiz = input(EXPERINCE_QUIZ_MESSAGE)

# Answers
ANSWER_YES_AZE = "hə"
ANSWER_NO_AZE = "yox"
ANSWER_YES_EN = "yes"
ANSWER_NO_EN = "no"

if experince_quiz == ANSWER_YES_EN or experince_quiz == ANSWER_YES_AZE:
    experince_count = int(input(EXPERINCE_COUNT_MESSAGE))
    if experince_count >= REQ_EXPERIENCE_YEAR:
        print("Salam, " + name, surname + " sizi " + str(experince_count) + " il tecrubeniz oldugu ucun use goturduk, tebrikler.")
    else:
        print(name, surname + " sizi ise goture bilmedik, tecrubeniz azdir.")      
elif experince_quiz == ANSWER_NO_EN or experince_quiz == ANSWER_NO_AZE:
    print(name, surname + " sizi ise goture bilmedik, tecrubeniz yoxdur.")
else:
    print("sizi anlamadim")
    