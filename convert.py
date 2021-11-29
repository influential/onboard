import PyInstaller.__main__
import os

name = 'onboard'

PyInstaller.__main__.run([  
     f'-n {name}',
     '--onefile',
     '--windowed',
    #  os.path.join(os.getcwd(), 'on.py'),
    'on.py'                                      
])