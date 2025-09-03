import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s:]: %(message)s:')
# logging.info('Hello everyone. Welcome to the project')
list_files=[
    'src/__init__.py','src/helper.py','src/prompt.py',
    '.env',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'app.py'
]

for filepath in list_files:
    print(filepath)
    file_path = Path(filepath)
    file_dir,filename = os.path.split(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            # pass
            logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f'File: {filepath} already exists')
