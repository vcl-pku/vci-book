# 网格细分

```{figure} fig/subdivision.png
:name: fig-geometry-processing-subdivision
:width: 90%

通过对粗糙表面进行多次细分（从左至右），可以得到平滑的曲面。
```

由上面的分析我们知道，通过增加组成几何表面的网格面片数量，减小每个面片的面积，可以使几何表面看起来更加光滑。
网格细分（mesh subdivision），也称为网格的上采样，是指通过反复细分初始的多边形网格，不断得到更精细的网格的过程。
因此，如 {numref}`fig-geometry-processing-subdivision` 所示，我们可以通过对几何表面进行不断细分，用这一系列细分的极限来定义出一个平滑的曲线或曲面。

## Catmull-Clark 细分

Catmull-Clark 细分 [^catumull_clark] 是最常用的几何表面细分方法之一，通过将表面的多边形细分为更小的多边形，用相邻的顶点重新定位先前的顶点，对三维多边形网格表面起到平滑效果。这种方法采用网格中包含的每一个原始多边形，并将多边形细分为四边形，基于平均值构建新的顶点，并根据周围环境调整原始多边形的先前顶点。

Catmull-Clark 细分在 1978 年由 Edwin Catmull 和 Jim Clark 提出，之后在各种渲染场景中都可以发挥作用，从学术界到游戏再到动画电影都有其身影，也因此获得了 2006 年奥斯卡技术成就奖。

[^catumull_clark]: [Wikipedia: Catmull-Clark](https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface)

````{subfigure} AB
:layout-sm: A|B
:gap: 8px
:subcaptions: below
:name: fig-geometry-processing-catmull_process
:width: 90%

```{image} fig/catmull_points.png
:alt: 增设面点，增设边点，更新顶点。
```

```{image} fig/catmull_edges.png
:alt: 形成新的边和面。
```

单轮 Catmull-Clark 细分 [^catumull_clark]。
````

```{figure} fig/catmull.png
:name: fig-geometry-processing-catmull
:width: 50%

通过不断地进行 Catmull-Clark 细分，原本有棱有角的几何表面被细分成平滑的曲面。
```

Catmull-Clark 算法每一次细分由增设面点（face point）、增设边点（edge point）、更新顶点(vertex point)、形成新的边和面四个步骤组成，如 {numref}`fig-geometry-processing-catmull_process` 所示，下面我们依次介绍。

1. 增设面点：对多面体的每个面片计算一个面点，这个面点是这个多边形面上所有顶点坐标的平均值。
2. 增设边点：对多面体的每条边计算一个边点，找出该条边的两个端点和共享该条边的两个面的面点，对这四个点的坐标取平均。
3. 更新顶点：对于多边形原有的每个顶点 $v$，使用：
    + 所有包含顶点 $v$ 的边的中点（注意不是上述步骤中的边点）的平均值 $R$
    + 所有包含顶点 $v$ 的多边形面片的面点的平均值 $F$
    + 以及顶点 $v$ 的原有值的加权平均值
    
    来调整其三维坐标。加权平均遵循以下公式：
    $$\frac{F+2R+(n-3)v}{n}$$
    其中 $n$ 是面点的数量。

4. 形成新的边和面：将每个面点连接到所有构成了它所在的原始面的边的边点，将每个新顶点连接到所有连接着它原始点的边的边点。新的面就由这些边包围而成。

可以证明，经过一轮细分后，不论原多边形网格是何结构，新得到的多边形网格将只由四边形构成。如 {numref}`fig-geometry-processing-catmull` 所示，在不断细分的过程中，表面会不断趋向平滑和圆润。

## Loop 细分

Loop 细分是常见的针对三角网格模型的细分方法，由 Charles Loop 在 1987 年提出。每一次细分将三角面片细分为四个更小的面片，迭代下去使几何表面变得平滑。

```{figure} fig/loop_process.png
:name: fig-geometry-processing-loop_process
:width: 80%

Loop 细分过程：在边上增加新顶点（左），并更新原有顶点（中、右）。
```

```{figure} fig/loop_example.png
:name: fig-geometry-processing-loop_example
:width: 60%

不断进行 Loop 细分的结果。
```

如 {numref}`fig-geometry-processing-loop_process` 所示，Loop 细分的过程由计算新顶点和更新原有顶点两步组成。

1. 计算新顶点：
    + 对于每一条边，如果这条边被两个三角形面所包含，如 {numref}`fig-geometry-processing-loop_process` 左图所示，则由这条边的两个端点 $\mathbf v_0, \mathbf v_2$ 和“跨过”这条边的两个顶点 $\mathbf v_1, \mathbf v_3$ 加权平均计算出新顶点 $\mathbf v^*$，具体的计算公式为：
    $$\mathbf v^*=\frac{3}{8}(\mathbf v_0+\mathbf v_2)+\frac{1}{8}(\mathbf v_1+\mathbf v_3)$$
    + 如果这条边只被一个三角形面所包含（即为边界上的边），则直接取这条边的中点作为新顶点。
2. 更新原有顶点：如 {numref}`fig-geometry-processing-loop_process` 中图、右图所示，对于每个原有顶点 $\mathbf v$，根据以下公式更新后的位置 $\mathbf v'$：
    $$\mathbf v'=(1-n*u)\mathbf v+\sum_{i=1}^{n}u\mathbf v_i$$
    其中 $n$ 为顶点 $v$ 的度数，$v_i$ 为与 $v$ 有边相连的顶点，当 $n=3$ 时 $u=3/16$，否则 $u=\frac{3}{8n}$。

通过不断地生成新顶点和更新原有顶点，每一次细分后连接新顶点与原有顶点，三角面片变得更加精细，得到的几何表面更加平滑，如 {numref}`fig-geometry-processing-subdivision` 及 {numref}`fig-geometry-processing-loop_example` 所示。
