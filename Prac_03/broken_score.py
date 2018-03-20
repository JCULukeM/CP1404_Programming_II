"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def get_score(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "passable"
    else:
        grade = "Bad"

    return grade


def main():
    score = float(input("Enter score: "))
    print(get_score(score))

main()


