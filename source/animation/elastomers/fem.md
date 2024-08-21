(sec-animation-elastomers-fem)=
# 有限元方法

```{figure} fig/animation-elastomers-tetrahedron.png
:width: 25 %
:name: fig-animation-elastomers-tetrahedron

一个正四面体形状的弹性体被离散化成弹簧质点系统，其底面三个黑色顶点固定，顶部蓝色顶点受到向下的力 $\boldsymbol F$ 的作用。
```

弹簧质点系统给出了一个对弹性物体十分简单的建模，在一定范围内的形变下能够较好地模拟出弹性的动态；然而对于一些较为极端的情形，它将会产生错误的结果。我们以一个体积很小的弹性正四面体为例，其底面固定，一较大的向下的外力 $\boldsymbol F$ 作用于四面体的顶部。如{numref}`fig-animation-elastomers-tetrahedron` 所示，在弹簧质点系统下这个正四面体会自然地被空间离散化成四个处于顶点处、由弹簧两两连接的质点，每根弹簧的原长为正四面体的边长 $l$，劲度系数为 $k$；底面的三个质点（{numref}`fig-animation-elastomers-tetrahedron` 中的黑色顶点）固定，顶部的质点（{numref}`fig-animation-elastomers-tetrahedron` 中的蓝色顶点）受到力 $\boldsymbol F$ 的作用。这个场景的动态如{numref}`fig-animation-elastomers-tetrahedron_dynamics` 所示：初始时四面体静止，顶部质点只受到 $\boldsymbol F$ 的作用开始向下运动；随后由于顶部质点所连接的三根弹簧被压缩，顶部质点还会受到三根弹簧的弹力，由于是正四面体，三个弹力的合力向上，这也符合弹性体总是倾向于恢复原状的性质；但是三根弹簧的合力大小存在上界，当 $\Vert\boldsymbol F\Vert>3kl$（即 $\boldsymbol F$ 的大小比三根弹簧压缩至 $0$ 长度的弹力总和还大）时，顶部质点的合力一直向下，从而会一直加速向下运动，即便整个四面体已经被完全压扁乃至反向；在四面体反向后更严重的问题发生了，此时弹簧的合力朝下，也就是说即便撤掉力 $\boldsymbol F$，四面体也不会恢复至原状。

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
\boldsymbol F\mathrel{\mathop:}=\frac{\partial(\phi_x,\phi_y,\phi_z)}{\partial(X,Y,Z)}=\begin{bmatrix}\frac{\partial\phi_x}{\partial X}&\frac{\partial\phi_x}{\partial Y}&\frac{\partial\phi_x}{\partial Z}\\\frac{\partial\phi_y}{\partial X}&\frac{\partial\phi_y}{\partial Y}&\frac{\partial\phi_z}{\partial Z}\\\frac{\partial\phi_z}{\partial X}&\frac{\partial\phi_z}{\partial Y}&\frac{\partial\phi_z}{\partial Z}\end{bmatrix}，
$$ (animation-elastomers-deformation_gradient)

其中 $\boldsymbol\phi(\boldsymbol X)=\begin{pmatrix}\phi_x&\phi_y&\phi_z\end{pmatrix}^\top$，$\boldsymbol X=\begin{pmatrix}X&Y&Z\end{pmatrix}^\top$。我们知道导数可以很好地反映原函数的局部特征，所以在连续介质力学中形变梯度是最常用也最直观的刻画弹性体形变的量之一，变形函数反而没有那么重要。

```{attention}
由式 {eq}`animation-elastomers-deformation_gradient` 可见，形变梯度 $\boldsymbol F$ 是一个关于形变前坐标 $\boldsymbol X$ 的矩阵函数。
```

(sec-animation-elastomers-fem-energy)=
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

(sec-animation-elastomers-fem-energy_force)=
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

前面的讨论中我们给出了弹性体的形变、能量和应力之间的关系，但是我们还没办法计算一个弹性体的具体受力情况。事实上，我们只需要知道能量密度 $\Psi(\boldsymbol F)$ 的具体表达式即可进行计算，每一种能量密度的具体形式对应于一种本构模型（constitutive model），它充分描述了弹性体的全部力学性质。在本节，我们将给出一些常见超弹性模型的能量密度的具体形式，并且为了避免每次都计算一遍矩阵求导，我们会同时给出 $\boldsymbol P$ 的表达式。

#### 线性模型

正常来讲，能量密度的具体形式应当是 $\boldsymbol F$ 的表达式。但是我们往往难以直接使用 $\boldsymbol F$ 的元素直接描述出形变与力的关系，而是需要借助一些中间变量。现在我们介绍其中一种中间变量——格林应变张量（Green strain tensor），定义如下：

$$
\boldsymbol E=\frac 12\left(\boldsymbol F^\top\boldsymbol F-\mathbf I\right)。
$$ (animation-elastomers-fem-green_strain_tensor)

格林应变张量具有一些良好的性质，使其能够较好地反映出弹性形变的程度。当弹性体只经历了刚性运动时，其变形函数为 $\boldsymbol\phi(\boldsymbol X)=\boldsymbol{RX}+\boldsymbol t$，其中 $\boldsymbol R$ 为旋转矩阵，$\boldsymbol t$ 为平移向量，则 $\boldsymbol F=\boldsymbol R$，此时格林应变张量为 $\boldsymbol E=\frac 12\left(\boldsymbol R^\top\boldsymbol R-\mathbf I\right)=\mathbf 0$——这表明格林应变张量不会受刚性运动的影响，又称为刚性运动下的不变量（invariant）。对于更一般的形变，我们可以将形变梯度进行极分解 $\boldsymbol F=\boldsymbol{RS}$，表示成旋转矩阵 $\boldsymbol R$ 和对称矩阵 $\boldsymbol S$ 乘积的形式，那么格林应变张量可化为

$$
\boldsymbol E=\frac 12\left(\boldsymbol S^\top\boldsymbol R^\top\boldsymbol{RS}-\mathbf I\right)=\frac 12\left(\boldsymbol S^2-\mathbf I\right)。
$$ (animation-elastomers-fem-green_strain_tensor_in_terms_of_s)

这表明格林应变张量只和形变梯度的对称因子 $\boldsymbol S$ 有关，而 $\boldsymbol S$ 中包含了拉伸、剪切这些真正导致弹力的信息。

但是，格林应变张量也存在缺点——关于 $\boldsymbol F$ 非线性，相比线性能量形式的本构模型而言，这会加大模拟的计算量。因此，为了解决这个问题，我们引入一个 $\boldsymbol E$ 的线性近似作为小应变张量（small strain tensor），其定义如下：

$$
\boldsymbol\epsilon=\frac 12\left(\boldsymbol F+\boldsymbol F^\top\right)-\mathbf I。
$$ (animation-elastomers-fem-small_strain_tensor)

关于 $\boldsymbol\epsilon$ 是 $\boldsymbol E$ 的线性近似的证明可以参考 {cite}`sifakis2012fem`。借助小应变张量，我们立即可以定义出线性模型的能量密度：

$$
\Psi(\boldsymbol F)=\mu\mathrm{tr}\left(\boldsymbol\epsilon^2\right)+\frac\lambda 2\mathrm{tr}^2(\boldsymbol\epsilon)，
$$ (animation-elastomers-fem-linear_elasticity_energy)

其中，$\mu,\lambda$ 是拉美系数（Lamé coefficients），它们可以通过杨氏模量（Young's modulus）$k$ 和泊松比（Poisson's ratio）$\nu$ 计算得到：

$$
\begin{array}
&\mu=\frac k{2(1+\nu)}，&\lambda=\frac{k\nu}{(1+\nu)(1-2\nu)}，
\end{array}
$$

其中杨氏模量反应了材料对拉伸的抵抗能力，泊松比反应了材料的不可压性。线性模型的第一类皮奥拉-基尔霍夫应力张量为

$$
\boldsymbol P(\boldsymbol F)=2\mu\boldsymbol\epsilon+\lambda\mathrm{tr}(\boldsymbol\epsilon)\mathbf I。
$$ (animation-elastomers-fem-linear_elasticity_stress)

在线性模型中，虽然应力能够表示成形变梯度的线性函数从而能够快速地模拟，但由于小应变张量 $\boldsymbol\epsilon$ 对格林应变张量 $\boldsymbol E$ 在无形变（$\boldsymbol F=\mathbf I$）处进行了线性近似，所以只在材料形变很小的情况下才具有较好的性质。当材料形变过大时，$\boldsymbol\epsilon$ 会与 $\boldsymbol E$ 相差甚远，从而不再具有 $\boldsymbol E$ 的忽略刚性运动等性质，模拟会产生错误的结果。

#### 圣维南-基尔霍夫模型

圣维南-基尔霍夫模型（St. Venant-Kirchhoff model）的能量形式就是将式 {eq}`animation-elastomers-fem-linear_elasticity_energy` 中的小应变张量替换成格林应变张量：

$$
\Psi(\boldsymbol F)=\mu\mathrm{tr}\left(\boldsymbol E^2\right)+\frac\lambda 2\mathrm{tr}^2(\boldsymbol E)，
$$ (animation-elastomers-fem-stvk_energy)

从而此模型具有格林应变张量的全部良好性质，但它不再是一个线性的本构模型。此模型的第一类皮奥拉-基尔霍夫应力张量为

$$
\boldsymbol P(\boldsymbol F)=\boldsymbol F[2\mu\boldsymbol E+\lambda\mathrm{tr}(\boldsymbol E)\mathbf I]。
$$ (animation-elastomers-fem-stvk_stress)

圣维南-基尔霍夫模型的一个典型问题在于无法抵抗过强的压缩。当一个该模型的材料从自然状态被压缩时，在刚开始它会产生抗拒压缩、恢复原体积的弹力；但随着压缩的力度逐渐增大、材料的体积逐渐减小，会出现弹力的最大值，此后弹力将逐渐减小；直至整个材料被压缩成一个质点，此时 $\boldsymbol F=\mathbf 0$，代入式 {eq}`animation-elastomers-fem-stvk_stress` 得到 $\boldsymbol P=\mathbf 0$，所以产生的力密度和牵引力均为 $\mathbf 0$；如果力的方向保持不变导致弹性体翻转，则产生出的弹力会试图恢复成翻转的参考构型，类似本章开头提到的弹簧质点系统产生的效果。这样的性质会导致模拟出的弹性体在强力的压缩作用下很容易产生打结、翻转等非物理的现象。

> jr: 这里可以加几张图片展示 STVK 的 failure case。

#### 共旋转线性模型

线性模型只能处理微小形变，圣维南-基尔霍夫模型又引入了过多的非线性项从而导致非物理的零应力现象，共旋转线性模型（corotated linear elasticity）的提出就是为了结合二者的设计、避免二者的问题，此模型尽可能地使用形变梯度的线性项去刻画应力，同时采用最少的非线性项来保证刚性运动下的不变性。此模型的能量形式为

$$
\Psi(\boldsymbol F)=\mu\Vert\boldsymbol S-\mathbf I\Vert_\mathrm F^2+\frac\lambda 2\mathrm{tr}^2(\boldsymbol S-\mathbf I)，
$$ (animation-elastomers-fem-corotated_energy)

其中形变梯度的极分解为 $\boldsymbol F=\boldsymbol S-\mathbf I$，所以这个模型的能量形式可以完全过滤掉材料的刚体运动，同时相比于式 {eq}`animation-elastomers-fem-stvk_energy`，式 {eq}`animation-elastomers-fem-corotated_energy` 中的能量模型关于 $\boldsymbol S$ 的次数更低（前者为 $4$ 次，后者为 $2$ 次）。此模型的第一类皮奥拉-基尔霍夫应力张量为

$$
\boldsymbol P(\boldsymbol F)=2\mu(\boldsymbol F-\boldsymbol R)+\lambda\mathrm{tr}\left(\boldsymbol R^\top\boldsymbol F-\mathbf I\right)\boldsymbol R。
$$ (animation-elastomers-fem-corotated_stress)

共旋转线性模型试图找到一个最贴近形变后位置的旋转，并在这个旋转下模仿线性模型的行为，其模拟的计算量介于线性模型与圣维南-基尔霍夫模型之间，并且不会有非物理的零应力现象。

#### 新胡克模型

我们已经知道，圣维南-基尔霍夫模型和共旋转线性模型的能量和力在刚体运动下都不会发生变化，这种性质叫做旋转不变性（rotational invariance）。关于这个名称，由于能量密度的形式 $\Psi(\boldsymbol F)$ 已经表明了平移下的不变性（形变梯度 $\boldsymbol F$ 不受材料平移的影响），所以我们只会关注刚体运动中的旋转变换。下面我们给出旋转不变性的数学定义：

```{prf:definition}
:label: def-animation-elastomers-fem-rotational_invariance

我们称一个超弹性本构模型是旋转不变的（或具有旋转不变性），当且仅当对于任意旋转矩阵 $\boldsymbol R$ 和任意形变梯度 $\boldsymbol F$，其能量密度函数满足

$$
\Psi(\boldsymbol{RF})=\Psi(\boldsymbol F)。
$$
```

一个本构模型具有旋转不变性，等价于其能量形式能够表示成形变梯度对称因子的函数，即对于任意形变梯度 $\boldsymbol F=\boldsymbol{RS}$，有 $\Psi(\boldsymbol F)=\Psi(\boldsymbol{RS})=\Psi(\boldsymbol S)$。显然，圣维南-基尔霍夫模型和共旋转线性模型的能量形式都能够表示成 $\boldsymbol S$ 的函数。

另外一个形似但不同的概念叫做各向同性（isotropy），它表明一个超弹性材料对任意方向形变的抵抗是同样强的。这个概念只有在研究材料的局部性质时才有意义，因为如果从宏观角度考虑，任意一种材料组成的物体都可以通过巧妙地设计它的形状来使得它在总体上对某个方向的形变与其他方向不同。我们考虑一个体积无限小的球形弹性体，首先将其关于一个过球心的轴进行旋转，然后再对它施加一个特定的形变，各向同性的材料意味着无论第一步的旋转变换如何，最终得到的能量都是相等的。下面我们给出各向同性的数学定义：

```{prf:definition}
:label: def-animation-elastomers-fem-isotropy

我们称一个超弹性本构模型是各向同性的，当且仅当对于任意旋转矩阵 $\boldsymbol R$ 和任意形变梯度 $\boldsymbol F$，其能量密度函数满足

$$
\Psi(\boldsymbol{FR})=\Psi(\boldsymbol F)。
$$
```

````{subfigure} A|B
:gap: 8px
:subcaptions: below
:name: fig-animation-elastomers-rotational_invariance_isotropy

```{image} fig/animation-elastomers-rotational_invariance.png
:alt: 旋转不变性
```

```{image} fig/animation-elastomers-isotropy.png
:alt: 各向同性
```

旋转不变性与各向同性的区别。考虑一个微小的球体超弹性材料，球心处于原点，设 $\boldsymbol F=\begin{bmatrix}\frac 12&0&0\\0&1&0\\0&0&1\end{bmatrix}$ 为将材料在 $x$ 轴方向压缩的形变，$\boldsymbol R=\begin{bmatrix}0&-1&0\\1&0&0\\0&0&1\end{bmatrix}$ 为将材料绕 $z$ 轴旋转 $\frac\pi 2$ 的变换。在旋转不变性的定义中，等式左侧的能量密度是在先进行 $\boldsymbol F$ 变换、后进行 $\boldsymbol R$ 变换的形变上度量的，它等于只进行 $\boldsymbol F$ 变换带来的能量密度，这表明后续进行的旋转变换不会改变能量密度。在各向同性的定义中，等式左侧的能量密度是在先进行 $\boldsymbol R$ 变换、后进行 $\boldsymbol F$ 变换的形变上度量的，原本沿 $y$ 轴分布的材料在第一步旋转之后变成了沿 $x$ 轴分布，第二步的 $\boldsymbol F$ 在 $x$ 轴方向压缩了原先沿 $y$ 轴分布的材料，而这样带来的能量密度与只进行 $\boldsymbol F$ 变换的能量密度表明材料沿 $x$ 轴的抵抗和沿 $y$ 轴的抵抗相同。
````

可以看到 {prf:ref}`def-animation-elastomers-fem-rotational_invariance` 和 {prf:ref}`def-animation-elastomers-fem-isotropy` 的区别仅仅在于旋转矩阵与形变梯度乘积的次序，但这个细微差别带来的含义是迥然不同的——前者指的是对材料进行旋转不影响能量，后者指的是对形变梯度的方向进行旋转不影响能量，如{numref}`fig-animation-elastomers-rotational_invariance_isotropy` 所示。

在我们身边，各向同性与各向异性的材料随处可见，如图所示。金属、橡胶等材料对各个方向的抵抗能力均相同，是典型的各向同性材料。我们每个人身上都有一种很典型的各向异性材料——肌肉，肌肉由多束平行的肌纤维组成，它对平行于肌纤维的形变与垂直方向的形变有着显著不同的响应。其余各向异性的材料还包括木材、各向异性的材料一般都在微观结构上具有一定的方向性。

> jr: 需要找一些各向同性、各向异性材料的图片。

对于同时满足旋转不变性且各向同性的材料而言，对于任意两个旋转矩阵 $\boldsymbol P,\boldsymbol Q$ 以及任意的形变梯度 $\boldsymbol F$，都有 $\Psi(\boldsymbol{PFQ})=\Psi(\boldsymbol F)$。那么如果我们对形变梯度进行奇异值分解 $\boldsymbol F=\boldsymbol{U\Sigma}\boldsymbol V^\top$，就可以立刻得到 $\Psi(\boldsymbol F)=\Psi(\boldsymbol\Sigma)$，也就是说能量密度的形式可以表示成形变梯度所有奇异值的函数。虽然任何一个旋转不变且各向同性的能量形式都能够直接用奇异值表示出来，但是在实践中	进行奇异值分解的计算量较大，所以我们会引入一些各向同性不变量（isotropic invariant），这些不变量只和奇异值相关，但无须奇异值分解就能计算出来；用这些不变量定义能量形式，就能够得到一个旋转不变且各向同性的本构模型，同时减少其模拟的计算量。这些不变量分别如下：

$$
&I_1(\boldsymbol F)=\mathrm{tr}\left(\boldsymbol\Sigma^2\right)=\mathrm{tr}\left(\boldsymbol F^\top\boldsymbol F\right)，\\
&I_2(\boldsymbol F)=\mathrm{tr}\left(\boldsymbol\Sigma^4\right)=\mathrm{tr}\left[\left(\boldsymbol F^\top\boldsymbol F\right)^2\right]，\\
&I_3(\boldsymbol F)=\det\left(\boldsymbol\Sigma^2\right)=(\det\boldsymbol F)^2。
$$ (animation-elastomers-fem-isotropic_invariants)

它们的导数分别是

$$
\begin{array}
&\frac{\partial I_1}{\partial\boldsymbol F}=2\boldsymbol F，&\frac{\partial I_2}{\partial\boldsymbol F}=4\boldsymbol F\boldsymbol F^\top\boldsymbol F，&\frac{\partial I_3}{\partial\boldsymbol F}=2I_3\boldsymbol F^{-\top}。
\end{array}
$$

因此，对于用这些不变量表示的能量形式 $\Psi(I_1,I_2,I_3)$，其第一类皮奥拉-基尔霍夫应力张量为

$$
\boldsymbol P(\boldsymbol F)=\frac{\partial\Psi}{\partial I_1}\cdot 2\boldsymbol F+\frac{\partial\Psi}{\partial I_2}\cdot 4\boldsymbol F\boldsymbol F^\top\boldsymbol F+\frac{\partial\Psi}{\partial I_3}\cdot 2I_3\boldsymbol F^{-\top}。
$$

新胡克模型（Neohookean elasticity）就是一个使用各向同性不变量定义能量形式的本构模型，其能量密度为

$$
\Psi(I_1,I_3)=\frac\mu 2[I_1-\log(I_3)-3]+\frac\lambda 8\log^2(I_3)，
$$ (animation-elastomers-fem-neohookean_energy)

其第一类皮奥拉-基尔霍夫应力张量为

$$
\boldsymbol P(\boldsymbol F)=\mu\boldsymbol F-\mu\boldsymbol F^{-\top}+\frac{\lambda\log(I_3)}2\boldsymbol F^{-\top}。
$$ (animation-elastomers-fem-neohookean_stress)

从 $I_3$ 的表达式可以看出，它反映了形变后材料相对形变前的体积大小。当体积被压缩至 $0$ 时，$I_3$ 会趋于 $0$，则式 {eq}`animation-elastomers-fem-neohookean_energy` 中的 $\log^2(I_3)$ 项会占主导地位，让能量密度趋于正无穷；这样快速增长的能量会让材料对强烈的压缩产生巨大的抵抗，与圣维南-基尔霍夫模型形成了对比。利用这个性质，在模拟高度不可压的弹性体时，第二拉美系数 $\lambda$ 会非常大，从而式 {eq}`animation-elastomers-fem-neohookean_energy` 中的 $\log^2(I_3)$ 项的权重变大，惩罚形变后的体积变化。与此同时，这个性质也会是此模型的一个缺点，在模拟当中不可避免地会出现一些因数值爆炸或边缘情况导致的体积变零甚至反向的情况（即 $\det\boldsymbol F\le 0$ 的情况），此时能量形式将不会有定义，所以在实际处理时会将当前形变梯度 $\boldsymbol F$ 替换为一个最接近的、行列式为一个很小的正值 $\varepsilon$ 的形变梯度。

#### 各种本构模型的比较

我们小结一下前面介绍的所有本构模型，{numref}`tab-animation-elastomers-constitutive_models` 总结了所有模型的优缺点，在了解每个模型的性质之后我们应当根据模拟的需求适当地选择。

```{table} 各种本构模型
:widths: auto
:align: center
:name: tab-animation-elastomers-constitutive_models

|名称|$\Psi$|$\boldsymbol P$|模拟效率|旋转不变性|各向同性|能处理强压缩|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|线性模型|$\mu\mathrm{tr}\left(\boldsymbol\epsilon^2\right)+\frac\lambda 2\mathrm{tr}^2(\boldsymbol\epsilon)$|$2\mu\boldsymbol\epsilon+\lambda\mathrm{tr}(\boldsymbol\epsilon)\mathbf I$|高|无|无|否|
|圣维南-基尔霍夫模型|$\mu\mathrm{tr}\left(\boldsymbol E^2\right)+\frac\lambda 2\mathrm{tr}^2(\boldsymbol E)$|$\boldsymbol F[2\mu\boldsymbol E+\lambda\mathrm{tr}(\boldsymbol E)\mathbf I]$|低|有|有|否|
|共旋转线性模型|$\mu\Vert\boldsymbol S-\mathbf I\Vert_\mathrm F^2+\frac\lambda 2\mathrm{tr}^2(\boldsymbol S-\mathbf I)$|$2\mu(\boldsymbol F-\boldsymbol R)+\lambda\mathrm{tr}\left(\boldsymbol R^\top\boldsymbol F-\mathbf I\right)\boldsymbol R$|中|有|有|否|
|新胡克模型|$\frac\mu 2[I_1-\log(I_3)-3]+\frac\lambda 8\log^2(I_3)$|$\mu\boldsymbol F-\mu\boldsymbol F^{-\top}+\frac{\lambda\log(I_3)}2\boldsymbol F^{-\top}$|低|有|有|是|
```

## 空间离散化

我们在前文讲到的所有物理模型都是建立在连续体上的，与弹簧质点系统一样，要使用计算机将这些物理模型模拟出来也需要进行空间离散化。在有限元方法中，一个连续的超弹性材料被表示成一个四面体网格（tetrahedral mesh），即一些紧密相连的四面体组成的图（如{numref}`fig-animation-elastomers-hand` 所示）。

```{figure} fig/animation-elastomers-hand.png
:name: fig-animation-elastomers-hand

一个手形弹性体分别在有限元方法（左）和弹簧质点系统（右）中的离散化
```

设四面体网格拥有 $N$ 个顶点和 $M$ 个四面体单元，离散化后的弹性体的全部自由度即为所有四面体的顶点，我们记未形变状态下顶点的坐标为 $\boldsymbol X_1,\cdots,\boldsymbol X_N$，形变后的顶点坐标为 $\boldsymbol x_1,\cdots,\boldsymbol x_N$。利用这些自由度，我们需要构造出一个合适的变形函数 $\boldsymbol\phi(\boldsymbol X)$，使其满足 $\boldsymbol\phi(\boldsymbol X_i)=\boldsymbol x_i,i=1,\cdots,N$；这样，我们就从离散的定点上定义的变形映射延拓到了一个连续区域内，便可以进一步地计算出形变梯度 $\boldsymbol F$，再结合本构模型计算出 $\Psi$ 和 $\boldsymbol P$。但是，在离散意义下，我们并不能简单地使用 {numref}`sec-animation-elastomers-fem-energy_force` 中的方法计算到的力密度和牵引力去更新弹性体的状态；因为在离散化之后，我们只能够通过更新这 $N$ 个顶点的位置来实现弹性体的动态，定义在连续域上的力密度和牵引力就不能直接使用了；我们的方法是利用力密度的积分计算总能量，然后将整个弹性体的质量分配在每个顶点上，每个顶点的受力就变成负能量梯度了。接下来，我们将一一讲述这些步骤。

### 变形函数的选择

我们假设每个四面体单元都只能经历线性形变，即在任意一个四面体 $\mathcal T_i$ 内部，变形函数都是线性函数。因此，整个变形函数 $\boldsymbol\phi$ 可以表示为一个分段线性函数：

$$
\boldsymbol\phi(\boldsymbol X)=\boldsymbol A_i\boldsymbol X+\boldsymbol b_i,\quad\boldsymbol X\in\mathcal T_i,\quad\quad i=1,\cdots,M，
$$ (animation-elastomers-discrete_deformation_map)

其中 $\boldsymbol A_i\in\mathbb R^{3\times 3}$ 和 $\boldsymbol b_i\in\mathbb R^3$ 刻画了第 $i$ 个四面体经历的线性变换。通过对式 {eq}`animation-elastomers-discrete_deformation_map` 两端关于 $\boldsymbol X$ 求导，可以得到每个四面体内的形变梯度：

$$
\boldsymbol F(\boldsymbol X)=\boldsymbol A_i,\quad\boldsymbol X\in\mathcal T_i,\quad\quad i=1,\cdots,M，
$$

因此在后文我们记四面体 $i$ 的形变梯度为 $\boldsymbol F_i$，式 {eq}`animation-elastomers-discrete_deformation_map` 又可以写为

$$
\boldsymbol\phi(\boldsymbol X)=\boldsymbol F_i\boldsymbol X+\boldsymbol b_i,\quad\boldsymbol X\in\mathcal T_i,\quad\quad i=1,\cdots,M。
$$

### 形变梯度的计算

### 能量与力的计算

## 数值求解算法
