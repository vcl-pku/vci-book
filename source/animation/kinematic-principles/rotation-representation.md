(sec-animation-kinematic_principles-rotation_representation)=
# 旋转的表示

在研究主观动态时，我们往往会忽略物体本身的细节，只关注它的整体运动，因此往往会将每个零部件抽象成刚体。刚体的严格定义可以参考 {numref}`sec-animation-rigid_bodies-dynamics`，在三维空间中，它有 $6$ 个自由度，其中 $3$ 个用于表示位置，另外 $3$ 个用于表示其朝向。表示一个刚体的位置十分简单，使用其质心坐标 $(x,y,z)$ 即可；但表示一个刚体的朝向或旋转则存在多种方法，接下来我们会一一介绍。

(sec-animation-kinematic_principles-rotation_representation-rotation_matrix)=
## 旋转矩阵

### 二维旋转矩阵

```{figure} fig/animation-kinematic_principles-rotation_2d.png
:width: 50 %
:name: fig-animation-kinematic_principles-rotation_2d

二维空间下向量的旋转
```

我们先回顾一下二维空间下的旋转。如{numref}`fig-animation-kinematic_principles-rotation_2d` 所示，二维空间下的旋转仅有一个自由度。记平面上旋转前的向量为 $(x,y)$，其绕原点逆时针旋转 $\alpha$ 弧度，得到旋转后的向量 $(x',y')$；设 $(x,y)$ 的模场为 $r$，极角为 $\theta$，据此可以列出如下方程组：

$$
\begin{aligned}
x&=r\cos\theta，\\
y&=r\sin\theta，\\
x'&=r\cos(\theta+\alpha)，\\
y'&=r\sin(\theta+\alpha)。
\end{aligned}
$$

利用三角函数和差公式可以得到

$$
\begin{aligned}
&x'=r\cos\theta\cos\alpha-r\sin\theta\sin\alpha=x\cos\alpha-y\sin\alpha，\\
&y'=r\sin\theta\cos\alpha+r\cos\theta\sin\alpha=x\sin\alpha+y\cos\alpha，
\end{aligned}
$$

写成矩阵形式即为

$$
\begin{bmatrix}x'\\y'\end{bmatrix}=
\begin{bmatrix}
\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha
\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}，
$$ (animation-kinematic_principles-rotation_2d)

因此，二维空间中逆时针旋转 $\alpha$ 对应于旋转矩阵 $\begin{bmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{bmatrix}$。

### 绕坐标轴旋转矩阵

现在我们尝试将旋转矩阵的概念拓展到三维。首先考虑一类简单的情形——绕 $z$ 轴的旋转，设旋转前向量为 $\boldsymbol P_0=(x,y,z)^\top$，旋转后向量为 $\boldsymbol P_0'=(x',y',z')^\top$。

```{figure} fig/animation-kinematic_principles-rotation_along_axis_z.png
:width: 50 %
:name: fig-animation-kinematic_principles-rotation_along_axis_z

三维空间下向量绕 $z$ 轴旋转
```

对于 $z$ 分量，由于 $z$ 分量在绕 $z$ 轴旋转时保持不变，因此 $z'=z$；对于 $x$、$y$ 分量，向量旋转方式等同于在 $x$ 轴与 $y$ 轴张成的平面上进行的二维旋转。据此我们可以得到该旋转的矩阵形式：

$$
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}=
\begin{bmatrix}
\cos\alpha&-\sin\alpha&0\\
\sin\alpha&\cos\alpha&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}。
$$ (animation-kinematic_principles-matrix_along_z)

类比于绕 $z$ 轴旋转的情况，我们可以分别得到绕 $x$ 轴和 $y$ 轴旋转的矩阵表示：

$$
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}=
\begin{bmatrix}
1&0&0\\
0&\cos\alpha&-\sin\alpha\\
0&\sin\alpha&\cos\alpha
\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}，
$$ (animation-kinematic_principles-matrix_along_x)


$$
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}=
\begin{bmatrix}
\cos\alpha&0&\sin\alpha\\
0&1&0\\
-\sin\alpha&0&\cos\alpha
\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}。
$$ (animation-kinematic_principles-matrix_along_y)

将绕 $z$、$x$、$y$ 轴进行旋转的矩阵分别记为 $\boldsymbol R_z(\alpha)$、$\boldsymbol R_x(\alpha)$、$\boldsymbol R_y(\alpha)$，则式 {eq}`animation-kinematic_principles-matrix_along_z`、{eq}`animation-kinematic_principles-matrix_along_x`、{eq}`animation-kinematic_principles-matrix_along_y` 可以分别简写为如下形式：

$$
\begin{aligned}
\boldsymbol P_0\boldsymbol R_z(\alpha)=\boldsymbol P_0'，\\
\boldsymbol P_0\boldsymbol R_x(\alpha)=\boldsymbol P_0'，\\
\boldsymbol P_0\boldsymbol R_y(\alpha)=\boldsymbol P_0'。
\end{aligned}
$$

### 三维正交变换

我们已经推导完毕了三维空间内绕坐标轴的旋转矩阵，但是对于绕任意轴进行的旋转仍然无能为力。好在我们可以考虑对整个空间进行正交变换，使得随空间一起变换的旋转轴恰好变为三个坐标轴中的某一个，从而将问题转化成我们已经学过的情形。

```{figure} fig/animation-kinematic_principles-rotation_along_axis_step1.png
:width: 50 %
:name: fig-animation-kinematic_principles-rotation_along_axis_step1

三维空间内的正交变换
```

考虑如{numref}`fig-animation-kinematic_principles-rotation_along_axis_step1` 所示的正交变换，设变换前的坐标系为 $xyz$，变换后为 $x'y'z'$，变换矩阵为 $\boldsymbol R$；那么对于任意一个向量，其变换前的坐标 $(x,y,z)$ 与变换后的坐标 $(x',y',z')$ 之间的关系满足

$$
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}=\boldsymbol R\begin{bmatrix}x\\y\\z\end{bmatrix}，
$$ (animation-kinematic_principles-orthogonal_transformation)

```{attention}
这里我们使用的坐标都是在 $xyz$ 坐标系下的。
```

现在我们的任务就是考虑如何求解 $\boldsymbol R$。记 $x$、$y$、$z$ 轴方向的单位向量分别为 $\boldsymbol e_x$、$\boldsymbol e_y$、$\boldsymbol e_z$，$x'$、$y'$、$z'$ 轴方向的单位向量分别为 $\boldsymbol e_x'$、$\boldsymbol e_y'$、$\boldsymbol e_z'$。将 $\boldsymbol e_x$ 代入式 {eq}`animation-kinematic_principles-orthogonal_transformation` 的右端项，则左端项应当变成 $\boldsymbol e_x'$；不难发现，旋转矩阵 $R$ 第一列的取值，恰好为 $\mathbf{e}_x'$。类似地，我们可以说明旋转矩阵 $R$ 的第二、三列的取值，分别 $\mathbf{e}_y'$ 和 $\mathbf{e}_z^\prime$。据此我们有 $\boldsymbol R=\begin{bmatrix}\boldsymbol e_x'&\boldsymbol e_y'&\boldsymbol e_z'\end{bmatrix}$。

自然地，将坐标轴 $x'y'z'$ 变换回 $xyz$ 的矩阵为 $\boldsymbol R^{-1}$，由于 $\boldsymbol R$ 的所有列向量均为单位向量且两两垂直，因此 $\boldsymbol R$ 是正交矩阵，有 $\boldsymbol R^{-1}=\boldsymbol R^\top$。

### 三维旋转矩阵

接下来，我们尝试构造绕向量 $\boldsymbol u$ 旋转 $\alpha$ 弧度的旋转矩阵。我们可以使用如{numref}`fig-animation-kinematic_principles-rotation_steps` 所示的步骤来旋转一个向量：
1. 通过旋转轴构造正交坐标系 $x'y'z'$，使得 $x'$ 轴与向量 $u$ 方向一致；
2. 将正交坐标系 $x'y'z'$ 变换为正交坐标系 $xyz$，旋转轴 $u$ 随之变换为 $x$ 轴，待旋转向量也进行相应的变换；
3. 将待旋转向量绕着 $x$ 轴旋转 $\alpha$ 弧度得到旋转后的向量；
4. 将正交坐标系 $xyz$ 变换回 $x'y'z'$，旋转后的向量也进行相应的变换。

````{subfigure} ABC
:layout-sm: A|B|C
:gap: 8px
:subcaptions: below
:name: fig-animation-kinematic_principles-rotation_steps
:width: 100 %

```{image} fig/animation-kinematic_principles-rotation_along_axis_step1.png
```

```{image} fig/animation-kinematic_principles-rotation_along_axis_step2.png
```

```{image} fig/animation-kinematic_principles-rotation_along_axis_step3.png
```

绕 $\boldsymbol u$ 旋转 $\alpha$ 的步骤。从左到右分别对应于正交坐标系 $x'y'z'$ 变换为正交坐标系 $xyz$，绕 $x$ 轴进行旋转，正交坐标系 $xyz$ 变换回正交坐标系 $x'y'z'$ 这三个步骤。
````

我们按照顺序依次解决每个步骤。首先构造正交坐标系 $x'y'z'$：
1. 任取一个与 $\boldsymbol u$ 不共线的单位向量 $\boldsymbol t$；
2. 取 $\boldsymbol w=\boldsymbol t\times\boldsymbol u$，则 $\boldsymbol w$ 与 $\boldsymbol u$ 垂直；
3. 取 $\boldsymbol v=\boldsymbol u\times\boldsymbol w$，则 $\boldsymbol u$、$\boldsymbol v$、$\boldsymbol w$ 两两垂直，且遵循右手螺旋定则。

将 $\boldsymbol u$、$\boldsymbol v$ 和 $\boldsymbol w$ 分别作为 $x'$ 轴、$y'$ 轴和 $z'$ 轴即可得到满足要求的坐标系 $x'y'z'$。根据上一小节，我们可以直接写出将 $xyz$ 坐标系变换成 $x'y'z'$ 坐标系的矩阵 $\boldsymbol R=\begin{bmatrix}\boldsymbol u&\boldsymbol v&\boldsymbol w\end{bmatrix}$。假设待旋转向量为 $\boldsymbol P_0$，我们可以写出它依次经过上述第二、三、四步的变换后得到的向量

$$
\boldsymbol P_0'=\boldsymbol R\boldsymbol R_x(\alpha)\boldsymbol R^\top\boldsymbol P_0。
$$ (animation-kinematic_principles-rotation_along_axis)

据此可得绕 $\boldsymbol u$ 旋转 $\alpha$ 的旋转矩阵为 $\boldsymbol R\boldsymbol R_x(\alpha)\boldsymbol R^\top$。

罗德里格旋转公式（Rodrigues' rotation formula）给出了绕轴旋转矩阵的封闭形式，设旋转矩阵 $\boldsymbol R$ 表示绕 $\boldsymbol u$ 旋转 $\alpha$，则

$$
\boldsymbol R=\mathbf I+\sin\alpha[\boldsymbol u]+(1-\cos\alpha)[\boldsymbol u]^2，
$$ (animation-kinematic_principles-rodrigues)

其中 $[\boldsymbol u]=\begin{bmatrix}0&-u_z&u_y\\u_z&0&-u_x\\-u_y&u_x&0\\\end{bmatrix}$ 为 $\boldsymbol u$ 的叉乘矩阵。

## 四元数

### 二维平面复数

```{figure} fig/animation-kinematic_principles-rotation_2d.png
:width: 50 %
:name: fig-animation-kinematic_principles-rotation_2d_complex

二维空间内的复数乘法与向量旋转
```

一个复数可以被记为 $x+y\mathrm i\in\mathbb C$，其中 $x,y\in\mathbb R$，$\mathrm i^2=-1$。将复数 $x+y\mathrm i$ 与平面上的向量 $(x,y)$ 建立一一对应，那么根据欧拉公式（Euler's formula）

$$
\mathrm e^{\mathrm i\theta}=\cos\theta+\mathrm i\sin\theta，
$$

向量 $(x,y)$ 与复数 $r\mathrm e^{\mathrm i\theta}$ 对应，其中 $r$ 为其模长，$\theta$ 为其极角。因此，若将向量 $(x,y)$ 逆时针旋转 $\alpha$ 弧度，则旋转后的向量对应于复数 $r\mathrm e^{\mathrm i(\theta+\alpha)}=r\mathrm e^{\mathrm i\theta}\cdot\mathrm e^{\mathrm i\alpha}$，即原复数乘上一个单位复数 $\mathrm e^{\mathrm i\alpha}$。故若将平面向量一一映射到复数，则二维的旋转可以用单位复数表示，具体地，绕原点逆时针旋转 $\alpha$ 可以表示成复数 $\mathrm e^{\mathrm i\alpha}$。

借助类似的思想，我们也可以将三维的向量映射成某种“数”，从而将三维旋转表示成这种“数”的乘积——这种“数”就是四元数。

### 四元数定义与运算

```{figure} fig/animation-kinematic_principles-quaternion_hamilton.jpg
:width: 50 %
:name: fig-animation-kinematic_principles-quaternion_hamilton

爱尔兰数学家哈密顿（William Rowan Hamilton）发明了四元数。[^fig-animation-kinematic_principles-quaternion_hamilton-ref]
```

[^fig-animation-kinematic_principles-quaternion_hamilton-ref]: 图片来源：https://en.wikipedia.org/wiki/Quaternion

定义四元数 $q=a+b\mathrm i+c\mathrm j+d\mathrm k$，其中 $a,b,c,d\in\mathbb R$。与复数的虚部类似，四元数中 $\mathrm i$、$\mathrm j$、$\mathrm k$ 同样满足 $\mathrm i^2=\mathrm j^2=\mathrm k^2=-1$；另外，它们之间的相互运算还满足一种类似三维空间上叉积运算的形式，将 $\mathrm i$、$\mathrm j$、$\mathrm k$ 分别对应于三维坐标的 $x$、$y$、$z$ 轴（如{numref}`fig-animation-kinematic_principles-quaternion_and_axis` 所示），前者的乘积就对应于后者的叉积：

$$
\begin{array}{lll}
\mathrm{ij}=\mathrm k，&\mathrm{jk}=\mathrm i，&\mathrm{ki}=\mathrm j，\\
\mathrm{ji}=-\mathrm k，&\mathrm{kj}=-\mathrm i，&\mathrm{ik}=-\mathrm j。
\end{array}
$$ (animation-kinematic_principles-quaternion_product)

```{figure} fig/animation-kinematic_principles-quaternion_and_axis.png
:width: 50 %
:name: fig-animation-kinematic_principles-quaternion_and_axis

四元数虚部和右手系坐标轴 $x$、$y$、$z$ 的对应
```

### 四元数表示旋转

### 四元数插值

## 欧拉角

## 轴角表示法

> jr: 这一小节可能不再需要或者得移到前面，在本文件开头提一下前面讲轴角表示的部分即可。
