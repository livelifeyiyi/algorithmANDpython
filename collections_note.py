import sys
import time
import _collections
from collections import Counter



fancy_loading = _collections.deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

c = Counter(a=4, b=2, c=0, d=-2)