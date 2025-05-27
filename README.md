## Reinhard Color Transfer 
[![PyPI version](https://badge.fury.io/py/reinhard-color-transfer.svg)](https://badge.fury.io/py/reinhard-color-transfer)

An implementation of ["Color transfer between images" by E. Reinhard et. al."](https://doi.org/10.1109/38.946629)

## Installation

You can install the package using `pip`:

```bash
pip install reinhard-color-transfer
```


## Usage

```python
from PIL import Image
from reinhard_color_transfer import transfer_color

source_image = Image.open("path/to/source/image")
color_image = Image.open("path/to/color/image")
alpha = 0.5 # Amount of color transfer
result_image: Image.Image = transfer_color(source_image, color_image, alpha)
```

Following is a visualization of result using sample images:

![Color Transfer Visualization](https://raw.githubusercontent.com/dariush-bahrami/reinhard_color_transfer/refs/heads/master/assets/Color-Transfer-Visualization.jpg)
