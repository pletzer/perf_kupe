import pandas as pd
from matplotlib import pylab
import numpy

df = pd.DataFrame({'compiler-target': ['Gnu 4.9.3 x86-64', 'Gnu 4.9.3 broadwell', 
	                                 'Gnu 7.1.0 broadwell', 'Gnu 7.1.0 x86-skylake', 
	                                 'Intel skylake', 'Cray skylake', ],
	               'times': numpy.array([271., 245., 192., 185., 237., 179.])})

ts = numpy.array(df['times'].tolist())
speedup = ts[0]/ts
df['speedup'] = speedup

p = df.plot(kind='bar', x='compiler-target', y='speedup', 
	        width=0.5, 
	        legend=False,
	        color=[pylab.cm.Paired(numpy.arange(len(df)))],
	        figsize=(3, 4) )
pylab.title('speedup')
pylab.show()