(chap-geometry-reconstruction)=
# 几何重建

```{figure} fig/teaser.png
:name: fig-geometry-reconstruction-teaser
:width: 96%

现实场景的几何重建。A：基于 COLMAP 进行室外场景点云重建。B：使用 KinectFusion 对桌面进行表面重建。C：使用 BundleFusion 对室内场景进行表面重建。
```

几何重建旨在对现实世界的物体或场景进行建模，研究如何恢复目标物体或场景的三维几何形状，如 {numref}`fig-geometry-reconstruction-teaser` 所示。作为几何建模的重要手段，几何重建是计算机视觉和计算机图形学中的一个经典问题。它不仅是实现虚拟现实、增强现实、和无人驾驶等技术的基础，在机器人领域中也有重要的应用价值，是实现机器人定位和导航的关键技术。经典的几何重建依赖特殊的传感设备（如深度相机）来直接感知三维空间中的几何形状，将目标对象表示为一组点云（point cloud）。形式上来说，点云是指一组三维空间中坐标点的集合：$\left\{(x_i,y_i,z_i)|i=1,\dots,N\right\}$。本章我们将围绕点云这一三维表示方法（3D representation），介绍从传感器获取点云的原理、不同区域间的点云如何进行融合配准，从而揭示几何重建过程中的算法细节；此外，本章还将介绍将点云转化为网格模型的后处理算法，包括表面提取和形状拟合，从而在两种不同的三维表示方法之间建立联系。

```{toctree}
:maxdepth: 2

point-cloud
surface
fit
summary
```
