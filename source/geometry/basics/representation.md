(chap-geometry-basics-representation)=
# 几何形状的表示方法

几何形状（geometric shape），指的是空间中的一组特定点所构成的集合。以平面空间为例，常见的几何形状包括直线、线段、正方形、圆形等；对于本章我们将讨论的三维欧几里得空间而言，基本的几何形状还包括立方体、四面体、球体等。然而，即使是最简单的几何形状（例如线段），构成它的点集一般也包含了无穷多个元素。因此，如何对几何形状进行表示、并将这种表示扩展为计算机能够存储和处理的形式，是可视计算领域最基本的问题之一。我们首先将沿着平面几何的背景知识，介绍如何从连续函数的角度对几何形状进行表示。

## 连续函数表示方法

在平面几何中，基本的几何基元可以很容易地通过函数来表示，这是因为构成它们的点集往往具有规则的边界，可以通过形式化的函数来刻画它们的表面。例如直线可以表示为 $\left\{(x,y)|Ax+By+C=0,x,y\in\mathbb{R}\right\}$，圆可以表示为 $\left\{(x,y)|x^2+y^2= R^2,x,y\in\mathbb{R}\right\}$。对于三维欧几里得空间中的几何形状，也同样可以使用类似的方式表达，例如我们可以将直线扩展到三维：

$$
\left\{(x,y,z)|Ax+By+Cz+D=0,x,y,z\in\mathbb{R}\right\}\,,
$$ (eq-geometry-basics-representation-line)

或者将圆扩展为球面：

$$
\left\{(x,y,z)|x^2+y^2+z^2= R^2,x,y,z\in\mathbb{R}\right\}\,.
$$ (eq-geometry-basics-representation-sphere)

一般地，对于更加复杂的几何形状 $M$，我们都可以用一个特定的连续函数 $\mathcal{S}_{M}\left(x,y,z\right)$ 来刻画它的表面 $\partial M$：

$$
\left\{(x,y,z)|\mathcal{S}_{M}\left(x,y,z\right)=0,x,y,z\in\mathbb{R}\right\}\,.
$$ (eq-geometry-basics-representation-func)

```{admonition} 练习
:class: tip

写出式 {eq}`eq-geometry-basics-representation-line` 和 {eq}`eq-geometry-basics-representation-sphere` 对应的 $\mathcal{S}_{M}$。
```

这样用连续函数来刻画复杂表面不仅能够准确地表示几何形状，更使得一系列数学工具能够被自然地引入，应用于几何形状的分析。微分几何就是一个经典的例子，对可微流形（differentiable manifold）上的微积分进行研究，在广义相对论和杨-米尔斯理论等物理理论中有重要的应用。用连续函数表示几何表面的基本思想，在后续章节中还会涉及，例如 {numref}`sec-geometry-representation-implicit_field` 中将介绍如何在计算机中用连续函数隐式地表征几何表面，以及 {numref}`sec-geometry-processing-smoothing` 中将从连续曲面的平均曲率流出发，实现一种对几何模型进行表面平滑的算法。

然而，连续函数的表示方法仍然具有局限。回想我们在曲线章节 {numref}`chap-getting-started-curves` 中绘制字母形状的例子（{numref}`fig-started-curves-letter`），即使是简单的字母“a”，其几何形状也已经很难用单一的函数来表示了。在三维空间中，几何形状往往更加复杂且不规则，而越复杂、越不规则的形状也就越难以用函数来进行刻画，这为几何形状在计算机中的存储和表示带来了困难。更重要的是，随着函数表达式本身变得复杂和冗长，函数求值的计算代价也会大大增加，这为几何形状的显示和处理也造成了不便。因此，正如 {numref}`sec-getting-started-curves-rasterization` 中对曲线进行光栅化所做的那样，为了将几何形状表示为计算机能够方便地存储和处理的形式，我们往往需要对上述连续表示进行离散化。

## 离散化方法

离散化（discretization），指的是将连续（continuous）的数据或函数转换为离散（discrete）形式的过程。我们将讨论两种基本的离散化手段，采样和线性拟合，分别对应点云和网格模型这两种三维表示方法。

### 采样

```{figure} fig/curve_sample.png
:name: fig-geometry-basis-curve_sample
:width: 90%

将曲线采样为一系列点。
```

采样方法基于这样一个最基本的思想：对于连续函数所表示的几何形状，构成它的点集往往具有无穷多个元素，因而必须依赖解析的表达式来隐式地描述；那么，如果从这个无穷点集中采样有限个点作为代表，便可以显式地通过枚举这些元素来表达形状本身。如 {numref}`fig-geometry-basis-curve_sample`，在一个复杂曲线上采样有限的点，便可以在保留形状信息的同时方便地储存形状数据。将这种方法应用在三维曲面上，采样得到的点便构成了点云（point cloud）这种三维表示方法。{numref}`sec-geometry-representation-voxel-pcd` 中我们将进一步讨论点云这种表示的实现与应用。

```{important}
形式上来说，点云是指一组三维空间中有限个坐标点的集合：$\left\{(x_i,y_i,z_i)|i=1,\dots,N\right\}$，这些点所描述的几何形状 $M$ 满足：对于点云中任意的点 $\left(x_i,y_i,z_i\right)$，有 $\mathcal{S}_{M}\left(x_i,y_i,z_i\right)=0$。
```

点云作为原本几何形状的采样结果，保留了原形状的一部分几何信息，这使得我们可以在点云上进行一些表面性质的计算，例如计算法向和曲率。然而，这种表示方式显然也具有局限性：采样总是伴随着信息的损失，点云也不例外。点云的采样密度决定了它对几何细节的表示能力。更重要的是，由于点云本身的非结构化和无序性，几何形状的拓扑关系往往是最容易在点云表示中变得模糊不清的，如 {numref}`fig-geometry-basis-curve_sample` 右图所示。这为基于点云的几何形状计算和处理带来了困难。

### 线性拟合

```{figure} fig/curve_linear_fit.png
:name: fig-geometry-basis-curve_linear_fit
:width: 90%

将几何形状的曲线边界（左）通过采样的方式（中），用一系列线段进行近似（右），从而得到线形拟合结果。
```

与采样不同，线性拟合方法仍然试图得到连续表示的几何形状，从而最大限度地保留原本形状的拓扑关系。如 {numref}`fig-geometry-basis-curve_linear_fit`，一个复杂曲线总是可以用若干线段来进行分段近似。线性拟合正是出于这样一种思想，它在采样方法的基础上，进一步保留了散点之间的连接关系，在相邻的散点之间使用线性插值来估计因采样不足而丢失的其他点。相较于直接采样，这种采样后使用线段进行分段近似的手段所得到的仍然是连续的几何表示，因此随着采样密度下降，其几何细节的丢失也更少。将这种线性拟合方法应用在三维曲面上，便得到了网格模型（mesh model）这种三维表示方法。{numref}`sec-geometry-representation-mesh` 和 {numref}`chap-geometry-processing` 中我们将进一步讨论网格模型这种表示的实现和应用；同时 {numref}`sec-geometry-reconstruction-surface` 还会介绍如何通过表面重建算法将点云转化为网格模型。

```{important}
形式上来说，网格模型是指一组三维空间中有限个坐标点构成的顶点集合 $\mathcal{V}=\left\{\mathbf{v}_i\right\}$ 和一组描述顶点连接关系的面集合 $\mathcal{F}=\left\{\mathbf{f}_i\right\}$ 所构成的表示，每个面 $\mathbf{f}_i$ 由 $K$ 个 $\mathcal{V}$ 中的顶点构成，表示这些顶点依次连接连成的 $K$ 边形面。这样的网格模型所描述的几何形状 $M$ 满足：对于任意 $\mathbf{f}_i$ 所表示的 $K$ 边形面，其上的任意一点 $\left(x_i,y_i,z_i\right)$ 都有 $\mathcal{S}_{M}\left(x_i,y_i,z_i\right)=0$。
```
