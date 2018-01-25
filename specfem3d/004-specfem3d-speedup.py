import pandas as pd
from matplotlib import pylab
import numpy

df = pd.DataFrame({'compiler-arch': ['gnu4.9', 'gnu-4.9-bdwl', 'gnu7.1-sklk', 'intel-bdwl', 'intel-sklk', ],
	               'times': numpy.array([4*60+22., 3*60+48., 2*60+44., 3*60+19., 3*60+27.])})

ts = numpy.array(df['times'].tolist())
speedup = ts[0]/ts
df['speedup'] = speedup

p = df.plot(kind='bar', x='compiler-arch', y='speedup', 
	        width=0.5, 
	        legend=False,
	        color=[pylab.cm.Paired(numpy.arange(len(df)))] )
pylab.title('speedup')
pylab.show()