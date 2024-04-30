import pandas as pd
import numpy as np

def winsorize(df, quantiles):
    q_low, q_high = np.percentile(df, quantiles, axis=0)
    df_clipped = df.clip(lower=q_low, upper=q_high, axis=1)
    return df_clipped

df = pd.DataFrame(range(1,11), columns=['sequence'])
print(winsorize(df, [20, 80]).to_markdown())

groups = np.concatenate([np.ones(10), np.ones(10)+1,  np.ones(10)+2, np.ones(10)+3, np.ones(10)+4])
df = pd.DataFrame(data=zip(groups, range(1,51)), columns=["group", "sequence"])

def winsorize_by_group(df, quantiles):
    def _winsorize_group(group):
        q_low, q_high = np.percentile(group['sequence'], quantiles)
        group['sequence'] = group['sequence'].clip(lower=q_low, upper=q_high)
        return group
    
    return df.groupby('group').apply(_winsorize_group).reset_index(drop=True)

winsorized_df = winsorize_by_group(df, [5, 95])
print(winsorized_df.head(15).to_markdown())

