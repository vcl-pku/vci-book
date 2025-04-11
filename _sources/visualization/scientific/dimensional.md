# 标量场、矢量场、张量场的可视化

## 按物理量性质分类：标量场、矢量场、张量场

### 标量场数据

标量场（Scalar Fields）数据是单值分布在空间网格上的数据，每个空间点对应一个标量值。
常见的标量场数据有：医学影像（CT 扫描的 Hounsfield 单位值），气象数据（全球温度分布、大气压强），材料科学（金属疲劳试验中的应力分布）。
标量场数据具有空间连续性和数值范围跨度大的特点，特征提取困难及三维体数据内部结构可能被外部遮挡，是其可视化的核心挑战。

### 矢量场数据

矢量场（Vector Fields）数据在空间每个点上具有方向与大小，通常表示为三维向量。在 3D 坐标系中常可以表述成坐标轴基矢和沿着基矢的方向投影数值，通常用空间中的一系列箭头去描述。
常见的矢量场数据有：流体力学（流速场、压力梯度场），电磁学（电场强度、磁场方向），气象学（风向与风速场）。
矢量场数据具有方向性、动态性和多尺度特性，视觉混乱（如密集箭头噪声）及复杂拓扑结构（如涡旋）的精确表达，是其可视化的主要难点。

### 张量场数据

张量场（Tensor Fields）数据在空间每个点上为二阶张量（如 3×3 矩阵），常用于描述各向异性现象。
常见的张量场数据有：材料科学（应力张量、应变率张量），医学成像（扩散张量成像），地质学（岩石渗透率张量）。
张量场数据具有方向各向异性和高维复杂性，信息过载及交互分析能力不足，是其可视化需克服的关键问题。


## 标量场可视化

标量可视化是将分布在空间中的标量值数据转换为人类可感知的视觉形式（如颜色、等值线）的过程，以下将介绍几种经典方法。

### 颜色映射

颜色映射（Color Mapping）将标量值通过预定义的颜色映射函数映射到颜色空间（如 RGB 或 HSV），使用图形库的标准着色和阴影功能来显示这些颜色，并以颜色差异来表示数值差异。
颜色映射的基本定义式如下：对域 $D$ 内的任意点 $x \in D$，

$$
C(x) = T(S(x))，
$$ (visualization-scientific-color_mapping)

$C$ 表示可视化的颜色值，$S$ 为定义在域 $D$ 上的标量场，$S:D \rightarrow \mathbb{R}$ ，其中 $D\subseteq \mathbb{R}^n$（通常 $n$ = 2 或 3），$\mathbb{R}$ 表示实数集。

$T$ 表示颜色映射函数，可以定义为： 

$$
T: [S_{\text{min}}, S_{\text{max}}] \rightarrow \text{Colors}，
$$ (visualization-scientific-function)

其中 $[S_{\text{min}}, S_{\text{max}}]$ 是颜色映射所考察的标量场取值范围（如，可取为 $S$ 的值域，或值域内某个取值区间），$\text{Colors}$ 表示一组颜色。
最终，对于所有 $x \in D$，都可以将 $x$ 在域 $D$ 中的标量值 $S(x)$ 通过颜色映射函数 $T$ 转换为一个颜色，从而实现可视化。

颜色映射函数通过传递函数将归一化后的标量值转换为颜色值，而颜色查找表是一种特殊形式的传递函数，如{numref}`color_mapping`。
基于颜色查找表是一种最直接的颜色映射方法，其流程包含如下步骤：
- **定义颜色查找表**：
查找表包含一组预定义的颜色数组（例如，红色、绿色、蓝色以及透明度分量或其他类似的表示），通常存储为 RGB 或 RGBA，每个颜色对应一个标量值。

- **标量归一化**：
按设定的 $[S_{\text{min}}, S_{\text{max}}]$ 范围，将原始标量值 $S$ 线性缩放到标准范围 $[0,1]$ 内，超出范围的值截断至边界：

$$
S_{\text{norm}} = 
\begin{cases}
0, & S < S_{\text{min}} \\
1, & S > S_{\text{max}} \\
\frac{S - S_{\text{min}}} {S_{\text{max}}-S_{\text{min}}}, & \text{otherwise}
\end{cases}
$$ (visualization-scientific-uniform)

- **计算索引**：
通过计算标量值在查找表中的索引位置计算出颜色值，从而将标量值映射到对应的颜色。
$N$ 为查找表颜色数，则索引值 $\text{index}$（浮点数） 为：

$$
\text{index}=S_{\text{norm}} \times (N-1)，
$$ (visualization-scientific-index)


- **颜色插值**
颜色插值用于在查找表的离散颜色之间生成平滑过渡，线性插值是一种常见的插值方法。
已知 $C_i$ 和 $C_{i+1}$ 为两个相邻的颜色，，$i = \lfloor \text{index} \rfloor$ 是索引值向下取整，则插值权重 $\alpha = \text{index}-i$，则颜色 $C$ 的插值公式如下：

$$
C=(1- \alpha) \times C_i+ \alpha \times C_{i+1}，
$$ (visualization-scientific-interpolation)

```{figure} fig/visualization-scientific-color_mapping.png
:name: color_mapping
颜色映射表的形式。
```

### 等高线/等值面

颜色映射的一个自然扩展是等高线（等值线）（contours）与等值面（isosurfaces）的绘制。
当我们看到一个用数据值着色的表面时，眼睛常常将颜色差别较大的相近区域区分为不同的区域。
当我们绘制等高线时，实际上就是在构造这些区域之间的边界。
特定的边界可以表示为两个区域 $F(x) < c$ 和 $F(x) > c$ 之间的 $n$ 维分隔面，其中 $c$ 是等高线值，$x$ 是数据集中的 $n$ 维点。

绘制等高线始终是从定义要生成的等高线或表面的等高线值开始的。
由于实际数据多为离散采样点，如{numref}`fig-visualization-scientific-isometric` 中显示的 2D 结构化网格（数字代表网格点处的标量值），生成连续等值线/面需通过插值计算等值点位置。

```{figure} fig/visualization-scientific-isometric.png
:name: fig-visualization-scientific-isometric
一个简单的等值线（$c=5$）测绘示意图。
```

最常见的插值技术是线性插值，我们沿单元格边缘定位等值点，从而确保拓扑连续性。
在二维网格单元格边缘，等值点 $p$ 的位置由相邻顶点 $x_1，x_2$计算，公式如下：

$$
p = x_1 + \frac{c-v_1}{v_2-v_1} \cdot (x_2-x_1)，
$$ (visualization-scientific-contours)
其中 $c$ 是目标等高线值，$v_1$，$v_2$ 是点 $x_1$，$x_2$ 处的标量值。

例如，如果一条边在其两个端点的标量值为10和0，并且我们试图生成值为5的等高线，则边缘插值计算等高线通过边缘的中点。

一旦在单元格边缘生成了点，我们就可以将这些点连接成等高线。
对于等高线的连接一种方法是使用分而治之的技术，独立处理每个单元格。这在二维中称为“行进方块算法”（Marching Squares），在三维中称为“行进立方体算法”（Marching Cubes），如{numref}`fig-visualization-scientific-marching_squares`和{numref}`fig-visualization-scientific-marching_cubes`所示。

```{figure} fig/visualization-scientific-marching_squares.png
:name: fig-visualization-scientific-marching_squares
Marching Squares 算法示意。
```

```{figure} fig/visualization-scientific-marching_cubes.png
:name: fig-visualization-scientific-marching_cubes
Marching Cubes 算法示意。
```

这些技术的基本假设是，等高线只能以有限的方式通过一个单元格。拓扑状态的数量取决于单元格顶点的数量以及顶点与等高线值相对的内部/外部关系的数量。如果顶点的标量值大于等高线的标量值，则认为该顶点在等高线内部。标量值小于等高线值的顶点则被认为在等高线外部。
对于一个方形单元格，有 16 种组合。通过将每个顶点的状态编码为一个二进制数字，可以计算出案例表中的索引。
对于三维数据，考虑到立方体单元格中有八个点，有 $2^8=256$ 种不同的标量值组合。但是由于旋转平移对称性可以进一步缩减案例中的数目。关于 Marching Cubes 的算法流程可以参考 Lorensen 等人的工作 {cite}`lorensen1998marching`。


一个 2D 温度场的等值线（等温线）绘制结果如{numref}`fig-visualization-scientific-temperature` 所示。
```{figure} fig/visualization-scientific-temperature.png
:name: fig-visualization-scientific-temperature
2D 温度场的等温线可视化。
```

{numref}`fig-visualization-scientific-marching_cubes_results`给出了一些利用Marching Cubes算法进行重建的结果。



```{figure} fig/visualization-scientific-marching_cubes_results.png
:name: fig-visualization-scientific-marching_cubes_results
行进立方体算法的一些结果。
```

## 矢量场可视化

矢量场可视化通过图形化手段表达矢量数据的方向、大小及动态特性，是流体力学、气象学、电磁学等领域的核心分析工具。

### 箭头表示法

对于矢量的可视化，常见的方法是使用箭头（arrows）来表示矢量的方向和大小。如{numref}`fig-visualization-scientific-vector_field` 展示了一些常用的箭头和用箭头表示的矢量场。

```{figure} fig/visualization-scientific-vector_field.png
:name: fig-visualization-scientific-vector_field
常用来描述矢量场的箭头和可视化的效果。
```

设 $\mathbf{V} $ 为定义在域 $D$ 上的矢量场，其中 $\mathbf{V}: D \rightarrow \mathbb{R}^n$（通常 $n$ = 2 或 3 ），表示每个点 $x \in D$ 的矢量值。

箭头方向对应矢量的方向，而箭头长度则是将矢量的数值大小映射到可视化中所用的一种尺度表示，通常会乘以一个缩放因子来避免过长或过短的箭头。
但需要注意的是，这个缩放因子只用于将“矢量大小”转换成“箭头长度”的可视比例，并不等同于场景的真实空间尺度。

- **方向**：
   在点 $x$ 处的箭头方向与矢量 $\mathbf{V}(x)$ 方向一致。可以用矢量的单位向量 $\hat{\mathbf{v}}(x) = \frac{\mathbf{V}(x)}{\|\mathbf{V}(x)\|}$ 表示，其中 $\|\mathbf{V}(x)\|$ 是矢量的大小（模长）。

- **长度**：
   箭头的长度通常与矢量的大小成比例。可以定义为 $L(x) = k \cdot \|\mathbf{V}(x)\|$，其中 $k$ 是缩放因子。

最终，矢量场的可视化 $\mathbf{V}$ 可以表示为一组箭头，其中每个箭头的位置、方向和长度由 $\mathbf{x}$、$\hat{\mathbf{v}}(x)$ 和 $L(x)$ 决定。这可以表示为 $\mathbf{U}(x) = (\text{position: } \mathbf{x}, \text{direction: } \hat{\mathbf{v}}(x), \text{length: } L(x))$。

这类方法能对矢量场进行直观的展示，且实现简单。但是要么在高密度区域易重叠（视觉混乱），要么使用足够大的图片画出箭头但像素利用率低。

### 流线，路径线，迹线

在矢量场可视化中，流场（例如空气流动、水流等）可视化是其中最常见且直观的重要应用，许多矢量场可视化技术最初就是为流场设计的。流场可视化用于研究和理解复杂的三维涡流动和湍流的物理过程。这些流动可能是稳定的或非稳定的，流动模式也可以以多种方式显示，如染料或烟雾注入流场后拍摄的照片，或是使用一些技术（如热线或数字粒子图像测速法）测量的矢量场。为了更系统地分析流动特性，人们通常会从测量数据中提取流线、迹线或路径线等辅助图形，用以揭示流体的局部行为和整体演变。
```{figure} fig/visualization-scientific-traditional_method.png
:name: fig-visualization-scientific-traditional_method
不同可视化技术在相同2D流场中的比较: (a) 箭头图, (b) 流线段, (c) 线积分卷积 (LIC), (d) 基于拓扑的方法。
```

**1. 流线（streamlines）**

流线是相对静止（稳态）或瞬时切片情况下，通过一个种子点在空间中连续积分速度向量得到的空间曲线。流线关注的是瞬时流场的结构，在非稳定流场中流线的形态会随时间变化。这里积分所使用的速度向量是在特定时刻的流场中各点的流速矢量。换言之，流线展示了“如果在特定时刻将粒子置于某点，它的瞬时流动方向轨迹”（如{numref}`fig-visualization-scientific-steamlines`），但并不是一条真实的运动轨迹，不应用于展示流体随时间的实际运动路径。

```{figure} fig/visualization-scientific-steamlines.png
:name: fig-visualization-scientific-steamlines
流线描述动态矢量场的效果。
```

设流场在时刻 $t_0$ 的速度场为 $\mathbf{v}(\mathbf{X}, t_0)$。
引入一个积分参数 $s$，流线 $\mathbf{X}(s)$ 可以定义为：

$$
\frac{d\mathbf{X}(s)}{ds} &= \mathbf{v}(\mathbf{X}(s), t_0), \\
\mathbf{X}(0) &= \mathbf{X}_0.
$$ (visualization-scientific-streamlines1)

其中：
- $ \mathbf{X}_0$ 是流线上一个起始点；
- $s$ 可以理解为沿曲线的“积分步”或“路径长度”参量；
- $\mathbf{v}(\mathbf{X}(s), t_0)$ 表示在时刻 $t_0$ 位置 $\mathbf{X}(s)$ 的速度向量。


流线的计算流程：
1. 选取种子点：可手动或自动选择若干点作为粒子的初始位置；
2. 数值积分：在向量场中，以初值 $\mathbf{X_0}$ 为起点，通过积分方法（如**欧拉方法**或**龙格-库塔方法**，
前者是一阶近似，计算快但精度低；后者有四阶精度，稳定性高，广泛应用于工程仿真）不断更新粒子位置；
3. 停止条件：达到网格边界、速度阈值过小或最大积分步数后终止。
4. 将积分得到的点序列连成曲线，并对曲线进行着色(如速度大小)或其它视觉编码。

也可以通过一些实验的方法观测流线。由于流线只有在很短的时间内才可以认为是恒定的，于是实验上观测流线的方法是，观察摄入染料的短时间内（曝光时间量级）线形。一些流线展示的实验结果如下图。

```{figure} fig/visualization-scientific-streamline.png
:name: fig-visualization-scientific-streamline
一些流线实验例子。
```

对于时变流场，则可以选择路径线和迹线来展示随时间变化的流动。

**2. 路径线（pathlines）**

与流线不同，路径线在非稳态流场（随时间变化的场）中表示从开始点到结束点的实际运动轨迹。它反映了粒子在真实时间维度下的移动过程。
因此，在稳态流场中，各处流速不随时间变化，路径线与流线重合，但在非稳态流场中，路径线与流线不再等价。

对于一个在时刻 $t_0$ 处于位置 $\mathbf{X_0}$ 的粒子，将其随时间 $t$ 变化的轨迹记为 $\mathbf{X}(t)$，则满足：

$$
\frac{d\mathbf{X}(t)}{dt} &= \mathbf{v}(\mathbf{X}(t),t),\\
\mathbf{X}(t_0) &= \mathbf{X_0}.
$$ (visualization-scientific-pathlines1)
其中：
- $\mathbf{v}(\mathbf{X},t)$ 是非稳态（或稳态）流场随时间变化的速度函数；
- $\mathbf{X}(t)$ 称为路径线或粒子轨迹。

路径线计算流程：
1. 时序数据获取：流场在多个时间步(如 $t_0$，$t_1$，$t_2$，…)上都有速度向量信息；
2. 积分方法：在每个时间步以粒子当前位置为初值，积分到下一时间步时的粒子位置；
3. 连接轨迹：将所有时间步粒子的空间位置连成曲线。

路径线可以通过跟踪射入的粒子的长程轨迹来实验得到。
如下面的实验图。

```{figure} fig/visualization-scientific-pathline.png
:name: fig-visualization-scientific-pathline
路径线样例：长时间曝光的篝火火花照片显示了热空气流动的路径。© Wikipedia
```

**3. 迹线（streaklines）**

用来表示在同一空间位置持续释放的粒子所形成的轨迹。直观地说，想象不断地往水流中滴墨水，那么这些墨滴在流体中被带动形成的一条连续曲线，就是迹线。迹线描述的事连续注入的粒子的集合运动，而不是依赖某个粒子的历史轨迹。迹线在实验流体动力学中常用，比如通过注入染料或烟雾来观察流动。

设:
- $\mathbf{v}(\mathbf{X},t) $为流场的速度场（向量场）；
- 在坐标 $\mathbf{X}_0$ 处持续释放粒子；
- $\tau$ 表示粒子的释放时刻（可从 0 到当前时刻 $t$ 范围内）。

对于在时间 $\tau$ 被释放的粒子，我们用 $\mathbf{X}(t;\tau)$ 表示它在时间 $t\ge\tau$ 时所处的位置，满足以下常微分方程：

$$
\frac{d\mathbf{X}(t;\tau)}{dt} = \mathbf{v}(\mathbf{X}(t;\tau),t),\\
$$ (visualization-scientific-streaklines1)

并且它的初值条件（初始位置）为:
$$
\mathbf{X}(\tau;\tau) = \mathbf{X}_0.
$$ 

即该粒子在被释放的瞬间（$t=\tau$）在 $\mathbf{X}_0$ 位置。

```{figure} fig/visualization-scientific-streakline.png
:name: fig-visualization-scientific-streakline
迹线样例：风洞中汽车周边的空气流动。© Wikipedia
```

总结来说，流线、路径线、迹线可视化在流体动力学、气象学和海洋学等领域中非常有用，它们帮助揭示流体流动的模式和结构。三者均是理解流体运动特征、构建流体可视化的重要工具。在非稳定流动中，迹线和流线、路径线会有明显的差异，而在稳定流动中，三者会重合。
在具体应用时，应根据是否稳态、对粒子演化的关注程度以及实验/模拟中注入位置等因素，选用或结合使用这几种曲线形式来进行分析与展示。

### 点噪声法

点噪声法（spot noise）属于基于纹理的矢量场可视化技术，通过在图像平面上铺设许多“微型噪声点（spots 或 dots）”，并且让这些小斑点的形状、方向、拉伸程度等与局部向量信息相对应，从而在整体上形成密集且连续的流动纹理效果。

点噪声法的核心原理：
1. 基础噪声纹理：先生成一张均匀随机噪声图（或散点图）；
2. 局部变形：在向量场每个像素/采样点周围放置一个“点扩散核”，根据该位置上的速度方向 $\mathbf{v}(x,y)$ 调整点扩散核形变（例如：让其朝流向方向拉伸）；
3. 叠加与渲染：将所有点扩散核投影或累加到最终图像中，形成从微观层面上就已指向流向的纹理图。

可以使用一个简单的线性组合来生成最终的可视化图像，例如：

$$
I(x, y) = I_0 + \alpha \cdot N(x, y) 
$$ (visualization-scientific-spot_noise)

其中，$I(x, y)$ 是最终图像的强度，$I_0$ 是背景强度，$\alpha$ 是一个调节因子，用来控制噪声对最终图像的影响程度。

```{figure} fig/visualization-scientific-spot_noise.png
:name: fig-visualization-scientific-spot_noise
基于点噪声法可视化标量场，（a）值，（b）梯度，（c）流，（d）速度势。
```

点噪声法算法的优点在于它能生成直观流场可视化图像，适合展示复杂的流体动力学特性。缺点是在处理非常高速或高度湍流的流场时，可能无法清晰展示所有细节。

### 线性积分卷积

线性积分卷积（Line Integral Convolution，LIC）是一种具有 2D/3D 矢量场通用性的新技术，能够成像密集矢量场、独立于预定义的纹理生成稠密可视化效果，并且可以应用于二维和三维数据中。

在引入LIC之前，我们先介绍图线和纹理之间的卷积融合。数字微分法（Digital Differential Analyzer, DDA）是一种用于栅格化直线段的技术，即将数学上的连续直线转换为像素网格上的近似表示。
通过将曲线进行栅格化，然后和背景纹理进行求卷积，可以得到包含两者信息的融合。DDA-Concolution算法的流程如下图所示：

```{figure} fig/visualization-scientific-ddac.png
:name: fig-visualization-scientific-ddac
数字微分卷积法的操作流程。
```

对于DDAC算法，假设速度场近似成直线效果还好，但是对于曲率半径很小的点不准确。而且本身简单地应用卷积，自带一个去噪平均化效果，高频的会看不出，造成信息频率缺失不平衡。还有aliasing的问题，受制于分辨率限制，导致可能会有不对称的结果。因此后续会提出LIC算法来修缮上述问题。

LIC算法简单来讲就是加上了两个限制，沿流线进行卷积就可以解决曲率精度不够的问题，同时通过内禀保证对称性来解决离散化时候的走样（aliasing）问题。


$$
P_{i} &= P_{i-1} + \frac{V(\lfloor P_{i-1} \rfloor)}{|V(\lfloor P_{i-1} \rfloor)|} \triangle s_{i-1}  \\
P_{i}' &= P_{i-1}' - \frac{V(\lfloor P_{i-1}' \rfloor)}{|V(\lfloor P_{i-1}' \rfloor)|} \Delta s'_{i-1} 
$$ (visualization-scientific-LIC1)


其中：

$$
P_{0} &= (x+0.5, y+0.5), \\
P_{0}' &= P_{0}
$$
$P$ 表示图像（纹理图像）中的像素位置。$V(\lfloor P \rfloor)$ 表示在格点 $(P_x, P_y)$ 上输入矢量场的矢量。

因此，流场的卷积结果可以表示为：

$$
h_{i} = \int_{s_i}^{s_i + \Delta s_i} k(w) dw 
$$ (visualization-scientific-LIC2)
其中  $\Delta s_i$ 和 $\Delta s_i'$ 是沿着平行于矢量场的线从 $P_i$ 到最近单元格边缘的正负参数距离。 
$\Delta s_i = \min(s_{top}, s_{bottom}, s_{left}, s_{right})$，$\Delta s_i'$ 类似。
最终图像上应该呈现的结果由 $F'(x, y)$ 给出：

$$
F'(x, y) = \frac{\sum_{i=0}^l F(\lfloor P_i \rfloor) h_i + \sum_{i=0}^{l'} F(\lfloor P_i' \rfloor) h_i'}{\sum_{i=0}^l h_i + \sum_{i=0}^{l'} h_i'}
$$ (visualization-scientific-LIC3)


对于LIC算法的分析可以参考[此博客网站](http://www.zhanpingliu.org/Research/FlowVis/LIC/LIC.htm)。此博客同时给出了其他经典的流场可视化实现例子，感兴趣的同学请自行阅读。

```{figure} fig/visualization-scientific-lic_wind.png
:name: fig-visualization-scientific-lic_wind
LIC算法效果类似于一堆细沙被强风吹散。
```

```{figure} fig/visualization-scientific-lic_pipeline.png
:name: fig-visualization-scientific-lic_pipeline
LIC算法流程。
```

在传统的 LIC 方法中，每个像素点的计算都是独立的，而 TexMap LIC 则通过将 LIC 运算映射到纹理空间中来优化这一过程。
这种方法使得 LIC 能够更好地利用现代图形硬件的能力，尤其是在处理大规模或复杂的矢量场数据时，能够显著提高渲染速度和图像质量。
Volume LIC 是将 LIC 方法扩展到三维空间的一种技术，用于三维矢量场的可视化。它通过在体积数据中沿着矢量流线进行积分卷积，生成能够表现三维流动特性的图像。

### 流场可视化前沿

可视化的前沿领域集中于对于以下问题的探索，如不稳定流（Unsteady Flow）的可视化、可视化算法的加速、结合网络的可视化。

- 不稳定流可视化

不稳定流可视化专注于展示随时间变化的流体动力学特性，VAUFLIC (Vector-Advection Upstream Line Integral Convolution)对传统 LIC 的一种改进，专门用于可视化非稳定流。
该方法通过考虑矢量场中的流动方向和速度，增强了图像的细节和流线的连续性，特别适合于描绘复杂的流动模式，如涡旋、湍流等。

- 可视化算法的加速

可视化的一个经典难题是对于较大的流场需要很大的时间开销，类似于光线追踪问题中的路径追踪求解方案，并行处理是一个经典的对策。
通过数据并行（每个线程处理部分数据）和任务并行（每个线程解决部分算法流程）处理，可以显著提高大规模流场数据集的处理速度和效率。

并行解决在处理复杂和大数据流场时尤为重要，如气候模拟和高分辨率流体动力学模拟。

- 结合网络的可视化

随着深度学习在各个领域迅速结合传统工作，长短时记忆网络（LSTM）在流场可视化中的应用也逐步出现，涉及到使用深度学习技术来分析和预测流体动力学行为。

LSTM 可以帮助识别流场中的复杂模式，如周期性涡旋，以及长期依赖关系。这种方法在预测未来的流体行为以及分析非稳定流动中表现出了巨大的潜力。

Flow Net 从流场数据集生成的一组流线或流面，然后使用自编码器来学习它们各自的潜在特征描述符。然后利用潜在空间中的隐变量去生成符合输入表征的流线或流面，来得到一个合理的混合预定义模式的结果。

### 其他方法

其他的矢量场可视化方法还有：流拓扑可视化 (Flow Topology Visualization)，粒子系统 (Particle-based Methods)等，如{numref}`fig-visualization-scientific-flow_vis` 所示。

```{figure} fig/visualization-scientific-flow_vis.png
:name: fig-visualization-scientific-flow_vis
Jarke J. van Wijk, Image Based Flow Visualization ©http://www.win.tue.nl/~vanwijk/ibfv/
```

在实际应用中，标量场也常与矢量场一起，被用来表述具有多类型数据的空间信息。
一个常见的组合是天气预报时的温度场和风场，如{numref}`fig-visualization-scientific-scalar_and_vector`。

```{figure} fig/visualization-scientific-scalar_and_vector.png
:name: fig-visualization-scientific-scalar_and_vector
由（a）传统风旗和（b）流线与风旗组合描绘的风场和温度场 {cite}`pilar2013representing`。
```

## 张量场可视化
张量场可视化是一种将复杂的多维数据转换成直观图形的技术，广泛应用于材料科学、医学成像（如扩散张量成像 DTI）、地球物理学等领域。
因为张量本身并不直观，所以张量可视化会采取一些已存在的局部基元特征来体现空间分布的张量信息。
在大部分应用中，张量一般是对称的（如应力张量），对称张量有三个特征值：$\lambda_1 \ge \lambda_2 \ge \lambda_3$，对应三个主方向/特征向量 $\mathbf{e_1}$，$\mathbf{e_2}$，$\mathbf{e_3}$，通过特征值分解，我们可以得到张量的几何特征，从而进行可视化。
以下是三种常见的张量可视化方案：

### 基于图元的可视化（Glyph-based Visualization）

此类方法通过几何形状（Glyph）的方向、大小和形状来编码张量的各向异性特性，常见图元包括箭头、椭球、圆柱、超二次曲面等。

- 椭球体：将对称正定张量分解为三个主方向和相应长度（特征值）后，绘制椭球体；椭球轴的方向与张量主方向一致，轴长与特征值大小相关。
- 圆柱：用于扩散张量成像（DTI），圆柱长轴方向为纤维主扩散方向，直径反映扩散各向异性指数。
- 盒状符号：以一个长方体来表示三个正交特征方向，长宽高对应特征值。

基于图元的可视化可以直观表达局部张量特性，但是在高密度区域易产生视觉混乱。

### 基于纹理的可视化（Texture-based Visualization）

这类方法通过在空间中铺设或合成规则或随机的纹理图案(如线条、条带、噪声纹理)，并根据张量的大小、方向或不变量等信息，调节相应纹理的“密度、形状、取向、颜色”等视觉特征，从而在整个区域内连续地渲染张量分布。
纹理可视化具有以下核心特点：
- 全局连续性：纹理覆盖整个数据区域，避免基于离散图元的视觉碎片化。
- 方向编码：纹理走向与张量主方向对齐（如条纹沿主方向延伸）。
- 各向异性表达：纹理密度或对比度反映各向异性程度（高各向异性区域纹理更密集/高对比）。
- 多属性融合：颜色映射可叠加其他标量属性（如应力大小）。

此类方法适用于大范围平滑张量场，具有很高的视觉连续性和表达精度，但是需要生成全局纹理，因此产生较大的计算开销。

### 超流线（Hyperstreamlines）

在矢量场中，流线体现局部向量方向。而在张量场中，如果我们将主方向之一当作“流动方向”，沿该方向跟踪曲线，并在垂直平面内用椭圆或其他形变展现张量在该点的其他主值和主方向，就得到超流线。
超流线同时保留空间走向（第一主方向）与局部张量形态（其他特征方向），在一条曲线上把张量随空间变化的特征“画出来”，从而能够提供空间上的直观感知，使观察者能够从不同角度观察和分析数据。
具体来说，超流线有以下三个特点：
- 主方向：超流线通常沿最大特征值方向 $\mathbf{e_1}$ 追踪。
- 局部截面：沿着曲线的每一采样点，生成一个截面，并在截面上用椭圆(或其他形状) 表示 $\lambda_2$，$\lambda_3$ 的相对大小和方向。
- 曲线积分：在坐标空间中，以 $\mathbf{e_1}(x)$ 作为导向向量场，数值积分出曲线 $\mathbf{x}(s)$，从而得到超流线主体走向。

超流线多应用在应力张量可视化中以进行材料断裂分析，或用于展示扩散张量场的各向异性传播。
该方法可以同时表达主方向趋势与横截面特性，但是也需要面临三维空间中视觉遮挡的挑战。


每种类型的方法都有其特定的应用场景和优势，选择哪一种取决于要可视化的数据类型和需要强调的数据特征。例如，图元适合强调数据点的局部特征，而纹理和超流线则更适合展示数据的整体流动和结构。{numref}`fig-visualization-scientific-mri` 和 {numref}`fig-visualization-scientific-tensor_types` 给出相应的张量可视化效果。

```{figure} fig/visualization-scientific-mri.png
:name: fig-visualization-scientific-mri
通过箭头来可视化核磁共振图像。
```

```{figure} fig/visualization-scientific-tensor_types.png
:name: fig-visualization-scientific-tensor_types
三种张量可视化的例子图。
```