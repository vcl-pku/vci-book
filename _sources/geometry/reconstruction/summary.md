# 本章小结

本章介绍了三维几何重建中的关键技术，涵盖了从数据获取到模型优化的完整流程。首先，我们探讨了如何通过深度相机（包括结构光、ToF 和立体视觉三种类型）从现实世界中采集三维数据，并将其表示为点云。由于单次采集往往无法覆盖整个场景，我们介绍了迭代最近点（ICP）算法，用于将不同视角下的局部点云配准、融合成一个完整的整体。

接着，我们讨论了点云的后处理技术。点云本身是非结构化的，为了更好地进行后续的几何处理和渲染，需要将其转换为具有明确拓扑连接的网格模型。本章介绍了两种主流的表面重建方法：德劳内三角剖分和泊松表面重建。德劳内三角剖分直接连接点云中的点来构建网格，力求生成的三角形“均匀”；而泊松表面重建则通过一个间接的流程，先从带有法向量的点云估计一个指示函数，再利用行进立方体算法提取等值面，这种方法对噪声数据具有更好的鲁棒性。

最后，本章还介绍了从点云中提取几何基元（如平面、球面）的模型拟合技术。我们以平面拟合为例，展示了如何通过最小二乘法求解理想情况下的模型参数。更重要的是，我们详细阐述了随机抽样一致性（RANSAC）算法，它能够从包含大量噪声和无关点的复杂数据中，鲁棒地识别出符合特定模型的“内点”，从而实现精确的几何拟合。

<!-- ## 扩展阅读

1. [ICP 可视化](https://laempy.github.io/pyoints/tutorials/icp.html#References)，[ICP 算法改进](https://gfx.cs.princeton.edu/proj/iccv05_course/iccv05_icp_gr.ppt)；

2. [德劳内三角化的2D可视化[1]](https://cartography-playground.gitlab.io/playgrounds/triangulation-delaunay-voronoi-diagram/)[[2]](https://travellermap.com/tmp/delaunay.htm)；
    
3. [行进立方体算法的可视化](https://www.willusher.io/webgl-marching-cubes/)；

4. [模型拟合的可视化](https://github.com/leomariga/pyRANSAC-3D/tree/Animations)。 -->

## 思考题

1. 事实上，{numref}`chap-geometry-reconstruction-icp` 中介绍的 ICP 算法也可以与 {numref}`chap-geometry-reconstruction-ransac` 中介绍的 RANSAC 算法结合。其具体流程是怎样的？这样做有什么好处？

2. 泊松表面重建采用了相对间接的方式来完成点云到网格的转换，相比于德劳内三角剖分这种直接连接点云得到网格的方式有什么好处？


## 习题

1. 证明式 {eq}`eq-geometry-reconstruction-fit6`。

2. 类似 {numref}`chap-geometry-reconstruction-plane-fit` 中对平面进行的拟合，写出对球面进行拟合的流程（设球心为 $C$、半径为 $R$）。

## 参考文献

```{bibliography} ref.bib
```
