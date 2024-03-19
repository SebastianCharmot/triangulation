from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
from scipy import linalg
import numpy as np 
import matplotlib.pyplot as plt

uvs1 = [[954,353],[1486,373],
        [453,787],[1674,917]]
uvs2 = [[560,322],[1085,314],
        [385,852],[1598,765]]

uvs1 = [(954,353),(1486,373),
        (453,787),(1674,917),
        
        (727,413),(730,478),(797,485),
        (1628,450),(1542,525),(1622,526)]

uvs2 = [(560,322),(1085,314),
        (385,852),(1598,765),
        
        (422,400),(430,473),(507,471),
        (1313,376),(1246,450),(1308,446)]


bounces_1 = [(1071,175),(1056,226),(1042,275),(1026,338),
             (1010,406),(1002,470),(993,549),(975,508),(954,461)]

bounces_2 = [(823,127),(811,177),(805,234),(796,298),
             (791,363),(785,437),(779,521),(768,479),(755,434)]
 
uvs1 = np.array(uvs1)
uvs2 = np.array(uvs2)

mtx0 = np.load('camera_calibration_long_ass.npz')['mtx']
dist0 = np.load('camera_calibration_long_ass.npz')['dist']
mtx1 = np.load('camera_calibration_long_ass.npz')['mtx']
dist1 = np.load('camera_calibration_long_ass.npz')['dist']

R = np.load('stereo_calib_R_T.npz')['R']
T = np.load('stereo_calib_R_T.npz')['T']

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
 
    print('Triangulated point: ')
    print(Vh[3,0:3]/Vh[3,3])
    return Vh[3,0:3]/Vh[3,3]

p3ds = []
for uv1, uv2 in zip(uvs1, uvs2):
    _p3d = DLT(P1, P2, uv1, uv2)
    p3ds.append(_p3d)
p3ds = np.array(p3ds)

p3ds = np.array(p3ds)
print(p3ds.shape)

print(p3ds)

bounces = []
for uv1, uv2 in zip(bounces_1, bounces_2):
    _p3d = DLT(P1, P2, uv1, uv2)
    bounces.append(_p3d)
bounces = np.array(bounces)

ax = plt.axes(projection='3d')
ax.plot_trisurf(p3ds[:4][:,0], p3ds[:4][:,1], p3ds[:4][:,2], alpha=0.5)
ax.scatter3D(p3ds[:,0], p3ds[:,1], p3ds[:,2],color="b")
ax.scatter3D(bounces[:,0], bounces[:,1], bounces[:,2],color="r")
plt.show()

print(p3ds[:5][:,0])