# Visualization 1: Distribution of Final Grades
plt.figure(figsize=(8,5))
sns.histplot(df['G3'], bins=10, kde=True, color='blue')
plt.xlabel("Final Grade (G3)")
plt.ylabel("Frequency")
plt.title("Distribution of Final Grades")
plt.savefig("grade_distribution_histogram.png")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df["lunch"], y=df["math score"], palette="Set2")  # Use math score as a proxy for final grade
plt.xlabel("Lunch Type")
plt.ylabel("Math Score")
plt.title("Lunch Type vs Math Score")
plt.savefig("lunch_vs_math_score_boxplot.png")
plt.show()

# Visualization 3: Math Score vs Final Grade
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["math score"], y=df["G3"], alpha=0.7, color='red')
plt.xlabel("Math Score")
plt.ylabel("Final Grade (G3)")
plt.title("Math Score vs Final Grade")
plt.savefig("math_score_vs_grades_scatterplot.png")
plt.show()

# Visualization 4: Parental Education Level vs Final Grade
plt.figure(figsize=(8,5))
sns.barplot(x=df["parental level of education"], y=df["G3"], palette="muted")
plt.xlabel("Parental Education Level")
plt.ylabel("Final Grade (G3)")
plt.title("Parental Education Level vs Final Grade")
plt.savefig("parental_education_vs_grades_barchart.png")
plt.show()

# Visualization 5: Gender Distribution in Final Grades
plt.figure(figsize=(8,5))
sns.violinplot(x=df["gender"], y=df["G3"], palette="coolwarm")
plt.xlabel("Gender")
plt.ylabel("Final Grade (G3)")
plt.title("Gender Distribution in Final Grades")
plt.savefig("gender_vs_grades_violinplot.png")
plt.show()
