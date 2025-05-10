import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#packageSample

#import extra.iota
#from extra.iota import funI
from extra.iota import funI as funIota

#print(extra.iota.funI())
#print(funI())
print(funIota())