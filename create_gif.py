import os
import imageio

# Folder containing PNGs
folder = 'footage/to_gif'

# Output files
gif_file = 'output.gif'
mp4_file = 'output.mp4'

# Frame rate (frames per second)
frame_rate = 3

# Get the list of PNG files in the folder, sorted numerically
png_files = sorted([f for f in os.listdir(folder) if f.endswith('.png')], key=lambda x: int(x.split('.')[0]))

# Create GIF
with imageio.get_writer(gif_file, mode='I', fps=frame_rate) as writer:
    for filename in png_files:
        image = imageio.imread(os.path.join(folder, filename))
        writer.append_data(image)

# Create MP4
with imageio.get_writer(mp4_file, mode='I', fps=frame_rate) as writer:
    for filename in png_files:
        image = imageio.imread(os.path.join(folder, filename))
        writer.append_data(image)

print(f'GIF file "{gif_file}" and MP4 file "{mp4_file}" created successfully.')
