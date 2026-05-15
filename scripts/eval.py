# © 2026 VINAYAK PATEL 

# All rights are reserved by the developer.

# This code is provided "as is" without warranties of any kind, express or implied.

# Unauthorized copying, reproduction, modification, or use of this code,
# in whole or in part, is strictly prohibited.

# The developer shall not be held liable for any damages arising from the use,
# misuse, or inability to use this code. 

# Permission to use this code is granted only through a formal process,
# which includes direct consultation with the developer, a signed agreement,
# and full payment of applicable fees.


def compareCSV(correct_file, submission_file):
    import csv
    import re
    import math

    decimal_place_accuracy_v = 1 #3
    # Normalize question number
    def normalize_question(q):
        """
        Converts:
        '1' -> '1'
        'Question 1' -> '1'
        'question 25' -> '25'
        """
        q = q.strip()

        # Extract numeric part
        match = re.search(r'(\d+)', q)
        return match.group(1) if match else q
    
    # Convert answer to float if possible
    def normalize_answer(ans):
        try:
            return float(ans)
        except:
            return ans.strip()

    # Compare answers up to 3 decimal places
    # def answers_match(a, b):
    #     try:
    #         return round(float(a), decimal_place_accuracy_v) == round(float(b), decimal_place_accuracy_v)
    #     except:
    #         return str(a).strip() == str(b).strip()

    def answers_match(a, b):
        try:
            fa, fb = float(a), float(b) 
            def truncate(x, places):
                factor = 10 ** places
                return math.trunc(x * factor) / factor
            
            return truncate(fa, decimal_place_accuracy_v) == truncate(fb, decimal_place_accuracy_v)
        except:
            return str(a).strip() == str(b).strip()


    # Read CSV into dictionary
    def load_answers(file_path):
        answers = {}

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                qno = normalize_question(row["Question Number"])
                answer = normalize_answer(row["Answer"])

                answers[qno] = answer

        return answers

    # Load files
    correct_answers = load_answers(correct_file)
    submission_answers = load_answers(submission_file)

    # Compare answers
    total = len(correct_answers)
    correct = 0
    wrong = []

    for qno, correct_ans in correct_answers.items():

        submitted_ans = submission_answers.get(qno)

        if answers_match(submitted_ans, correct_ans): #if submitted_ans == correct_ans:
            correct += 1
        else:
            wrong.append({
                "Question Number": qno,
                "Expected": correct_ans,
                "Found": submitted_ans
            })


    # Print mismatches
    Result = f"Total Questions: {total}" + f"\nCorrect Answers: {correct}" + f"\nWrong Answers: {len(wrong)}" + f"\nAccuracy: {(correct / total) * 100:.2f}%\n"

    print(Result)

    if wrong:
        # print("\nMismatched Answers:")
        Result = Result + "\nMismatched Answers:"
        for item in wrong:
            temp = f"\nQ{item['Question Number']}: Expected={item['Expected']} | Found={item['Found']}"
            Result = Result + temp
        


    Result = Result +  f"\n\nTotal Questions: {total}" + f"\nCorrect Answers: {correct}" + f"\nWrong Answers: {len(wrong)}" + f"\nAccuracy: {(correct / total) * 100:.2f}%"

    Compare_File_name = f"Report of ({submission_file}) file.txt"
    with open(Compare_File_name, "w") as file:
        file.write(Result)
    


file_to_compare_list = [

] 


# File paths
correct_file = "AnswerSheet.csv"
submission_file = ""

for submission_file in file_to_compare_list:
    print("submission_file >> ", submission_file)
    compareCSV(correct_file, submission_file)





