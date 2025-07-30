questions = [
    ["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 2],
    ["Who is the current Prime Minister of India?", "Narendra Modi", "Vidya Modi", "Rahul Gandhi", "Suresh Narendra Modi", 1],
    ["What is the current currency of India?", "Indian Rupee", "United States Dollar", "Euro", "Pound Sterling", 1],
    ["In which year did India gain independence from British rule?", 1947, 1948, 1950, 1951, 2],
    ["Who won the 2020 FIFA World Cup?", "Brazil", "Germany", "Spain", "Argentina", 1],
    ["How many countries are there in South America?", 5, 6, 7, 8, 3],
    ["What is the largest country in Africa?", "Egypt", "South Africa", "Morocco", "Nigeria", 2]

]
for question in questions:
    print(question[0])
    print(f"a.{question[1]}\nb.{question[2]}\nc.{question[3]}\nd.{question[4]}")
    answer = int(input("Enter your answer. 1 for a , 2 for b , 3 for c , 4 for d : "))
    if answer == question[5]:
        print("Correct!")
    else:
        print("incorrect! The correct answer is:", question[5])
        break