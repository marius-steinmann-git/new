import pandas as pd
import numpy as np


s = pd.Series([1, 3, 5, np.nan, 6, 8])


print (s)


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index = list(range(4)), dtype="float32"),
    }
)
print(df2)