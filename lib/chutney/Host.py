# Future imports for Python 2.7, mandatory in 3.0
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import socket
import chutney.Util

@chutney.Util.memoized
def is_ipv6_supported():
    """Return true iff ipv6 is supported on this host."""
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.bind(("::1", 0))
        s.listen(128)
        a = s.getsockname()
        s2 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s2.settimeout(1)
        s2.connect(a)
        return True
    except socket.error:
        return False


