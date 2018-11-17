import sys
from cx_Freeze import setup, Executable



# build_exe_options = {"optimize": 2,
# "include_files": ["/usr/local/Cellar/qt/5.11.0/plugins/platforms/libqcocoa.dylib"]}
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['numpy','matplotlib','multiprocessing','PyQt5','xml','pycryptodome','web3','urllib3'],
        'excludes': ['Tkinter']  # Sometimes a little finetuning is needed
    }
}

executables = [
    Executable('Mainform.py', base=base)
]

setup(name='Mainform',
      version='0.1',
      description='Sample PyQt5 GUI',
      executables=executables,
      options=options
      )