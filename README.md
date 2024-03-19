![](https://github.com/SebastianCharmot/triangulation/blob/main/output.gif)

Given synchronized footage, `3d_final.py` can be used to generate the 3D reconstruction of the ball trajectory. To obtain synchronized footage, `get_sync_frames.py` contains useful helper functions to play two synched videos at the same time and save frames that are clear. 

First, make sure to obtain camera and stereo calibraton parameters. In my case, I have these stored in .npz files for convenience. To obtain the parameters, use `stereo_calibrate.py`. 

To get the best estimates for camera and stereo calibration, make sure that the checkerboard pattern is clearly visible and the corners are in high resolution. Also make sure to include plenty of angles as well as images where the checkerboard takes up the majority of the image. 

A helpful checklist of best practices for calibration can be found [here](https://calib.io/blogs/knowledge-base/calibration-best-practices). 