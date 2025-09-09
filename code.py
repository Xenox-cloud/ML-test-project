import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



a={'col1':213,'col2':123,'col3':456}
data = pd.DataFrame([a])
data.to_csv("data.csv")
print(data)
pkq=data.loc[0,"col1"]
print(pkq)


x=np.linspace(0,4*np.pi,100)
y=np.cos(x)
plt.plot(x,y)
plt.show()
