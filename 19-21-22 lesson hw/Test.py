import random
questions = 0
correct = 0

while True:

    functions = ["+", "-", "*", "/"]
    a = random.randrange(50)
    b = random.randrange(50)
    c = random.choice(functions)
    answer = float(input(f"{a} {c} {b} = ?\nYour answer: "))
    questions += 1

    if c == "+":
        jem = a + b

        if answer == jem:
            print("Your answer is correct !")
            correct += 1

        else:
            print(f"Your answer is incorrect ! Correct answer is: {jem}")

    elif c == "-":
        jem2 = a - b

        if answer == jem2:
            print("Your answer is correct !")
            correct += 1

        else:
            print(f"Your answer is incorrect ! Correct answer is: {jem2}")
    elif c == "*":
        jem3 = a * b

        if answer == jem3:
            print("Your answer is correct !")
            correct += 1
        else:
            print(f"Your answer is incorrect ! Correct answer is: {jem3}")
    elif c == "/":
        jem4 = a / b

        if answer == jem4:
            print("Your answer is correct !")
            correct += 1
        else:
            print(f"Your answer is incorrect ! Correct answer is: {jem4}")

    if questions == 10:
            print("* * * YOUR RESULT * * *")
            print(f"Questions: {questions}")
            print(f"Correct answers: {correct}")
            print(f"{correct * 100 / questions}%")
            break  