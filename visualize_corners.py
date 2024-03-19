import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_path = "footage/blue_bounce_final_2/187.png"
img = mpimg.imread(image_path)

# plt.imshow(img)

# # Double checked labelled points 
# pixel_coordinates_blue = [(560,322),(1085,314),
#                     (385,852),(1598,765),
                    
#                     (422,400),(430,473),(507,471),
#                     (1313,376),(1246,450),(1308,446),
                    
#                     (888,460)] #blue
# pixel_coordinates = [(1104,296), (206,584), (1000,884)] #black
# pixel_coordinates = [(954,353),(1486,373),
#                      (453,787),(1674,917),
                     
#                      (727,413),(730,478),(797,485),
#                      (1628,450),(1542,525),(1622,526),
                     
#                      (1150,504)] #black

pixel_coordinates_blue = [
    (989,338),(1403,373),
    (335,749),(1124,926)
]

pixel_coordinates = [
    (528,547),(912,498),
    (761,982),(1458, 816)
]

pixel_coordinates = pixel_coordinates_blue

# Separate the x and y coordinates
# x_coords, y_coords = zip(*pixel_coordinates)

# # Plot the red "+" signs
# plt.scatter(x_coords, y_coords, marker='+', color='red')

# for x, y in zip(x_coords, y_coords):
#     plt.text(x, y, f'({x}, {y})', fontsize=8, ha='right', va='bottom', color='red')

# plt.savefig('blue_corners_final.png')

# plt.show()

def show():
    l = [frame for frame in range(187,243)]
    for i in l:
        image_path = f"footage/black_bounce_final_2/{i}.png"
        img = mpimg.imread(image_path)

        plt.imshow(img)
        plt.show()

show()