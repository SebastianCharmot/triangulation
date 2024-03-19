from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
from scipy import linalg
import numpy as np 
import matplotlib.pyplot as plt

# black 
uvs1 = [
    (528,547),(912,498),
    (761,982),(1458, 816)
]

# blue 
uvs2 = [
    (989,338),(1403,373),
    (335,749),(1124,926)
]

bounces_1 = [
    (1496,383),
    (1385,401),
    (1302,426),
    (1213,486),
    (1155,542),
    (1102,609),
    (1055,684),
    (1021,662),
    (997,557),
    (974,485),
    (956,423),
    (936,347),
    (920,347),
    (903,330),
    (889,328),
    (876,336),
    (864,362),
    (853,391),
    (843,436),
    (837,482),
    (829,545),
    (819,493),
    (812,444),
    (802,397),
    (793,362),
    (784,338),
    (779,326),
    (774,322),
    (768,329),
    (769,330),
    (782,316),
    (796,308),
    (811,312),
    (829,330),
    (845,357),
    (866,405),
    (890,465),
    (915,533),
    (942,627),
    (959,596),
    (976,539),
    (990,500),
    (1009,465),
    (1030,443),
    (1053,436),
    (1078,446),
    (1103,474),
    (1127,515),
    (1157,585),
    (1184,667),
    (1216,776),
    (1254,842),
    (1307,819),
    (1368,812),
    (1440,820),
    (1517,869)
]

bounces_2 = [
    (376,283),
    (529,296),
    (637,339),
    (729,389),
    (802,453),
    (863,524),
    (913,608),
    (945,548),
    (969,432),
    (990,334),
    (1010,268),
    (1032,213),
    (1052,176),
    (1073,159),
    (1091,155),
    (1107,169),
    (1121,194),
    (1132,232),
    (1146,282),
    (1159,331),
    (1166,396),
    (1180,335),
    (1192,272),
    (1202,222),
    (1213,181),
    (1224,155),
    (1235,139),
    (1245,136),
    (1252,144),
    (1251,143),
    (1236,128),
    (1216,122),
    (1198,131),
    (1176,150),
    (1154,189),
    (1129,242),
    (1101,314),
    (1073,401),
    (1039,517),
    (1023,466),
    (1003,400),
    (983,352),
    (963,320),
    (940,302),
    (918,298),
    (893,313),
    (867,353),
    (838,414),
    (812,503),
    (784,619),
    (761,761),
    (717,812),
    (644,806),
    (567,817),
    (474,859),
    (384,928)
]
 
uvs1 = np.array(uvs1)
uvs2 = np.array(uvs2)

mtx0 = np.load('camera_calibration_long_ass.npz')['mtx']
dist0 = np.load('camera_calibration_long_ass.npz')['dist']
mtx1 = np.load('camera_calibration_long_ass.npz')['mtx']
dist1 = np.load('camera_calibration_long_ass.npz')['dist']

R = np.load('stereo_calib_R_T_final.npz')['R']
T = np.load('stereo_calib_R_T_final.npz')['T']

#RT matrix for C1 is identity.
RT1 = np.concatenate([np.eye(3), [[0],[0],[0]]], axis = -1)
P1 = mtx0 @ RT1 #projection matrix for C1
 
#RT matrix for C2 is the R and T obtained from stereo calibration.
RT2 = np.concatenate([R, T], axis = -1)
P2 = mtx1 @ RT2 #projection matrix for C2

def DLT(P1, P2, point1, point2):
 
    A = [point1[1]*P1[2,:] - P1[1,:],
         P1[0,:] - point1[0]*P1[2,:],
         point2[1]*P2[2,:] - P2[1,:],
         P2[0,:] - point2[0]*P2[2,:]
        ]
    A = np.array(A).reshape((4,4))
    #print('A: ')
    #print(A)
 
    B = A.transpose() @ A
    U, s, Vh = linalg.svd(B, full_matrices = False)
 
    # print(f'Triangulated point: {Vh[3,0:3]/Vh[3,3]}')
    return Vh[3,0:3]/Vh[3,3]


def rotate(arr,x,y,z):
    r_x = np.array([[ 1, 0, 0],
                   [0 , np.cos(x), -np.sin(x)],
                   [ 0, np.sin(x), np.cos(x)]])
    
    r_y = np.array([[ np.cos(y),0, np.sin(y)],
                   [ 0, 1, 0],
                   [ -np.sin(y), 0, np.cos(y)]])
    
    r_z = np.array([[ np.cos(z), -np.sin(z), 0],
                   [ np.sin(z), np.cos(z), 0],
                   [ 0, 0, 1]])
    
    R = r_x@r_y@r_z
    translation = np.hstack((R,np.array([[40],
                                        [-40],
                                        [0]])))
    
    arr = np.array(arr)
    arr = arr.T
    
    translation = np.append(translation, np.array([[0,0,0,1]]),axis=0)

    arr = np.append(arr, 1)

    # print(arr.shape)
    # print(arr)

    # print(translation)

    rotated = arr@translation
    # print(rotated)
    # print(rotated[:-1])
    return rotated[:-1] + np.array([-40,
                                    -30,
                                    25])

# ROTATION 
# r_x = -np.pi/2
# r_y = np.pi -0.4
# r_z = np.pi*3/4

r_x =  np.pi/1.5
r_y = np.pi/15
r_z = np.pi/3.5

p3ds = []
for uv1, uv2 in zip(uvs1, uvs2):
    _p3d = DLT(P1, P2, uv1, uv2)
    _p3d = rotate(_p3d,r_x,r_y,r_z)
    p3ds.append(_p3d)

p3ds = np.array(p3ds)

print("adfasf")
print(p3ds)

# for r in p3ds:
#     rotate(r,0,0,0)

# p3ds = np.array(p3ds)
# print(p3ds.shape)

# print(p3ds)

frame = 187

print(len(bounces_1))
print(len(bounces_2))

for i in range(1,len(bounces_1)-1):
    bounces = []
    count = 0
    for uv1, uv2 in zip(bounces_1, bounces_2):
        if count >= i:
            break
        try:
            _p3d = DLT(P1, P2, uv1, uv2)
            _p3d = rotate(_p3d,r_x,r_y,r_z)
        except:
            print(uv1)
            print("uv2")
            print(uv2)
            # print(f"Frame {frame} not working")
        bounces.append(_p3d)
        # frame += 1
        count += 1
    bounces = np.array(bounces)

    plt.figure(figsize=(10,5))
    ax = plt.axes(projection='3d')
    ax.plot_trisurf(p3ds[:4][:,0], p3ds[:4][:,1], p3ds[:4][:,2], alpha=0.5)
    ax.scatter3D(p3ds[:,0], p3ds[:,1], p3ds[:,2],color="b")
    ax.scatter3D(bounces[:,0], bounces[:,1], bounces[:,2],color="r")

    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')

    ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1.59, 1.2, 1, 1]))

    plt.savefig(f'footage/bounce_final_2_reconstructed/{frame + i-1}.png', dpi=300)
    # plt.show()footage/bounce_final_2_reconstructed

# print(p3ds[:5][:,0])

# print(rotate(p3ds,0,0,0))