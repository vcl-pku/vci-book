# 网格编辑

网格编辑（mesh editing），是操纵和修改网格表面的几何形状，同时能够保留原始网格几何细节（detail preserving）的操作。由于几何细节是对网格内在特质的描述，因此直接编辑网格顶点的位置坐标并不是一个好的想法，往往导致细节的失真。

我们可以首先回顾在 {numref}`chap-getting-started-images-completion` 中进行图像编辑时的做法，考虑如何给图片中的特定区域注入某些给定信息。对于定义在区域 $\Omega$ 上的目标颜色场 $g(x,y)$，泊松图像编辑通过求解下面的优化问题来得到融入后的颜色场 $f(x,y)$：

$$
    \mathop{\arg\min}_f\int_\Omega\|\nabla f-\nabla g\|^2\mathrm dx\mathrm dy,\quad\text{s.t.}\quad f|_{\partial\Omega}=f^*|_{\partial\Omega}
$$ (eq-geometry-processing-editing-cloning1)

它在保证边界上无缝衔接的同时使得填补后区域的颜色梯度 $\nabla f$ 与给定颜色场的梯度 $\nabla g$ 尽可能接近。
拉普拉斯编辑是 $\nabla g=0$ 的一类特殊情况，它完成的是图像补全的任务。

```{figure} fig/edit_move.png
:name: fig-geometry-processing-edit_move
:width: 70%

拉普拉斯网格编辑。左侧章鱼模型的腕足经过编辑后形状发生了变化，但保持了腕足上吸盘的几何细节。
```

类似的思想在三维的应用就是拉普拉斯网格编辑技术 {cite}`Sorkine2004`，它通过尽可能对齐编辑后网格上的拉普拉斯微分坐标来保留细节内容，如图
拉普拉斯微分坐标本质上就是每个网格顶点上关于位置坐标的均匀拉普拉斯算子，记为：

$$
    \mathcal{L}(\mathbf v_i)=\mathbf v_i-\frac{1}{N_i}\sum_{j\in \Omega(i)}\mathbf v_j
$$ (eq-geometry-processing-editing-laplace)

它是一种相对坐标，在给定边界条件的情况下可以与世界空间的位置坐标互相转化。
拉普拉斯坐标是网格顶点坐标的线性组合，与点的法向和曲率无关，因此可以被用来描述局部特征。

拉普拉斯网格编辑的思路是：在交互中指定一些顶点的目标位置后，重建一个既满足这些顶点约束、又尽可能保持局部拉普拉斯微分坐标的网格。
具体来说，设给出的具有$n$个顶点的网格模型的顶点坐标为
$\{\mathbf v_1,\,\dots,\,\mathbf v_n\}$
，首先计算出对应的拉普拉斯坐标：$\Delta_i = \mathcal{L}(\mathbf v_i),\,i=1,\dots,n$。而后对需要调整的顶点给出约束：$\mathbf v'_j=\mathbf u_j,\,j\in C$，其中 $C$ 是受约束点的集合。于是我们可以构造出拉普拉斯网格编辑对应的最优化问题：

$$
    \mathop{\arg\min}_{\mathbf v'_1,\dots,\mathbf v'_n}\left(\sum_{i=1}^n\|\mathcal{L}(\mathbf v'_i)-\Delta_i\|^2 + \sum_{j\in C}\|\mathbf v'_j-\mathbf u_j\|^2\right)
$$ (eq-geometry-processing-editing-cloning2)

利用最小二乘方法求解该优化问题即可得到生成编辑后的网格。

拉普拉斯网格编辑技术可以被用在众多应用中，包括并不限于网格编辑、涂层迁移、表面移植等等，如 {numref}`fig-geometry-processing-laplace_editing` 所示。

````{subfigure} A|B
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-geometry-processing-laplace_editing
:width: 70%

```{image} fig/edit_coat.png
:alt: 涂层迁移：将兔子模型的几何细节（左）迁移到动物腿的模型上（中）形成兔毛涂层的效果（右）。
```

```{image} fig/edit_transport.png
:alt: 网格移植：将虎模型的后半部分移植到龙模型上。
```

拉普拉斯网格编辑在涂层迁移和网格移植任务上的应用。
````
