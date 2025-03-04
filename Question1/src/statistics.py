# Statistical Analysis: T-test comparing grip strength between frail and non-frail participants
frail = df[df['Frailty'] == 1]['Grip Strength']
non_frail = df[df['Frailty'] == 0]['Grip Strength']

t_stat, p_value = stats.ttest_ind(non_frail, frail, equal_var=False)
print(f"T-test Results: t-statistic = {t_stat:.3f}, p-value = {p_value:.5f}")
