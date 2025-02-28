# 信息数据可视化类型
<!-- :label:`informational-types` -->

## 基础绘图

绘图（plot）是数据可视化中的一种基本工具，将数据点在二维或三维坐标系中通过图形化方式呈现，展示数据的关系、趋势、分布,从而帮助用户直观地理解数据的结构和模式。简单来说，绘图技术，通过某些图形表示，将数据中的大量信息简化为最简单和最干净的形式，使得数据（点）中固有的关系可以容易地被感知。

如{numref}`fig-visualization-informational-plot`所示，plot 是一个非常通用的可视化操作，在不同的编程语言和工具中，均有对 plot 的默认实现。但，对同样的数据，有无数种可采用的可视化方法，而不恰当的绘图方式很容易给人们以不同的甚至错误的信息，因此如何使用绘图来正确传达数据所包含的信息是一件值得思考的事情。

```{figure} fig/visualization-informational-plot.png
:name: fig-visualization-informational-plot
不同编程工具中的默认绘图。
```

从{numref}`fig-visualization-informational-plot`的对比图中，我们可以得到重要的两点结论：首先，绘图没有明确的使用标准或使用公式，这不同绘图在坐标轴和比例线、图内的数据矩形以及数据值的实际表示等方面上的差异可以看出来；其次，创建一张绘图是一个迭代的设计过程，一次绘图的设计方案不能普遍适用于所有类型的数据。

然而，人们也已经提出了一些普遍的绘图原则，可以被用作指导，以提高绘图能传达出有用信息的可能性。下面我们将介绍 William S. Cleveland 提出的提升绘图质量的两条路线和相应原则{cite}`Cleveland1993visualizing, Cleveland1994graphing`。

### 提升绘图质量的原则

**提升视觉效果**（improving the vision）的目标是提高图表的可读性，使其更加清晰、直观，从而确保数据能够被轻松理解。设计时应避免过于复杂的元素，防止用户感到困惑或视觉疲劳。

- **原则 1：减少杂乱，突出数据。**
绘图应聚焦于数据本身，移除所有可能干扰或分散注意力的多余元素。确保数据是视觉的焦点，让观众能够立即抓住关键信息。
```{figure} fig/visualization-informational-plot_vision1.png
:width: 60%
:name: fig-visualization-informational-plot_vision1
左：图中添加了多余的背景网格线。右：简单清晰的绘图让数据趋势更加易读。
```

- **原则 2：使用视觉突出元素展示数据。**
连接点的线条不应遮挡数据点，确保每个数据点都清晰可见。如果图表中展示多个数据集，它们应在视觉上可区分开。若数据重叠，考虑将数据分拆到多个共享轴的相邻图表中。
```{figure} fig/visualization-informational-plot_vision2.png
:width: 60%
:name: fig-visualization-informational-plot_vision2
左：图中添加了适当数量的点。右：图中添加了过多数量的点。
```

- **原则 3：使用简洁的参考线、标签、注释和图例。**
参考线应仅用于标示数据中的重要阈值，并且应尽量简洁，只在必要时使用。避免过多的参考线、标签或注释，以免干扰数据本身的展示。
```{figure} fig/visualization-informational-plot_vision3.png
:width: 60%
:name: fig-visualization-informational-plot_vision3
左：适当的辅助线帮助用户阅读数据。右：多余的参考线使图像杂乱、重点不突出。
```

- **原则 4：确保叠加数据集中的不同组的符号可分离，同组的符号在视觉上易于组合。**
如果在同一图表中显示多个数据集，使用不同且可区分的符号来表示不同的数据集。同一数据集中的视觉元素应便于组合和理解，确保用户能轻松识别各组数据。
```{figure} fig/visualization-informational-plot_vision4.png
:width: 60%
:name: fig-visualization-informational-plot_vision4
左：对不同数据集采用相同的视觉符号使之无法区分。右：对不同数据集采用易于区分的视觉符号，图中不同直线对应不同线型有助于在仅黑白两色的媒介中清楚展示不同直线的图像。
```

- **原则 5：使用适当的比例刻度和数据边距。**
每个坐标轴应包含至少两条比例刻度线（如左/右或上/下），以清晰界定数据区域。适当的边距有助于突出图表中的核心内容，避免数据被挤压在边缘。每个坐标轴应标明 3 至 10 条刻度线，确保数据的清晰呈现。
```{figure} fig/visualization-informational-plot_vision5.png
:width: 60%
:name: fig-visualization-informational-plot_vision5
对比左侧两图，右侧图中没有刻度框线和边距，数据点之间相互重叠，横坐标刻度过多因此拥挤且难以阅读。
```

**提升理解效果**（improving the understanding）的目标是确保图形有效地传达信息，使用户能够抓住核心要点。通过使用恰当的标签、标题和注解等，帮助用户理解图形背后的故事和数据逻辑。

- **原则 1：提供清晰的解释并得出结论。**
图形是验证假设或传达结果的工具。为了有效传达信息，需要通过文字（如段落或标题）描述一切所需信息（包括并不限于背景信息、实验设置、图例含义以及从图中提取的结论等）。文字重点应放在解释主要特点和阐述结论上。
```{figure} fig/visualization-informational-plot_understanding1.png
:width: 60%
:name: fig-visualization-informational-plot_understanding1
在图片标题中利用文字说明详细信息。
```

- **原则 2：充分利用可用空间。**
尽量填充数据矩形区域，避免无意义的空白。只有在必要时（例如科学数据中表示零值的空白）才使用空白区域，这有助于确保数据的可见性和图表的紧凑性。
```{figure} fig/visualization-informational-plot_understanding2.png
:width: 60%
:name: fig-visualization-informational-plot_understanding2
左图中，不正确的坐标比例选取使得数据矩形中留白过多，且导致不恰当的结论。
```

- **原则 3：适时使用对数刻度。**
对数刻度适用于显示百分比变化、乘法因子和数据偏度。它能有效展示数据的变化趋势，特别是在处理指数增长或极差值时。
```{figure} fig/visualization-informational-plot_understanding3.png
:width: 60%
:name: fig-visualization-informational-plot_understanding3
右图中，使用对数坐标可以得到几乎直线的数据分布，从而说明了数据的具体变化趋势。
```

- **原则 4：调整图表的纵横比。**
通过优化图表的纵横比，使图形中的线条方向更加清晰可辨。通常，45度的倾斜角度有助于提高图表的可读性。
```{figure} fig/visualization-informational-plot_understanding4.png
:width: 60%
:name: fig-visualization-informational-plot_understanding4
不同的图表纵横比会导致数据连线呈现出不同的倾斜度。
```

- **原则 5：确保图表对齐与比例一致。**
对齐并列图表时，确保它们的比例一致且对齐，以便用户能方便地进行对比分析，避免图表之间的视觉不一致造成误解。
```{figure} fig/visualization-informational-plot_understanding5.png
:width: 40%
:name: fig-visualization-informational-plot_understanding5
在并列图标中使用相同的坐标比例从而利于对比分析。
```

### 基础绘图技术

**连接符号图（Connected symbol plots）**：是一种最常用的绘图技术，通过连接数据点来显示数据之间关系的图形。每个数据点用符号（例如圆圈、方块、点等）表示，并通过线条连接相邻的数据点。这类图表常用于展示连续数据之间的趋势或关系，如时间序列或其他有序的一维数据，如{numref}`fig-visualization-informational-lineplot`所示。在连接符号图中，符号标出了可能带有高频噪音的数据，连线显示出平滑数据的低频特征，符号连线则结合了两者的功能，利用符号展现数据实际分布并用连接线更清晰地跟踪数据随时间或其他变量的变化趋势。
```{figure} fig/visualization-informational-lineplot.png
:width: 80%
:name: fig-visualization-informational-lineplot
连线图。
```

**点图（Dot plots）**：是一种与柱状图或饼状图性质类似的绘图形式，适用于有定量标注的且相互之间没有顺序关系的数据，如{numref}`fig-visualization-informational-dotplot`和{numref}`fig-visualization-informational-dotplot_multidim`所示。
```{figure} fig/visualization-informational-dotplot.png
:width: 60%
:name: fig-visualization-informational-dotplot
点图。通常按数据值由大到小绘制，并将最大值排在顶部（除非需要保留数据的固有顺序）。该图中使用了对数坐标来减少数据绘制的偏斜，更好地展示数据规律。
```
```{figure} fig/visualization-informational-dotplot_multidim.png
:width: 60%
:name: fig-visualization-informational-dotplot_multidim
多路点图（multiway dot plots）。用对齐了的多个并列点图展示多维数据。
```

**散点图（Scatter plots）**：常被用来展示二维数据的两个维度之间关系或相关性。如{numref}`fig-visualization-informational-scatter_correlation`所示，恰当地使用散点图能直观地揭示数据之间的相关性。如{numref}`fig-visualization-informational-scatter_line`所示，对于具有相关性的数据，通常还可以在图中加入一条最佳拟合的直线来展现相关性。
```{figure} fig/visualization-informational-scatter_correlation.png
:width: 80%
:name: fig-visualization-informational-scatter_correlation
散点图，从左到右依次展现了高相关性、低相关性、无相关性。
```
```{figure} fig/visualization-informational-scatter_line.png
:width: 80%
:name: fig-visualization-informational-scatter_line
利用最小二乘法求解最佳拟合直线。具有相关性的数据（左、中）将能得到较好拟合，但可能会受到离群值的影响（右）。
```
通过将散点图排列成矩阵，散点图也可用于展示更高维度的数据。如{numref}`fig-visualization-informational-scatter_highdim`所示，将高维数据的每个维度分别分配给各行和各列，得到一个方阵，方阵的每个元素即为取出行列的对应维度的数据绘制出的标准散点图。为避免重复绘制扰乱视线，可以只绘制方阵的上三角部分。
```{figure} fig/visualization-informational-scatter_highdim.png
:width: 60%
:name: fig-visualization-informational-scatter_highdim
利用散点图矩阵展示高维数据，并通过观察特定散点图或整行/列散点图中的散点分布形态得到维度之间的相关性（绿色方框）。
```

**直方图（Histograms）**：是一类特殊的柱状图（Bar charts），被用于展示数据的分布情况。如{numref}`fig-visualization-informational-histogram`所示，它将数据分为若干个固定的区间（bins），并通过柱形的高度表示每个区间内数据点的数量。直方图常用于分析数据的分布特征，例如查看数据的集中趋势、离散程度以及是否存在偏态或多峰分布。
```{figure} fig/visualization-informational-histogram.png
:width: 90%
:name: fig-visualization-informational-histogram
柱状直方图。
```

**箱形图（Box plots）**：通常用于展示数据的统计方差，如{numref}`fig-visualization-informational-box`所示，显示数据的四分位数（Quartile）、中位数及最大值、最小值，以及可能的离群值。
```{figure} fig/visualization-informational-box.png
:width: 60%
:name: fig-visualization-informational-box
箱形图。黑色上下短横线、蓝色箱体上下边、红色中间线分别对应数据的最大值、最小值、Q1 四分位数、Q3 四分位数、中位数。
```

<!-- ## 多变量绘图 -->
## 多维数据可视化

在现实世界中，数据往往包含多个维度（如金融指标、用户行为特征等），而人类的视觉系统通常只能有效地理解三维空间以下的数据，因此，如何直观呈现这些复杂的高维信息是可视化领域的核心挑战之一。
在处理高维数据时，有几个难点需要克服：

- 数据稀疏性：高维空间中的数据点通常是稀疏的，这意味着数据点之间的距离很大，很难在可视化中显示出来。这会导致可视化失真，因为只有一小部分数据点会被显示，而其他数据点被忽略了。
- 数据维度灾难：随着维度的增加，数据点之间的距离变得更加模糊，这使得难以找到有效的可视化方式来表示数据的结构和关系。高维数据的复杂性增加了可视化的挑战。
- 可视化的可解释性：高维数据可视化通常会导致信息的丢失和可视化的复杂性，这可能会降低可视化结果的可解释性。解释可视化结果对于理解数据和从中提取见解至关重要。
- 可视化的互动性：为了更好地理解高维数据，通常需要与可视化进行互动，探索不同的视图和维度组合。设计交互性可视化界面是一个挑战，需要考虑如何有效地将高维信息传达给用户。

高维数据不仅难以直接绘制，还有可能掩盖关键模式或关系。为此，研究者提出了多种创新方法，通过降维、投影等技术，将高维数据映射到人类可感知的低维空间，揭示其中隐藏的结构、聚类或异常。
选择适当的高维数据可视化方法是一个重要的决策，因为不同的方法可能会呈现不同的数据结构和关系。
<!-- 常用的高维数据可视化方法包括并不限于：
- 降维技术（如 PCA、t-SNE、UMAP）：利用正交变换将数据投影到方差最大的低维子空间。
- 多维尺度法（MDS）：保持数据点间的距离关系，将高维空间映射到低维空间。
- 平行坐标
- 热力图
- t-SNE：基于数据点的相似性概率分布，实现非线性降维。 -->

本节将介绍两种主要的多维数据可视化技术：多维尺度法和平行坐标法。

### 多维尺度法（Multidimensional Scaling，MDS）

为了显示包含在距离矩阵中的信息，我们采用一种称为多维尺度法的降维形式，通过线性或非线性的映射，将高维数据映射到低维空间，从而展现数据之间的相似性。多维尺度法又称相似度结构分析（similarity structure analysis），其核心思想是如果高维空间中的距离能够反映数据的相似性或差异性，那么在低维空间中保持这些距离关系，就能有效揭示数据的结构。
具体而言，多维尺度法根据数据点之间的距离或相似度矩阵（如欧式距离或余弦相似度等度量），在尽可能地保留数据间原有的距离结构的基础上，将高维数据映射到一个较低的维度（通常是二维或三维空间）中，并将映射后的低维数据绘制在二维或三维图像中，如{numref}`fig-visualization-informational-mds`所示。
```{figure} fig/visualization-informational-mds.png
:width: 80%
:name: fig-visualization-informational-mds
利用多维尺度法进行降维并绘制二维图像。图中线段长度大致表现了两点对应的城市间的距离。（https://www.displayr.com/what-is-multidimensional-scaling-mds/）
```
多维尺度法是社会学、心理学、市场营销学等领域中常用的数据分析方法，它能够帮助揭示数据中的潜在结构和关系。这种方法直观且易于解释，且不依赖数据的分布假设，适合探索性数据分析。例如，在心理学研究中，MDS可以用来分析人们对不同物体或概念的相似性；在市场分析中，它可以帮助展示不同产品或品牌之间的相对关系。
```{figure} fig/visualization-informational-mds_conflict.png
:width: 80%
:name: fig-visualization-informational-mds_conflict
多维尺度法可能会产生冲突：图中三个点，两两之间的相似度关系难以合理地反映在一张二维图像上。
```
但在降维过程中，由于原高维空间的复杂性，数据的距离关系无法完全被保留或准确反映，甚至可能会出现冲突（conflict），如{numref}`fig-visualization-informational-mds_conflict`所示。

### 平行坐标法（Parallel Coordinates）

经典可视化中假设不同维度的坐标轴相互正交，因此人们能够直观理解并可视化的正交坐标系最多不超过三维。
于是当数据维度超过了三维后，这种基于正交坐标系的可视化技术就失败了，于是人们考虑放弃“正交”约束，改将各维度坐标轴画成平面内的一系列平行线，每个数据点的各维度分量对应有各坐标轴的取值，相连起来可形成一条折线。这种方法被称为平行坐标法，如{numref}`fig-visualization-informational-parallel`所示，每个数据点具有唯一的一种折线表示，且坐标轴的数量（即数据维度）是没有限制的（实际中需要考虑屏幕的大小和分辨率）。
```{figure} fig/visualization-informational-parallel.png
:width: 60%
:name: fig-visualization-informational-parallel
echarts.js 中的平行坐标样例，通过空气中各气体含量的指标展示不同城市的空气污染情况。
```

平行坐标空间和数据所处的原笛卡尔空间有着有趣的对应关系。一个基本的射影几何对偶性：笛卡尔坐标系中的点在平行坐标系对应一条折线，而笛卡尔坐标系中的一条直线则对应着平行坐标系中的一个点，如{numref}`fig-visualization-informational-parallel_duality`所示，对于分布在同一条直线上的一组数据，当数据的两个维度呈现负相关时（左一图），这组数据对应的平行坐标线段将相交于同一点；当数据的两个维度呈现正相关时（左二图），这组数据对应了一组平行的线段（可以看成相交于无穷远点）。另外，两个空间中的趋势、操作等也存在一定的几何对应关系，例如：
- 笛卡尔空间中的圆和椭圆映射成平行坐标空间中的双曲线；
- 笛卡尔空间中的旋转映射到平行坐标空间中的平移，反之亦然；
- 笛卡尔空间中的拐点映射为平行坐标空间中的顶点。
```{figure} fig/visualization-informational-parallel_duality.png
:width: 80%
:name: fig-visualization-informational-parallel_duality
平行坐标空间和笛卡尔坐标空间的几何对偶性示例。
```

平行坐标可以同时展示数据所有维度的信息，很合适用来为用户给出对多维数据的概览可视化。但密集的数据被集中展示时，也有可能给用户带来困扰，如{numref}`fig-visualization-informational-parallel_dense`所示。
```{figure} fig/visualization-informational-parallel_dense.png
:width: 50%
:name: fig-visualization-informational-parallel_dense
离群线段和部分相关性可以得到体现，但密集的平行坐标使图像杂乱而难以阅读。
```
一种方法是通过高亮来突出单个数据，用户可以通过选择特定点/数据折线来高亮整条折线，来获得更好的针对特定数据的可视化效果。这种方法不仅限于高亮单个数据，也可以被拓展到高亮一个数据子集上，并且可以与多维尺度法联合使用，如{numref}`fig-visualization-informational-parallel_mds`所示，多维尺度法提供映射到低维的数据散点分布，用户可以通过点选散点图中的特定点（比如离群值），查看在平行坐标中被高亮出的折线，从而观察出它们的独有特征。
```{figure} fig/visualization-informational-parallel_mds.png
:width: 60%
:name: fig-visualization-informational-parallel_mds
平行坐标和多维尺度方法的综合应用，通过高亮展示离群值相对于整体数据的独有特征。
```

平行坐标法的一个常见问题是邻接性问题：相邻的坐标轴之间更容易进行比较和分析，而不相邻的坐标轴之间则困难得多。因此，如果想要研究所有维度两两之间的关系，则需要采用一系列的轴排列方式，绘制一组不同的平行坐标图，从而无冗余且无遗漏地用相邻坐标轴展示所有维度之间的所有两两组合{cite}`Heinrich2012ThePC`。另外，平行坐标法难以扩展到大规模的数据上，如{numref}`fig-visualization-informational-parallel_largescale`所示，过多的数据折线将完全掩盖掉可用信息，一种解决办法是使用一定聚类技术和透明渲染，从而重复出现的数据将占据更大的比重，数据之间的脉络关系也将获得更清晰的显示。也有研究{cite}`Zhou2008Clustering`尝试将连接平行坐标的折线改为弯曲边，通过最小化弯曲边的曲率和最大化相邻边的平行度，来优化边缘边的形状，提高了整体视觉上的聚类效果。
```{figure} fig/visualization-informational-parallel_largescale.png
:width: 60%
:name: fig-visualization-informational-parallel_largescale
3848个数据绘制成的平行坐标图像。
```

## 文本数据可视化

文本可视化（Text Visualization）是一种将文本数据以可视化方式呈现的技术，旨在帮助用户更好地理解文本信息、发现模式、关系和见解，以及支持文本数据的分析和决策。文本可视化通常涉及将文本数据映射到图形、图表或其他视觉元素上，以便直观地呈现文本的特征和结构。不同的文本可视化技术可以根据数据和分析任务的需求选择和定制。本小节将介绍文本可视化的一些常见技术和应用。

### 词云（Word Clouds）

词云（Word Cloud）是一种常见的文本可视化技术，用于将文本中的关键词汇以可视化方式呈现。如{numref}`fig-visualization-informational-wordle_init`所示，它通过将文本中的词汇按照其出现频率绘制成图像，以便用户可以直观地看到哪些词汇在文本中出现得更频繁，从而突出显示文本的关键特征，帮助用户更容易地理解文本的内容和重点。如{numref}`fig-visualization-informational-wordle_variety`所示，词云通常以一种艺术性的方式排列词汇，使其形成一个视觉上吸引人的图形。在词云中，词汇的字体大小通常与其在文本中的频率成正比，出现频率更高的词汇通常会显示为更大的字体，而出现频率较低的词汇则以较小的字体呈现。有时，词云还可以使用不同的颜色来表示词汇的重要性或情感极性。词云中的词汇通常以不同的角度和位置排列，以使整个图像看起来更加吸引人。这种可视化排列并不依赖于词汇的实际顺序，而是根据可视化设计来确定的。

```{figure} fig/visualization-informational-wordle_init.png
:name: fig-visualization-informational-wordle_init
:width: 50%
词云。
```

```{figure} fig/visualization-informational-wordle_variety.png
:name: fig-visualization-informational-wordle_variety
组成不同视觉图形的词云。
```
词云可用于多种应用，包括：

- 文本摘要：通过生成文本的词云，用户可以快速了解文本的主题和关键词汇，从而进行文本摘要。
- 社交媒体分析：在社交媒体数据中生成词云可以帮助用户了解用户在社交媒体上的热门话题和讨论内容。
- 新闻报道分析：通过生成新闻文章的词云，可以迅速了解新闻报道的关键主题和重要词汇。
- 情感分析：在情感分析中，词云可以用来可视化情感相关的关键词汇，帮助用户理解文本的情感极性。

```{figure} fig/visualization-informational-edwordle.png
:name: fig-visualization-informational-edwordle
EdWordle框架，允许更紧凑的词云排布和用户交互。
```
研究也关注如何使词云应用支持更丰富的用户交互和定制。
如{numref}`fig-visualization-informational-wordle_init`所示，EdWordle {cite}`Wang2018EdWordleCW` 将每个词汇看成一个二维平面内的矩形刚体，在刚体上施加相互之间的吸引力、向画布中心的吸引力、阻尼力，并利用基于冲量的方法解除碰撞，而后通过刚体仿真器对词云刚体系统进行仿真，从而获得更紧密的词云排布。另外，它支持用户的拖拽、放缩、旋转、增删等多样的操作，在尽可能保证邻居关系的基础上，通过绕中心的旋转查找，找到被修改词条的目标位置，并形成符合用户需求的紧密排布。

总之，词云是一种简单而有用的文本可视化工具，可用于快速了解文本数据的主要特征和重点。但需要注意，词云通常只提供了文本数据的高层次摘要，对于深入的文本分析可能需要更多复杂的技术和工具。

### 文本网络（Text Networks）

文本网络（Text Network）是一种文本可视化技术，用于可视化和分析文本数据中的关系、链接和连接。文本网络通过将文本中的关键词汇、实体或主题之间的关系表示为网络中的节点和边，以揭示文本数据中的模式、结构和关联。文本网络可以帮助用户更好地理解文本数据，并用于多种应用，如主题建模、信息检索、知识图谱构建和文本摘要。文本网络的构建和分析通常涉及自然语言处理（NLP）技术，如文本分析、关系抽取和主题建模。在文本网络中，文本数据中的关键词汇、实体或主题通常表示为节点，节点之间的关系表示为边。节点和边的属性可以用来表示节点的重要性、连接强度或其他相关信息。文本网络可以实现以下功能：

- 主题建模：文本网络可以用于主题建模，其中节点代表文本中的主题，边代表主题之间的相关性。这有助于识别文本中的主题和子主题，以及它们之间的关联。
- 关键词汇提取：文本网络可以用于提取文本数据中的关键词汇。通过分析节点的连接强度，可以确定哪些词汇在文本中具有重要性。
- 信息检索：文本网络可以用于改进信息检索系统，通过使用节点之间的关联来提高搜索结果的相关性。
- 知识图谱构建：文本网络可以用于构建知识图谱，其中实体、事件和关系都可以表示为节点和边。这有助于组织和查询大量的结构化信息。
- 文本摘要：通过分析文本网络中的节点和边，可以生成文本摘要，其中包含文本中的关键信息和关系。


{numref}`fig-visualization-informational-text_group` 和{numref}`fig-visualization-informational-text_network` 给出一个文本网络的例子。

```{figure} fig/visualization-informational-text_group.png
:name: fig-visualization-informational-text_group
原始文本。
```

```{figure} fig/visualization-informational-text_network.png
:name: fig-visualization-informational-text_network
文本网络。
```

### 文本时间轴可视化（Text Timeline Visualization）

文本时间轴可视化（Text Timeline Visualization）是一种用于可视化和分析文本数据随时间变化的技术。它将文本数据按照时间顺序呈现在一个时间轴上，以便用户可以追踪文本数据的演变、事件发展和趋势变化。文本时间轴可视化通常用于分析新闻文章、社交媒体帖子、历史文本和其他与时间相关的文本数据。

文本数据按照时间顺序排列在一个时间轴上，通常是从左到右或从下到上。每个时间点对应一个文本文档或事件，如{numref}`fig-visualization-informational-timeline`。通过观察文本时间轴上的趋势、峰值和突发事件，用户可以识别文本数据中的重要事件和趋势变化。这有助于了解文本数据的发展动态。用户可以在文本时间轴上选择特定时间范围内的文本数据，以进行文本检索和过滤。这有助于查找与特定事件或时间段相关的文本。文本时间轴可视化还可以与情感分析结合使用，以显示文本数据中情感的变化趋势。这有助于理解文本数据中的情感极性。用户可以观察文本时间轴上的主题和关键词汇随时间的变化，以了解文本数据中的主题演变。文本时间轴可视化通常具有交互性，用户可以通过缩放、拖动和选择时间范围等方式与数据进行互动，以更深入地探索文本数据。

文本时间轴可视化在多个领域中都有应用，包括新闻分析、历史研究、社交媒体分析、品牌监测和事件追踪。它可以帮助用户更全面地理解文本数据的演变和变化，以便支持决策制定、趋势分析和见解发现。文本时间轴可视化通常需要使用时间序列数据的处理和可视化技术，以有效地呈现和分析时间相关的文本数据。

```{figure} fig/visualization-informational-timeline.png
:name: fig-visualization-informational-timeline
文本时间轴https://asana.com/
```

### 主题建模和热度图（Topic Modeling and Heatmaps）

主题建模可将文本数据分解为不同主题，并将每个主题的关键词汇可视化呈现。热度图则可以显示文本中主题、词汇或实体的相对热度，帮助用户理解哪些主题或内容受到关注。

### 文本聚类（Text Clustering）

文本聚类是一种文本分析技术，旨在将相似的文本文档或数据点分组到同一簇中，以便发现文本数据中的潜在模式、关系和结构。聚类是无监督学习的一种方法，它不需要事先标记的类别信息，而是通过文本数据本身的特征来自动分组文本。聚类可以用于生成文本数据的摘要或代表性文档，每个簇可以用其代表性文档来表示簇内的所有文本。

文本聚类通常使用相似性度量方法来计算文本文档之间的相似性或距离。常用的相似性度量包括余弦相似度、欧氏距离、Jaccard相似性等。文本聚类可以使用各种聚类算法来执行，包括K均值聚类、层次聚类、DBSCAN、谱聚类等。不同的算法适用于不同的数据和分析需求。

文本聚类在信息检索、文档分类、推荐系统、社交媒体分析、舆情监测等领域都有广泛的应用。它可以帮助研究人员和分析师更好地理解大规模文本数据集，发现数据中的有趣模式和见解。然而，文本聚类也面临一些挑战，如处理高维度数据、选择适当的特征表示和聚类算法等。因此，在实际应用中，需要仔细考虑数据的特性和任务的需求来选择合适的文本聚类方法。

### TIARA（Text Insight via Automated Responsive Analytics）

如{numref}`fig-visualization-informational-tiara`所示，TIARA {cite}`TIARA2010` 采用流的形式来可视化文本：给定一组文档，TIARA首先使用主题分析技术将文档汇总为一组主题，每个主题由一组关键字表示（一层流）。除了提取主题外，TIARA还派生出随时间变化的关键字序列来描述每个主题随时间的内容演变（流中随横轴变化的关键字排布），关键字的纵轴宽度（每处流的纵轴宽度）表示了它出现的频率。

```{figure} fig/visualization-informational-tiara.png
:name: fig-visualization-informational-tiara
TIARA。
```

### 情感分析可视化

情感分析可视化是一种将情感分析结果以可视化方式呈现的技术，是文本数据可视化的重要子类，旨在帮助用户更好地理解文本数据中的情感极性、情感趋势和情感分布。情感分析（又称情感情感极性分析或情感情感分类）是一种自然语言处理技术，用于确定文本数据中包含的情感，通常分为正面、负面和中性。

以下是情感分析可视化的一些关键技术：

- 情感分布图：情感分析可视化通常使用情感分布图来表示文本数据中情感的分布。这些图表通常包括正面、负面和中性情感的百分比或计数，以及可能的情感极性变化趋势。

- 情感词云：情感分析可视化中，可以使用词云来可视化文本数据中与不同情感相关的关键词汇。每个情感类别的关键词通常以不同的颜色或字体大小呈现。

- 情感趋势图：对于时间序列数据，情感分析可视化可以绘制情感趋势图，显示情感随时间的变化。这对于分析文本数据中情感的演变非常有用，如社交媒体上的情感变化或品牌声誉的波动。

- 情感热力图：情感分析可视化可以使用情感热力图来表示情感之间的关系。这些图表显示了不同情感之间的相互作用，例如哪些情感常常同时出现在同一段文本中。

互动性是情感分析可视化的重点之一，用户可以通过鼠标悬停、点击或缩放等方式与可视化图表进行互动，以更深入地探索情感分析结果。

情感分析可视化在多个领域中都有应用，包括社交媒体分析、舆情监测、品牌管理、产品反馈分析和情感研究。它有助于企业和研究人员了解文本数据中的情感信息，识别用户情感倾向，监测情感变化，并根据情感分析结果制定决策和战略。这些可视化工具可以提供更深入的洞察力，帮助用户更好地理解情感数据中的模式和趋势。

## 图可视化

图可视化（Graph Visualization）是将图结构数据（如社交网络、交通网络、推荐系统等）可视化的技术。图数据由节点（代表实体）和边（表示实体之间的关系）构成。很多信息数据具有图结构，如{numref}`fig-visualization-informational-graph_apps`所示，包括并不限于组织架构、文件目录、社交网络等。图数据可视化的目的是帮助分析人员理解网络中的结构特征、节点之间的关系以及信息传播的路径。
```{figure} fig/visualization-informational-graph_apps.png
:name: fig-visualization-informational-graph_apps
不同类型的图数据。
```

**力导向布局（Force-Directed Layout）** 是一种常用于图数据可视化的布局算法，通过模拟物理力学中的相互作用力来优化节点位置。该方法基于以下原理{cite}`Fruchterman1991`：
- 节点之间的排斥力（Repulsive Force）：节点之间会相互排斥，类似于同电荷的粒子之间的排斥作用，这有助于避免节点之间的重叠，并使得节点分布更加均匀。
- 边的吸引力（Spring-like Hooke Attraction）：图中的边像弹簧一样起到吸引作用，边的长度与节点之间的距离成比例。边的吸引力确保节点之间保持合理的距离，并有助于图的结构稳定。
- 减少节点重叠：力导向布局通过综合作用力（排斥力和吸引力），在优化图结构的同时，最大限度地减少节点的重叠，使得图的可视化更加清晰易读。
如{numref}`fig-visualization-informational-graph_force`所示，这种布局方式能够直观地展示图中的结构关系，常用于社交网络、推荐系统等图数据的可视化，帮助用户识别核心节点和群体结构。另外，这一可视化方法具有良好的交互性能，可以为用户提供直观的从混乱的布局到整理完毕的规整布局的演变过程，且允许用户的随意拖拽，支持实时动态的图可视化与交互。

```{figure} fig/visualization-informational-graph_force.png
:name: fig-visualization-informational-graph_force
:width: 40%
力导向布局图。
```

力导向布局的主要缺点在于：
- 计算复杂度高：力导向布局需要计算每对节点之间的排斥力和吸引力，这对于大规模图来说计算开销非常大，其计算复杂度是 $O(n^3)$ 的。但通过设计空间加速结构（如四叉树）可以加速力导向布局图的计算，如基于 Barnes - Hut 算法{cite}`Harel2002`可以达到 $O(n\log(n))$ 的计算效率。
- 局部最优解：力导向布局通常使用迭代算法进行优化来达到一个能量极小的布局，这可能导致算法陷入局部最优解而非全局最优解，最终结果很大程度上受到初始布局的影响。Kamada - Kawai 算法{cite}`KK1989`和 Fruchterman - Reingold 算法{cite}`FR1991`可以被用来优化初始布局和节点排布。

社交网络是一种特殊的图，社区网络中的节点倾向于形成紧密连接的子群（社区），社区内部连接密集，而社区之间连接稀疏。
社区发现是面向社交网络数据的重要应用，通过分析这些连接模式，社区发现技术能够揭示网络中的潜在群体（如兴趣小组、社交圈子），帮助理解用户行为、信息传播以及网络演化规律，为社交分析、推荐系统等应用提供重要支持。

Vizster{cite}`Vizster2005`是早期社交网络可视化的代表性工具，如{numref}`fig-visualization-informational-graph_vizster`所示，它在力导向图中配置了多种交互策略：可以通过点击来高亮单个用户信息，展示与其直接相关的社交关系；或通过选点多个用户来查看他们的社交网络，发现他们共有的社交关系。
另外，Vizster在力导向布局中利用了**聚类布局**的思想来发现社区，自动检测社交网络中的社区结构，并用颜色编码区分不同社区。

```{figure} fig/visualization-informational-graph_vizster.png
:name: fig-visualization-informational-graph_vizster
:width: 60%
Vizster。
```

**聚类布局（Cluster Layout）**利用聚类算法将图中的节点按照相似性划分为多个子群体或社区，从而揭示数据的内在结构。以 Newman 的社区识别算法{cite}`Newman2003`为例，该算法通过以下步骤执行聚类：
- 初始状态：每个节点最初都被认为是一个独立的类，即图中的每个节点都代表一个单独的社区。
- 合并步骤：在每一步中，算法计算每对社区之间的“能量”，“能量”越小意味着节点或社区之前的相关性或亲密度越高，选择合并能量最小的两个社区。
- 结束条件：算法持续进行合并，直到所有节点合并成一个单一的社区（整个图作为一个类）。
- 输出结果：最终，算法输出一个划分树，通常为完全二叉树，每一层表示一次聚类操作，每层的划分反映了图结构的不同层次。这使得用户可以从整体到局部观察图中的聚类关系。
通过这种聚类算法，Vizster 得以自动检测社区结构，并允许用户通过拖动滑块来调节划分出“社区”的个数，社区个数越少、单个社区越大，社区内部人员的关系越紧密。

包含聚类布局的力导向图可以与邻接矩阵分析结合，提供更直观的
子图表达（Subgraph Represention）和社区模式，如{numref}`fig-visualization-informational-subgraph`所示，在邻接矩阵中，根据发现的社群对节点顺序进行重新排序后，非零值（有邻接边）集中在对角线附近，于是子对角块将对应各社区结构，社区信息被集中展示在子对角块中。

```{figure} fig/visualization-informational-subgraph.png
:name: fig-visualization-informational-subgraph
:width: 60%
包含聚类布局的力导向图（左）与根据社区进行重新排列的邻接矩阵（右），
```

**环状图（Circular graph）**用嵌套的圆形排布节点，适用于树状结构或层次结构的可视化，如师生关系网络、组织架构等。在环状图中，如{numref}`fig-visualization-informational-circular`所示，根节点通常位于中心，子节点按层次向外辐射，层次关系一目了然。嵌套圆周排列充分利用屏幕空间，对称美观，支持通过缩放、高亮等交互操作聚焦特定分支或节点，适合用于展示中等规模的层次数据。但环状图泛化性有限，只适用于最基础的具有树状结构的图，若节点具有非单一父节点或图中存在回路，则环状图会被一定程度上破坏且显得混乱。

```{figure} fig/visualization-informational-circular.png
:name: fig-visualization-informational-circular
:width: 60%
环状图。
```

**环形布局（Circular Layout）**将图中的所有节点排布在一个圆周上，边以弧线或直线的形式连接节点，被放置在圆周内部，如{numref}`fig-visualization-informational-circular_layout`所示。
为了更清晰地组织节点间的连接关系、体现图中包含的组织结构，环形布局也适合与着色和聚类方法相结合，如{numref}`fig-visualization-informational-circular_cluster`所示，从而减少杂乱的连线交叉，优化曲线曲率和形状，提高环形布局图的可读性。

```{figure} fig/visualization-informational-circular_layout.png
:name: fig-visualization-informational-circular_layout
:width: 60%
支持高亮的环形布局。
```
```{figure} fig/visualization-informational-circular_cluster.png
:name: fig-visualization-informational-circular_cluster
:width: 80%
与聚类方法相结合的环形布局。
```

总体来说，图可视化是介绍层次数据与网络数据中的结构特征和关系模式的重要手段，需要在空间布局（如力导向布局、环形布局等）、节点与链接的视觉编码（如尺寸、颜色等）等方面进行周密设计，从而提高图可视化的信息表达效率。

<!-- 
## 层次与网络数据可视化

很多信息数据具有层次或网络结构，如组织架构、文件目录、社交网络等。层次与网络可视化旨在揭示数据的拓扑结构、连接模式等特征。

对于层次数据，常用的可视化方法有:

- 树图(Treemap):用嵌套的矩形展示层次结构和数值属性。
- 辐射树(Radial Tree):用径向布局的节点-链接图展示层次结构。
- 旭日图(Sunburst):用嵌套的环形扇区展示层次结构和数值属性。
- 圆形打包图(Circle Packing):用嵌套的圆形展示层次结构。
对于网络数据，常用的可视化方法有:

- 节点-链接图(Node-Link Diagram):用点表示节点，线表示链接。
- 矩阵图(Matrix Diagram):用矩阵的行列交叉点表示节点间的连接。
- 平行坐标图(Parallel Coordinates):用平行轴展示多维属性，轴间的连线表示关系。
- 和弦图(Chord Diagram):用圆周上的弧线连接表示实体间的流量或关系。
在层次与网络可视化中，需要重点关注以下问题:

- 布局算法的选择，如力导向布局、辐射布局、层次布局等。
- 节点与链接的视觉编码，如尺寸、颜色等表示节点的重要性或类别。
- 网络的聚合与简化，平衡信息密度和可读性。
- 多属性网络数据的关联分析与展示。
- 动态网络演化过程的表达。
总的来说，层次与网络可视化试图揭示数据中的结构特征和关系模式，需要在空间布局、拓扑表达、信息编码等方面进行周密设计 -->


<!-- ## 时空数据可视化

很多信息数据都包含时间属性，反映事物的动态演化过程。地理信息数据则附加了空间坐标，刻画了现象在地理空间的分布。时空数据可视化的目标是同时展现数据的时间和空间特征，揭示时空模式、进程、异常等。

对于时间数据，常用的可视化方法有:

- 时间线(Timeline):在一条横轴上展示事件序列。
- 甘特图(Gantt Chart):展示任务、进程的起止时间和持续时间。
- 主题河流(ThemeRiver):用层叠的条带展示主题随时间的演化。
- 时间轮(Time Wheel):用圆环分割展示周期性、循环的时间模式。

对于时空数据，常用的可视化方法有:

- 时空立方体(Space-Time Cube):用三维空间表示二维地理空间和一维时间。
- 轨迹图(Trajectory):在地图上用线条连接移动对象的位置变化序列。
- 热力图(Heatmap):用色彩编码表示空间现象的密度和强度变化。
- 时空流线图(Flow Map):用带宽度的曲线表示时空流量的迁移模式。
在时空数据可视化中，需要重点关注以下问题:

- 时间和空间尺度的选取，平衡局部细节和全局概览。
- 时间维度的展示形式，如线性、周期性、分支型等。
- 时空数据的聚合与抽象，平衡信息密度和可读性。
- 多源、异构时空数据的关联分析与融合展示。
- 时空语义信息的提取与可视化表达。
总的来说，时空数据可视化试图在有限的屏幕空间内展现时间和空间的无限变化，需要在时空尺度、分辨率、形式和美感等方面进行精心设计。 -->




<!-- ## 高维数据可视化

高维数据可视化是数据科学和机器学习领域中的一个重要挑战，因为人类的视觉系统通常只能有效地理解三维空间以下的数据。在处理高维数据时，有几个难点需要克服：

- 数据稀疏性：高维空间中的数据点通常是稀疏的，这意味着数据点之间的距离很大，很难在可视化中显示出来。这会导致可视化失真，因为只有一小部分数据点会被显示，而其他数据点被忽略了。
- 数据维度灾难：随着维度的增加，数据点之间的距离变得更加模糊，这使得难以找到有效的可视化方式来表示数据的结构和关系。高维数据的复杂性增加了可视化的挑战。
- 可视化的可解释性：高维数据可视化通常会导致信息的丢失和可视化的复杂性，这可能会降低可视化结果的可解释性。解释可视化结果对于理解数据和从中提取见解至关重要。
- 可视化的互动性：为了更好地理解高维数据，通常需要与可视化进行互动，探索不同的视图和维度组合。设计交互性可视化界面是一个挑战，需要考虑如何有效地将高维信息传达给用户。

选择适当的高维数据可视化方法是一个重要的决策，因为不同的方法可能会呈现不同的数据结构和关系。
在高维数据可视化中，降维方法发挥着重要作用。常见的降维方法有:

- 降维技术（如 PCA、t-SNE、UMAP）:利用正交变换将数据投影到方差最大的低维子空间。
- 多维尺度法（MDS）:保持数据点间的距离关系，将高维空间映射到低维空间。
- 并行坐标
- 热力图
- t-SNE:基于数据点的相似性概率分布，实现非线性降维。

常用的高维数据可视化方法有:

- 散点图矩阵(Scatter Plot Matrix):在矩阵的每个子图中展示两两维度的散点图。
- **平行坐标（Parallel Coordinates）** 
（是否需要介绍这么详细，其他方法是否也要详细描述？）

平行坐标是一种用于可视化多维数据的图形表示方法。它可以有效地显示和分析包含多个特征或属性的数据集，其中每个特征都在平行的垂直坐标轴上表示，而数据点则通过在这些坐标轴上绘制线段来表示。每个数据点都是一条连接各个坐标轴的线段，线段的位置和形状可以反映数据点在各个特征上的取值。

以下是平行坐标的关键特点和用途：

多维数据可视化：平行坐标适用于具有多个特征或属性的数据集，因为它可以在同一图表中同时显示多个维度的信息，而无需将数据降维到二维。

发现模式和趋势：通过观察数据点之间的线段交叉、平行和聚集等情况，可以识别数据中的模式、趋势和关系。这有助于理解数据的结构和特点。

数据筛选和比较：你可以使用平行坐标来选择特定范围内的数据点，从而进行数据筛选。此外，你还可以比较不同数据点或数据集之间的模式和趋势。

异常检测：异常值通常在平行坐标中很容易被识别，因为它们可能导致线段与大多数其他线段明显不同。

交互性：在平行坐标图中添加交互性可以使用户更轻松地探索数据，例如通过移动坐标轴、缩放、筛选和高亮显示数据点等方式。

尽管平行坐标图在可视化多维数据方面具有很大优势，但也存在一些挑战，如坐标轴的交叉可能导致可视化变得混乱，需要谨慎设计和交互操作来提高可读性和有效性。平行坐标图通常用于数据挖掘、数据分析、机器学习和可视化领域，以帮助研究人员和分析师理解和发现复杂数据集中的模式和关系。

- 雷达图(Radar Chart):将多维数据映射为封闭的多边形。
- 维度堆叠(Dimensional Stacking):递归地将高维空间嵌套划分为层次的子空间。
- 像素导向(Pixel-oriented):用像素编码表示每个数据点的多维量值



高维数据可视化的难点在于，如何避免维度缺失、视觉混乱，如何揭示高维数据的内在结构和特征，如何设计便于用户理解和交互的可视化隐喻。这需要可视化工作者积极吸收信息论、机器学习等领域的最新研究成果，探索创新的可视化设计。 -->
