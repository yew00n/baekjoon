total_credit = 0
total_score = 0
score_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
              "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range(20):
    lecture, credit, score = input().split()  # 입력받고 과목명, 학점, 등급 저장
    credit = float(credit)

    if score != "P":
        score = score_dict[score]

        total_credit += credit
        total_score += credit * score

print(total_score/total_credit)
