import numpy as np
import pandas as pd




a={'col1':213,'col2':123,'col3':456}
data = pd.DataFrame([a])
data.to_excel("data.xlsx")
print(data)