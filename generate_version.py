import os
from datetime import datetime

import toml

with open('pyproject.toml', 'r') as file:
    pyproject_data = toml.load(file)

version = pyproject_data['project']['version']
version_date = datetime.now().strftime('%Y%m%d%H%M%S')
version = f'{version}-{version_date}'
version_file_path = os.path.join('wallet', 'version.py')
with open(version_file_path, 'w') as version_file:
    version_file.write(f'__version__ = "{version}"\n')

print(f'Generated {version_file_path} with version {version}')
