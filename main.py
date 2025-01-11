from PIL import Image
import numpy as np

input_image = "input.jpg"
output_image = "output.jpg"

img = Image.open(input_image).convert("RGB")
pixels =  np.array(img)
flat_pixels = pixels.reshape(-1, 3)
sorted_pixels = np.array(sorted(flat_pixels, key=lambda x: (x[0], x[1], x[2])))    
sorted_image_array = sorted_pixels.reshape(pixels.shape)
sorted_image = Image.fromarray(np.uint8(sorted_image_array))
sorted_image.save(output_image)
