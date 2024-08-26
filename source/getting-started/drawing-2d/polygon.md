# 多边形

与绘制线不同，绘制多边形需要对多边形的内部进行填充。我们先从如何画一个纯色的多边形开始，再考虑如何在内部填充颜色。

## 多边形的光栅化

三角形是最简单的多边形，对于计算机图形学来说非常重要。任意一个二维多边形都可以切割成多个三角形的组合，同时三角形也是三维模型的重要组成部分（{numref}`chap-geometry-basics`）。我们考虑绘制由 $P_0=(x_0, y_0)$，$P_1=(x_1, y_1)$，$P_2=(x_2, y_2)$ 三个顶点定义的三角形，三个顶点保证逆时针顺序。在最简单的想法下，我们可以判断每个像素是否在三角形内部，如果是就绘制颜色，如{numref}`code-started-drawing-tri` 所示。

```{code-block} python
:caption: 最简单的三角形光栅化算法
:lineno-start: 1
:emphasize-lines: 4-7
:name: code-started-drawing-tri

def draw_triangle(x0: int, y0: int, x1: int, y1: int, x2: int, y2: int):
  xmin, xmax = min(x0, x1, x2), max(x0, x1, x2)
  ymin, ymax = min(y0, y1, y2), max(y0, y1, y2)
  for x in range(xmin, xmax + 1):
    for y in range(ymin, ymax + 1):
      if inside(x, y, x0, y0, x1, y1, x2, y2):
        draw(x, y)
```

那么如何判断点 $P=(x,y)$ 是否在三角形内部？我们可以借助上一节提到的直线的隐式函数。如{numref}`fig-started-drawing-triangle-test` 所示，我们规定边的方向为逆时针方向，也就是从 $P_i$ 指向 $P_{i+1}$（$P_2$ 指向 $P_0$），将其逆时针旋转 $90^\circ$ 得到垂直于边的法向 $N_i$，那么 $N_i$ 一定指向三角形的内部。如果点 $P$ 位于三条边的法向一侧，也就是代入三条边的隐式方程 $F_i(P)$ 都大于 0，那么点 $P$ 就位于三角形内部。反之如果有任意一条边的 $F_i(P)<0$，那么点 $P$ 就位于三角形的外部。

```{figure} fig/triangle-test.png
:name: fig-started-drawing-triangle-test
:width: 70%

三角形内外检测
```

这里我们遇到了和直线绘制中类似的情况。这个算法并没有什么问题，但是每个点都需要计算三次直线的隐式方程，包含整数乘法运算，有没有可能通过累加的方式避免乘法运算呢？观察最简单的三角形绘制算法，我们其实是在一行一行地绘制三角形中的像素。如果已知三角形在一行中的左边端点 $y_L$ 和右边端点 $y_R$，中间的像素其实没有必要进行内外检测，可以直接绘制。而维护左右端点的过程其实就是在绘制直线的过程。我们没有必要重复计算三条边与当前行的交点，而是可以通过上一行的交点和直线的斜率，增量更新到当前行的交点，这正是绘制直线的 DDA 算法。通过这种方式我们能够避免对所有像素进行三角形内外检测，而只通过增量更新的方法逐行绘制，这种算法被称为**扫描线算法（Sweep-Line Algorithm）**。这里我们仅在{numref}`code-started-drawing-tri-dda` 中给出大致的伪代码。

```{code-block} python
:caption: 三角形光栅化的扫描线算法
:lineno-start: 1
:emphasize-lines: 5-9
:name: code-started-drawing-tri-dda

def draw_triangle(T):
  for each edge pair:
  initialize x_L, x_R
  compute dx_L/dy_L, dx_R/dy_R
  for each scanline at y:
    for x in range(x_L, x_R + 1): 
    draw(x, y)
    x_L += dx_L/dy_L
    x_R += dx_R/dy_R
```

扫描线算法的想法可以自然拓展到多边形中。我们可以首先对多边形的所有边进行排序，然后用类似方法维护左右交点，从上到下进行扫描线的绘制。在面对多边形时，我们还要额外注意多边形非凸的情况。如{numref}`fig-started-drawing-poly` 所示，一条扫描线有可能和多边形有不只两个交点。为了处理这种情况，我们可以将所有边与扫描线的交点从左到右排序，可以发现第奇数交点到第偶数交点中间就是需要绘制的像素，而第偶数交点到第奇数交点之间是在多边形外部的区域。

````{subfigure} AB 
:name: fig-started-drawing-poly
:width: 100 %
:gap: 8px

```{image} fig/poly1.png
```

```{image} fig/poly2.png
```

扫描线算法绘制填充多边形
````

扫描线算法相比于简单的三角形算法更高效，然而在现代计算机上，其实使用的最多的是并行版的简单算法。这背后的原因在于，三角形在现代图形学中的地位非常重要，在后面 {numref}`chap-rendering-shading` 的学习中我们会发现现代的渲染管线是完全围绕三角形搭建起来的，现代显卡的重要功能就是绘制三角形。为了能够快速绘制大量的三角形，现代显卡基本都会提供三角形内外检测的专门硬件模块，从而在硬件上实现并行的三角形绘制。

## 颜色插值

## 图像拉伸
