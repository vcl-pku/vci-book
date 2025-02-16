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
$$ (animation-kinematic_principles-quat_imaginary_product)

```{figure} fig/animation-kinematic_principles-quaternion_and_axis.png
:width: 50 %
:name: fig-animation-kinematic_principles-quaternion_and_axis

四元数虚部和右手系坐标轴 $x$、$y$、$z$ 的对应
```

我们还可以将四元数表示成实部 $w=a$ 和虚部向量 $\boldsymbol v=(b,c,d)^\top$ 拼接而成的形式，记作 $[w,\boldsymbol v]$。

四元数的加减法、模长、点乘运算与传统的四维向量运算规则相同。令 $q_1=a_1+b_1\mathrm i+c_1\mathrm j+d_1\mathrm k=[w_1,\boldsymbol v_1]$、$q_2=a_2+b_2\mathrm i+c_2\mathrm j+d_2\mathrm k=[w_2,\boldsymbol v_2]$，有

$$
\begin{aligned}
q_1\pm q_2&=(a_1\pm a_2)+(b_1\pm b_2)\mathrm i+(c_1\pm c_2)\mathrm j+(d_1\pm d_2)\mathrm k，\\
tq_1&=ta_1+tb_1\mathrm i+tc_1\mathrm j+td_1\mathrm k，\\
q_1\cdot q_2&=a_1a_2+b_1b_2+c_1c_2+d_1d_2，\\
\Vert q_1\Vert_2&=\sqrt{q_1\cdot q_1}。
\end{aligned}
$$

四元数的乘法运算会稍微复杂一些，我们可以根据式 {eq}`animation-kinematic_principles-quat_imaginary_product` 给出的虚部乘法规则计算出 $q_1$ 与 $q_2$ 的乘积：

$$
\begin{array}{llll}
q_1q_2 & = & &(a_1 + b_1\mathrm i +c_1\mathrm j + d_1\mathrm k)(a_2 + b_2\mathrm i +c_2\mathrm j + d_2\mathrm k)\\
& = & &  (a_1a_2 - b_1b_2 - c_1c_2 - d_1d_2) \\
& & + &  (a_1b_2 + b_1a_2 + c_1d_2 - d_1c_2)\mathrm i \\ 
& & + &  (a_1c_2 - b_1d_2 + c_1a_2 + d_1b_2)\mathrm j \\ 
& & + &  (a_1d_2 + b_1c_2 - c_1b_2 + d_1a_2)\mathrm k。 \\ 
\end{array}
$$

用实部与虚部向量的方式来表示则会简便很多：

$$
q_1q_2=[w_1w_2-\boldsymbol v_1\cdot\boldsymbol v_2,w_1\boldsymbol v_2+w_2\boldsymbol v_1+\boldsymbol v_1\times\boldsymbol v_2]。
$$ (animation-kinematic_principles-quaternion_product)

四元数的共轭定义与复数共轭定义类似，均为将虚部取反的结果。四元数 $q = [w,\boldsymbol v]$ 的共轭为 $q^\star = [w,-\boldsymbol v]$。

利用四元数乘法与共轭的定义，我们不难得出 $qq^\star = [w^2 + \boldsymbol v\cdot \boldsymbol v,\boldsymbol 0]=\Vert q\Vert^2$。四元数的单位元为 $[1,\boldsymbol 0]$，因此我们可以构造任意非零四元数 $q$ 的逆元为 $q^{-1} = \frac{q^\star}{\Vert q\Vert^2}$。

单位四元数为所有模长为 $1$ 的四元数，若将四元数看成四维向量，则所有单位四元数构成了四维超球面。根据定义不难得出单位四元数 $q$ 满足 $q^{-1}=q^\star$，即其共轭就是其逆元。类似于单位复数的分解 $z=\cos\theta+\mathrm i\sin\theta$，单位四元数也可以写成类似的形式 $q=[\cos\theta,(\sin\theta)\boldsymbol u]$，其中 $\boldsymbol u$ 是单位向量。

### 四元数表示旋转

单位四元数也可以用来表示旋转，其与三维旋转的对应关系可通过如下定理看出：

```{prf:theorem}
:label: thm-animation-kinematic_principles-quaternion_rotation

设 $q=[\cos\theta,(\sin\theta)\boldsymbol u]$ 是一个单位四元数，$v=[0,\boldsymbol v]$ 是一个实部为 $0$ 的四元数，则有：
- $qvq^\star$ 实部为 $0$。
- $qvq^\star$ 的虚部是向量 $\boldsymbol v$ 绕旋转轴 $\boldsymbol u$ 旋转 $2\theta$ 弧度后的结果。
```

`````{prf:proof}
我们可以将向量 $\boldsymbol v$ 分解成平行于旋转轴 $\boldsymbol u$ 以及垂直于旋转轴的两个分量 $\boldsymbol v_\parallel$ 和 $\boldsymbol v_\perp$，对应的四元数分别为 $v_\parallel=[0,\boldsymbol v_\parallel]$ 和 $v_\perp=[0,\boldsymbol v_\perp]$。那么我们只需要说明，平行分量在进行上述变换后保持不变，垂直分量在垂直于 $\boldsymbol u$ 的平面内逆时针旋转了 $2\theta$ 即可。


````{subfigure} ABC
:layout-sm: A|B|C
:gap: 8px
:subcaptions: below
:name: fig-animation-kinematic_principles-quaternion_rotation_proof
:width: 100 %

```{image} fig/animation-kinematic_principles-rotation_decomposite.png
:alt: 待旋转向量的分解
```

```{image} fig/animation-kinematic_principles-rotation_top_view.png
:alt: 旋转的顶视图
```

```{image} fig/animation-kinematic_principles-rotation_front_view.png
:alt: 旋转的前视图
```

定理 {prf:ref}`thm-animation-kinematic_principles-quaternion_rotation` 的证明思路
````

首先我们证明平行分量在进行上述变换后保持不变，且实部为 $0$。由于 $\boldsymbol u$ 是单位向量，且 $\boldsymbol u\times\boldsymbol v_\parallel=\boldsymbol 0$，那么根据四元数乘法规则有

$$
\begin{aligned}
qv_\parallel q^\star&=[\cos\theta,(\sin\theta)\boldsymbol u][0,\boldsymbol v_\parallel][\cos\theta,-(\sin\theta)\boldsymbol u]\\
&=[-(\boldsymbol u\cdot\boldsymbol v_\parallel)\sin\theta,(\cos\theta)\boldsymbol v_\parallel][\cos\theta,-(\sin\theta)\boldsymbol u]\\
&=[-(\boldsymbol u\cdot\boldsymbol v_\parallel)\sin\theta\cos\theta+(\cos\theta)\boldsymbol v_\parallel\cdot(\sin\theta)\boldsymbol u,((-\sin\theta)^2+(\cos\theta)^2)\boldsymbol v_\parallel]\\
&=[0,\boldsymbol v_\parallel]。
\end{aligned}
$$

接下来我们证明垂直分量在进行上述变换后等价于在垂直于 $\boldsymbol u$ 的平面内逆时针旋转了 $2\theta$，且得到的四元数实部为 $0$。由于 $\boldsymbol v_\perp\cdot\boldsymbol u=0$，取 $\boldsymbol w=\boldsymbol u\times\boldsymbol v_\perp$，则 $\boldsymbol u$、$\boldsymbol v_\perp$、$\boldsymbol w$ 两两垂直。据此有

$$
\begin{aligned}
qv_\perp q^\star&=[\cos\theta,(\sin\theta)\boldsymbol u][0,\boldsymbol v_\perp][\cos\theta,-(\sin\theta)\boldsymbol u]\\
&=[0,(\cos\theta)\boldsymbol v_\perp+(\sin\theta)\boldsymbol w][\cos\theta,-(\sin\theta)\boldsymbol u]\\
&=[0,(\cos^2\theta)\boldsymbol v_\perp+(\sin\theta\cos\theta)\boldsymbol w-(\cos\theta)\boldsymbol v_\perp\times(\sin\theta)\boldsymbol u-(\sin\theta)\boldsymbol w\times(\sin\theta)\boldsymbol u]\\
&=[0,(\cos^2\theta-\sin^2\theta)\boldsymbol v_\perp+2(\sin\theta\cos\theta)\boldsymbol w]\\
&=[0,(\cos 2\theta)\boldsymbol v_\perp+(\sin 2\theta)\boldsymbol w]。
\end{aligned}
$$

我们知道 $qvq^\star=q(v_\parallel+v_\perp)q^\star=qv_\parallel q^\star+qv_\perp q^\star$，因此定理得证。

`````

因此，如果我们希望将一个三维向量 $\boldsymbol v$ 绕单位长度的旋转轴 $\boldsymbol u$ 旋转 $\theta$ 弧度，进行如下步骤即可：
1. 构造四元数 $q=\left[\cos\frac\theta 2,\left(\sin\frac\theta 2\right)\boldsymbol u\right]$ 和 $v=[0,\boldsymbol v]$。
2. 取 $qvq^\star$ 的虚部得到旋转后的向量。

值得注意的是，对于任意四元数 $q$、$v$，都有 $qvq^\star=(-q)v(-q)^\star$，因此单位四元数 $q$ 与其相反数 $-q$ 表示的是一样的旋转。

四元数也可以很方便地进行旋转的复合运算。假设我们对三维向量 $\boldsymbol v$ 依次进行了单位四元数 $q_1$ 和 $q_2$ 所表示的旋转，则旋转后向量即为 $q_2(q_1vq_1^\star)q_2^\star$ 的虚部；根据乘法和共轭的定义不难得出 $q_1^\star q_2^\star=(q_2q_1)^\star$，因此旋转后的向量就是 $(q_2q_1)v(q_2q_1)^\star$ 的虚部。这说明先进行 $q_1$ 所表示的旋转，再进行 $q_2$ 的，等价于进行 $q_2q_1$ 所表示的旋转。

### 四元数插值

运动学中一个很常见的问题就是四元数插值，即计算出两个旋转之间的某个中间值；例如在将一个单点固定的物体从一个姿态随时间匀速旋转到另一个姿态时，就会用到四元数的插值。现在我们用更严谨的语言描述这个问题：给定两个单位四元数 $p, q$，和一个参数 $t \in [0, 1]$, 我们希望能够找到这么一个中间四元数 $r(p, q, t)$ 作为插值结果，使得当 $t$ 取值从 $0$ 变为 $1$ 的时候，$r(p, q, t)$ 取值能够平滑的从 $p$ 过渡到 $q$。对于二元插值问题，常用的解法是取 $r(t,p,q)=a(t)p+b(t)q$，即用 $p$ 和 $q$ 的加权和作为结果。


````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-kinematic_principles-quaternion_interpolation
:width: 100 %

```{image} fig/animation-kinematic_principles-quaternion_lerp.png
:alt: 四元数的线性插值
```

```{image} fig/animation-kinematic_principles-quaternion_slerp.png
:alt: 四元数的球面线性插值
```

四元数的插值方式
````

最简单的方法是进行线性插值（linear interpolation，Lerp），即取 $a(t)=1-t$、$b(t)=t$。但是线性插值效果并不理想：首先，线性插值的结果都落在四维超球面的二维弦上，因此插值结果不一定是单位四元数。即使通过归一化将结果变为单一四元数，但是其在球面上的运动速度并不均匀。不难得出当 $t$ 在 $[0,1]$ 内匀速运动时，归一化之前四元数模长越小，归一化后其在球面上的运动速度越快。

另外一种想法是在四维超球面上进行线性插值。假定 $p$、$q$ 之间的夹角为 $\theta$，也即 $\cos \theta = p \cdot q$，我们找出球面上位于 $p$、$q$ 连线上的点 $r$，使得 $p \cdot r = \cos t\theta$ 且 $q \cdot r = \cos [(1-t)\theta]$，此时球面上的线性插值就可以克服普通线性插值的所有问题。仍然假设 $r = a(t)p + b(t)q$，我们考虑如何求解 $a(t)$ 和 $b(t)$ 的取值。对插值公式两侧点乘 $q$ 可得

$$
\begin{aligned}
r\cdot p&=a(t)p\cdot p+b(t)q\cdot p，\\
\cos t\theta&=a(t)+b(t)\cos\theta，
\end{aligned}
$$

再对插值公式两侧点乘 $q$ 可得

$$
\begin{aligned}
r\cdot q&=a(t)p\cdot q+b(t)q\cdot q，\\
\cos[(1-t)\theta]&=a(t)\cos\theta+b(t)。
\end{aligned}
$$

联立上述方程可解得

$$
\begin{aligned}
a(t)&=\frac{\cos t\theta-\cos[(1-t)\theta]\cos\theta}{1-\cos^2\theta}=\frac{\sin[(1-t)\theta]}{\sin\theta}，\\
b(t)&=\frac{\cos[(1-t)\theta]-\cos t\theta\cos\theta}{1-\cos^2\theta}=\frac{\sin t\theta}{\sin\theta}。
\end{aligned}
$$

这个插值方式称为球面线性插值（spherical linear interpolation，Slerp），其公式为

$$
\mathrm{Slerp}(p,q,t)=\frac{p\sin[(1-t)\theta]+q\sin t\theta}{\sin\theta}。
$$ (animation-kinematic_principles-quaternion_slerp)

## 其他旋转表示

三维旋转还可以由 {numref}`sec-geometry-transformation-3d` 中介绍的欧拉角以及轴角法来表示，前者将三自由度的旋转表示成三个绕坐标轴旋转的复合，后者使用一个向量来表示，向量的方向为旋转轴，模长为绕旋转轴按右手螺旋定则旋转的弧度。在主观动态的处理当中，这两种旋转表示并不常见，即便遇到也是将其转换成矩阵或者四元数再处理。
