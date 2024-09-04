# 样条曲线

**样条曲线（spline curve）** 是定义非常广泛，也是最常用的曲线类型。事实上，只要是使用分段多项式表达的曲线，并且在连接处满足一定的连续性，我们就可以称这条曲线为样条曲线。样条的名
称来源于早期的船舶和飞机制造工业中的一种技术：通过将细木条 (称为“样条”) 穿过布置在大型设计阁楼地板上的点来构建飞机模板，如{numref}`fig-started-curves-spline` 所示。如果我们使用分段的多项式近似整个细木条，得到的曲线就称为样条插值曲线。后来样条曲线被赋予了更广泛的定义，不需要经过这些控制点也可以被称为样条曲线。

```{figure} fig/spline.png
:name: fig-started-curves-spline
:width: 40%

样条的原型[^spline]
```

[^spline]: [Wikipedia: Flat spline](https://en.wikipedia.org/wiki/Flat_spline)

## 插值样条

给出点列 $\{\mathbf P_0,\,\mathbf P_1,\,\dots,\,\mathbf  P_m\}$，其中每个点的坐标为 $\mathbf P_i = (x_i,\,y_i)$。我们的任务是在每个区间内定义一个多项式，使其经过每个点并保持一定连续性。常见的选择是**三次样条（cubic spline）**：假设在每一段 $(\mathbf P_i, \mathbf P_{i+1})$ 之间我们都定义一个参数 $t\in [0, 1]$，然后假设 $x=f_i(t)=a_i t^3 + b_i t^2 + c_i t + d_i$，$y=g_i(t)=e_i t^3 + f_i t^2 + g_i t + h_i$，一共 8 个参数需要确定。由于 $x$ 和 $y$ 可以单独考虑，我们下面的推导只针对 $x$ 分量，$y$ 分量同理。

```{figure} fig/cubic-spline.svg
:name: fig-started-curves-cubic-spline
:width: 60%

三次样条曲线[^cubic-spline]
```

[^cubic-spline]: [Wolfram MathWorld: Cubic Spline](https://mathworld.wolfram.com/CubicSpline.html)

针对 $x$ 分量我们一共需要确定 $4m$ 个参数，对应要列出 $4m$ 个方程。首先，每个区间应该经过左右两个端点，这样有 $2m$ 个方程：

$$
f_i(0) = x_{i}, \ f_i(1) = x_{i+1}, \ i = 0, \cdots, m - 1
$$ (eq-started-curve-cubic1)

在每个点上我们要求左右连续：对于 $\mathbf{P}_i$，左侧区间代入 $t=1$ 的一阶导数和二阶导数应该和右侧 $t=0$ 的一阶导数和二阶导数相等。这样的方程我们一共可以列 $2(m-1)$ 个，因为最两侧的点不需要考虑：

$$
f'_i(1) = f'_{i+1}(0), \ f''_i(1) = f''_{i+1}(0), \ i = 1, \dots, m - 1
$$ (eq-started-curve-cubic2)

这些方程加起来一共有 $4m - 2$ 个，还差 2 个方程。这两个方程可以自行指定，比如我们可以规定两个端点处的二阶导数为 0：$f''_0(0)=0$，$f''_{m}(1)=0$，这种特例称为自然边界条件。这样我们一共列出了 $4m$ 个方程，对应 $4m$ 个未知数，只需要求解 $4m\times 4m$ 的线性方程组就能得到所有参数。{numref}`fig-started-curves-cubic-spline` 给出了一个示例结果。

从定义中我们可以发现，三次样条支持 $C^2$ 的连续性，并且是插值曲线。但是相对的，我们需要解方程确定每一段的参数，如果我们移动了某一个控制点就需要重新求解整个曲线。并且，由于我们要求解线性方程，一个控制点的移动会影响整个曲线非常远地方的形状。这种特性称为非局部性，如{numref}`fig-started-curves-cubic-gif` 所示。因此三次样条并不是最理想的曲线选择。

```{figure} fig/cubic.gif
:name: fig-started-curves-cubic-gif
:width: 60%

三次样条曲线的非局部性
```

为了改进三次样条的缺点，有一种非常类似的样条曲线，称为**三次厄米样条（cubic Hermite spline）**。三次厄米样条依然使用分段的三次多项式表示曲线，与三次样条不同的地方在于，三次厄米样条不要求二阶导数的连续。作为交换，我们可以指定每个顶点上的一阶导数的值。

## B样条

## NURBS