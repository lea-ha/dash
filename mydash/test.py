import pandas as pd
import numpy as np

df = pd.DataFrame({"Col " + str(i + 1): np.random.rand(30) for i in range(6)})
print(df.head())