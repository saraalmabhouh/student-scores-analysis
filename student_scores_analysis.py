import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_scores.csv")

average_score = data["Score"].mean()
print("Average Score:", average_score)

data.plot(x="Student", y="Score", kind="bar")
plt.title("Student Scores")
plt.ylabel("Score")
plt.tight_layout()
plt.show()