(sec-geometry-representation-voxel-pcd)=
# 体素和点云表示

在网格表示之外，还有两种重要的显式表示：体素与点云。

## 体素

```{figure} fig/voxel.png
:name: fig-geometry-representation-voxel
:width: 50%

体素示意图。
```

体素（voxel）是一种特殊的三维表示方法。类似像素这一概念在三维上的扩展，体素表示方式通过在三维空间中定义规则网格，将空间划分成一系列方形的体素网格（voxel grid），如 {numref}`fig-geometry-representation-voxel` 所示。形式化地来说，体素可以看作一个三维数组，每个元素具有 $0,1$ 两种取值：$\mathcal{V}=\{0,1\}^{R_x\times R_y\times R_z}$。其中，$R_x,R_y,R_z$ 是体素网格的分辨率。正如二维中的像素那样，体素本身并不携带位置信息，而是依赖体素之间的相对位置关系表达几何形状；但有时，体素也会有预设的网格范围，此时每个体素的位置和大小就可以确定。例如对于一个 $\mathcal{V}=\{0,1\}^{R\times R\times R}$ 的体素，如果预设了体素网格覆盖的范围是 $[-1,1]^3$，即以原点为中心、边长为 $2$ 的立方体区域，那么每个体素格子的边长为 $2/R$，且体素格子 $\mathcal{V}[i][j][k]$ 的中心位置可以表示为 xyz 坐标：

$$
(\frac{2i+1}{R}-1,\frac{2j+1}{R}-1,\frac{2k+1}{R}-1) \,.
$$ (eq-geometry-representation-voxel)

不同于网格模型可以看作对连续曲面的离散化，体素实际上是对实心三维体的离散化，需要额外的空间来表示物体内部的实心区域。因此，尽管体素表达紧凑而且简单并具有定义明确的邻接关系，但是相对网格模型而言，用体素来表示精细模型所需要的存储空间将大大增加，导致了较大的局限。对于 $512\times512\times512$ 分辨率下的体素，如果每个体素占据 1 字节的存储空间，那么整个数据结构就将占用 128MB，使用这样大小的网格模型来表达同一个三维对象能够精细得多。

## 点云

```{figure} fig/pcd.png
:name: fig-geometry-representation-pcd
:width: 70%

同一模型的网格表示与点云表示。
```

正如此前 {numref}`chap-geometry-basics-representation` 中所介绍的，点云是空间中一组离散的数据点，刻画了三维形状的几何信息。点云通常由 3D 扫描仪或摄影测量软件生成，并用于包括计算机辅助设计（CAD）、地理信息系统（GIS）在内的一系列场景。点云中的每个点除了包含位置信息，也可以附带额外的属性，例如 RGB 颜色、法线方向等。在 {numref}`sec-geometry-reconstruction-pcd` 中，我们将详细地讨论点云的获取与注册；在 {numref}`sec-geometry-reconstruction-surface` 中，我们将介绍点云到网格模型的转换。

点云最重要的特点是无序性和非结构性，这意味着点云内部的点之间既没有次序，也没有额外的关系。尽管这使得点云成为了一种简洁的三维表示，但同时也为点云上的计算和处理带来了一定困难。这种无序性和非结构性决定了点云中的几何信息很大程度上只能从每个点的位置信息本身获得。例如，在点云上进行法向或曲率估计，便是依赖每个点与邻近点之间的位置关系来计算。这里我们将首先介绍一种分析点云之间相似性的方式，作为点云处理的一个实例；随后，我们将介绍对点云进行降采样的一些技术。

### 倒角距离

倒角距离（Chamfer Distance，CD）是衡量两个点云之间相似程度的指标之一。两个点云 $P_1 = \{\mathbf{x}_i \in \mathbb{R}^3\}_{i=1}^n$ 和 $P_2 = \{\mathbf{x}_j \in \mathbb{R}^3\}_{j=1}^m$ 之间的倒角距离被定义为两个点云之间最近点对的平均距离。形式化地来说，有：

$$
\text{CD}(P_1, P_2) = \frac{1}{2n} \sum_{i=1}^n \|\mathbf{x}_i - \text{NN}(\mathbf{x}_i, P_2)\|_1 + \frac{1}{2m} \sum_{j=1}^n \|\mathbf{x}_j - \text{NN}(\mathbf{x}_j, P_1)\|_1 \,,
$$ (eq-geometry-representation-cd)

其中，$\text{NN}(\mathbf{x}, P) = \mathop{\mathrm{arg\,min}}_{\mathbf{x}' \in P} \|\mathbf{x} - \mathbf{x}'\|_1$ 表示点 $\mathbf{x}$ 在点云 $P$ 中的最近邻居（nearest neighbor）。显然，倒角距离具有简单形式的同时，并不要求两个点云具有相同的点数，并且保持了对称的性质，因此被广泛应用于点云的相似度分析。

(sec-geometry-representation-downsample)=
### 下采样

实际应用中，点云往往包含较多数量的点，因而占据较大的存储空间并导致相对较慢的处理速度。有时我们并不需要如此密集的点，希望能够在降低点云密度的同时，尽可能保持其所表示的几何形状。这时，一系列点云下采样（downsampling）算法便可以用于点云的稀疏化：

+ 随机下采样（random downsampling）：根据采样率 $r$，对点云中的每一个点以 $1-r$ 的概率丢弃。
+ 最远点采样（farthest point sampling）：初始化时，从原点云 $P$ 中选取一个点作为新点云 $P'$，随后迭代若干次，每次从 $P$ 剩下的点中选取一个“最远点” $\mathbf{x}^*$ 加入 $P'$，满足：
    
    $$
    \mathbf{x}^*=\mathop{\mathrm{arg\,max}}_{\mathbf{x}\in P-P'}\,\text{NN}(\mathbf{x}, P')\,.
    $$ (eq-geometry-representation-fps)
    
    重复迭代这一步骤直到 $P'$ 中的点达到指定数量。
+ 体素下采样（voxel downsampling）：根据一定的分辨率和网格范围，在空间中划分体素网格，统计落在每个体素格子中的点。每个非空体素产生一个点，合并成为降采样后的新点云。根据产生点的规则，可以分为两种方式：
    + 体素质心下采样：根据体素格子所包含的点，计算其位置的平均值作为结果。
    + 体素中心下采样：直接选取体素格子的中心位置作为结果。
