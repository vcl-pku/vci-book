(sec-geometry-processing-smoothing)=
# 网格平滑

随着三维扫描和曲面重建技术的发展，得到实体表面的多边形网格表示已经不是难事，但所得到的表面往往包含噪声。在形状设计领域，散点拟合、形状光滑、纹理映射等应用都有对平滑曲面的极大需求。故产生了网格平滑这一个研究点。

网格平滑（smoothing）也称为网格降噪（denoising）。降噪一般是指去掉噪音（高频信息）保留整体形状（低频信息）从而获得一个相对光滑的几何模型的过程，比如去掉扫描或者采集数据因为误差或者其他原因导致的噪声。平滑在统计学中指的是通过一个近似函数对输入数据进行较好的拟合，从而保留重要的模式，去掉噪音或者其他不重要的信息。如图 {numref}`fig-geometry-processing-smoothing_teaser` 所示，我们可以对一个具有噪音的初始扫描人脸进行平滑处理。实际上，噪音在几何上是很难判定的，并不是高频的就一定是噪音，比如棱角分明的几何体的顶点。因此，不严格的对噪音的定义会给算法的设计带来许多困难。本部分我们主要介绍拉普拉斯平滑（Laplacian smooting）。

```{figure} fig/smoothing_teaser.png
:name: fig-geometry-processing-smoothing_teaser
:width: 60%

左边是带有噪音的三维扫描的人脸。右边上面一行表示原始的几何以及平均曲率，下面表示经过降噪后的几何和平均曲率 {cite}`Duarte2017`。
```

我们可以借助扩散流的数学模型来帮助理解，它常被用来平滑给定的时空信号 $f(x,t)$。很多常见的物理现象可以用扩散流解释，比如热量从高温处逐渐往低温处扩散的过程，可以看作是一个扩散流的过程。扩散流公式写作：

$$
  \frac{\partial f(x,t)}{\partial t}=\lambda 
  \Delta f(x,t)
$$ (eq-geometry-processing-smoothing1)

扩散流的过程应用到网格平滑上，也就是将带噪音的顶点坐标理解成杂乱分布的热量。随着扩散过程的进行，热量分布趋于平衡，对应着顶点构成的表面趋于平滑。
因此，我们可以通过定义在表面上的拉普拉斯算子，利用扩散流模型，对表面进行平滑。首先，我们需要对公式中的时空信息进行离散化。

对于空间上的离散化，我们依旧把函数值离散为网格顶点上的值，记 $\mathbf f(t)=(f(v_1,t),\,...,\,f(v_n,t))^\mathrm T$，于是对每个顶点有：

$$
  \frac{\partial f(v_i,t)}{\partial t}   = \lambda 
  \Delta f(v_i,t), i=1,...,n.
$$ (eq-geometry-processing-smoothing2)

写成矩阵形式为 $\partial \mathbf f(t)/\partial t = \lambda L\mathbf f(t)$。

对于时间上的离散化，我们可以采用均匀间隔的时间步长 $h$ 将时间划分为若干段 $(0,h,2h,\,\dots,\,t,t+h,t+2h,\,\dots)$，于是通过有限差分可以将偏微分用差值来近似，即：

$$
  \frac{\partial \mathbf f(t)}{\partial t}   = \frac{\mathbf f(t+h)-\mathbf f(t)}{h}
$$ (eq-geometry-processing-smoothing3)

这种差分格式被称为显式欧拉，它的形式可以改写为：

$$
  \mathbf f(t+h)=\mathbf f(t)+h\frac{\partial \mathbf f(t)}{\partial \mathbf t} = \mathbf f(t)+h\lambda L\mathbf f(t)
$$ (eq-geometry-processing-smoothing4)

此式给出了经过时空离散化后函数值的迭代更新方法，每经过一个 $h$ 时间步，用此式更新每个顶点上的函数值，直至达到设定的迭代停止条件。

在上式中代入第 $k$ 次更新后的顶点坐标 $f(v_i, kh)=\mathbf x_i^{(k)}$，我们就可以得到拉普拉斯平滑在第 $k+1$ 步的更新公式：

$$
  \mathbf x_i^{(k+1)} \leftarrow \mathbf x_i^{(k)}+h\lambda  \Delta \mathbf x_i^{(k)}
$$ (eq-geometry-processing-smoothing5)

在两种不同的拉普拉斯算子下，可以得到不同的平滑效果。在取余切算子时，由于满足 $\Delta \mathbf x=-2H\mathbf{n}$ 公式，于是所有顶点将沿着平均曲率定义的方向移动，因此也称为平均曲率流（mean curvature flow）。{numref}`fig-geometry-processing-curvature_flow` 展示的就是对模型进行平均曲率平滑之后的效果。

```{figure} fig/curvature_flow.png
:name: fig-geometry-processing-curvature_flow
:width: 60%

左：初始网格的曲率可视化；中：平均曲率平滑迭代 10 次后的曲率；右：平均曲率平滑迭代 100 次后的曲率。
```

在取均匀算子的情况下，因为没有考虑面的信息，只考虑了顶点位置，那么平滑不会沿着曲率方向，而是会往重心方向移动，即将每个顶点往相邻顶点的平均位置移动。这个过程等价于某种能量函数最小化，平衡状态下的形状应该是所有边长度相同。这种方式定义的拉普拉斯算子不反映网格形状，可能导致局部几何特征的失真。
从 {numref}`fig-geometry-processing-camparison_laplace` 中可以看出，余切算子能更好地保持几何特征，而均匀算子导致了三角网格切向的松弛。

```{figure} fig/camparison_laplace.png
:name: fig-geometry-processing-camparison_laplace
:width: 60%

不同算子在网格平滑的过程中对几何特征保持的不同程度。
```

