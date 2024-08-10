(sec-animation-elastomers-fem)=
# 有限元方法

```{figure} fig/animation-elastomers-tetrahedron.png
:width: 25 %
:name: fig-animation-elastomers-tetrahedron

一个正四面体形状的弹性体被离散化成弹簧质点系统，其底面三个黑色顶点固定，顶部蓝色顶点受到向下的力 $\mathbf F$ 的作用。
```

弹簧质点系统给出了一个对弹性物体十分简单的建模，在一定范围内的形变下能够较好地模拟出弹性的动态；然而对于一些较为极端的情形，它将会产生错误的结果。我们以一个体积很小的弹性正四面体为例，其底面固定，一较大的向下的外力 $\mathbf F$ 作用于四面体的顶部。如{numref}`fig-animation-elastomers-tetrahedron` 所示，在弹簧质点系统下这个正四面体会自然地被空间离散化成四个处于顶点处、由弹簧两两连接的质点，每根弹簧的原长为正四面体的边长 $l$，劲度系数为 $k$；底面的三个质点（{numref}`fig-animation-elastomers-tetrahedron` 中的黑色顶点）固定，顶部的质点（{numref}`fig-animation-elastomers-tetrahedron` 中的蓝色顶点）受到力 $\mathbf F$ 的作用。这个场景的动态如{numref}`fig-animation-elastomers-tetrahedron_dynamics` 所示：初始时四面体静止，顶部质点只受到 $\mathbf F$ 的作用开始向下运动；随后由于顶部质点所连接的三根弹簧被压缩，顶部质点还会受到三根弹簧的弹力，由于是正四面体，三个弹力的合力向上，这也符合弹性体总是倾向于恢复原状的性质；但是三根弹簧的合力大小存在上界，当 $\|\mathbf F\|>3kl$（即 $\mathbf F$ 的大小比三根弹簧压缩至 $0$ 长度的弹力总和还大）时，顶部质点的合力一直向下，从而会一直加速向下运动，即便整个四面体已经被完全压扁乃至反向；在四面体反向后更严重的问题发生了，此时弹簧的合力朝下，也就是说即便撤掉力 $\mathbf F$，四面体也不会恢复至原状。

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

## 空间离散化

## 数值求解算法
