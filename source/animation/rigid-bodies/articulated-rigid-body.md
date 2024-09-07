(sec-animation-rigid_bodies-articulated)=
# 铰链刚体

在一些特殊的场景中，还会出现一些铰链刚体（articulated rigid body），即通过一些关节（joint）连接成一体的多个刚体。常见的铰链刚体包括人体骨骼、机械臂、门窗、车辆等，在机器人学、人体动画、具身控制等应用场景中出现频率尤其多。在铰链刚体仿真中，我们需要额外处理由关节带来的约束力，这个约束力不像碰撞处理那样容易给出显式的形式，往往需要借助其他的形式隐式地引入到系统中。

在本节，我们会介绍两种处理铰链刚体的方法——约束法和广义坐标法。这两种方法的本质不同在于描述关节的方式，前者是使用关于速度的约束来描述关节，后者使用关节的自由度来描述。

## 约束法

{numref}`fig-animation-rigid_bodies-joints` 中包含了常见的四种关节，球关节（ball joint）允许两个刚体围绕着一个公共点做自由旋转，但不允许该点的相对位移；万向节（universal joint）包含两个旋转轴，允许刚体之间做两个自由度的旋转；合页（hinge joint）允许两个刚体围绕同一个轴转动；滑动关节（slider joint）允许两个刚体之间产生单个方向的相对滑动，不允许刚体之间的相对转动。

````{subfigure} AB|CD
:layout-sm: A|B|C|D
:gap: 8px
:subcaptions: below
:name: fig-animation-rigid_bodies-joints
:width: 100 %

```{image} fig/animation-rigid_bodies-ball_joint.jpg
:alt: 球关节
```

```{image} fig/animation-rigid_bodies-universal_joint.jpg
:alt: 万向节
```

```{image} fig/animation-rigid_bodies-hinge_joint.jpg
:alt: 合页
```

```{image} fig/animation-rigid_bodies-slider_joint.jpg
:alt: 滑动关节
```

一些常见的关节[^fig-joints]
````

[^fig-joints]: 图片来源：http://ode.org/ode-latest-userguide.html#sec_7_0_0

现在我们假设场景中只有一个由单个关节连接两个刚体的铰链刚体。设关节的位置在两个刚体的标准构型下坐标分别为 $\boldsymbol X_1$ 和 $\boldsymbol X_2$（对于滑动关节这个定义并不重要），当前两个刚体的旋转矩阵分别为 $\boldsymbol R_1$ 和 $\boldsymbol R_2$，质心位置分别为 $\boldsymbol c_1$ 和 $\boldsymbol c_2$。接下来我们分步推导这个系统要如何模拟。

### 用约束描述关节

球关节对两个刚体运动的限制即为 $\boldsymbol X_1$ 和 $\boldsymbol X_2$ 在刚性变换后的位置相同，即

$$
\boldsymbol R_1\boldsymbol X_1+\boldsymbol c_1=\boldsymbol R_2\boldsymbol X_2+\boldsymbol c_2。
$$ (animation-rigid_bodies-articulated-ball_position)

在约束法中，我们需要将关节带来的限制表示成关于速度和角速度的约束，这个约束可以由式 {eq}`animation-rigid_bodies-articulated-ball_position` 两端关于时间求导得到：

$$
\boldsymbol\omega_1\times\boldsymbol R_1\boldsymbol X_1+\boldsymbol v_1-\boldsymbol\omega_2\times\boldsymbol R_2\boldsymbol X_2-\boldsymbol v_2=\mathbf 0。
$$ (animation-rigid_bodies-articulated-ball_constraint)

若将 $\boldsymbol R_1$ 和 $\boldsymbol R_2$ 视为常量，我们可以将式 {eq}`animation-rigid_bodies-articulated-ball_constraint` 中的约束写成矩阵的形式：

$$
\boldsymbol J_\mathrm{ball}\boldsymbol u\mathrel{\mathop:}=\begin{pmatrix}\mathbf I&-[\boldsymbol R_1\boldsymbol X_1]&-\mathbf I&[\boldsymbol R_2\boldsymbol X_2]\end{pmatrix}\begin{pmatrix}\boldsymbol v_1\\\boldsymbol\omega_1\\\boldsymbol v_2\\\boldsymbol\omega_2\end{pmatrix}=\mathbf 0，
$$ (animation-rigid_bodies-articulated-ball_matrix)

其中 $\boldsymbol J_\mathrm{ball}$ 是速度约束关于两个刚体的速度与角速度的雅可比矩阵；并且为了方便推导，我们将所有刚体的速度与角速度堆叠成向量 $\boldsymbol u$。

万向节对两个刚体运动的限制在球关节的基础上增加了一条：两刚体之间不能沿一个特定轴 $\boldsymbol a$（即与{numref}`fig-animation-rigid_bodies-joints` 中万向节两个轴垂直的向量，这是一个随时间变化的量）发生相对旋转，即

$$
(\boldsymbol\omega_1-\boldsymbol\omega_2)\cdot\boldsymbol a=0。
$$ (animation-rigid_bodies-articulated-universal_constraint)

```{hint}
读者不妨想一想：为何相对角速度等于 $\boldsymbol\omega_1-\boldsymbol\omega_2$？
```

因此万向节约束的雅可比矩阵可以表示成

$$
\boldsymbol J_\mathrm{universal}=\begin{pmatrix}\mathbf I&-[\boldsymbol R_1\boldsymbol X_1]&-\mathbf I&[\boldsymbol R_2\boldsymbol X_2]\\\mathbf 0&\boldsymbol a^\top&\mathbf 0&-\boldsymbol a^\top\end{pmatrix}。
$$

合页与万向节很相似，在球关节约束的基础上增加两个轴 $\boldsymbol a_1$ 和 $\boldsymbol a_2$ 上不能产生相对旋转即可，因此我们可以直接写出合页约束的雅可比矩阵：

$$
\boldsymbol J_\mathrm{hinge}=\begin{pmatrix}\mathbf I&-[\boldsymbol R_1\boldsymbol X_1]&-\mathbf I&[\boldsymbol R_2\boldsymbol X_2]\\\mathbf 0&\boldsymbol a_1^\top&\mathbf 0&-\boldsymbol a_1^\top\\\mathbf 0&\boldsymbol a_2^\top&\mathbf 0&-\boldsymbol a_2^\top\end{pmatrix}。
$$

### 重新表达刚体时间积分

在 {numref}`sec-animation-rigid_bodies-dynamics-time_integration` 的步骤中，对速度和角速度的时间积分可表示成如下等式：

$$
&\boldsymbol v_i^\mathrm{new}=\boldsymbol v_i+hm_i^{-1}\boldsymbol F_i，\\
&\boldsymbol\omega_i^\mathrm{new}=\boldsymbol\omega_i+h\boldsymbol I_i^{-1}(\boldsymbol\tau_i-\boldsymbol\omega_i\times\boldsymbol I_i\boldsymbol\omega_i)，
$$

其中下标 $i\in\{1,2\}$ 表明该物理量属于哪个刚体，这里我们用上标 $\mathrm{new}$ 表示下一个时间步的量，无上标表示当前时刻的量；这两个式子还可以统一写成如下的矩阵形式：

$$
\begin{pmatrix}\boldsymbol v_i^\mathrm{new}\\\boldsymbol\omega_i^\mathrm{new}\end{pmatrix}=\begin{pmatrix}\boldsymbol v_i\\\boldsymbol\omega_i\end{pmatrix}+h\begin{pmatrix}m_i\mathbf I&\mathbf 0\\\mathbf 0&\boldsymbol I_i\end{pmatrix}^{-1}\begin{pmatrix}\boldsymbol F_i\\\boldsymbol\tau_i-\boldsymbol\omega_i\times\boldsymbol I_i\boldsymbol\omega_i\end{pmatrix}。
$$

我们记 $\boldsymbol M_i=\begin{pmatrix}m_i\mathbf I&\mathbf 0\\\mathbf 0&\boldsymbol I_i\end{pmatrix}$，$\boldsymbol\xi_i=\begin{pmatrix}\boldsymbol F_i\\\boldsymbol\tau_i-\boldsymbol\omega_i\times\boldsymbol I_i\boldsymbol\omega_i\end{pmatrix}$，则上式可继续简化为

$$
\boldsymbol u_i^\mathrm{new}=\boldsymbol u_i+h\boldsymbol M_i^{-1}\boldsymbol\xi_i。
$$

我们还可以将 $i=1$ 和 $i=2$ 的情形合并到一起，记 $\boldsymbol M=\begin{pmatrix}\boldsymbol M_1&\mathbf 0\\\mathbf 0&\boldsymbol M_2\end{pmatrix}$，$\boldsymbol\xi=\begin{pmatrix}\boldsymbol\xi_1\\\boldsymbol\xi_2\end{pmatrix}$，即可得到重新表达成矩阵形式的刚体时间积分步骤：

$$
\boldsymbol u^\mathrm{new}=\boldsymbol u+h\boldsymbol M^{-1}\boldsymbol\xi。
$$ (animation-rigid_bodies-mat_time_int)

### 带约束的时间积分

现在我们要为式 {eq}`animation-rigid_bodies-mat_time_int` 的时间积分加上由关节带来的速度约束，即 $\boldsymbol J\boldsymbol u^\mathrm{new}=\mathbf 0$，其中 $\boldsymbol J$ 根据关节的种类取 $\boldsymbol J_\mathrm{ball}$、$\boldsymbol J_\mathrm{universal}$ 或 $\boldsymbol J_\mathrm{hinge}$ 中的一种。关节之所以能让速度满足这样的约束，是因为提供了一个额外的约束力，也即在考虑到关节的作用时，式 {eq}`animation-rigid_bodies-mat_time_int` 等号右边要再加一项。现在我们假设关节是光滑的（不会导致能量的损耗），则它的约束就是理想约束；根据理论力学中的定义，约束力的虚功为 $0$，也即约束力方向应与任意满足 $\boldsymbol{Jw}=\mathbf 0$ 的速度 $\boldsymbol w$ 正交，也就是与 $\ker\boldsymbol J$ 正交，这说明约束力属于 $\boldsymbol J$ 的行空间，我们用 $\boldsymbol J^\top\boldsymbol\lambda$ 表示约束力。

至此，我们的时间积分从式 {eq}`animation-rigid_bodies-mat_time_int` 变成了如下关于 $\boldsymbol\xi$ 和 $\boldsymbol u^\mathrm{new}$ 的线性方程组：

$$
\begin{cases}
\boldsymbol u^\mathrm{new}=\boldsymbol u+h\boldsymbol M^{-1}(\boldsymbol\xi+\boldsymbol J^\top\boldsymbol\lambda)\\
\boldsymbol J\boldsymbol u^\mathrm{new}=\mathbf 0
\end{cases}。
$$

将 $\boldsymbol u^\mathrm{new}$ 代入 $\boldsymbol J\boldsymbol u^\mathrm{new}=\mathbf 0$ 可得到关于 $\boldsymbol\lambda$ 的线性系统：

$$
\boldsymbol J\boldsymbol M^{-1}\boldsymbol J^\top\boldsymbol\lambda=-\frac 1h\boldsymbol{Ju}-\boldsymbol J\boldsymbol M^{-1}\boldsymbol\xi。
$$

不难看出 $\boldsymbol J\boldsymbol M^{-1}\boldsymbol J^\top$ 是正定的，因此有很多高效的求解算法；在求得 $\boldsymbol\lambda$ 之后代入第一个方程即可得到下个时间步的速度与角速度。

至此我们已经完全可以模拟带有一个关节、两个刚体的场景了，对于多个关节、多个刚体的场景只需要我们关节连接的拓扑结构构造好 $\boldsymbol J$ 和 $\boldsymbol M$ 的形式，也能用同样的方法求出 $\boldsymbol u^\mathrm{new}$，具体的实现方法交给读者思考。

## 广义坐标法