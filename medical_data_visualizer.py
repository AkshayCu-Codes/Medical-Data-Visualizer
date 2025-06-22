import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('medical_examination.csv')

# 2. Add 'overweight' column (BMI > 25 → 1, else 0)
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# 3. Normalize 'cholesterol' and 'gluc': 1 → 0 (good), >1 → 1 (bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5. Melt the DataFrame to long-form
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group by cardio, variable, value
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # Rename size column to total
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # 7. Draw catplot with seaborn
    graph = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                        data=df_cat, kind='bar', height=5, aspect=1)

    # 8. Get the figure
    fig = graph.fig

    # 9. Save and return figure
    fig.savefig('catplot.png')
    return fig

# 10. Draw Heat Map
def draw_heat_map():
    # 11. Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ].copy()

    # Rename 'gender' → 'sex' to match test expectation
    df_heat.rename(columns={'gender': 'sex'}, inplace=True)

    # 12. Calculate correlation matrix (rounded to 1 decimal for consistent format)
    corr = df_heat.corr().round(1)

    # 13. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Draw heatmap
    sns.heatmap(corr,
                mask=mask,
                annot=True,
                fmt=".1f",
                center=0,
                vmin=-0.1,
                vmax=0.25,
                square=True,
                linewidths=0.5,
                cbar_kws={"shrink": 0.5})

    # 16. Save and return figure
    fig.savefig('heatmap.png')
    return fig
