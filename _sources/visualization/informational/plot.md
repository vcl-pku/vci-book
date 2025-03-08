# 基础绘图

绘图（plot）是数据可视化中的一种基本工具，将数据点在二维或三维坐标系中通过图形化方式呈现，展示数据的关系、趋势、分布,从而帮助用户直观地理解数据的结构和模式。简单来说，绘图技术，通过某些图形表示，将数据中的大量信息简化为最简单和最干净的形式，使得数据（点）中固有的关系可以容易地被感知。

如{numref}`fig-visualization-informational-plot`所示，plot 是一个非常通用的可视化操作，在不同的编程语言和工具中，均有对 plot 的默认实现。但，对同样的数据，有无数种可采用的可视化方法，而不恰当的绘图方式很容易给人们以不同的甚至错误的信息，因此如何使用绘图来正确传达数据所包含的信息是一件值得思考的事情。

```{figure} fig/visualization-informational-plot.png
:name: fig-visualization-informational-plot
不同编程工具中的默认绘图。
```

从{numref}`fig-visualization-informational-plot`的对比图中，我们可以得到重要的两点结论：首先，绘图没有明确的使用标准或使用公式，这不同绘图在坐标轴和比例线、图内的数据矩形以及数据值的实际表示等方面上的差异可以看出来；其次，创建一张绘图是一个迭代的设计过程，一次绘图的设计方案不能普遍适用于所有类型的数据。

然而，人们也已经提出了一些普遍的绘图原则，可以被用作指导，以提高绘图能传达出有用信息的可能性。下面我们将介绍 William S. Cleveland 提出的提升绘图质量的两条路线和相应原则{cite}`Cleveland1993visualizing, Cleveland1994graphing`。

## 提升绘图质量的原则

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

## 基础绘图技术

**折线图（line plot）**：也被称为**连接符号图（Connected symbol plot）**，是一种最常用的绘图技术，通过连接数据点来显示数据之间关系的图形。每个数据点用符号（例如圆圈、方块、点等）表示，并通过线条连接相邻的数据点。这类图表常用于展示连续数据之间的趋势或关系，如时间序列或其他有序的一维数据，如{numref}`fig-visualization-informational-lineplot`所示。在连接符号图中，符号标出了可能带有高频噪音的数据，连线显示出平滑数据的低频特征，符号连线则结合了两者的功能，利用符号展现数据实际分布并用连接线更清晰地跟踪数据随时间或其他变量的变化趋势。折线图非常适合于展现连续型数据（如时间序列、温度变化、收益率等）的趋势、峰值、波动等特征。
对比多条折线时，应区分颜色或线型，避免信息混淆。
```{figure} fig/visualization-informational-lineplot.png
:width: 80%
:name: fig-visualization-informational-lineplot
连线图。
```

**点图（dot plot）**：是一种与柱状图或饼状图性质类似的绘图形式，适用于有定量标注的且相互之间没有顺序关系的数据，如{numref}`fig-visualization-informational-dotplot`和{numref}`fig-visualization-informational-dotplot_multidim`所示。
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

**散点图（scatter plot）**：利用二维或三维笛卡尔坐标来标识二维数据或三维数据的数据值，适用于需要观察“数值型数据之间的分布与关联度”的场合，可以用于直观识别集群、离群点、线性/非线性关系。如{numref}`fig-visualization-informational-scatter_correlation`所示，恰当地使用散点图能直观地揭示数据之间的相关性。如{numref}`fig-visualization-informational-scatter_line`所示，对于具有相关性的数据，通常还可以在图中加入一条最佳拟合的直线来展现相关性。
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
散点图的一个扩展是**气泡图 (Bubble Chart) **，它将散点改成具有大小或颜色的圆圈，利用这一新增的视觉通道表达第三个维度。
```{figure} fig/visualization-informational-bubble.png
:width: 80%
:name: fig-visualization-informational-bubble
带颜色的散点图：利用颜色编码“性别”这一信息维度。
```
通过将散点图排列成矩阵，散点图也可用于展示更高维度的数据。如{numref}`fig-visualization-informational-scatter_highdim`所示，将高维数据的每个维度分别分配给各行和各列，得到一个方阵，方阵的每个元素即为取出行列的对应维度的数据绘制出的标准散点图。为避免重复绘制扰乱视线，可以只绘制方阵的上三角部分。
```{figure} fig/visualization-informational-scatter_highdim.png
:width: 60%
:name: fig-visualization-informational-scatter_highdim
利用散点图矩阵展示高维数据，并通过观察特定散点图或整行/列散点图中的散点分布形态得到维度之间的相关性（绿色方框）。
```

**条形图（bar chart）**：常被用于离散型或分类型数据（如不同城市、产品、月份等）之间的数值比较，利用每个类别的矩形条的长度标识对应的数据值。一般矩形条的长边会被纵向摆放（类别被排列在横轴），这类条形图也被称为**柱状图**。在类别较多或类名过长时，矩形条也可以被横向摆放（类别被排列在纵轴），如{numref}`fig-visualization-informational-popularity`所示，这让条形图更加易读。
```{figure} fig/visualization-informational-popularity.png
:width: 60%
:name: fig-visualization-informational-popularity
世界人口数量条形图。 ©Apache ECharts
```

**直方图（histogram）**：是一类特殊的条形图，被用于展示数据的分布情况。如{numref}`fig-visualization-informational-histogram`所示，它将数据分为若干个连续且不重叠的区间（bins），并通过柱形的高度表示每个区间内数据点的数量。直方图常用于分析数据的分布特征，例如查看数据的集中趋势、离散程度以及是否存在偏态或多峰分布。
```{figure} fig/visualization-informational-histogram.png
:width: 90%
:name: fig-visualization-informational-histogram
柱状直方图。
```

**箱形图（box plot）**：通常用于展示数据的统计方差，如{numref}`fig-visualization-informational-box`所示，显示数据的四分位数（Quartile）、中位数及最大值、最小值，以及可能的离群值。
```{figure} fig/visualization-informational-box.png
:width: 60%
:name: fig-visualization-informational-box
箱形图。黑色上下短横线、蓝色箱体上下边、红色中间线分别对应数据的最大值、最小值、Q1 四分位数、Q3 四分位数、中位数。
```

**饼图（pie chart）**：也被成为扇形图（sector diagrams），用于显示数据的组成部分，如{numref}`fig-visualization-analytics-pie`所示，每个组成部分占据圆形的一个扇形子区域，扇形对应的中心角/面积展示了组成部分的占比。这种绘图方式可以直观地展示各组成部分的占比关系，但在组成类别过多或数值差异不大时，不同扇形不易比较，此时条形图等其它绘图技术可能是更合适的方案。
```{figure} fig/visualization-informational-pie.png
:width: 60%
:name: fig-visualization-informational-pie
饼图。
```

**雷达图（radar chart）**：是一种用于展示多变量数据的可视化图表，适合用于比较多个指标之间的关系。它通过在一个圆形区域内绘制多个从中心向外辐射的轴线（对应不同“维度”或“指标”），并在每个轴线上标记数据点，最后将这些点连接起来形成一个多边形，从而直观地展示数据在多个维度上的表现。
```{figure} fig/visualization-informational-radar.png
:width: 60%
:name: fig-visualization-informational-radar
雷达图。© Wikipedia
```

**热力图（heat map）**：在二维图像中通过颜色的深浅或冷暖等变化来表示数据的数值大小，通常用于二维矩阵数据或地理分布场景。热力图的核心在于将数据的数值范围映射到颜色谱上，从而直观地展示数据的分布、密度或强度。如{numref}`fig-visualization-informational-heatmap`所示，对于二维矩阵数据，热力图的颜色分布在规则排列的矩阵单元格中；对于地理数据，如人口密度，则可以将数据转换成的颜色标在对应的地理位置处。
```{figure} fig/visualization-informational-heatmap.png
:width: 60%
:name: fig-visualization-informational-heatmap
热力图。© Wikipedia
```

**桑基图（Sankey diagram）**：是一种“流图”，它通过宽度不同的弧线来展示数据的流动和比例关系，表示不同类别之间的能量、物质或成本的转移和分配情况，如{numref}`fig-visualization-informational-sankey`所示。桑基图的一个经典例子是拿破仑出征图，它是一种与地图相结合的桑基图。
```{figure} fig/visualization-informational-sankey.png
:width: 60%
:name: fig-visualization-informational-sankey
桑基图：工资使用情况图。 © Reddit
```
<!-- ```{figure} fig/visualization-informational-congress.png
:width: 60%
:name: fig-visualization-informational-congress
桑基图：美国国会议员路径图。 © The New York Times
``` -->
