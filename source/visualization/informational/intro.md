# 概览
<!-- :label:`information-visualization` -->

```{figure} fig/visualization-informational-infovis.png
:name: fig-visualization-informational-infovis
信息可视化。
```

信息可视化（Information Visualization）是指将抽象的非空间数据通过图形化的方式呈现，以帮助用户理解和分析数据中蕴含的信息和规律。与科学可视化处理的物理场数据不同，信息可视化面对的数据通常是来自商业、金融、社会等领域的非结构化、半结构化数据，如文本、网络、层次结构等，不具有明确的空间坐标，维度较高，数据类型多样。因此，信息可视化的重点是设计合适的视觉隐喻和交互机制，有效组织和呈现信息，促进用户对数据的探索和理解。

<!-- 仪表板和散点图是信息可视化的常见示例。通过提供概述并显示相关连接，信息可视化允许用户以高效和有效的方式从抽象数据中得出见解。
信息可视化在使数据易于理解和将原始信息转化为可操作见解方面发挥着重要作用。它汲取了人机交互、视觉设计、计算机科学、认知科学等领域的知识。示例包括世界地图风格的表示、折线图以及三维虚拟建筑或城镇规划设计。 -->

<!-- 创建信息可视化的过程通常始于了解目标用户群体的信息需求。定性研究（例如用户访谈）可以揭示可视化将如何、何时和何地使用。借助这些见解，设计师可以确定需要哪种形式的数据组织以实现用户的目标。一旦信息以有助于用户更好地理解和应用数据以达到他们的目标的方式组织，设计师就会使用可视化技术。视觉元素（例如地图和图表）以及适当的标签被创建，视觉参数如颜色、对比度、距离和大小被用来创建适当的视觉层次和信息的视觉路径。 -->

```{figure} fig/visualization-informational-infovis_pipeline.png
:name: fig-visualization-informational-infovis_pipeline
信息可视化的流程示意图。
```
如{numref}`fig-visualization-informational-infovis_pipeline`，信息可视化参考模型（Information Visualization Reference Model）{cite}`Card1999`展示了信息可视化的大致流程，将可视化过程分为以下几个阶段：
- 原始数据（Raw Data）：可视化的起点，是未经处理的原始数据集，可能包括表格、文本、图像、时间序列等多种形式。
- 数据表（Data Tables）：原始数据经过预处理和**数据转换（Data Transformation）**，包括并不限于清理，过滤，格式化等，转换为适合可视化和分析的数据表形式。数据表通常由行（记录）和列（属性）组成，每个单元格存储具体的数值或类别。
- 可视化结构（Visual Structures）：通过**视觉映射（Visual Mapping）**，数据表被映射为可视化结构，即图形的视觉表现形式。这一阶段涉及：（1）视觉编码：将数据属性映射为视觉变量（如位置、颜色、大小、形状等）；（2）布局设计：确定图形元素在空间中的排列方式（如节点链接图、矩阵图等）。
- 视图（Views）：可视化结构最终呈现为用户看到的视图，并经过视角调整和用户交互等**视图变换（View Transformation）**，来增强对视图中所蕴含信息的探索。

相比于科学可视化，信息可视化的一大特点是具有很强的互动性。信息可视化应用中，数据包含大量而丰富的信息，信息可视化的目标是寻找信息中潜藏的模式关系或特征，应用面向的用户是广泛而非专业的，因此用户需要参与到数据筛选、视觉表达选择、视图调整等各环节中，以此来获得用户满意的可视化结果。通过互动信息可视化，特别是在网站或应用程序中使用时，用户能够从不同的角度查看信息主题，并操作其可视化，直到达到所需的见解并满足广泛的用户需求和探索性体验。
<!-- 特别是在网站或应用程序中使用时。互动性允许用户操纵可视化，使其在满足他们需求方面非常有效。通过互动信息可视化，用户能够从不同的角度查看主题，并操作其可视化，直到达到所需的见解。如果用户需要一种探索性体验，这尤其有用。 -->

在信息可视化流程中，针对不同的信息数据类型有着多样的视觉映射方法，这也是信息可视化的技术核心，接下来，本章将围绕不同类型的信息数据及其相关的可视化技术展开介绍。