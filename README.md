# pixel sorter

Organizing books by color is like sorting the pixels in an image by color.

~ Paul Graham

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x pxlsrt
```

## Usage

```bash
./pxlsrt <input_image> [output_image]
```

- `<input_image>`: Path to the input image file. (Required)
- `[output_image]`: Path to save the output image file. Optional. Defaults to `output.jpg` if not provided.

### Examples

1. Specify both input and output image paths:

```bash
./pxlsrt input.jpg output.jpg
```

2. Specify only the input image path (output saved as `output.jpg`):

```bash
./pxlsrt input.jpg
```
