from pathlib import Path
from os.path import join

# Directory paths
root_dir = Path('..')
data_dir = Path(join(root_dir, 'data'))
assets_dir = Path(join(root_dir, 'assets'))
code_dir = Path(join(root_dir, 'code'))
products_dir = Path(join(root_dir, 'products'))

# File paths
raw_data_path = join(data_dir, 'raw_weather.csv')
processed_data_path = join(data_dir, 'processed_weather.csv')