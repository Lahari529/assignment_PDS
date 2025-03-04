# Stage 3: Visualization
sns.pairplot(df, hue='Frailty', diag_kind='kde')
plt.savefig("pairplot.png")
plt.show()

# Boxplot of grip strength by frailty status
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Frailty"], y=df["Grip Strength"], palette="Set2")
plt.xlabel("Frailty (0=No, 1=Yes)")
plt.ylabel("Grip Strength (kg)")
plt.title("Grip Strength Distribution by Frailty Status")
plt.savefig("grip_strength_vs_frailty.png")
plt.show()
