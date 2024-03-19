![](https://github.com/SebastianCharmot/triangulation/blob/main/output.gif)

Given synchronized footage, 3d_final.py can be used to generate the 3D reconstruction of the ball trajectory. To obtain synchronized footage, get_sync_frames.py contains useful helper functions to play two synched videos at the same time and save frames that are clear. 

First, make sure to obtain camera and stereo calibraton parameters. In my case, I have these stored in .npz files for convenience. To obtain the parameters, use stereo_calibrate.py. 