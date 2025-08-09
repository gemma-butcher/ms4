from PIL import Image, ImageDraw
import os

# Create a 32x32 camera icon
size = (32, 32)
img = Image.new('RGBA', size, (0, 0, 0, 0))  # Transparent background
draw = ImageDraw.Draw(img)

# Camera body color (brand color)
camera_color = '#369b95'

# Draw a simple camera shape
# Camera body
draw.rectangle([4, 8, 28, 24], fill=camera_color)

# Camera lens
draw.ellipse([10, 12, 22, 24], fill='white')
draw.ellipse([12, 14, 20, 22], fill='black')

# Viewfinder
draw.rectangle([8, 6, 12, 8], fill=camera_color)

# Flash
draw.rectangle([20, 6, 24, 8], fill='white')

# Save as ICO
favicon_path = os.path.join('static', 'img', 'favicon.ico')
img.save(favicon_path, format='ICO', sizes=[(16, 16), (24, 24), (32, 32)])

print(f"Favicon saved as {favicon_path}")
