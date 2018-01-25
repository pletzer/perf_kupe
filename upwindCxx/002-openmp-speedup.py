import pandas as pd
import matplotlib.pylab as plt
import numpy

# the Gnu 6.1 i7 results obtained on abraracourcix using 10 steps and multiplying 
# the exec time by 10
df = pd.DataFrame({'num threads': [1, 2, 4, 10, 20, 40],
	              'Gnu 7.1 times': numpy.array([9*60+37., 11*60+4., 6*60+58., 4*60+34., 2*60+51., 2*60+23.]),
	              'Intel times': numpy.array([9*60+44., 11*60+55., 8*60+43., 4*60+11., 4*60+11., 3*60+12.]),
	              'Cray times': numpy.array([10*60+42., 6*60+7., 3*60+19., 1*60+32., 0*60+60., 0*60+35.7]), 
                      'Gnu 6.1 i7 times': numpy.array([996., 573., 403., 266., 264., 233.,]),
                      'Pan impi GCC 5.4 times': numpy.array([13*60+11., 7*60+23., 4*60+18., 1*60+51., 3*60+50., float('nan'),]),
})

# add speedup columns
for k in ["Gnu 7.1", "Intel", "Cray", 'Gnu 6.1 i7', 'Pan impi GCC 5.4']:
	colname = k
	df[colname] = df["Cray times"].tolist()[0]/numpy.array(df[k + " times"].tolist())


df.plot(kind='bar', x='num threads', y=['Intel', 'Gnu 7.1', 'Cray', 'Pan impi GCC 5.4', 'Gnu 6.1 i7'])
plt.title('upwindCxx OpenMP speedup')
plt.show()
