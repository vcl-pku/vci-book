(sec-animation-fluids-eulerian)=
# 欧拉网格流体

使用拉格朗日法进行流体模拟十分直观、便捷且高效，但其对物理模型做了过于简化的处理，因此模拟结果往往不够准确也不够真实。欧拉法则将流体视为一种连续介质，并且由于纳维-斯托克斯方程本身的形式就是欧拉视角，欧拉法也能够更自然地对其进行处理。本节我们会介绍如何使用欧拉法模拟自由表面流体，与上一节不同，本节将会更加系统地对流体的物理方程进行离散化，并更加严格地遵循 {numref}`sec-animation-fluids-physics` 中介绍的分裂法进行求解。

## 空间离散化

本节中我们考虑的流体场景与上一节相同（见{numref}`fig-animation-fluids-sph_fluid_setting`），不同的是我们现在将整个容器内的空间均匀划分成正方体网格，每个单元格的边长为 $\Delta x$。场景中包含的水、固体、空气三种元素，以及各物理量，都存储在网格当中；接下来我们首先介绍网格本身的结构，并依次说明这些信息都是如何存储的。

### 标记网格

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-fluids-mac_grid
:width: 100 %

```{image} fig/animation-fluids-mac_grid_2d.png
:alt: 二维标记网格
```

```{image} fig/animation-fluids-mac_grid_3d.png
:alt: 三维标记网格
```

标记网格。$\phi(\boldsymbol x)$ 与 $p(\boldsymbol x)$ 均为标量场；$\boldsymbol u(\boldsymbol x)$ 为一与定义域维度相同的向量场，二维情形下记 $\boldsymbol u(\boldsymbol x)=\begin{bmatrix}u(\boldsymbol x)\\v(\boldsymbol x)\end{bmatrix}$，三维情形下记 $\boldsymbol u(\boldsymbol x)=\begin{bmatrix}u(\boldsymbol x)\\v(\boldsymbol x)\\w(\boldsymbol x)\end{bmatrix}$。下标反映了取值点的位置，假设网格最左下角的格子中心位于原点，则三维下标 $(a,b,c)$ 对应于位置 $\boldsymbol x_{a,b,c}=\begin{bmatrix}a\Delta x\\b\Delta x\\c\Delta x\end{bmatrix}$，二维同理。
````

标记网格（Marker-And-Cell grid，MAC grid）是一种设计十分巧妙的网格，充分利用了每个单元格的顶点、面和体来存储不同的量，使得它们之间能够很协调地配合在一起求解流体方程。{numref}`fig-animation-fluids-mac_grid` 展示了二维和三维的标记网格，其中标量场 $\phi(\boldsymbol x)$、向量场 $\boldsymbol u(\boldsymbol x)$、标量场 $p(\boldsymbol x)$ 分别存储在顶点上、面上和格子内部，存储在面上的量一般标记在面的中心，存储在格子内部的量一般标记在格子中心。

不难发现，我们可以根据需要把不同的标量场存储在格子顶点或者格子内部，存储的值分别是标量场在格子顶点或中心处的取值。而对于流体模拟中的向量场，其维度一般都等于定义域的维度（如速度场、压强梯度），我们恰好可以将其每个分量分别存储在格子的每个面上（二维格子的面就是边）——每个面上存储向量场在该面中心处的取值与该面垂直的分量。

### 流体场景的表示

借助标记网格，我们可以使用水平集方法（level set method）表示水的自由表面，尽管这里用了一个新词，其实我们在 {numref}`sec-geometry-representation-implicit_field-sdf` 学习有符号距离场的时候就已经熟悉了这个概念。水平集方法使用一个标量场 $\phi(\boldsymbol x)$ 来隐式地定义一个几何体，对于空间中任意一点 $\boldsymbol x$：
- 若 $\phi(\boldsymbol x)>0$，则 $\boldsymbol x$ 在几何体的外部；
- 若 $\phi(\boldsymbol x)=0$，则 $\boldsymbol x$ 在几何体的表面上；
- 若 $\phi(\boldsymbol x)<0$，则 $\boldsymbol x$ 在几何体的内部。

换言之，几何体的表面就是 $\phi$ 的 $0$ 等值面，又称为 $\phi$ 的 $0$ 水平集，故此方法名为水平集方法。不难发现，我们可以直接把这里的 $\phi$ 取成我们要表示的几何体的有符号距离场，这样就可以使用 {numref}`sec-geometry-representation-implicit_field-sdf-grid` 中介绍的方法得到一个网格化表示的标量场，存储在标记网格的顶点上。因此，在初始化流体场景时，我们就可以将水在初始时的形状转换成水平集表示保存在标记网格当中了，在后续的模拟时间步中，我们会进一步演化这个水平集表示，以实现水的几何动态。

接下来，为了方便后续的数值求解，我们还需要将整个场景进行体素化表示（voxelize），即确定标记网格中每一个格子是属于固体、水还是空气。场景中的固体边界已知，我们可以求出它的有符号距离场，随后依次判断每个格子的中心处有符号距离场的正负性，并将负的网格标记为固体。对于剩下的格子我们要分出包含水与不包含水两类，因此只需要检查所有顶点上的 $\phi$ 值，如果有存在小于 $0$ 的即标记为水，否则标记为空气。{numref}`fig-animation-fluids-voxelize` 展示了将{numref}`fig-animation-fluids-sph_fluid_setting` 中所示场景体素化后的大致结果。

```{figure} fig/animation-fluids-voxelize.png
:width: 50 %
:name: fig-animation-fluids-voxelize

{numref}`fig-animation-fluids-sph_fluid_setting` 体素化成 $16\times 16$ 的网格后的结果。固体、水和空气分别对应于灰色格子、蓝色格子和白色格子。
```

在接下来的讨论中，我们只考虑二维情形，三维的推广留给读者作为练习。

### 速度场与速度散度

速度场的维度恰好等于定义域的维度，因此我们可以将其储存在标记网格的面上。记速度场为 $\boldsymbol u(\boldsymbol x)$，其保存在标记网格上的两个分量为 $u_{i\pm\frac 12,j}$ 和 $v_{i,j\pm\frac 12}$，则根据散度的表达式

$$
\nabla\cdot\boldsymbol u(\boldsymbol x)=\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)(\boldsymbol x)
$$

可以得到离散化的散度

$$
(\nabla\cdot\boldsymbol u)_{i,j}=\frac{u_{i+\frac 12,j}-u_{i-\frac 12,j}}{\Delta x}+\frac{v_{i,j+\frac 12}-v_{i,j-\frac 12}}{\Delta x}=\frac 1{\Delta x}\left(u_{i+\frac 12,j}-u_{i-\frac 12,j}+v_{i,j+\frac 12}-v_{i,j-\frac 12}\right)。
$$ (animation-fluids-velocity_divergence)

这里我们使用有限差分来近似导数，由于我们将速度的分量保存在标记网格的面上，每个分量的导数恰好落在网格的中心，因此得到的离散化的散度场恰好定义在标记网格的格点中心。

我们还可以借助格林公式（三维中对应于高斯公式）来理解式 {eq}`animation-fluids-velocity_divergence`。对于一个由分段光滑的简单闭曲线围成的有界闭区域 $\Omega$，根据格林公式有

$$
\iint_\Omega\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)\mathrm dA=\oint_{\partial\Omega}-v(x,y)\mathrm dx+u(x,y)\mathrm dy
$$ (animation-fluids-green)

成立；其中 $\mathrm dA$ 表示微元的面积，$\partial\Omega$ 上的线积分取逆时针方向。我们可以形象地理解格林公式：向量场的散度在区域内部的积分等于在边界上外向法向分量的积分，若把向量场想象成速度场，则散度在内部的积分即为边界上观测到的“流出”区域的量。将式 {eq}`animation-fluids-green` 中的 $\Omega$ 取成位于 $(i,j)$ 的格子，并且假设格子内部的散度为常量、格子面上的速度值也为常量，那么等号左侧变为 $(\Delta x)^2(\nabla\cdot\boldsymbol u)_{i,j}$，等号右侧的线积分将分成正方形的下、右、上、左四条边（注意积分方向）：

$$
\oint_{\partial\Omega}-v(x,y)\mathrm dx+u(x,y)\mathrm dy=\Delta x\left(-v_{i,j-\frac 12}+u_{i+\frac 12,j}+v_{i,j+\frac 12}-u_{i-\frac 12,j}\right)，
$$

再将等式两边同时除以 $(\Delta x)^2$，即可得到式 {eq}`animation-fluids-velocity_divergence`。

### 压强场与压强梯度

我们将压强场存储在标记网格的格子中心。记压强场为 $p(\boldsymbol x)$，其保存在格子中心的值为 $p_{i,j}$，则可以分别求出其关于两个坐标的导数：

$$
\begin{aligned}
\left(\frac{\partial p}{\partial x}\right)_{i+\frac 12,j}=\frac{p_{i+1,j}-p_{i,j}}{\Delta x}，\\
\left(\frac{\partial p}{\partial y}\right)_{i,j+\frac 12}=\frac{p_{i,j+1}-p_{i,j}}{\Delta x}。
\end{aligned}
$$ (animation-fluids-pressure_gradient)

不难发现，除了标记网格最外层表面之外，压强梯度的两个分量正好与速度场的两个分量的取值位置完全相同。这会很大地简化后面介绍的投影步骤——在我们求解出每个格子中心的压强值之后，需要为速度场加上 $-\frac 1\rho\nabla p$ 将其变成无散场，由于我们这里得到的压强梯度与速度场的取值位置完全相同，场之间的加法直接对应于网格上存储的数组的加法。

## 数值求解

在 {numref}`sec-animation-fluids-physics` 中我们已经介绍过求解流体方程常用的分裂法，对于无粘性流体，将纳维-斯托克斯方程（式 {eq}`animation-fluids-ns_equation`）拆成三个更简单的偏微分方程并依次求解，因此在欧拉法流体模拟的每个时间步内，会执行对流、施加外力和投影三个步骤。

接下来的三个小节将会分别介绍这三个步骤的实现方法。在时间步开始的时候，我们已经构建好了一个完整的标记网格，包含上个时间步计算好的（或模拟最开始初始化好的）速度场 $\boldsymbol u^n$ 以及自由表面的有符号距离场 $\phi^n$；等到经过以下的操作，我们就能够得到时间步结束后的速度场 $\boldsymbol u^{n+1}$ 以及有符号距离场 $\phi^{n+1}$。

### 对流

在对流（advection）步骤我们需要将流体按照它的速度场向前移动一个时间步，也即求解如下的对流方程：

$$
\frac{\mathrm D\boldsymbol u}{\mathrm Dt}=\boldsymbol 0，\\
\frac{\mathrm D\phi}{\mathrm Dt}=0，
$$

分别对应于速度场 $\boldsymbol u^n$ 和有符号距离场 $\phi^n$ 的对流。在拉格朗日方法中，这个步骤就是将粒子沿它的速度向前进行一步时间积分，粒子上携带的物理量不变，但是由于我们的标记网格并不能随时间移动或变形，在欧拉法中对流将会更加复杂一些。

我们首先考虑 $\phi^n$ 的对流，设对流后的场为 $\phi^*$。目标其实很简单，就是求出每个顶点上 $\phi^*$ 的值，而想要做到这一点，我们首先需要知道这个顶点在上一个时间步处于什么位置，即“它从哪里来”。我们可以假想一个粒子按照流体的速度场连续地移动，并且在 $n+1$ 时刻（即当前时间步结束的时刻）恰好经过格点 $\left(i+\frac 12,j+\frac 12\right)$，它在时刻 $n$ 和 $n+1$ 之间的轨迹如{numref}`fig-animation-fluids-advection` 所示。

```{figure} fig/animation-fluids-advection.png
:width: 50 %
:name: fig-animation-fluids-advection

于 $n+1$ 时刻经过 $\boldsymbol x_{i+\frac 12,j+\frac 12}$ 的虚拟粒子在时刻 $n$ 和 $n+1$ 之间的运动轨迹
```

记时刻 $n$ 为 $t_n$，粒子在 $t$ 时刻的位置为 $\boldsymbol y(t)$，$t$ 时刻流体的速度场为 $\boldsymbol u(t;\boldsymbol x)$，则 $t\in[t_n,t_{n+1}]$ 时有粒子的速度（记 $\Delta t=t-t_n$，$\Delta\boldsymbol x=\boldsymbol y(t)-\boldsymbol x_{i+\frac 12,j-\frac 12}$）

$$
\begin{aligned}
\boldsymbol u(t;\boldsymbol y(t))&=\boldsymbol u\left(t_n+\Delta t;\boldsymbol x_{i+\frac 12,j+\frac 12}+\Delta\boldsymbol x\right)\\
&=\boldsymbol u\left(t_n,\boldsymbol x_{i+\frac 12,j+\frac 12}\right)+\frac{\partial\boldsymbol u\left(t_n,\boldsymbol x_{i+\frac 12,j+\frac 12}\right)}{\partial t}\Delta t+\nabla\boldsymbol u\left(t_n,\boldsymbol x_{i+\frac 12,j+\frac 12}\right)\cdot\Delta\boldsymbol x+O\left((\Delta t)^2+\Vert\Delta\boldsymbol x\Vert^2\right)。\\
\end{aligned}
$$

注意到 $\boldsymbol u\left(t_n,\boldsymbol x_{i+\frac 12,j+\frac 12}\right)=\boldsymbol u^n_{i+\frac 12,j+\frac 12}$ 就是时刻 $n$ 的标记网格上的速度（但注意这里是顶点上的速度，还需要通过保存在面上的速度分量插值得到），我们可以大致估计出轨迹上任意一点的速度与这个速度之间的差距的上界：

$$
\left\Vert\boldsymbol u(t;\boldsymbol y(t))-\boldsymbol u^n_{i+\frac 12,j+\frac 12}\right\Vert\le\left\Vert\frac{\partial\boldsymbol u}{\partial t}\right\Vert\Delta t+\Vert\nabla\boldsymbol u\Vert_2 u_\mathrm{max}\Delta t+O\left((\Delta t)^2\right)，
$$

其中 $u_\mathrm{max}$ 是流速大小的上界。我们知道现实情况下流速场都是有界可导的，因此只要时间步 $t_{n+1}-t_n\ge\Delta t$ 取得足够小，可以认为轨迹上任意一点的速度都近似等于 $\boldsymbol u^n_{i+\frac 12,j+\frac 12}$。根据这个近似，我们就可以估计出虚拟粒子在时刻 $n$ 的大致位置 $\boldsymbol y(t_n)=\boldsymbol x_{i+\frac 12,j+\frac 12}-(t_{n+1}-t_n)\boldsymbol u^n_{i+\frac 12,j+\frac 12}$，即以 $n$ 时刻顶点 $\left(i+\frac 12,j+\frac 12\right)$ 上的速度反向运动一个时间步的位置。找到位置之后，利用 $\phi^n$ 进行双线性插值（三维情形下做三线性插值）求出 $\boldsymbol y(t_n)$ 处的值作为对流后的 $\phi^*_{i+\frac 12,j+\frac 12}$。我们将这个对流过程简单记为 $\phi^*\gets\mathrm{Advect}(\boldsymbol u^n,t_{n+1}-t_n,\phi^n)$，表示将场 $\phi^n$ 按照速度场 $\boldsymbol u^n$ 对流 $t_{n+1}-t_n$ 的时间并保存到 $\phi^*$ 中。

值得注意的一点是，$\phi^*$ 不再是一个有符号距离场了：一个距离表面较远的点，在对流之后和表面的距离是有可能变化的，而我们的对流操作则假设这个距离没有变化。事实上，这个假设在距离表面较近时是合理的，我们可以保留距离表面一个格子范围内的 $\phi^*$ 值，然后基于这些值重新计算其余格点上的有符号距离场。这个过程非常类似我们在初始时从一个已知几何体构建有符号距离场的过程，回想 {numref}`sec-geometry-representation-implicit_field-sdf-grid` 中的做法，我们同样按照快速步进法或者快速扫描法的遍历顺序依次推导出其余格点的值。不同的是，遍历过程中我们不再知道每个格点在表面上的最近点位置，因此我们需要使用有符号距离场的梯度性质来求解，即 $\Vert\nabla\phi\Vert=1$；例如，在遍历到格点 $\left(i+\frac 12,j+\frac 12\right)$ 时，假设其左、上格点的距离场已知，则可以列出如下方程：

$$
\left(\frac{\phi_{i+\frac 12,j+\frac 12}-\phi_{i-\frac 12,j+\frac 12}}{\Delta x}\right)^2+\left(\frac{\phi_{i+\frac 12,j+\frac 32}-\phi_{i+\frac 12,j+\frac 12}}{\Delta x}\right)^2=1，
$$

这是一个关于 $\phi_{i+\frac 12,j+\frac 12}$ 的二元一次方程，我们应当挑选一个比两个已知的值都大的解（想一想为什么），即

$$
\phi_{i+\frac 12,j+\frac 12}=\frac 12\left(\phi_{i-\frac 12,j+\frac 12}+\phi_{i+\frac 12,j+\frac 32}+\sqrt{2(\Delta x)^2-\left(\phi_{i-\frac 12,j+\frac 12}-\phi_{i+\frac 12,j+\frac 32}\right)^2}\right)。
$$

重新计算有符号距离场从而得到 $\phi^{n+1}$ 总共分为以下步骤：
1. 将 $\phi^{n+1}$ 全部初始化为 $\pm\infty$，正负性与 $\phi^*$ 保持一致。
2. 检查标记网格的每个格子 $(i,j)$，若格子的四个顶点既包含正值也包含负值，或者包含 $0$，则将其四个格点设为 $\phi^*$ 的值：
   - $\phi^{n+1}_{i-\frac 12,j-\frac 12}\gets\phi^*_{i-\frac 12,j-\frac 12}$；
   - $\phi^{n+1}_{i-\frac 12,j+\frac 12}\gets\phi^*_{i-\frac 12,j+\frac 12}$；
   - $\phi^{n+1}_{i+\frac 12,j-\frac 12}\gets\phi^*_{i+\frac 12,j-\frac 12}$；
   - $\phi^{n+1}_{i+\frac 12,j+\frac 12}\gets\phi^*_{i+\frac 12,j+\frac 12}$。
3. 按照快速步进法或者快速扫描法的顺序遍历每个顶点 $\left(i+\frac 12,j+\frac 12\right)$：
   - 若该顶点的邻居节点既有正值也有负值，或者包含 $0$，则跳过当前顶点；接下来不妨设所有的值均为正，否则可以全部取反，计算完毕后再次取反；
   - 令 $\phi_0=\min\left\{\phi^*_{i-\frac 12,j+\frac 12},\phi^*_{i+\frac 32,j+\frac 12}\right\}$，$\phi_1=\min\left\{\phi^*_{i+\frac 12,j-\frac 12},\phi^*_{i+\frac 12,j+\frac 32}\right\}$（分别对应于 $x$ 轴方向和 $y$ 轴方向上邻居的较小值）；
   - 若 $\phi_0>\phi_1$，交换二者；
   - 令 $d=\phi_0+\Delta x$（仅使用一个邻居推算当前点的值）；
   - 若 $\phi_1<+\infty$，$d\gets\min\left\{d,\frac 12\left(\phi_0+\phi_1+\sqrt{2(\Delta x)^2-(\phi_0-\phi_1)^2}\right)\right\}$（使用两个邻居推算当前点的值）；
   - $\phi^{n+1}_{i+\frac 12,j+\frac 12}\gets\min\left\{\phi^{n+1}_{i+\frac 12,j+\frac 12},d\right\}$。

速度场 $\boldsymbol u^n$ 的对流与得到 $\phi^*$ 的过程十分类似，只是需要反向追踪的点与之前不同，以及使用的插值方法不同。现在我们需要从每个面的中心点出发，反向查询它在上个时间步的位置；此外，需要逐分量依次进行线性插值得到相应点的速度值。我们把对流速度场的过程记为 $\boldsymbol u^*\gets\mathrm{Advect}(\boldsymbol u^n,t_{n+1}-t_n,\boldsymbol u^n)$。

至此，对流已经几乎完成，但是现有的步骤还存在问题。考虑图所示的一个流体场景：在不存在重力的情况下，一个

### 施加外力

### 投影

### 算法流程