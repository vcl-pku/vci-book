# 本章小结

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
