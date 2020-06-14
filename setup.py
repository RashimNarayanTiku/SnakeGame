import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("pygame1.py")]

cx_Freeze.setup(
    name='SnakeGame',
    options={"build_exe":{"packages":["pygame"], "include_files":["apple.png","snakeHead.png"]}},
    executables = executables
    )