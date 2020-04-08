# Data

Find an explanation on the data and the references here.

## Overview

This folder contains three KITTI sample files, all corresponding to the same scene.
We use them for our demonstration in the [jupyter notebook](../example.ipynb).

### Where can I get the data?
The `.bin` files are directly from [KITTI Vision Bechmark Suite](http://www.cvlibs.net/datasets/kitti/).
These hold the point clouds itself, given in `[N, (x,y,z,remission)]`.
With `N` being the number of points.
The `.label` file is from [Semantic KITTI](http://semantic-kitti.org/) [3] and
contains point-wise annotations for semantics and instances for `N` points.
This annotations are valid for both point cloud files.

### Why two `.bin` files of the same scene?
The `raw` file is from the [Raw Data](http://www.cvlibs.net/datasets/kitti/raw_data.php) [1] and
the `ego` file is from the [Visual Odometry Benchmark](http://www.cvlibs.net/datasets/kitti/eval_odometry.php) [2].
The latter one is the ego-motion corrected version of the first.

### What is ego-motion correction?
Ego-motion correction means that all measurements in one 360 degree scan are
corrected towards one time stamp.
This is necessary since the ego-vehicle is moving over the time a
360 degree scan, also called "frame", is recorded.
To be correct, there is no such thing as a "frame" for LiDAR.
The measurements are a continuous stream of data where each measurement
"column" corresponds to a different time stamp.
The ego-motion correction can be conducted if the motion of the ego-vehicle is known.

### Why include the ego-motion corrected sample?
Using the [jupyter notebook](../example.ipynb), you man want to replace
`sample_raw.bin` with `sample_ego.bin`.
You will see, that the projection fails since the unfolding method cannot be
applied to ego-motion corrected data.
Keep in mind, that this method is not a general algorithm, it is rather a nice
engineering trick for raw KITTI data and raw KITTI data only.

### Which scene is it?
For our sample data, we used the first frame `000000` of sequence `00` of the Semantic KITTI dataset.
This is equivalent to the sequence and frame number in the Odometry benchmark dataset.
The corresponding raw sequence is called `2011_10_03_drive_0027`, the frame number is the same.

## References

[1] A. Geiger, P. Lenz, and R. Urtasun. _Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite_.
Conference on Computer Vision and Pattern	Recognition (CVPR). 2012

[2] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun. _Vision meets Robotics: The KITTI Dataset_.
International Journal of Robotics Research (IJRR). 2013

[3] J. Behley et al. _SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences_.
International Conference on Computer Vision (ICCV). 2019
