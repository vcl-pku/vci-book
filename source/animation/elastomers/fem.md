(sec-animation-elastomers-fem)=
# 有限元方法

```{figure} fig/animation-elastomers-tetrahedron.png
:width: 25 %
:name: fig-animation-elastomers-tetrahedron

一个正四面体形状的弹性体被离散化成弹簧质点系统，其底面三个黑色顶点固定，顶部蓝色顶点受到向下的力 $\boldsymbol F$ 的作用。
```

弹簧质点系统给出了一个对弹性物体十分简单的建模，在一定范围内的形变下能够较好地模拟出弹性的动态；然而对于一些较为极端的情形，它将会产生错误的结果。我们以一个体积很小的弹性正四面体为例，其底面固定，一较大的向下的外力 $\boldsymbol F$ 作用于四面体的顶部。如{numref}`fig-animation-elastomers-tetrahedron` 所示，在弹簧质点系统下这个正四面体会自然地被空间离散化成四个处于顶点处、由弹簧两两连接的质点，每根弹簧的原长为正四面体的边长 $l$，劲度系数为 $k$；底面的三个质点（{numref}`fig-animation-elastomers-tetrahedron` 中的黑色顶点）固定，顶部的质点（{numref}`fig-animation-elastomers-tetrahedron` 中的蓝色顶点）受到力 $\boldsymbol F$ 的作用。这个场景的动态如{numref}`fig-animation-elastomers-tetrahedron_dynamics` 所示：初始时四面体静止，顶部质点只受到 $\boldsymbol F$ 的作用开始向下运动；随后由于顶部质点所连接的三根弹簧被压缩，顶部质点还会受到三根弹簧的弹力，由于是正四面体，三个弹力的合力向上，这也符合弹性体总是倾向于恢复原状的性质；但是三根弹簧的合力大小存在上界，当 $\|\boldsymbol F\|>3kl$（即 $\boldsymbol F$ 的大小比三根弹簧压缩至 $0$ 长度的弹力总和还大）时，顶部质点的合力一直向下，从而会一直加速向下运动，即便整个四面体已经被完全压扁乃至反向；在四面体反向后更严重的问题发生了，此时弹簧的合力朝下，也就是说即便撤掉力 $\boldsymbol F$，四面体也不会恢复至原状。

````{subfigure} ABCD
:layout-sm: AB|CD
:gap: 8px
:name: fig-animation-elastomers-tetrahedron_dynamics
:width: 100 %

```{image} fig/animation-elastomers-tetrahedron_a.png
```


```{image} fig/animation-elastomers-tetrahedron_b.png
```


```{image} fig/animation-elastomers-tetrahedron_c.png
```


```{image} fig/animation-elastomers-tetrahedron_d.png
```

正四面体弹簧质点系统的动态
````

这个例子告诉我们弹簧质点系统只能模拟一个弹性的“框架”，而在生活中常见的弹性体通常是具有一定体积的连续物体，所以不应当出现上述被完全压扁至 $0$ 体积的情况；即便是在一些极端的数值条件下出现了体积翻转的情况，弹性力也应当趋向于恢复成体积翻转前的原本形状。

有限元方法就具备这样的性质，它将一个物体空间离散化成四面体网格，每个最小模拟单元不再是弹簧与质点，而是单个四面体；每个四面体无缝拼接在一起，形成一个占有一定体积的连续形状，从而能够更加贴近现实中弹性体的行为。但是这样的模型也会更加的复杂，我们需要了解更多的物理背景才能够正确地借助这个模型进行模拟。

## 物理模型

在本章中，我们需要借助连续介质力学（continuum mechanics）中的一些概念来刻画弹性体的物理动态。在接触一个新的力学分支时，我们应当先了解它的语言，理解它描述各种力学概念的方式，随后才能够应用它完成我们想要的任务。对于弹性体来讲，我们先从其运动学开始，理解如何描述一个弹性体的形变；随后再进入到动力学，从弹性体的能量到它的内力；再将二者联系起来，从而理解力如何影响弹性体的运动。

### 描述形变

在弹簧质点系统中，我们通过记录每个质点的位置来描述弹性体的当前形状；但对于一个连续介质，存在不可数个质点，因此我们也应当将形变的描述方式拓展成场，将未形变状态下每一个点的位置都映射成形变后的位置。具体来讲，我们首先将未形变的弹性体放置于一个空间坐标系当中，并记其所占据的空间区域为 $\Omega$，这个区域又称为参考构型（reference configuration）；我们记参考构型内的点为 $\boldsymbol X$，该点在形变后的位置为 $\boldsymbol x$，定义变形函数（deformation function）

$$
\boldsymbol\phi:\Omega&\to\mathbb R^3\\
\boldsymbol X&\mapsto\boldsymbol x
$$ (animation-elastomers-deformation_function)

即为对弹性体形变的描述。

```{figure} fig/animation-elastomers-deform_map.png
:width: 100 %
:name: fig-animation-elastomers-deform_map

参考构型 $\Omega$、形变前位置 $\boldsymbol X$、形变后位置 $\boldsymbol x$ 与变形函数 $\boldsymbol\phi$ 的关系
```

> jr: {numref}`fig-animation-elastomers-deform_map` 需要重画。

变形函数 $\boldsymbol\phi$ 确实能够充分地表示出弹性体的形变，但作为一个**全局**的信息表示，它包含了过多的信息。我们马上就会看到，弹性体每一个点的能量与内力只由其**局部**的形变所决定。因此，在连续介质力学中会引入形变梯度（deformation gradient）的概念，形变梯度一般记为 $\boldsymbol F$，其定义为变形函数 $\boldsymbol\phi$ 关于形变前位置 $\boldsymbol X$ 的雅可比矩阵：

$$
\boldsymbol F\mathrel{\mathop:}=\frac{\partial(\phi_1,\phi_2,\phi_3)}{\partial(X_1,X_2,X_3)}=\begin{bmatrix}\frac{\partial\phi_1}{\partial X_1}&\frac{\partial\phi_1}{\partial X_2}&\frac{\partial\phi_1}{\partial X_3}\\\frac{\partial\phi_2}{\partial X_1}&\frac{\partial\phi_2}{\partial X_2}&\frac{\partial\phi_2}{\partial X_3}\\\frac{\partial\phi_3}{\partial X_1}&\frac{\partial\phi_3}{\partial X_2}&\frac{\partial\phi_3}{\partial X_3}\end{bmatrix}，
$$ (animation-elastomers-deformation_gradient)

其中 $\boldsymbol\phi(\boldsymbol X)=\begin{pmatrix}\phi_1&\phi_2&\phi_3\end{pmatrix}^\top$，$\boldsymbol X=\begin{pmatrix}X_1&X_2&X_3\end{pmatrix}^\top$。我们知道导数可以很好地反映原函数的局部特征，所以在连续介质力学中形变梯度是最常用也最直观的刻画弹性体形变的量之一，变形函数反而没有那么重要。

```{attention}
由式 {eq}`animation-elastomers-deformation_gradient` 可见，形变梯度 $\boldsymbol F$ 是一个关于形变前坐标 $\boldsymbol X$ 的矩阵函数。
```

### 描述能量

弹性体的形变会累积弹性势能，在连续介质力学中又称为应变能（strain energy）。由于总能量完全由弹性体的形变决定，我们可以将应变能表示成变形函数的泛函 $E[\boldsymbol\phi]$。值得注意的是，在这种表示中，应变能的值仅与弹性体的**最终**形变有关，和弹性体的变形**路径**（或**历史时刻**的形变）无关，也即弹性力是保守力（conservative force）。这个性质是超弹性（hyperelastic）材料的特性，在本章中我们只会讨论这一种材料的模拟。

一般来讲，弹性体不同位置的材料会有不同的形变，因此为了准确描述每一处材料的动态，我们应当把能量定义在局部范围上。与变形函数的定义类似，我们定义一个以参考构型下的位置为自变量的能量密度函数 $\Psi[\boldsymbol\phi;\boldsymbol X]$，其含义为单位体积未形变材料所蕴含的应变能。将能量密度在参考构型上积分即可得到应变能：

$$
E[\boldsymbol\phi]=\int_\Omega\Psi[\boldsymbol\phi;\boldsymbol X]\mathrm d\boldsymbol X。
$$

```{attention}
我们现在没有给出能量密度 $\Psi$ 的具体形式，只描述了能量由什么决定。事实上，$\Psi$ 的形式有多种，对应于不同性质的弹性材料，{numref}`sec-animation-elastomers-fem-models` 将会给出一些常见的形式。
```

下面我们考虑参考构型下一个特定位置 $\boldsymbol X_0$ 的能量密度 $\Psi[\boldsymbol\phi;\boldsymbol X_0]$。由于能量密度是一个局部的物理量，它应当只与 $\boldsymbol X_0$ 附近一个无穷小的邻域形变后的状态相关，在 $\boldsymbol X_0$ 处 $\boldsymbol\phi(\boldsymbol X)$ 进行一阶泰勒展开

$$
\boldsymbol\phi(\boldsymbol X)&\approx\boldsymbol\phi(\boldsymbol X_0)+\frac{\partial\boldsymbol\phi}{\partial\boldsymbol X}(\boldsymbol X_0)(\boldsymbol X-\boldsymbol X_0)\\
&=\boldsymbol x_0+\boldsymbol F(\boldsymbol X_0)(\boldsymbol X-\boldsymbol X_0)\\
&=\boldsymbol F(\boldsymbol X_0)\boldsymbol X+\boldsymbol x_0-\boldsymbol F(\boldsymbol X_0)\boldsymbol X_0，
$$ (animation-elastomers-phi_taylor_expansion)

其中，$\boldsymbol x_0=\boldsymbol\phi(\boldsymbol X_0)$ 为其大写字母符号对应的形变后位置，本章中将继续遵循这个命名习惯。令 $\boldsymbol F_0=\boldsymbol F(\boldsymbol X_0)$（这个命名习惯也会在本章中继续使用），$\boldsymbol t=\boldsymbol x_0-\boldsymbol F_0\boldsymbol X_0$，则式 {eq}`animation-elastomers-phi_taylor_expansion` 最终可化为 $\boldsymbol\phi(\boldsymbol X)\approx\boldsymbol F_0\boldsymbol X+\boldsymbol t$。这告诉我们参考构型下 $\boldsymbol X_0$ 周围很小一块区域的形变可以完全由 $\boldsymbol F_0$ 和 $\boldsymbol t$ 刻画，而 $\boldsymbol t$ 仅仅代表这个小区域整体的平移，不会带来任何变形，所以这个小区域的能量应当完全由 $\boldsymbol F_0$ 决定，也即 $\Psi$ 能够表示成只关于形变梯度的函数：$\Psi[\boldsymbol\phi;\boldsymbol X_0]=\hat\Psi(\boldsymbol F(\boldsymbol X_0))$。为了简便，我们在接下来将使用 $\Psi(\boldsymbol F)$ 来表示能量密度函数。

(sec-animation-elastomers-fem-force)=
### 描述力

弹性体积累了弹性势能就会产生弹性力，我们仍然可以借助{numref}`fig-animation-elastomers-simple_example` 中的例子来回顾一下势能与保守力之间的关系：当粒子处于位置 $\boldsymbol x=\begin{pmatrix}x&y&z\end{pmatrix}^\top$ 时，其重力势能为 $E(\boldsymbol x)=m\boldsymbol{G\cdot x}=mgz$，其中 $\boldsymbol G=\begin{pmatrix}0&0&g\end{pmatrix}^\top$ 为重力加速度（取 $z$ 轴正方向为竖直向上），那么粒子所受重力即为

$$
\boldsymbol f_\mathrm{gravity}=-\frac{\partial E(\boldsymbol x)}{\partial\boldsymbol x}=\begin{pmatrix}0\\0\\-mg\end{pmatrix}。
$$

由此可见，保守力等于能量的负梯度。在连续介质中，由于存在不可数无穷多个质点，我们同样需要类似能量密度一样定义一个力密度（force density）$\boldsymbol f(\boldsymbol X)$，代表单位体积未形变材料所受的力。对于标准构型内的任意有限区域 $A\subset\Omega$，其形变后所受力的总和为力密度在 $A$ 上的积分：

$$
\boldsymbol f_\mathrm{aggregate}(A)=\int_A\boldsymbol f(\boldsymbol X)\mathrm d\boldsymbol X。
$$

然而，只定义这样一种力密度不足以描述一个弹性体的全部受力，我们还需要引入牵引力（traction）的概念来描述弹性体表面所受的力。牵引力 $\boldsymbol\tau:\partial\Omega\to\mathbb R^3$ 是一个定义在标准构型表面的向量函数，含义是每单位面积未形变材料表面所受的力。对于标准构型边界上任意有限区域 $B\subset\partial\Omega$，其形变后所受的表面力为牵引力在 $B$ 上的积分：

$$
\boldsymbol f_\mathrm{aggregate}(B)=\oint_S\boldsymbol\tau(\boldsymbol X)\mathrm dS。
$$

我们为什么要将弹性体的力密度与表面受力分开表示呢？读者不难注意到，牵引力的单位是牛顿每平方米，而力密度的单位是牛顿每立方米，也就是说牵引力带来的力是远比力密度带来的大。这也是弹性体常见的受力情况——表面的受力要远大于内部的受力，如果我们仅使用力密度来描述整个弹性体的受力的话，那么表面处的力密度将会变成无穷大，这样在计算上就没有意义了。因此，为了弥补定义上的缺陷，我们额外引入牵引力来描述弹性体表面所受的力，这样一来力密度和牵引力就都是有限函数了。

但仅到这里还不能解开读者所有的疑惑——为什么弹性体表面的受力和内部受力会有这么大差别呢？如{numref}`fig-animation-elastomers-interior_surface` 所示，我们在弹性体的内部取一点 $P_1$，表面处取一点 $P_2$，然后考察两点附近小邻域的受力：它们都会受到来自周围材料的弹性力，而区别在于内部点 $P_1$ 受到的力是来自四面八方的，几乎能够完全抵消；$P_2$ 由于处在表面，有一侧没有材料，所以只会受到单侧的弹性力，形成一种“强烈”的不平衡状态。这就是为什么表面受到的力一般会远大于内部受到的力。

```{figure} fig/animation-elastomers-interior_surface.png
:width: 50 %
:name: fig-animation-elastomers-interior_surface

内部与表面处受力的区别
```

### 能量与力的关系

在 {numref}`sec-animation-elastomers-fem-force` 的开头我们回顾了质点重力场中能量与力的关系，但是对本章讨论的弹性体而言情况会更加复杂一些，我们不能直接建立能量密度 $\Psi$ 与力密度 $\boldsymbol f(\boldsymbol X)$ 和牵引力 $\boldsymbol\tau(\boldsymbol X)$ 之间的关系。幸运的是，这个关系可以通过引入一个中间变量建立起来，这个中间变量叫做第一类皮奥拉-基尔霍夫应力张量（first Piola-Kirchhoff stress tensor），一般记作 $\boldsymbol P$。接下来我们不加证明地给出 $\boldsymbol P$ 的性质，对更深层原理感兴趣的同学可以参考 {cite}`sifakis2012fem`。

首先，我们可以通过能量密度 $\Psi$ 计算 $\boldsymbol P$：

$$
\boldsymbol P=\frac{\partial\Psi(\boldsymbol F)}{\partial\boldsymbol F}。
$$ (animation-elastomers-calc_stress)

边界上的牵引力 $\boldsymbol\tau$ 与 $\boldsymbol P$ 具有如下的关系：

$$
\boldsymbol\tau(\boldsymbol X)=-\boldsymbol P\cdot\boldsymbol N,\quad\forall\boldsymbol X\in\partial\Omega，
$$

其中 $\boldsymbol N$ 为 $\boldsymbol X$ 处**形变前**物体的表面法向，这里的点乘就是矩阵乘法。

另外，力密度 $\boldsymbol f$ 与 $\boldsymbol P$ 具有如下的关系：

$$
\boldsymbol f(\boldsymbol X)=\mathrm{div}\boldsymbol P(\boldsymbol X)，
$$

写成分量形式就是（省略自变量 $\boldsymbol X$）

$$
f_i=\sum_{j=1}^3\frac{\partial P_{ij}}{\partial X_j}。
$$

(sec-animation-elastomers-fem-models)=
### 常见超弹性模型

前面的讨论中我们给出了弹性体的形变、能量和应力之间的关系，但是我们还没办法计算一个弹性体的具体受力情况，事实上，我们只需要知道能量密度 $\Psi(\boldsymbol F)$ 的具体表达式即可进行计算。在本节，我们将给出一些常见超弹性模型的能量密度的具体形式，并且为了避免每次都计算一遍矩阵求导，我们会同时给出 $\boldsymbol P$ 的表达式。

## 空间离散化

## 数值求解算法
