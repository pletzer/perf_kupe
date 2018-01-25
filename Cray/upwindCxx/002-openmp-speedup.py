import pandas as pd
import matplotlib.pylab as plt
import numpy

df = pd.DataFrame({'nthreads': [1, 2, 4, 10, 20, 40],
	              'gnu7_times': numpy.array([9*60+37., 11*60+4., 6*60+58., 4*60+34., 2*60+51., 2*60+23.]),
	              'intel_times': numpy.array([9*60+44., 11*60+55., 8*60+43., 4*60+11., 4*60+11., 3*60+12.]),
	              'cray_times': numpy.array([10*60+42., 6*60+7., 3*60+19., 1*60+32., 0*60+60., 0*60+35.7])})

# add speedup columns
for k in ["gnu7", "intel", "cray"]:
	colname = k + "_speedup"
	df[colname] = df["cray_times"].tolist()[0]/numpy.array(df[k + "_times"].tolist())

fig = plt.figure()
#ax = fig.add_subplot(111)
#ax2 = ax.twinx()
df.intel_speedup.plot(kind = 'bar', color = 'green', x='nthreads', position = 1, width=0.2)
df.gnu7_speedup.plot(kind = 'bar', color = 'blue', x='nthreads', position = 2, width=0.2)
df.cray_speedup.plot(kind = 'bar', color = 'red', x='nthreads', position = 3, width=0.2)
plt.legend(['intel', 'gnu 7.1', 'cray'])
plt.title('upwindCxx OpenMP speedup')
plt.show()
