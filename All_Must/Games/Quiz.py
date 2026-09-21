#MCQ's Questions
from MCQ import Question


q3 = [
    "Which gas is the most abundant in the Earth's atmosphere?\n(a) Oxygen\n(b) Nitrogen\n(c) Carbon Dioxide\n\n",    "Who is considered the 'Father of the Indian Constitution'?\n(a) Mahatma Gandhi\n(b) Dr. B.R. Ambedkar\n(c) Jawaharlal Nehru\n\n",
    "What is the capital city of the United Arab Emirates (UAE)?\n(a) Dubai\n(b) Abu Dhabi\n(c) Sharjah\n\n",
        "Which organ in the human body is responsible for filtering blood?\n(a) Heart\n(b) Lungs\n(c) Kidneys\n\n",
    "What is the process by which green plants manufacture their own food using sunlight?\n(a) Respiration\n(b) Photosynthesis\n(c) Digestion\n\n",
    "Which planet in our solar system is known as the 'Morning Star' or 'Evening Star'?\n(a) Mars\n(b) Venus\n(c) Jupiter\n\n",
    "Who was the first woman to win a Nobel Prize?\n(a) Marie Curie\n(b) Mother Teresa\n(c) Florence Nightingale\n\n",
    "Which is the largest part of the human brain?\n(a) Cerebellum\n(b) Brainstem\n(c) Cerebrum\n\n",
    "In the context of computer hardware, what does RAM stand for?\n(a) Random Access Memory\n(b) Read Access Memory\n(c) Rapid Application Memory\n\n",
    "What specialized tissue in plants is responsible for transporting water from the roots to the leaves?\n(a) Phloem\n(b) Xylem\n(c) Epidermis\n\n"
]


ques = [

   Question(q3[0], "b"),

Question(q3[1], "b"),

Question(q3[2], "b"),

Question(q3[3], "c"),

Question(q3[4], "b"),

Question(q3[5], "b"),

Question(q3[6], "a"),

Question(q3[7], "c"),

Question(q3[8], "a"),

Question(q3[9], "b")

]

def run_test(ques):
    score = 0 
    for question in ques:
        ans = input(question.prompt)
        if ans == question.ans:
            score += 1
    print("you got " + str(score) + "/" + str(len(ques))+ " correct") 

run_test(ques)

