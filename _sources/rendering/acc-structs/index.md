(chap-rendering-acc-structs)=
# 空间加速结构

为了实现光线追踪等全局光照算法，我们需要中计算射线与场景中物体表面的第一个交点。一个典型渲染场景所涉及到的三角形面片数量是数以百万计的，线性遍历每个三角形的时间代价无疑难以承受。为此，我们需要引入空间加速结构（spatial acceleration structures），以尽可能压缩光线求交的时间。

空间加速结构是一类布设于几何基元（以三角形面片为主）之上的数据结构，常见的空间加速结构包括层次包围体、KD 树和均匀网格等，它们各自具有不同的优势。本章将回顾上述三种空间加速结构的基本原理，说明其用于加速光线追踪的方法。值得注意的是，这些结构不仅被广泛用于渲染中，也会对后续所涉及的动态生成部分产生深远的影响。

```{toctree}
:maxdepth: 2

bvh
kd-trees
grids
summary
```