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

借助标记网格，我们可以使用水平集方法（level set method）表示水的自由表面，尽管这里用了一个新词，其实我们在 {numref}`sec-geometry-representation-implicit_field-df` 学习有符号距离场的时候就已经熟悉了这个概念。水平集方法使用一个标量场 $\phi(\boldsymbol x)$ 来隐式地定义一个几何体，对于空间中任意一点 $\boldsymbol x$：
- 若 $\phi(\boldsymbol x)>0$，则 $\boldsymbol x$ 在几何体的外部；
- 若 $\phi(\boldsymbol x)=0$，则 $\boldsymbol x$ 在几何体的表面上；
- 若 $\phi(\boldsymbol x)<0$，则 $\boldsymbol x$ 在几何体的内部。

换言之，几何体的表面就是 $\phi$ 的 $0$ 等值面，又称为 $\phi$ 的 $0$ 水平集，故此方法名为水平集方法。不难发现，我们可以直接把这里的 $\phi$ 取成我们要表示的几何体的有符号距离场，这样就可以使用 {numref}`sec-geometry-representation-implicit_field-construction` 中介绍的方法得到一个网格化表示的标量场，存储在标记网格的顶点上。因此，在初始化流体场景时，我们就可以将水在初始时的形状转换成水平集表示保存在标记网格当中了，在后续的模拟时间步中，我们会进一步演化这个水平集表示，以实现水的几何动态。

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

值得注意的一点是，$\phi^*$ 不再是一个有符号距离场了：一个距离表面较远的点，在对流之后和表面的距离是有可能变化的，而我们的对流操作则假设这个距离没有变化。事实上，这个假设在距离表面较近时是合理的，我们可以保留距离表面一个格子范围内的 $\phi^*$ 值，然后基于这些值重新计算其余格点上的有符号距离场。这个过程非常类似我们在初始时从一个已知几何体构建有符号距离场的过程，回想 {numref}`sec-geometry-representation-implicit_field-construction` 中的做法，我们同样按照快速步进法或者快速扫描法的遍历顺序依次推导出其余格点的值。不同的是，遍历过程中我们不再知道每个格点在表面上的最近点位置，因此我们需要使用有符号距离场的梯度性质来求解，即 $\Vert\nabla\phi\Vert=1$；例如，在遍历到格点 $\left(i+\frac 12,j+\frac 12\right)$ 时，假设其左、上格点的距离场已知，则可以列出如下方程：

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

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-fluids-noextrapolation
:width: 100 %

```{image} fig/animation-fluids-noextrapolation_0.png
:alt: 初始状态
```

```{image} fig/animation-fluids-noextrapolation_1.png
:alt: 对流一个时间步后的状态
```

无重力环境下一个方形水体沿 $x$ 轴正方向运动的对流结果。网格中蓝色的区域为水体，箭头为速度场，格点上所标数字为有符号距离场；右图仅展示了刚刚对流后的 $\phi^*$，红色字体代表计算有误的值，灰色字体代表后续重新计算步骤会更改的值。
````

至此，对流已经几乎完成，但是现有的步骤还存在问题。考虑{numref}`fig-animation-fluids-noextrapolation` 所示的一个流体场景：在无重力环境下，一个方形的水体沿 $x$ 轴正方向匀速直线运动，速度为 $\frac{\Delta x}{t_{n+1}-t_n}$，即一个时间步恰好能够前进一格。首先考虑速度场的对流，由于水体外部速度均为 $\boldsymbol 0$，水体最右侧一列的速度不会被反向追踪到，导致这一列的速度无法向右传播，从结果上看就是速度不为 $\boldsymbol 0$ 的格子少了一列；有符号距离场的对流则更加复杂一些，读者可以对照{numref}`fig-animation-fluids-noextrapolation` 自行分析对流过程，对流结果会导致水的体积变小（左侧对流速度正常而右侧偏慢），并且在靠近边界的部分出现梯度模长不为 $1$ 的错误情形。

细心的读者不难发现，造成上述问题的原因在于水体之外速度为 $\boldsymbol 0$，在迎风面（即速度前进方向的一侧）外部的反向追踪无法定位到流体内部有用的信息，导致我们的对流算法不能实现边界的“扩张”。针对这个问题，我们需要使用外插（extrapolation）方法，对流体速度场进行一定范围的延拓，让迎风面外部的反向追踪能够和正向对流完全对应上。外插可以通过宽度优先搜索（Breath First Search，BFS）实现，假设我们需要外插一个保存在标记网格上的量 $q_{a,b}$，步骤如下：
1. 创建一个与 $q_{a,b}$ 形状相同、值为 $+\infty$ 的数组 $d_{a,b}$ 表示宽度搜索的步数，以及一个先进先出的队列 $Q$。
2. 对于所有已知 $q_{a,b}$ 值的位置 $(a,b)$，令 $d_{a,b}\gets 0$。
3. 遍历所有的位置 $(a,b)$，若有 $d_{a,b}=+\infty$ 且存在一个 $d=0$ 的邻居，则 $d_{a,b}\gets 1$ 并将 $(a,b)$ 加入 $Q$。
4. 若 $Q$ 非空，循环执行以下步骤：
   - 从 $Q$ 中取出元素 $(a,b)$；
   - 设集合 $\mathcal N=\{(a',b'):d_{a',b'}<d_{a,b},(a',b')\text{与}(a,b)\text{相邻}\}$，$q_{a,b}\gets\frac 1{\vert\mathcal N\vert}\sum_{(a',b')\in\mathcal N}q_{a',b'}$；
   - 对于 $(a,b)$ 的邻居 $(a',b')$，若 $d_{a',b'}=+\infty$，则 $d_{a',b'}=d_{a,b}+1$ 并将 $(a',b')$ 加入 $Q$。

我们分别外插速度场 $\boldsymbol u^n$ 的两个分量得到新的速度场 $\hat{\boldsymbol u}^n$，然后在反向追踪的时候换用 $\hat{\boldsymbol u}^n$ 即可；$\phi^n$ 与 $\boldsymbol u^n$ 的对流步骤分别修改成 $\phi^*\gets\mathrm{Advect}(\hat{\boldsymbol u}^n,t_{n+1}-t_n,\phi^n)$ 和 $\boldsymbol u^*\gets\mathrm{Advect}(\hat{\boldsymbol u}^n,t_{n+1}-t_n,\boldsymbol u^n)$。读者不妨尝试一下外插后的速度场是否能够正确对流{numref}`fig-animation-fluids-noextrapolation` 所示的场景。

### 施加外力

在施加外力的步骤中，我们求解纳维-斯托克斯方程的第二个部分：

$$
\frac{\partial\boldsymbol u}{\partial t}=\boldsymbol g。
$$

我们考虑的场景中外力只有重力，而固体边界受力平衡，空气的质量忽略不计，因此我们只需要考虑水受重力的影响。我们首先利用上一小节得到的 $\phi^{n+1}$ 对场景进行体素化，并更新标记为水的格子上的速度场即可。由于重力方向竖直向下，大小为重力加速度 $g\approx 9.8$，我们应将标记为水的格子上保存的速度的 $y$ 分量（即 $v^*_{i,j\pm\frac 12}$）增加 $-g\Delta t$。

### 投影

投影的目的是求解纳维-斯托克斯方程的第三个部分，即压强带来的影响：

$$
\frac{\partial\boldsymbol u}{\partial t}=-\frac 1\rho\nabla p\quad\text{s.t.}\,\nabla\cdot\boldsymbol u=0。
$$

在本节我们记时间步长为 $\Delta t$，将这个偏微分方程离散化后可以得到：

$$
\frac{\boldsymbol u^{n+1}-\boldsymbol u^*}{\Delta t}=-\frac 1\rho\nabla p\quad\text{s.t.}\,\nabla\cdot\boldsymbol u^{n+1}=0。
$$

由于我们模拟的是不可压流体，这里的密度就是一个常数，令 $p^*=\frac{\Delta t}\rho p$，将上式整理后可以得到一个关于 $p^*$ 的泊松方程：

$$
\nabla^2p^*=\nabla\cdot\boldsymbol u^*，
$$ (animation-fluids-poisson)

其中 $\nabla^2=\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}\right)$ 称为拉普拉斯算子。此外，在本节处理的场景中，还存在两类边界条件：
- 在自由表面上要求 $p^*=0$，即气体压强恒定，这种直接约束待求解函数值的边界条件称为迪利克雷边界条件（Dirichlet boundary condition）。
- 在固液边界上要求 $\boldsymbol u^{n+1}\cdot\boldsymbol n=0$（$\boldsymbol n$ 为固体表面法向），整理后得 $\nabla p^*\cdot\boldsymbol n=\boldsymbol u^*\cdot\boldsymbol n$，即限制流体不能穿过固体，这种约束待求解函数一阶导数的边界条件称为纽曼边界条件（Neumann boundary condition）。

接下来，我们需要在遵守边界条件的情况下求解方程 {eq}`animation-fluids-poisson`。还记得我们把压强场保存在标记网格的格子中心吗？现在我们就是要把格子中心的 $p^*_{i,j}$ 作为未知量，根据式 {eq}`animation-fluids-poisson` 列出一个代数方程组。方程的右端项读者已经不陌生，根据式 {eq}`animation-fluids-velocity_divergence` 即可求出；而方程的左端项可以写成 $\nabla\cdot(\nabla p^*)$，即 $p^*$ 梯度的散度，根据式 {eq}`animation-fluids-pressure_gradient` 我们可以算出定义在标记网格面上的 $\nabla p^*$，接下来和求速度的散度一样，套用式 {eq}`animation-fluids-velocity_divergence` 就可以算出定义在标记网格中心的 $\nabla^2p^*$ 了。不难发现，若暂时不考虑边界条件，我们可以为除最外圈的每一个格子列出一个方程，即对于格子 $(i,j)$ 有

$$
p^*_{i+1,j}+p^*_{i-1,j}+p^*_{i,j+1}+p^*_{i,j-1}-4p^*_{i,j}=\Delta x\left(u^*_{i+\frac 12,j}-u^*_{i-\frac 12,j}+v^*_{i,j+\frac 12}-v^*_{i,j-\frac 12}\right)。
$$ (animation-fluids-poisson_discrete)

在此基础上我们可以很轻松地加上迪利克雷边界条件。对于标记为空气的格子 $(i,j)$，有 $p^*_{i,j}=0$，既然变成已知量，我们应当删除这个格子对应的上述方程，并将其余方程中的 $p^*_{i,j}$ 一项替换成 $0$，因此与该格子相邻的所有格子对应的方程都需要修改。

随后我们需要添加纽曼边界条件。假设标记为水的格子 $(i,j)$ 的下方是一个固体格子 $(i,j-1)$，其余邻居均为水格子，那么根据纽曼边界条件的表达式 $\nabla p^*\cdot\boldsymbol n=\boldsymbol u^*\cdot\boldsymbol n$ 有如下关系：

$$
\frac 1{\Delta x}\left(p^*_{i,j}-p^*_{i,j-1}\right)=v^*_{i,j-\frac 12}，
$$

整理得

$$
p^*_{i,j-1}=p^*_{i,j}-\Delta xv^*_{i,j-\frac 12}，
$$

再代入 {eq}`animation-fluids-poisson_discrete` 可得格子 $(i,j)$ 对应的修改后的方程

$$
p^*_{i+1,j}+p^*_{i-1,j}+p^*_{i,j+1}-3p^*_{i,j}=\Delta x\left(u^*_{i+\frac 12,j}-u^*_{i-\frac 12,j}+v^*_{i,j+\frac 12}\right)。
$$

因此纽曼边界条件也可以消除一个未知量，格子 $(i,j-1)$ 对应的方程也应当删除。

总结一下，我们只需要为每个标记为水的格子列一个形如 {eq}`animation-fluids-poisson_discrete` 的方程；然后依次检查它的每一个邻居，如果有一个空气格子，则将左端项对应的 $p^*$ 项删除；如果有一个固体格子，则将左端项对应的 $p^*$ 项删除，并将自身的 $p^*$ 项系数加一，同时右端项抹掉对应的 $\boldsymbol u^*$ 的分量。无论方程如何修改，整个方程组都是关于所有水格子上的 $p^*_{i,j}$ 的线性方程组，并且系数矩阵是对称的，使用线性求解器进行求解即可。最后，从 $\boldsymbol u^*$ 减去 $\nabla p^*$，即可得到无散的速度场 $\boldsymbol u^{n+1}$。

### 算法流程

作为总结，我们给出欧拉网格流体从时刻 $n$ 到 $n+1$ 的完整算法。设时间步长为 $\Delta t$；算法开始时，我们拥有时刻 $n$ 的速度场 $\boldsymbol u^n$ 和有符号距离场 $\phi^n$，然后执行如下步骤：
1. 外插速度场 $\boldsymbol u^n$ 得到 $\hat{\boldsymbol u}^n$。
2. 对流有符号距离场：$\phi^*\gets\mathrm{Advect}(\hat{\boldsymbol u}^n,\Delta t,\phi^n)$。
3. 根据 $\phi^*$ 重新计算有符号距离场得到 $\phi^{n+1}$。
4. 对流速度场：$\boldsymbol u^*\gets\mathrm{Advect}(\hat{\boldsymbol u}^n,\Delta t,\boldsymbol u^n)$。
5. 对 $\boldsymbol u^*$ 施加外力。
6. 求解方程 {eq}`animation-fluids-poisson`，遵循迪利克雷和纽曼边界条件，得到 $p^*$。
7. 更新速度场：$\boldsymbol u^{n+1}\gets\boldsymbol u^*-\nabla p^*$。

最后得到的 $\boldsymbol u^{n+1}$ 和 $\phi^{n+1}$ 即为下一个时间步的状态。