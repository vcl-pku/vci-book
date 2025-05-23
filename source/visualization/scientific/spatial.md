# 表面数据、体数据的可视化

<!-- 与二维数据主要聚焦于物理量类型不同，在三维空间中，数据还可能以不同的几何形式呈现在空间中，
科学数据的空间结构成为可视化设计的关键依据。常见的三维科学数据可以分为两类：表面数据和体数据。前者通常指具有明确几何边界的二维嵌入式结构，如医学图像中的器官表面或地质断层；而后者则描述填满空间的体积信息，如CT扫描结果、气象体场或模拟中的物质密度分布。对不同结构的数据，可视化技术需要在几何建模、渲染策略与交互方式上做出相应调整，以有效呈现其内部结构与分布特征。 -->
在实际应用中，数据不仅会有物理属性上的不同，还可能以不同的几何形式呈现在空间中：
某些数据仅限定在诸如曲面、地形、CAD 模型边界等“表面”上，需要进行**表面可视化**。
更多时候，数据分布在三维体内部，如医学成像的 CT 或 MRI 扫描结果、流体模拟的 3D 网格数据等，这些数据往往需要**体积可视化**技术才能揭示其内部结构。
因此，本节中我们继续探讨“表面数据”和“体数据”在可视化时所采用的不同技术。
<!-- 还可能有着多种多样的组织方式，包括且不限于：结构化网格（按规则、均匀间隔进行采样，形成具有行列索引关系的网格）、非结构化网格（三角形、四面体、多面体网格等具有不规则连接关系的网格）、无网格拓扑的离散点点云等等。 -->

<!-- - **结构网格**数据指在空间或时空范围内按规则、均匀间隔进行采样，形成具有行列（或行列层）索引关系的网格。例如：流体力学中的规则网格（如 CFD 仿真输出，采用均匀笛卡尔网格），医学影像的 3D 体素数据（CT、MRI 采用固定分辨率扫描）。 结构网格具备简单的拓扑关系，因而易于索引、插值和处理；但其不灵活的分辨率布置会导致数据量庞大或分辨率不足，在非均匀或复杂几何域中也难以适配。

- **非结构网格**数据指在空间中采用三角形、四面体、多面体等具有不规则连接关系的网格单元对域进行剖分，存储每个单元的属性。
例如：有限元分析（FEM）模型、地质构造模拟网格（地层间往往复杂，需自适应网格）、海洋/气象模型对海岸线等不规则区域的剖分。
非结构网格可灵活适应复杂几何边界，并可在感兴趣区域加密采样，但数据结构较复杂，渲染和拓扑运算(如等值面提取、流线跟踪)需要针对单元连接关系做更多预处理。

- **离散点云**数据指在空间或时空中仅给出一组拥有坐标及测量值（标量或矢量等）的散点，没有显式的网格连接关系。 常见的离散点云数据包括：激光雷达扫描（LiDAR）、粒子仿真输出（如分子动力学、天体多体模拟）、观测仪器采样的稀疏离散测量数据。 离散点云数据无需事先网格化，灵活度高，容易真实地反映局部细节；但可视化算法需要做插值、重构或聚类，才能形成连续可视效果，且在大规模点云下的渲染与交互也面临性能挑战。 -->

## 按空间结构分类：表面数据、体数据

### 表面数据

表面数据（Surface Data）用于表示三维对象的外部形状和结构，通常以网格和参数化表示，其中网格是由顶点、边和面组成的集合，通常用于表示复杂的三维形状，参数化表示为通过数学公式来定义表面，如贝塞尔曲面或 NURBS (非均匀有理 B 样条)。
表面数据具有高维嵌套（二维结构嵌入三维空间）和局部细节丰富的特点。可视化时，准确展现几何细节、处理复杂拓扑结构以及支持高效渲染是主要挑战。

### 体积数据

体积数据（Volume Data）表示的是三维空间内部的数据分布，每个空间位置对应一个数据值。常见的体积数据包括：医学成像（如 CT 或 MRI 扫描）、气象模拟（如三维风速场或云量分布）、工程仿真（如流体动力学模拟的速度和压力场）。
体积数据具有数据量大、内部结构复杂且可能缺乏明确边界的特点，如何有效提取内部特征、减少遮挡干扰，以及在保证细节的同时进行高效绘制是体积数据可视化的关注重点。

## 表面可视化

表面可视化通过几何网格（如三角面片、NURBS 曲面）表达物体的边界或等值面，聚焦于几何形状与表面属性的展示。

### 网格渲染（Mesh Rendering）

通过基本的光照与着色模型，网格可以被渲染为具有立体感的图像。虽然这一过程在现代图形管线中已高度标准化，但它仍是表面可视化的基础：网格不仅提供几何支撑结构，还为进一步的数据映射（如纹理、颜色）提供载体。此类方法可高效支持旋转、缩放、剖切等交互，适用于工程设计、地形建模等强调几何细节的可视化任务。

### 表面纹理映射（Surface Texture Mapping）

为了表达几何之外的数值信息，常需将数据映射为纹理贴附在曲面上。与“纹理贴图”思想相似，可在表面上铺设或合成纹理图案，用纹理的颜色、透明度或条带方向来编码数据，如{numref}`fig-visualization-scientific-surface_fields` 所示。
该方法技术核心有以下两点：
- 纹理坐标：每个网格顶点可关联纹理坐标 $(u, v)$，然后把标量或矢量信息转换为纹理像素，再在着色阶段将纹理“贴”到曲面上。
- 属性叠加：可将纹理与颜色映射或光照效果结合，在曲面的某些区域高亮显示关键信息，或通过透明度揭示下层结构。

<!-- 为了表达几何之外的数值信息，常需将数据映射为纹理贴附在曲面上。与传统纹理贴图类似，这类方法将每个网格顶点关联纹理坐标 $(u, v)$，再将物理量（如温度、应力、速度）转换为纹理像素，实现对连续数据场的编码和可视。 -->

这种方法特别适用于在复杂曲面上表达连续但细节丰富的信息，如流动路径、结构应力分布、生理参数场等，是连接数据与几何的一座“桥梁”。

```{figure} fig/visualization-scientific-surface_fields.png
:name: fig-visualization-scientific-surface_fields
表面可视化示例。左：表面颜色映射；右：表面矢量场（主曲率方向）可视化。© Libigl
```

## 体积可视化

当数据不只存在于表面，而是填充整个三维区域时，则需要用体积可视化技术来展示体内部的信息。一种可视化思路是将体积数据转换成表面数据然后进行可视化，另一条思路则希望通过某种手段直接渲染体数据，使我们的视线能透过表层直达内部，这种方法被称为体渲染（volume rendering）。我们将首先介绍体数据的表面渲染方法，而后介绍体渲染方法。

### 剖面法

为了观察体数据的内部结构，一种最直观的方法是直接切开查看：选取任意角度和位置的二维切面（slice），在该剖面上应用常见的二维可视化技术，展示其所截取的数据特征。对于使用四面体等不规则网格表示的体数据，也可以采用相应的剖切策略——沿四面体单元的边界进行裁剪，丢弃位于剖面一侧或被剖面穿过的单元，仅保留其余部分，从而在保留拓扑结构的同时展示截面内的数据分布。

```{figure} fig/visualization-scientific-slicing_based.png
:name: fig-visualization-scientific-slicing_based
:width: 80%
剖面法示例。上：场馆空气流动情况，二维切面上的矢量场可视化 © Wikipedia；左下：二维切面上的标量场可视化 {cite}`walking2024`；右下：沿不规则西面体网格剖分后进行标量场可视化 © Libigl。
```
<!-- 


````{subfigure} AB
:gap: 20px
:subcaptions: below
:name: fig-visualization-scientific-slicing_based

```{image} fig/visualization-scientific-slice_bunny.png
```

```{image} fig/visualization-scientific-octree.png
```
光线投影算法加速。左：自适应采样；右：八叉树结构。
```` -->


### 等值面

等值面绘制从三维标量场中提取出所有等于某个给定数值（等值）的点所构成的等值面，常用于可视化密度、温度、压力等空间分布特征。通过如 Marching Cubes 等经典算法，可将体数据转化为可渲染的多边形网格，支持进一步上色、纹理贴图等表面可视化操作。等值面绘制能有效揭示体数据中隐含的边界结构与连续变化趋势，是医学图像分析、流体模拟分析等领域的重要方法。前文已有介绍，这里不再赘述。

### 体渲染

体渲染最初用于在计算机图形中生成云、烟、火焰、果冻等半透明物体的可视化效果。这些物体通常不具有明确的表面边界，并且物质的密度相对较低，，形状模糊且内部结构复杂。于是研究者们提出了一种新的思路：直接描述空间中的物理属性分布（如密度、温度、颜色、发光强度），并模拟光线在参与性介质（如云雾、生物组织）中的传播过程，将3D体内部的“密度”或“标量值”映射为颜色和透明度，再投影到屏幕上，形成半透明的可视化效果。这种方法的最大优势在于它无需提取表面的几何网格，而是直接考察物质介质中的属性分布情况并计算透射出介质的光照，实现了对飘渺的云彩、朦胧的烟雾等自然现象的真实模拟。

而后体渲染技术也被广泛用于科学可视化，尤其是在医学成像领域。这些领域中的数据通常以规则的模式采集到，如体素（三维像素，如{numref}`fig-visualization-scientific-voxels` 中的三维立方体或体单元）数据。体渲染可以突出体积数据中感兴趣的数值范围（如医学中突出骨骼、血管等），揭示数据的全局特征与局部细节。

```{figure} fig/visualization-scientific-voxels.png
:width: 70%
:name: fig-visualization-scientific-voxels
三维体素数据示例。
```

<!-- 在这种表示中，物体被视为由大量小粒子组成的集合体，而非一个具有固定形状和边界的实体，这允许光线以更自然的方式穿过物体，从而更好地模拟光子与粒子间的相互作用。
当光线穿过这些由粒子群构成的物体时，它们不断与粒子发生相互作用，例如散射和吸收。这种相互作用导致光线路径的改变，从而产生了体渲染中独特的视觉效果。 -->


在体渲染过程中，传递函数（transfer function）的设计是其中的关键环节：
传递函数用于将体素所携带的各种数据信息映射成颜色和不透明度，从而在视觉上表现出不同的密度或材质特征。
如{numref}`fig-visualization-scientific-tooth` 所示，简单的转换可以得到一张黑白图像（左），而通过对不同的生物组织设计具有不同颜色映射和透明度的设计函数（如：透明的蓝色表层、红色的半透明血管、白色的不透明牙釉质），则可以更清晰地体现其中的关键结构。

```{figure} fig/visualization-scientific-tooth.png
:width: 100%
:name: fig-visualization-scientific-tooth
传递函数设计示例：人类牙齿 CT 结果可视化。
```

<!-- 我们首先对比体渲染和之前提到的表面渲染，然后介绍体渲染的物理公式，最后介绍体渲染的经典实现算法。 -->

接下来，我们将首先介绍体渲染技术的基本原理，而后介绍其经典的实现算法。

#### 体渲染的原理

体渲染建立在光学传输模型的基础上：如{numref}`fig-visualization-scientific-transmission` 所示，光透射过体积介质打到相机屏幕上，出射光强决定了图像的渲染结果。

```{figure} fig/visualization-scientific-transmission.png
:width: 40%
:name: fig-visualization-scientific-transmission
体渲染的原理：光与介质作用后的出射光强决定了图像渲染结果。©️ https://www.scratchapixel.com/ [^ref]
```
[^ref]: 图片来源于网站 https://www.scratchapixel.com/lessons/3d-basic-rendering/volume-rendering-for-developers/volume-rendering-summary-equations.html

在光的透射过程中，由于光子与体积介质中的粒子发生作用，光强会因以下现象发生改变，如{numref}`fig-visualization-scientific-phenomena` 所示：

- 吸收 (absorption)：光子被粒子吸收，会导致入射光的辐射强度减弱。
- 放射 (emission)：粒子本身可能发光，这会进一步增大辐射强度。
- 散射 (scattering)：光子和其他粒子相碰撞后，导致方向发生偏移，如果偏移朝向光束方向则会增加光路上的辐射强度（内散射，in-scattering），反之则会减弱入射光强度（外散射，out-scattering）。

值得注意的是，体渲染中一般不涉及反射模型。因为反射通常出现在具有明确表面或镜面特性的物体中，故在经典的体渲染里并不常用。

```{figure} fig/visualization-scientific-phenomena.png
:width: 60%
:name: fig-visualization-scientific-phenomena
体渲染的原理：光与介质作用的四种现象。[^ref]
```

<!-- 我们通过{numref}`fig-visualization-scientific-transmission` 来说明这些系数导致的光学方程。 -->

如{numref}`fig-visualization-scientific-transmission` 所示，接下来我们将对上述现象进行建模并导出光学方程。

取一处厚度为 $\Delta s$、横截面积为 $E$的介质微元。
记粒子面密度为 $\rho$，则在这个空间内的粒子数目为 $\rho E \Delta s$（假设所取的介质足够薄，薄到跟粒子直径近似时，可以认为粒子无重叠地散开在这一薄层内），记介质中的杂质粒子的横截面积为 $A=\pi r^2$，则总的遮挡面积为 $\rho E \Delta s A$。则粒子在介质中的遮挡的比率为 $\epsilon=\rho E \Delta s A / E = \rho A \Delta s$。也就是说在所有入射光线中，有占比 $\epsilon$ 的光线被粒子遮挡，剩余 $1-\epsilon$ 的光线穿透介质。需要注意的是：该计算方法需要粒子的平均密度较低，从而粒子的大小与粒子间的平均距离相比可以忽略不计——这是统计独立碰撞的先决条件，通常适用于任何气态介质，但不适用于沙子和雪等致密颗粒介质。

这意味着，记入射光强度为 $I_\text{i}$，出射光强度为 $I_\text{o}$，那么由于介质中的杂质粒子遮挡，光强的变化量为：

$$
I_\text{o} - I_\text{i} = \Delta I = -\rho(s) A I_\text{i} \Delta s 。
$$ 

将上式扩展到普遍情形：对于连续介质而言，在光束路径 $[s_\text{start},s_\text{end}]$ 上，假设 $\rho(s)$ 是沿着光路的函数，那么光强也将沿着光路变化，记为 $I(s)$，则上式可写为：
$$
\mathrm{d}I(s)= -\rho(s) A I(s) \mathrm{d} s = -\tau_a(s)I(s) \mathrm{d} s 。
$$ 

<!-- 类似地，记射入介质时的光强为 $I(s_\text{start})=I_\text{i}$，射出介质时光强为 $I(s_\text{end})=I_\text{o}$，那么通过积分得到二者之间的关系：

$$ 
I_o = I_i \exp \left( -\int_{s_\text{start}}^{s_\text{end}} \rho(s) A I(s) \, \mathrm{d} s \right) 
= I_i \exp \left( -\int_{s_\text{start}}^{s_\text{end}} \tau_a(s) I(s) \, \mathrm{d} s \right) ，
$$  -->

其中我们记 $\tau_a = \rho A$ 为吸收系数。对于其他的放射和散射项，也可以建立类似的数学模型。

对于放射而言，假设介质粒子放射发出的光的光强为 $I_e$，那么类似地，在介质微元一侧能接收到的光线占比即为例子占据微元截面的比例系数，因此放射系数 $\tau_e = \tau_a$。

对于散射而言，假设外部光的光强为 $I_s$，我们简单地将受到散射的光子占比记为散射系数 $\tau_s$，包括外散射（弹射光子偏移当前光路）系数和内散射（弹射外部光子偏向光路）系数。

将上述四个现象集合起来，于是可以得到：

$$ 
\frac{\mathrm{d} I}{\mathrm{d} s} = -\tau_a I(s) + \tau_a(s) I_e(s) - \tau_s(s) I(s) + \tau_s I_s(s)，
$$ (visualization-scientific-volume_rendering_diff)

其中等式右边四项分别对应吸收、放射、外散射和内散射。为方便，记 $\sigma_t = \sigma_a+\sigma_s$ 为消光系数（extinction coefficient），$q(s)=\tau_a(s) I_e(s)+\tau_s I_s(s)$ 为源项，包含介质的自放射和内散射，从而上述方程可以整理为一个典型的一阶线性常微分方程形式：

$$
\frac{\mathrm{d} I}{\mathrm{d} s} +\tau_t(s) I(s) = q(s)。
$$ (visualization-scientific-volume_rendering_typicaldiff)

为积分该方程，我们记积分变量为 $x$，并引入积分因子：

$$
\bar{T}(x)=\exp(-\int_{0}^x\sigma_t(x')\mathrm{d}x')，
$$ (visualization-scientific-volume_rendering_transmittance)

它代表了光从原点（相机位置）$0$ 到积分点 $x$ 后未被吸收或散射出去的概率，也被称作**透射率（Transmittance）**，满足：$\mathrm{d}\bar{T}(x) = - \sigma (x)\bar{T}(x)\mathrm{d} x$。

考虑到：光线在起点处无衰减：$\bar{T}(0)=1$，且光强即为背景光强：$I(0)=I_{\text{bg}}$。
于是对式 {eq}`visualization-scientific-volume_rendering_typicaldiff` 从 $0$ 到 $s$ 积分得到：

$$
I(s)&=\bar{T}(s)\left[\frac{I(0)}{\bar{T}(0)}+\int_{0}^s \frac{q(x)}{\bar{T}(x)}\mathrm{d}x\right]\\
&=\bar{T}(s)I_{\mathrm{bg}}+\int_{0}^s \frac{\bar{T}(s)}{\bar{T}(x)}q(x)\mathrm{d}x。
$$ (visualization-scientific-volume_rendering_integral)

而一般来说，我们更习惯逆着光线方向积分，即，从观察者位置 $x=s$ 出发到相机位置 $x=0$ 为止，因此我们重新设置积分变量 $t=s-x$ 来代替 $x$，如{numref}`fig-visualization-scientific-volume_rendering_ray_direction` 所示，并重写透射率和光强的积分结果：式 {eq}`visualization-scientific-volume_rendering_integral`中，

$$
\bar{T}(s)&=\exp(-\int_{0}^s\sigma_t(x')\mathrm{d}x')=\exp(-\int_{0}^s\sigma_t(t')\mathrm{d}t')=T(s)
\\
\frac{\bar{T}(s)}{\bar{T}(x)}&=\exp(-\int_{x}^s\sigma_t(x')\mathrm{d}x')
=\exp(-\int_{0}^t\sigma_t(t')\mathrm{d}t')
=T(t)，
$$

这里我们将改写积分方向后的透射率表达式记为 $T(t)$。故最后得到简化形式：

$$
I(s)=T(s)I_{\text{bg}}+\int_{0}^s T(t)q(t)\mathrm{d}t，
$$ (visualization-scientific-volume_rendering)

这就是体渲染中最常用的积分方程形式。

```{figure} fig/visualization-scientific-volume_rendering_ray_direction.png
:width: 60%
:name: fig-visualization-scientific-volume_rendering_ray_direction
体渲染中的积分方向示意：实线为顺光线方向，虚线为逆光线方向。
```

<!-- 
```{admonition} 思考
:class: tip
{eq}`visualization-scientific-volume_rendering_integral` 是如何从{eq}`visualization-scientific-volume_rendering_diff` 中推导出来的呢？（提示：使用 $1/\bar{T}(s)$ 作为积分因子。）
``` -->

#### 体渲染经典实现算法

对从每个像素点发射出的每条给定方向的光线路径，我们需要计算出式 {eq}`visualization-scientific-volume_rendering` 的具体值来获得渲染结果。

<!-- 而显然这个复杂的积分是无法直接计算的，为此，研究者们开发出了各种数值积分方法。如{numref}`fig-visualization-scientific-numerical_integral` 所示。这里我们
```{figure} fig/visualization-scientific-numerical_integral.png
:name: fig-visualization-scientific-numerical_integral
各类数值积分方法，从左至右：基于均分积分区间并求和的黎曼和方法，基于高斯积分点的高斯方法，基于随机采样的蒙特卡洛方法。{cite}`rendering2021course`
``` -->

体渲染的经典实现包括光线投影与体积泼溅两套思路：前者类似于光线追踪，从视点出发逐像素发射射线，沿着体数据采样并积累颜色与透明度；后者类似于光栅化，逐个将体积数据投影到图像平面进行加权合成。接下来我们将分别进行介绍。

**1. 光线投影**

光线投影（ray casting）通过追踪从视点出发穿过体数据的虚拟光线来生成图像。每条光线与数据体内的元素相交，并计算这些相交点的颜色和强度，最终生成图像。

如{numref}`fig-visualization-scientific-ray_casting` 所示，
光线投影的步骤可以总结如下：

1. 发射光线：从观察点（通常是相机或者用户的视点）发射光线。在最基本的光线投影中，每条光线对应屏幕上的一个像素。
2. 找交点：沿光线方向步进采样体素数据（如均匀步长或自适应步长），如果采样点非整数坐标处，则可以通过一定的插值方法来计算该处的数据值。这步本质上是将体渲染的积分式通过采样转换成求和式。
3. 法线计算：渲染算法通常需要知道在每个采样点的表面法线方向。由于体积数据通常不包含法线信息，因此需要通过梯度估计（如中心差分法）来计算。
4. 分类：通过传递函数将标量值及其衍生属性（如梯度模长、曲率）映射为颜色（RGB）与不透明度（Alpha），定义不同组织的视觉表现。（图中 $\alpha=0$ 表示完全透明，$\alpha=1$ 表示完全不透明。）
5. 着色：按照光照模型的计算，比如 Phong 光照模型，来确定物体在当前位置和历史光照条件下的颜色。
6. 合成：沿着光线路径采样的多个数据值结合起来，以生成最终的像素值。每向采样一步，更新一次整条光线对应的颜色值和透明度（公式见图中）。若不透明度已积累至 1，则可以提前终止光线采样，因为后面的物质已经被完全阻挡。

````{subfigure} AB|CD|EF
:layout-sm: A|B|C|D|E|F
:gap: 20px
:subcaptions: below
:name: fig-visualization-scientific-ray_casting
:width: 80 %

```{image} fig/visualization-scientific-ray_casting0.png
:alt: 步骤1：发射光线
```

```{image} fig/visualization-scientific-ray_casting1.png
:alt: 步骤2：找交点
```

```{image} fig/visualization-scientific-ray_casting2.png
:alt: 步骤3：法线计算
```

```{image} fig/visualization-scientific-ray_casting3.png
:alt: 步骤4：分类
```

```{image} fig/visualization-scientific-ray_casting4.png
:alt: 步骤5：着色
```

```{image} fig/visualization-scientific-ray_casting5.png
:alt: 步骤6：合成
```

光线投影示意图
````

其中，分类步骤也可以作为预处理操作，置于整个渲染流程之前：预先为每个体素应用传递函数，计算出其对应的颜色和不透明度值，并将这些结果存储在体素数据中。在实际渲染过程中，系统可以直接读取这些预计算值，或在需要时通过插值获得，从而显著减少运行时的计算负担。由于这一预处理过程本身适合并行化操作，也便于在现代硬件上加速执行，因此能够有效提升整体渲染效率。然而，这种方法也存在一定的局限性——由于分类结果在预处理阶段已被固化，可视化的灵活性和精度可能相应降低。

与光线追踪中的加速策略类似，我们可以引入自适应采样或构建适当的空间数据结构来优化光线投影算法，如{numref}`fig-visualization-scientific-ray_casting_acc` 所示。自适应采样在不同空间区域采用不同采样精度。例如，在靠近视点或屏幕的位置，多个光线会聚集于相邻区域，因此即使降低采样密度也能维持较高的图像质量；而在远离观察者的区域，光线分布稀疏，需要更高采样精度以保证细节表达。空间加速结构如八叉树、KD树或稀疏体素哈希（SVH）等，则在体积数据中构建层次结构，使得光线在穿越过程中能快速跳过透明或空洞区域，仅对有效区域进行采样。这两种方法都显著降低了冗余采样的数量，提升整体渲染效率，特别适用于数据规模庞大或实时可视化需求较高的场景。


````{subfigure} AB
:gap: 20px
:subcaptions: below
:name: fig-visualization-scientific-ray_casting_acc

```{image} fig/visualization-scientific-adaptive_sampling.png
```

```{image} fig/visualization-scientific-octree.png
```
光线投影算法加速。左：自适应采样；右：八叉树结构。
````


**2. 体积泼溅**

体积泼溅（volume splatting）方法的核心思想是：将体数据视作一组三维插值核（interpolation kernels）的集合，每个核对应一个体积元（例如一个体素），并将其在图像平面上展开为二维“足迹”（footprint），再通过加权叠加这些足迹，逐步合成最终图像，如{numref}`fig-visualization-scientific-splatting` 所示。其流程可以总结如下：

1. 定义三维插值核：
在体积泼溅中，整个体积被看作由一个个分布在规则网格上的插值核组成。每个核通常具有中心对称性，例如高斯核或球形核，定义了该体素在空间中的影响范围。这些核共同描述了体数据的连续性，是与体积密度场相关的“模糊表示”。

2. 投影到二维屏幕：
当我们将这些核从三维投影到二维图像平面上时，每个核会留下一个二维投影足迹（footprint）。这一足迹描述了该体素在图像上的贡献区域，即：这个体素会影响哪些像素。

3. 颜色与透明度加权：
每个体素不仅有空间上的扩散影响，还携带着与之相关的颜色与不透明度信息。在渲染时，体素为在其投影区域内的多个像素贡献其属性值，而这个贡献是通过足迹权重乘以颜色和不透明度进行加权的。

4. 图像合成与累加：
所有体素的投影足迹在图像平面上相互叠加。为了获得正确的图像，需要处理体素之间的遮挡关系。这通常通过深度排序（例如从后向前或使用分层泼溅）实现，使得透明体素按照正确顺序进行融合。最终，图像平面上每个像素的值是所有相关体素贡献的加权和。

```{figure} fig/visualization-scientific-splatting.png
:width: 100%
:name: fig-visualization-scientific-splatting
体积泼溅基本原理。
```

体积泼溅方法基于体素发射而非像素采样，避免了逐射线的深度采样，提高了效率，
在高分辨率下更容易保留局部结构，也易于实现模糊或平滑效果。它与传统图形管线的良好契合性，激发了一些研究在其基础上设计专用硬件（special-purpose hardware）以进一步提高体渲染效率。

**3. 纹理切片**

纹理切片是一种利用纹理映射进行体积渲染的方法，它最大的优势是可以充分利用图形硬件的纹理功能（尤其是3D纹理或2D纹理的堆叠）来完成体数据的采样与合成。如{numref}`fig-visualization-scientific-slicing` 所示，其核心思想是将三维体数据打包进显卡的纹理内存，并通过一系列平面切片（slicing）与硬件光栅化功能来模拟光线与体素的交互过程，对这些切片进行纹理映射并逐层合成，从而重建出整个体数据在屏幕上的投影效果。其流程可以总结如下：

1. 切片生成：
首先，根据当前观察视角，在三维体积中切割出一系列与视线平行的二维平面。这些切片通常垂直于观察方向，并覆盖整个体积范围。可以在体积的物理空间中动态生成这些平面，也可以采用固定轴对齐方式切片。

2. 纹理映射：
对每一个切片，将其映射为一个带有颜色和不透明度信息的纹理图像。映射关系同样通过传递函数定义。

3. 合成叠加：
渲染过程中按从远到近或从近到远的顺序对这些切片进行混合叠加，采用标准的 alpha blending 技术，逐层将纹理片段合成为最终图像。合成顺序取决于是否使用前向或后向合成策略。

```{figure} fig/visualization-scientific-slicing.png
:width: 100%
:name: fig-visualization-scientific-slicing
纹理切片示例。
```

切片指在三维数据中取若干平面，这些平面通常与视线正交或近似正交，以更准确地模拟光线逐层穿过体数据的过程；在需要大幅度旋转角度的应用中，也可以采用多个方向的切片。典型做法分为两类：

- 视平面切片：如{numref}`fig-visualization-scientific-slicing` 所示，切片平面始终与当前视线垂直，即当相机（视点）旋转或移动时，每个切片平面也动态调整方向，从而最大程度上模拟光线穿透体数据的真实顺序。该方法能在视点变化时自动保证正确的采样顺序，但是需要实时更新切片方向，会有一定的重绘代价。

- 固定坐标切片：切片平面固定于某个坐标轴（如 x、y 或 z），实现简单且非常易于与传统2D纹理堆叠结合。该方法实现成本低，尤其在正交视图或小范围交互中容易控制，但是当视点与切片轴差异过大时，可能导致采样不准确，需要更多切片或插值技巧来减小误差。

在传统光线投射方法尚未有足够 GPU 支持的时代，基于纹理映射的体渲染一度成为实时或准实时体扫描可视化的主流方案。即使在现代硬件条件下，这种方法依旧在某些场景下具备速度和实现上的优势。

<!-- **4. 神经辐射场（Neural Radiance Fields，NeRF）**

神经辐射场是一种基于深度学习的体渲染方法，尽管其核心思想与传统体渲染（如光线投射）有显著差异，但它确实已成为现代体渲染领域的经典算法之一。
NeRF 通过学习隐式神经表示，能够从多视角图像中重建高质量的三维场景，并在新视角合成任务中表现出色。
NeRF 的核心是通过神经网络隐式地建模三维场景的辐射场（Radiance Field）。具体来说，它将场景表示为一个连续的 5D 函数：

$$ 
F_\theta (x,y,x,\theta, \phi) \rightarrow (RGB, \sigma)
$$ (visualization-scientific-nerf)

- 输入：三维空间坐标 $(x,y,z)$ 和视角方向 $(\theta, \phi)$。
- 输出：体密度 $\sigma$（控制光线衰减）和颜色 $RGB$（依赖视角方向）。

与传统体渲染不同，NeRF不需要显式存储体素或网格，而是通过神经网络参数化整个场景。

NeRF的渲染过程基于经典的体渲染方程，但通过神经网络实现：

1. 光线采样：
    - 生成光线：从相机出发，为每个像素生成一条光线 $\mathbf{r}(t)=\mathbf{o}+t \mathbf{d}$ 。
    - 分层采样：沿光线在近远平面之间采样 $N$ 个点 ${t_i}$（图 光线采样）。
    
2. 颜色与密度计算：
对每个采样点，通过神经网络 $F_\theta$预测：
    - 密度 $\sigma_i$：与视角无关，表示该点对光线的阻挡程度。 
    - 颜色 $\mathbf{c}_i$：与视角方向 $\mathbf{d}$ 相关，模拟材质的光泽特性。

3. 体渲染积分：
沿光线积分颜色和透明度，计算像素最终颜色：
$$ 
C(\mathbf(r)) = \sum_{i=1}^{N} T_i(1- exp(- \sigma_i \delta_i )) \mathbf{c_i}
$$ 
其中： 
    - $T_i = exp(- \sum_{j=1}^{i-1} \sigma_j \delta_j)$ 表示累积透明度；
    - $\delta_i = t_{i+1} -t_i$ 为步长。

神经辐射场能够生成高质量的新视角合成，同时无需显式存储三维结构，能捕捉复杂材质（如透明、反射）和几何。
但是训练速度慢，难以处理动态物体或运动模糊，还依赖大量视角一致的输入图像。 -->


#### 对比：表面渲染和体渲染

```{table} 表面渲染与体渲染的比较
:widths: auto
:align: center
:name: tab-visualization-scientific-rendering_comparison
| **特性**  | **表面渲染 (Surface Rendering)**   | **体渲染 (Volume Rendering)**  |
|:-----------:|:---------------------------:|:---------------------------:|
| 数据转换     | 数据被转换为表面基元（如三角形），然后进行绘制。       | 不需要提取表面基元，数据由一个或多个（假定连续的）3D 场构成。 |
| 可视化表示   | 所有可见内容都是嵌入在 3D 空间中的 2D 表面。          | 直接渲染整个体积，类似于一团彩色的果冻。                    |
| 数据隐藏风险 | 转换为几何基元可能会丢失或隐藏某些数据。              | 数据较少可能被隐藏，提供更全面的视觉信息。                   |
| 适用场景     | 适用于不透明物体。                                  | 适用于需要详细展示内部结构的应用场景。                      |
```

表面渲染和体渲染的对比如{numref}`fig-visualization-scientific-rendering_comparison`、{numref}`fig-visualization-scientific-vis_comparison` 所示，可以看到，表面渲染可以给出更清晰的几何结构，而体渲染可以在给出大致形状的前提下给出一些关于内部的信息。

```{figure} fig/visualization-scientific-rendering_comparison.png
:name: fig-visualization-scientific-rendering_comparison
表面渲染和体渲染的对比图
```


<!-- {numref}`fig-visualization-scientific-vis_comparison`展示了使用 3D 等值面来可视化标量场的结果以及对于生物组织的体渲染结果。 -->

```{figure} fig/visualization-scientific-vis_comparison.png
:name: fig-visualization-scientific-vis_comparison
左图：使用 3D 等值面来可视化标量场，右图：对于生物组织的体渲染。
```


## 对比：表面可视化与体积可视化
{numref}`tab-visualization-scientific-vis_comparison` 总结了表面可视化和体积可视化的差异。

```{table} 表面可视化和体积可视化的比较
:widths: auto
:align: center
:name: tab-visualization-scientific-vis_comparison
| **特性**   | **表面可视化**         | **体积可视化**             |
|:------------:|:---------------------:|:-------------------------:|
| 数据类型   |   通常是二维或三维表面    | 三维体积数据               |
| 表示方法   |   边界和表面             | 整个数据体                 |
| 细节展示   |   局部细节，如边缘        | 整体结构和内部细节         |
| 应用场景   |   工程设计，地形图        | 医学成像，科学模拟         |
| 可视化技术 |   网格，NURBS            | 体渲染，等值面提取           |
```
