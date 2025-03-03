# 可视化设计
<!-- :label:`visualization-design` -->

## 可视化流程

### 科学可视化流程

如{numref}`fig-visualization-analytics-scientific_pipeline`，Haber 和 McNabb 等人提出科学可视化流水线，将科学可视化过程分为以下几个阶段：

```{figure} fig/visualization-analytics-scientific_pipeline.png
:name: fig-visualization-analytics-scientific_pipeline
数据可视化流程。
```
- 原始数据（Raw Data）：可视化的起点，通常包括实验数据、模拟数据或观测数据等未经处理的原始数据。这些数据可能是多维的、复杂的，并且通常需要经过预处理才能用于可视化。
- 准备好的数据（Prepared Data）：通过应用平滑滤波器、插值缺失值或校正错误测量等**数据准备（Data Preparation）**，使原始数据变为可用状态，并通过用户选择过滤出要进行可视化的数据部分，以确保数据中的核心信息得到进一步处理和分析。
- 图形元素（Graphical Primitives）：将准备好的数据**映射（Mapping）** 到适当的几何图元（如点、线等）及其属性（如颜色、位置、大小等），使数据在可视化空间中获得对应的表达。这一阶段涉及：（1）视觉编码：将数据属性映射为视觉变量（如位置、颜色、大小、形状等）；（2）布局设计：确定图形元素在空间中的排列方式（如节点链接图、矩阵图等）。
- 图像（Image）：将映射后的图形元素进行**渲染（Rendering）**，最终绘制成图像。如果选择的图形元素是三维空间中的元素，那么渲染还会包括光照、阴影处理、纹理映射等。

### 信息可视化流程

与科学可视化的流程类似，如{numref}`fig-visualization-analytics-info_pipeline`，信息可视化参考模型（Information Visualization Reference Model）{cite}`card1999readings`展示了信息可视化的大致流程，将可视化过程分为以下几个阶段：
```{figure} fig/visualization-analytics-info_pipeline.png
:name: fig-visualization-analytics-info_pipeline
信息可视化的流程示意图。
```
- 原始数据（Raw Data）：可视化的起点，是未经处理的原始数据集，可能包括表格、文本、图像、时间序列等多种形式。
- 数据表（Data Tables）：原始数据经过预处理和**数据转换（Data Transformation）**，包括并不限于清理，过滤，格式化等，转换为适合可视化和分析的数据表形式。数据表通常由行（记录）和列（属性）组成，每个单元格存储具体的数值或类别。
- 可视化结构（Visual Structures）：通过**视觉映射（Visual Mapping）**，数据表被映射为可视化结构，即图形的视觉表现形式。
- 视图（Views）：可视化结构最终呈现为用户看到的视图，并经过视角调整和用户交互等**视图变换（View Transformation）**，来增强对视图中所蕴含信息的探索。

相比于科学可视化，信息可视化的一大特点是具有很强的互动性。信息可视化应用中，数据包含大量而丰富的信息，信息可视化的目标是寻找信息中潜藏的模式关系或特征，应用面向的用户是广泛而非专业的，因此用户需要参与到数据筛选、视觉表达选择、视图调整等各环节中，以此来获得用户满意的可视化结果。通过互动信息可视化，特别是在网站或应用程序中使用时，用户能够从不同的角度查看信息主题，并操作其可视化，直到达到所需的见解并满足广泛的用户需求和探索性体验。

### 视觉映射

在可视化流水线（{numref}`fig-visualization-analytics-scientific_pipeline`, {numref}`fig-visualization-analytics-info_pipeline`）中，**视觉映射**是决定其表达效果的关键步骤。
视觉映射也被称为视觉编码（Visual Encoding），负责将数据从数据空间转化为可视化空间的视觉元素。这一过程通过**视觉通道（Visual Channels）** 实现，例如位置、颜色、大小、形状等，将数据属性映射为可感知的图形特征，从而帮助用户理解数据内在的模式与关系。

不同的视觉通道直接影响用户的认知效率。常见的视觉通道包括：

- 位置（Position）：最有效的通道，适合表示定量数据（如折线图、散点图）。
- 颜色（Color）：
  - 色相（Hue）：区分类别数据（如不同产品类别）。
  - 亮度/饱和度（Brightness/Saturation）：表示数值大小或强度（如热力图）。
- 大小（Size）：表示数值差异（如气泡图）。
- 形状（Shape）：区分定性数据（如不同节点类型）。
- 方向（Orientation）：适合表示趋势或方向性数据（如箭头图）。

一般来说，定量类通道（如位置、长度、面积等）在人类的视觉感知上优先级高于定性类通道（如颜色、形状等）
根据 Cleverland 等人的研究{cite}`Cleveland1984GraphicalPT`，人类对视觉通道的感知效率排序如下：
位置 > 长度 > 角度/斜率 > 面积 > 体积 > 颜色饱和度。
因此，在可视化设计中，应优先将关键数据维度映射到高感知效率的通道（例如用位置表示核心指标）。

在一张图表中，有时也需要使用多种视觉通道协同工作，从而编码更丰富的视觉信息。但需要注意的是，人类在同一时间内只能处理有限的视觉信息，当过多通道在同一空间内竞争用户的注意力时，视觉通道之间相互干扰会导致认知负荷增加：
- 当多个视觉通道同时使用时，某些通道可能干扰用户对数据的感知。例如，在散点图中，同时使用颜色和形状编码类别数据，可能导致用户难以区分类别（红色圆形 vs. 红色方形）。
- 当使用多个视觉通道传达同类的信息，也会导致资源浪费或视觉过载。例如，在饼状图中，同时使用颜色和标签标注类别，可能导致信息重复和图表拥挤。
因此，应使用恰当数量的视觉通道（通常不超过3-4个），尽量使用能协同工作的通道，并根据数据维度的重要性安排对应优先级的视觉通道。

## 可视化设计准则

一个优秀的可视化设计需要在有限的图表内有效地传达出数据中包含的重要信息，可视化设计需要综合考虑多方面的资源限制因素，包括并不限于计算机的计算能力、人类本身的认知能力的以及显示器的性能等。

- 计算限制
  - 处理时间：可视化设计必须考虑计算机的处理效率，需要确保生成和呈现大规模或复杂的数据可视化不会导致性能问题。在与用户进行交互的可视化应用中，快速的可视化生成对用户体验至关重要，一般来说，对交互的反应时间不应超过500ms，否则用户将感到厌烦。一些静态可视化（如科学可视化）能接受更高的渲染耗时，但对耗时的忍受度也是有限的。
  - 系统内存：超大规模的数据集和复杂的图形可能需要大量的内存来存储和处理，这涉及到数据管理（data management）策略。

- 认知限制：可视化设计必须考虑到人类的认知能力。信息过载可能导致注意力分散，因此设计必须注重突出显示最重要的数据，以帮助用户集中注意力并记住关键信息。

- 显示限制：屏幕像素是有限的，因此在可视化时需要优化像素的使用，确保信息清晰可见。不合理的像素使用可能导致图形不清晰或加载速度缓慢。一个好的可视化设计需要在信息的紧凑性和可读性之间取得平衡，太拥挤的图表可能难以解释，而太稀疏的图表可能无法有效传达信息。

为了有效使用有限的资源，人们总结出了一系列的可视化设计指导原则。
根据数据具体类型和可视化的任务目标及用户群体，选择合适的视觉映射方案，这是创建有效的数据可视化的关键步骤。

1. 任务抽象
<!-- **目标驱动选择** -->

在决定具体的可视化类型时，首要考虑的是可视化的任务目标，例如是否要比较值、显示趋势、发现模式、探索关系、展示分布等。
<!-- **考虑受众** -->

2. 用户抽象

其次，考虑可视化的受众群体和想要传达给他们什么样的信息。考虑到受众的背景知识，要确保可视化能够满足受众的理解水平。
对于可视化或相关领域的专业用户，可提供具备高级交互功能（如多维过滤、动态关联）的可视化工具；而对于一般的对数据分析不熟悉的用户，简单直观的可视化可能更有用，因此需简化设计，突出核心信息。

3. 数据抽象

不同数据类型（定类、定量、定序等）在映射到不同视觉通道时，会导致不同的用户认知效率。了解要处理的数据类型并合理分配视觉通道，将更加重要的维度放到认知效率更高的通道上去表示，是可视化设计的关键，于是产生了不同种类的可视化类型。
**定量**数据，如数字和测量值，通常适合使用柱状图、折线图或散点图来表示。而**定性**数据，如类别或标签，更适合使用饼图、条形图或词云等可视化方式。**定序**数据，即随时间变化的数据，如股价、气温等，适合用瀑布图、折线图、时间轴、流程图等方式可视化。

```{figure} fig/visualization-analytics-news.png
:name: fig-visualization-analytics-news
2014年美国新闻热度可视化。 ©https://echeloninsights.tumblr.com/post/105911206078/theyearinnews-2014
```
数据集的大小和复杂性也是选择可视化类型的重要因素。人能够同时处理的信息是有限的，包括视觉元素数量和视觉通道种类。如果要处理大量数据点或复杂的数据结构，可能需要利用一些高级可视化技术，如热力图、网络图或树状图，并且对数据进行筛选、合并等预处理，使图表重点突出。
一个反例如{numref}`fig-visualization-analytics-wrong_redundant`所示，单个可视化文件中的过多数据会立即使观看者不知所措。当可视化包含太多数据时，信息就会淹没，并且数据会融化成大多数观众无法忍受的图形。

```{figure} fig/visualization-analytics-wrong_redundant.png
:name: fig-visualization-analytics-wrong_redundant
单个可视化文件中包含过多数据会令观看者不知所措。
```

4. 视觉映射的经验法则

- 一致性：保持可视化元素的一致性是重要的，包括颜色、字体、标签和图表样式。一致性有助于降低用户的认知负担，使他们更容易理解和比较不同的数据。
- 强调关键信息：可视化应该有助于突出展示最重要的数据和趋势。通过颜色、标签、注释和高亮显示等方式，强调关键信息有助于观众快速识别要点。
- 避免误导：设计应该努力避免制造误导性的图表或图形。这包括避免截断轴、使用不恰当的比例、选择不合适的图表类型等。可视化应该真实反映数据，而不是歪曲或夸大。
如{numref}`fig-visualization-analytics-wrong_block` 所示，这里的三维图形就造成了遮挡。
```{figure} fig/visualization-analytics-wrong_block.jpg
:name: fig-visualization-analytics-wrong_block
三维图形会造成遮挡。
```
- 色彩和标签优化：颜色应该谨慎使用，避免过多的颜色或使用不明确的颜色方案。合适的颜色选择有助于提高可视化的可读性。每个可视化元素都应该具有清晰的标签和标题，以解释图表的含义和数据的来源。这有助于避免混淆和误解。
- 交互性：交互性在可视化工具中扮演着重要的角色，尤其是在信息可视化中，它使用户能够更深入地探索和理解数据，以及与可视化图形进行互动，从而获得更。如缩放、过滤、交互式图例、滑动条和时间轴、链接等。
- 经验和灵活性：查看类似领域或问题的可视化示例，以获取灵感和最佳实践。最重要的是要灵活，如果一种可视化类型不起作用，尝试其他类型。有时候，根据经验和反馈，可能需要组合多种可视化类型，以更全面地呈现数据。

<!-- 这些设计准则在前文和后续内容中得到体现。 -->

## 常见的可视化图表及工具库

有许多可视化工具可供选择，具体取决于数据类型和可视化需求。以下是一些常见的可视化工具：

```{figure} fig/visualization-analytics-popularity.png
:name: fig-visualization-analytics-popularity
世界人口数量条形图。 ©Apache ECharts
```
```{figure} fig/visualization-analytics-aqi.png
:name: fig-visualization-analytics-aqi
空气质量折线图。 ©Apache ECharts
```
```{figure} fig/visualization-analytics-gender.png
:name: fig-visualization-analytics-gender
男女身高体重分布图。
```
```{figure} fig/visualization-analytics-pie.png
:name: fig-visualization-analytics-pie
饼状图。
```
```{figure} fig/visualization-analytics-income.png
:name: fig-visualization-analytics-income
工资使用情况图。 ©Reddit
```
```{figure} fig/visualization-analytics-congress.png
:name: fig-visualization-analytics-congress
美国国会议员路径图。 ©The New York Times
```

- 条形图和柱状图：用于比较不同类别的数据，如{numref}`fig-visualization-analytics-popularity`。
- 折线图：用于显示数据随时间变化的趋势，如{numref}`fig-visualization-analytics-aqi`。
- 散点图：用于显示两个变量之间的关系，如{numref}`fig-visualization-analytics-gender`。
- 饼图：用于显示数据的组成部分，如{numref}`fig-visualization-analytics-pie`。
- 热力图：用于显示数据的密度和分布。
- 地图：用于可视化地理数据。
- 雷达图：用于比较多个变量之间的关系。
- 树状图和网络图：用于可视化层次结构和关系数据，如{numref}`fig-visualization-analytics-income`和{numref}`fig-visualization-analytics-congress`。


学习可视化最好的方法是实际操作。使用真实数据集创建可视化，尝试不同的图形类型和设计选择，以提高可视化技能。有许多可视化工具和库可供使用，例如：
Python中的Matplotlib 、Seaborn和Plotly。
JavaScript中的D3.js、Chart.js和Three.js。
商业工具如Tableau和Power BI。
