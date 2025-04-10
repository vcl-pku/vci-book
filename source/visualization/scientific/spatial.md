# 表面可视化与体积可视化

在前面对标量场、矢量场、张量场的可视化方法进行介绍时，我们主要是根据数据本身的属性（标量、矢量、张量）来区分可视化类型。然而在实际应用中，数据还可能以不同的几何形式呈现在空间中，例如：
某些数据仅限定在诸如曲面、地形、CAD 模型边界等“表面”上，需要进行**表面可视化**。
更多时候，数据分布在三维体内部，如医学成像的 CT 或 MRI 扫描结果、流体模拟的 3D 网格数据等，这些数据往往需要**体积可视化**技术才能揭示其内部结构。
因此我们继续探讨“表面数据”和“体数据”在可视化时所采用的不同技术。


## 按空间结构分类：表面数据、体数据

### 表面数据（Surface Data）

表面数据用于表示三维对象的外部形状和结构，通常以网格和参数化表示，其中网格是由顶点、边和面组成的集合，通常用于表示复杂的三维形状，参数化表示为通过数学公式来定义表面，如贝塞尔曲面或 NURBS (非均匀有理 B 样条)。
表面数据具有高维嵌套（二维结构嵌入三维空间）和局部细节丰富的特点。可视化时，准确展现几何细节、处理复杂拓扑结构以及支持高效渲染是主要挑战。

### 体积数据（Volume Data）

体积数据表示的是三维空间内部的数据分布，每个空间位置对应一个数据值。常见的体积数据包括：医学成像（如 CT 或 MRI 扫描）、气象模拟（如三维风速场或云量分布）、工程仿真（如流体动力学模拟的速度和压力场）。
体积数据具有数据量大、内部结构复杂且可能缺乏明确边界的特点，如何有效提取内部特征、减少遮挡干扰，以及在保证细节的同时进行高效绘制是体积数据可视化的关注重点。

常见的体积数据的存储模式包括：结构化网格、非结构化网格、无网格拓扑的离散点点云等。

- **结构网格**数据指在空间或时空范围内按规则、均匀间隔进行采样，形成具有行列（或行列层）索引关系的网格。例如：流体力学中的规则网格（如 CFD 仿真输出，采用均匀笛卡尔网格），医学影像的 3D 体素数据（CT、MRI 采用固定分辨率扫描）。 结构网格具备简单的拓扑关系，因而易于索引、插值和处理；但其不灵活的分辨率布置会导致数据量庞大或分辨率不足，在非均匀或复杂几何域中也难以适配。

- **非结构网格**数据指在空间中采用三角形、四面体、多面体等具有不规则连接关系的网格单元对域进行剖分，存储每个单元的属性。
例如：有限元分析（FEM）模型、地质构造模拟网格（地层间往往复杂，需自适应网格）、海洋/气象模型对海岸线等不规则区域的剖分。
非结构网格可灵活适应复杂几何边界，并可在感兴趣区域加密采样，但数据结构较复杂，渲染和拓扑运算(如等值面提取、流线跟踪)需要针对单元连接关系做更多预处理。

- **离散点云**数据指在空间或时空中仅给出一组拥有坐标及测量值（标量或矢量等）的散点，没有显式的网格连接关系。 常见的离散点云数据包括：激光雷达扫描（LiDAR）、粒子仿真输出（如分子动力学、天体多体模拟）、观测仪器采样的稀疏离散测量数据。 离散点云数据无需事先网格化，灵活度高，容易真实地反映局部细节；但可视化算法需要做插值、重构或聚类，才能形成连续可视效果，且在大规模点云下的渲染与交互也面临性能挑战。


## 表面可视化
表面可视化通过几何网格（如三角面片、NURBS 曲面）表达物体的边界或等值面，聚焦于几何形状与表面属性的展示。

### 网格渲染（Mesh Rendering）

网格渲染通过将几何面片（如三角形、四边形）与光照、纹理结合，生成逼真的表面图像。这一过程包含几何处理、光栅化、像素着色等阶段，在之前的渲染章节中已经有了充分的介绍。

此类可视化方法支持高效实时渲染，以及复杂几何交互（如旋转、剖切），但是仅能表达表面，无法展示内部结构，常用于机械零件 CAD 模型审查、地质地形表面渲染（数字高程模型+卫星纹理）等注重表面信息的可视化应用中。

### 表面纹理映射（Surface Texture Mapping）

与“纹理贴图”思想相似，可在表面上铺设或合成纹理图案，用纹理的颜色、透明度或条带方向来编码数据。适合在曲面上表现一些局部或细腻的数据结构，如应力分布、流动形态等。
该方法技术核心有以下两点：
- 纹理坐标：每个网格顶点可关联纹理坐标 $(u, v)$，然后把标量或矢量信息转换为纹理像素，再在着色阶段将纹理“贴”到曲面上。
- 属性叠加：可将纹理与颜色映射或光照效果结合，在曲面的某些区域高亮显示关键信息，或通过透明度揭示下层结构。


## 体积可视化

当数据不只存在于表面，而是填充整个三维区域时，则需要用体积可视化技术来展示体内部的信息。以下介绍两种经典方法：直接体绘制与等值面提取。

### 体渲染

体渲染（volume rendering）是科学可视化中用于探索三维体数据内部结构的核心技术。
与传统的表面渲染不同，体渲染无需提取表面的几何网格，而是直接操作体素（三维像素，如{numref}`fig-visualization-scientific-voxels` 中的三维立方体或体单元）数据：通过对体数据进行逐像素或逐射线的光线跟踪，模拟光线在参与性介质（如云雾、生物组织）中的传播过程，将3D体内部的“密度”或“标量值”映射为颜色和透明度，再投影到屏幕上，形成半透明的可视化效果，从而突出体积中感兴趣的数值范围（如医学中突出骨骼、血管等）。揭示数据的全局特征与局部细节。
其核心价值在于平衡透明度与对比度，使观察者既能捕捉整体分布，又能聚焦关键区域，因此适用于无明确边界或内部结构复杂的数据。


```{figure} fig/visualization-scientific-voxels.png
:scale: 70%
:name: fig-visualization-scientific-voxels
三维体素数据
```

体渲染最初用于在计算机图形中生成非刚性物体的可视化效果，如云、烟、果冻等。这些物体通常不具有明确的表面边界，并且其物质的密度相对较低。
体渲染通过将气体或其他非刚性物质抽象为粒子群或体素群来更好地处理这些物体的半透明和不规则特性，使其在视觉上更为真实。
<!-- 在这种表示中，物体被视为由大量小粒子组成的集合体，而非一个具有固定形状和边界的实体，这允许光线以更自然的方式穿过物体，从而更好地模拟光子与粒子间的相互作用。
当光线穿过这些由粒子群构成的物体时，它们不断与粒子发生相互作用，例如散射和吸收。这种相互作用导致光线路径的改变，从而产生了体渲染中独特的视觉效果。 -->

在体渲染过程中，传递函数（Transfer Function）和光线投影（Ray Casting）是密不可分的两个关键环节。
传递函数用于将体素所携带的标量值映射成颜色和不透明度，从而在视觉上表现出不同的密度或材质特征。
光线投射算法则通过模拟光线在体数据内的吸收与（部分）散射过程，累积形成最终可视化图像。
值得注意的是，体渲染中一般不涉及反射模型；大多数直接体绘制只考虑介质对光的吸收与散射，而反射通常出现在具有明确表面或镜面特性的物体中，故在经典的体渲染里并不常用。


我们首先对比体渲染和之前提到的表面渲染，然后介绍体渲染的物理公式，最后介绍体渲染的经典实现算法。

#### 体渲染和表面渲染的对比

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

表面渲染和体渲染的对比如{numref}`fig-visualization-scientific-rendering_comparison` 所示，可见体渲染可以在给出相应的形状的前提下并对于内部给出一些信息。

```{figure} fig/visualization-scientific-rendering_comparison.png
:name: fig-visualization-scientific-rendering_comparison
表面渲染和体渲染的对比图
```

#### 体渲染的原理

体渲染把光子与粒子发生作用的过程，进一步细化为三种类型：

- 吸收 (absorption)：光子被粒子吸收，会导致入射光的辐射强度减弱。
- 放射 (emission)：粒子本身可能发光，这会进一步增大辐射强度。
- 散射 (scattering)：光子和其他粒子相碰撞后，导致方向发生偏移，如果偏移朝向光束方向则会增加光路上的辐射强度，反之则会减弱入射光强度。

我们通过{numref}`fig-visualization-scientific-beam` 来说明这些系数导致的光学方程。

```{figure} fig/visualization-scientific-beam.png
:scale: 80%
:name: fig-visualization-scientific-beam
体渲染的光与介质作用的示意图
```
    
取一处介质微元，一束光线从介质的一个面到另一个面。其中假设介质的厚度为 $\Delta s$，介质的横截面积为 $E$，介质中的杂质粒子的横截面积为 $A=\pi r^2$，粒子面密度为 $\rho$，则在这个空间内的粒子数目为 $\rho E \Delta s$（假设所取的介质足够薄，薄到跟粒子直径近似时，可以认为粒子无重叠地散开在这一薄层内），总的遮挡面积为 $\rho E \Delta s A$。则遮挡的比率为 $\epsilon=\rho E \Delta s A / E = \rho A \Delta s$。也就是说在所有入射光线中，有占比 $\epsilon$ 的光线被粒子遮挡，剩余 $1-\epsilon$ 的光线穿透介质。这意味着，记入射光强度为 $I_\text{i}$，出射光强度为 $I_\text{o}$，那么由于介质中的杂质粒子遮挡，光强的变化量为：

$$
I_\text{o} - I_\text{i} = \Delta I = -\rho(s) A I_\text{o} \Delta s 
$$ (visualization-scientific-volume1)

将上式扩展到普遍情形：对于连续介质而言，在光束路径 $[s_\text{start},s_\text{end}]$ 上，假设 $\rho(s)$ 是沿着光路的函数，那么光强也将沿着光路变化，记为 $I(s)$，则上式可写为：
$$
\mathrm{d}I(s)= -\rho(s) A I(s) \mathrm{d} s 
$$(visualization-scientific-volume2)

类似地，记射入介质时的光强为 $I(s_\text{start})=I_\text{i}$，射出介质时光强为 $I(s_\text{end})=I_\text{o}$，那么通过积分得到二者之间的关系：

$$ 
I_o = I_i \exp \left( -\int_{s_\text{start}}^{s_\text{end}} \rho(s) A I(s) \, ds \right) 
= I_i \exp \left( -\int_{s_\text{start}}^{s_\text{end}} \tau_a(s) I(s) \, ds \right) 
$$ (visualization-scientific-volume3)

其中 $\tau_a = \rho A$ 是吸收系数。对于其他的放射和散射项，也可以定义类似的系数。对于放射而言，假设介质粒子放射发出的光的光强为 $I_e$，那么类似地，在介质微元一侧能接收到的光线占比即为例子占据微元截面的比例系数，因此放射系数 $\tau_e = \tau_a$。对于散射而言，记外部光的光强为 $I_s$，散射系数 $\tau_s$，包括外散射（弹射光子偏移光路）系数和内散射（弹射光子偏向光路）系数。于是有：

$$ 
\frac{dI}{ds} = -(\tau_a + \tau_s) I(s) + \tau_a(s) I_e(s) + \tau_s(s) I_s(s) 
$$ (visualization-scientific-volume4)

其中 $I_s$ 为内散射的光强。对该方程进行积分求解便可以得到光强，然后通过光强和颜色的对应关系，可以得到某视角观测得到的颜色。一些体渲染得到的结果图如下。

```{figure} fig/visualization-scientific-beam.png
:scale: 80%
:name: fig-visualization-scientific-volume
体渲染结果图
```

#### 体渲染经典实现算法

**1. 光线投影**

下面我们将介绍体渲染的一种经典实现算法：光线投影。
光线投影通过追踪从视点出发穿过体数据的虚拟光线来生成图像。每条光线与数据体内的元素相交，并计算这些相交点的颜色和强度，最终生成图像。

光线投影的步骤可以总结如下：

1. 发射光线：从观察点（通常是相机或者用户的视点）发射光线。在基本的光线投影中，每个光线对应屏幕上的一个像素。
2. 找交点：沿光线方向步进采样体素数据（如均匀步长或自适应步长），通过三线性插值计算非整数坐标处的标量值。
3. 法线计算：渲染算法通常需要知道在每个采样点的表面法线方向。由于体积数据通常不包含法线信息，因此需要通过梯度估计（如中心差分法）来计算。
4. 分类：通过传递函数将标量值及其衍生属性（如梯度模长、曲率）映射为颜色（RGB）与不透明度（Alpha），定义不同组织的视觉表现。
5. 着色：按照光照模型的计算，比如 Phong 光照模型，来确定物体在当前位置和历史光照条件下的颜色。
6. 合成：沿着光线路径采样的多个数据值结合起来，以生成最终的像素值。
上述步骤的操作如{numref}`fig-visualization-scientific-ray_casting` 所示。

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

**2. 纹理切片**

纹理切片是一种利用纹理映射进行体积渲染的方法，主要利用图形硬件的纹理功能（尤其是3D纹理或2D纹理的堆叠）来完成体数据的采样与合成。
其核心思想是将三维体数据打包进显卡的纹理内存，并通过一系列平面切片（Slicing）与硬件光栅化功能来模拟光线与体素的交互过程，从而高效地生成体渲染图像。
在传统光线投射方法尚未有足够 GPU 支持的时代，纹理映射的体渲染一度成为实时或准实时体扫描可视化的主流方案。即使在现代硬件条件下，这种方法依旧在某些场景下具备速度和实现上的优势。

切片指在三维数据中取若干平面，这些平面通常与视线正交或近似正交，以模拟光线逐层穿过体数据的过程。典型做法分为两类：
- 视平面切片：切片平面始终与当前视线垂直，即当相机（视点）旋转或移动时，每个切片平面也动态调整方向，从而最大程度上模拟光线穿透体数据的真实顺序。该方法能在视点变化时自动保证正确的采样顺序，但是需要实时更新切片方向，会有一定的重绘代价。
- 固定坐标切片：切片平面固定于某个坐标轴（如 x、y 或 z），实现简单且非常易于与传统2D纹理堆叠结合。该方法实现成本低，尤其在正交视图或小范围交互中容易控制，但是当视点与切片轴差异过大时，可能导致采样不准确，需要更多切片或插值技巧来减小误差。


**3. 剖面法**

剖面法是对三维体数据进行局部截取并在一个（或多个）平面上显示数据切面的可视化技术。
它将体积数据表示为一系列具有位置、颜色和不透明度的点，然后在视平面上进行重构和混合。为了加速体积渲染，常用的技术包括多级渐进纹理（MIP Mapping），根据视图距离选择不同分辨率的纹理来优化渲染；以及使用空间数据结构（如八叉树或 K-D 树）组织数据，快速剔除不可见区域。
这些方法和技术在提高渲染速度和处理大型体积数据集方面会有显著效果。
与“体绘制”直接对整个数据体进行光线投射（或由纹理切片逐层合成）不同，剖面法更关注在任意或特定方向上的局部截面，以一种“剖开体内、只看截面”的方式来观察数据的内部分布，从而让使用者可以以一种更直观、更“物理直觉式”的方式来查看“切面”上的数据分布情况。

剖面法的实现流程有以下几步：
- 确定切片平面：首先需定义一个切片平面（或多个平面），可以是与坐标轴平行的固定方向，也可以是与视线正交、或由用户交互选择任意三点决定的倾斜面。
- 数据采样：确定切片平面后，需要对平面与体素网格（Voxel Grid）的交集区域进行采样。通常做法是在平面上划分一个规则网格，对照三维数据坐标，获取平面每个网格点（或像素）对应的体素值。
若体素不在网格采样点的正好位置，往往需要做插值（如三线性插值）来获得更平滑、连续的结果。
- 着色映射：将采样得到的标量值（如密度、灰度、温度等）映射到颜色或灰度图，即形成一个二维纹理显示。
- 可选的交互叠加：略微“挖空”或“裁剪”数据体，以同时显示剖面与剖面后方体数据的半透明渲染，让用户在一个视图中既能看到局部截面的清晰细节，也能保留对整体位置的定位感。

**4. 神经辐射场（Neural Radiance Fields，NeRF）**

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
但是训练速度慢，难以处理动态物体或运动模糊，还依赖大量视角一致的输入图像。

### 等值面提取（Isosurface Extraction）

等值面提取指从体数据中提取特定标量值 $c$ 对应的表面网格。这与前面“标量场可视化”中的等高线与等值面类似，只不过这里是在三维体数据中运用。
最经典的方法是 Marching Cubes 算法，前文已有介绍，此处不再赘述。

```{figure} fig/visualization-scientific-vis_comparison.png
:name: fig-visualization-scientific-vis_comparison
左图：使用 3D 等值面来可视化标量场，右图：对于生物组织的体渲染。
```

{numref}`fig-visualization-scientific-vis_comparison`展示了使用 3D 等值面来可视化标量场的结果以及对于生物组织的体渲染结果。

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
