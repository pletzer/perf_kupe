import pandas as pd
import matplotlib.pylab as plt
import numpy

# upwindF03 test

df = pd.DataFrame({'num threads': [1, 2, 4, 10, 20, 40],
	              'Intel times': numpy.array([11*60+48., 6*60+6., 3*60+26., 1*60+47., 1*60+15., 0*60+55.]),
	              'Gnu 7.1 times': numpy.array([7*60+5., 3*60+40., 2*60+7., 1*60+8., 0*60+49., 0*60+37.]),
	              'Cray times': numpy.array([7*60+50., 4*60+3., 2*60+13., 1*60+1., 0*60+39., 0*60+25.]), 
})

# add speedup columns
for k in ["Gnu 7.1", "Intel", "Cray",]:
	colname = k
	df[colname] = df["Cray times"].tolist()[0]/numpy.array(df[k + " times"].tolist())


df.plot(kind='bar', x='num threads', y=['Intel', 'Gnu 7.1', 'Cray',])
plt.title('upwindF03 OpenMP speedup')
plt.show()
