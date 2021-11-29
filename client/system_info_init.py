import subprocess
import platform
import os

__os_arch__ = None

def os_arch():
    os_arch = '32-bit'
    if os.name == 'nt':
        output = subprocess.check_output(['wmic', 'os', 'get', 'OSArchitecture'])
        os_arch = output.split()[1]
    else:
        output = subprocess.check_output(['uname', '-m'])
        if 'x86_64' in output:
            os_arch = '64-bit'
        else:
            os_arch = '32-bit'
    return str(os_arch).replace("b'", "").replace("'", "")

def os_check():
    uname = platform.uname()
    return uname.system