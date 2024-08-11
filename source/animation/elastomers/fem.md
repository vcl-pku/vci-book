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
\phi:\Omega&\to\mathbb R^3\\
\boldsymbol X&\mapsto\boldsymbol x
$$ (animation-elastomers-deformation_function)

即为对弹性体形变的描述。

```{figure} fig/animation-elastomers-deform_map.png
:width: 100 %
:name: fig-animation-elastomers-deform_map

参考构型 $\Omega$、形变前位置 $\boldsymbol X$、形变后位置 $\boldsymbol x$ 与变形函数 $\phi$ 的关系
```

> jr: {numref}`fig-animation-elastomers-deform_map` 需要重画。

变形函数 $\phi$ 确实能够充分地表示出弹性体的形变，但作为一个**全局**的信息表示，它包含了过多的信息。我们马上就会看到，弹性体每一个点的能量与内力只由其**局部**的形变所决定。因此，在连续介质力学中会引入形变梯度（deformation gradient）的概念，形变梯度一般记为 $\boldsymbol F$，其定义为变形函数 $\phi$ 关于形变前位置 $\boldsymbol X$ 的雅可比矩阵：

$$
\boldsymbol F\mathrel{\mathop:}=\frac{\partial(\phi_1,\phi_2,\phi_3)}{\partial(X_1,X_2,X_3)}=\begin{bmatrix}\frac{\partial\phi_1}{\partial X_1}&\frac{\partial\phi_1}{\partial X_2}&\frac{\partial\phi_1}{\partial X_3}\\\frac{\partial\phi_2}{\partial X_1}&\frac{\partial\phi_2}{\partial X_2}&\frac{\partial\phi_2}{\partial X_3}\\\frac{\partial\phi_3}{\partial X_1}&\frac{\partial\phi_3}{\partial X_2}&\frac{\partial\phi_3}{\partial X_3}\end{bmatrix}，
$$ (animation-elastomers-deformation_gradient)

其中 $\phi(\boldsymbol X)=\begin{pmatrix}\phi_1&\phi_2&\phi_3\end{pmatrix}^\top$，$\boldsymbol X=\begin{pmatrix}X_1&X_2&X_3\end{pmatrix}^\top$。我们知道导数可以很好地反映原函数的局部特征，所以在连续介质力学中形变梯度是最常用也最直观的刻画弹性体形变的量之一，变形函数反而没有那么重要。

```{attention}
由式 {eq}`animation-elastomers-deformation_gradient` 可见，形变梯度 $\boldsymbol F$ 是一个关于形变前坐标 $\boldsymbol X$ 的矩阵函数。
```

### 描述能量

### 描述力

### 能量与力的关系

## 空间离散化

## 数值求解算法
