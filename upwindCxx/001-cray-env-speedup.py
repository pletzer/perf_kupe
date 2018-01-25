import pandas as pd
from matplotlib import pylab
import numpy

df = pd.DataFrame({'': ['before', 'after'],
	               'times': numpy.array([48.8, 34.4])})

ts = numpy.array(df['times'].tolist())
speedup = ts[0]/ts
df['speedup'] = speedup

p = df.plot(kind='bar', x='', y='speedup', 
	        width=0.5, 
	        legend=False,
	        color=[pylab.cm.Paired(numpy.arange(len(df)))] )
pylab.title('speedup')
pylab.show()