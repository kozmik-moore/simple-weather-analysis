from pathlib import Path
from os.path import join

# Directory paths
root_dir = Path('..')
data_dir = Path(join(root_dir, 'data'))
asset_dir = Path(join(root_dir, 'assets'))
notebook_dir = Path(join(root_dir, 'notebooks'))
script_dir = Path(join(root_dir, 'scripts'))

# File paths
raw_data_path = join(data_dir, 'raw_weather.csv')
processed_data_path = join(data_dir, 'processed_weather.csv')