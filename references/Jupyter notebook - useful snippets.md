---
tags:
  - snippet
---
# Notebook setup

## Standard boilerplate
Auto-reload for working modules:
```python
%load_ext autoreload
%autoreload 2
```

```python
import os
import sys
from pathlib import Path
import datetime as dt

import pandas as pd
import geopandas as gpd


pd.set_option('display.max_columns', None)

# BEST PRACTICE - put this in your path & file definitions cell
today = dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d')

```

## Other common setup
Load python modules into the notebook
```python
import os  
import sys  
module_path = os.path.abspath(os.path.join(r'../src'))  # use raw text, not a Path object
sys.path.insert(0, module_path)
```

Set up date
```python
import datetime as dt
today = dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d')
```

Show current python path and environment
```python
import sys
is_venv = sys.prefix != sys.base_prefix 
print(f"Inside virtual env: {is_venv}") 
print(f"Python path: {sys.executable}")
print(f"Environment path: {sys.prefix}")
```
...
## Pandas tips
Print all dataframe columns or rows - scrollable:
```python
pd.set_option('display.max_columns', None)

# These two together will allow up to 50 rows to be printed:
pd.set_option('display.max_rows', 50)
pd.set_option('display.min_rows', None)

# Using context manager for temp setting
with pd.option_context('display.max_rows', None):
    display(df)

```


# File exporting

```python
# Define some dict
layer_dict = {}

# Function to check for object (gdf) with name in dict, add for future output
def stage_for_output(df, layer_name, replace=False):
    def check_and_add(layer_dict, layer_name, gdf):
        assert isinstance(gdf, gpd.geodataframe.GeoDataFrame), 'Layer must be a geodataframe for now.' # could maybe allow df as well
        layer_dict[layer_name] = gdf
    
    if layer_name in layer_dict:
        if replace:
            print(f'Updating layer for gdb: {layer_name}')
            check_and_add(layer_dict, layer_name, gdf)
        else:
            print(f'Layer "{layer_name}" already slated for gdb save')
    else:
        print(f'Staging layer for gdb write: {layer_name}')
        check_and_add(layer_dict, layer_name, gdf)

    return
```

### Figure Functions
```python
def print_png_fig(name, 
				fig=None, 
				output_dir=figures_dir, 
				transparent=False):
    if fig is None:
        fig = plt.gcf()
    else:
        assert isinstance(fig, mpl.figure.Figure), '"Fig" must be matplotlib figures.'
        plt.figure(fig)
    fig_path = os.path.join(output_dir, name) + '.png'
    print(f'Saving figure:\n\t{fig_path}')
    plt.savefig(fig_path, bbox_inches='tight', dpi=400, transparent=transparent)
    
def print_svg_fig(name, 
				fig=None,
				output_dir=os.path.join(figures_dir,'svg'),
				transparent=False):
    if fig is None:
        fig = plt.gcf()
    else:
        assert isinstance(fig, mpl.figure.Figure), '"Fig" must be matplotlib figures.'
        plt.figure(fig)
    fig_path = os.path.join(output_dir, name) + '.svg'
    print(f'Saving figure:\n\t{fig_path}')
    plt.savefig(fig_path, bbox_inches='tight', transparent=transparent)
```