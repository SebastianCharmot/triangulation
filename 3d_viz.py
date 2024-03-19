import matplotlib.pyplot as plt
from PIL import Image

# File paths for the images in three different directories
dir2 = 'footage/black_bounce_final_2'
dir3 = 'footage/bounce_final_2_reconstructed'
dir1 = 'footage/blue_bounce_final_2'

frame = 187

for i in range(56):
    filename = f'{frame + i}.png'

    # Load images
    img1 = Image.open(f'{dir1}/{filename}')
    img2 = Image.open(f'{dir2}/{filename}')
    img3 = Image.open(f'{dir3}/{filename}')

    scaling_factor = 0.5  # You can adjust this value as needed

    # Resize img1 and img2 by scaling_factor
    img1 = img1.resize((int(img1.width * scaling_factor), int(img1.height * scaling_factor)))
    img2 = img2.resize((int(img2.width * scaling_factor), int(img2.height * scaling_factor)))

    # Create a 2x2 grid of subplots
    # fig, axs = plt.subplots(2, 2)

    # Plot images from dir1 and dir2 on the first row
    plt.subplot(2, 1, 1).imshow(img3)
    plt.subplot(2, 1, 1).set_title(f'3D Reconstruction')
    plt.subplot(2, 1, 1).axis('off')

    plt.subplot(2, 2, 3).imshow(img2)
    plt.subplot(2, 2, 3).set_title(f'Frame {frame+i} from Camera One')
    plt.subplot(2, 2, 3).axis('off')

    # Plot image from dir3 on the second row
    plt.subplot(2, 2, 4).imshow(img1)
    plt.subplot(2, 2, 4).set_title(f'Frame {frame+i} from Camera Two')
    plt.subplot(2, 2, 4).axis('off')

    # Hide the empty subplot in the second row
    # axs[1, 1].axis('off')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plot as a PNG file
    plt.savefig(f'footage/to_gif/{frame+i}.png', dpi=300)

    # Show the plot
    # plt.show()