(sec-visualization-analytics-system)=
# 可视分析系统

在理解了可视分析的基本概念和知识生成理念之后，如何构建一个实用的可视分析系统就成为下一步关注的重点。

## 系统构建的背景与定位
体系化思维
可视分析系统往往需要涵盖：数据管理层、算法和模型层、可视化交互层以及支撑这三者循环往复的交互机制。
随着分析任务的复杂化，系统需要在人-机-数据三者之间形成紧密的闭环，通过动态反馈驱动知识迭代。
与传统可视化系统之差异
传统可视化系统：更多关注图形呈现、交互界面美观及基本分析功能；
可视分析系统：在可视化和数据挖掘/模型构建之上，进一步强调用户的探索与验证需求，往往整合了日志记录、交互历史、自动化建议等功能。

## 典型系统框架

可视分析系统的设计遵循**“数据-模型-可视化”三元框架**，通过动态交互将计算机的计算能力与人类的认知推理能力紧密结合。其核心组件包括：

- 数据层（Data Layer）
  - 功能：负责数据的采集、存储、清洗与预处理。
  - 原始数据：结构化、非结构化或实时流式数据。
  - 数据预处理：数据集成、清洗、抽样、聚合、增强、索引构建。

- 模型层（Model Layer）
  - 功能：通过统计与机器学习模型抽象数据特征。 
  - 多种模型类型：描述性模型、预测性模型。
  - 动态适配：允许用户调整模型参数（如K-means聚类数）数或训练策略，并实时反馈结果。
  - 在线/离线分析：可根据任务需求选择在本地或云端集群进行训练或推断。

- 可视化与交互层（Visualization & Interaction Layer）
  - 功能：将数据或模型结果映射为可交互的视觉表示。
  - 设计原则：视图呈现如散点图、平行坐标、地理地图、网络图等；基于感知原则选择合适的可视编码。
  - 交互操作：刷选、过滤、多视图联动、细节提示、标记与注释；
  - 结果解读：将模型输出（如聚类结果、特征重要度）与可视界面直观结合，辅助洞察。

```{figure} fig/visualization-analytics-inform_model.png
:name: fig-visualization-analytics-pipeline2
图中展示了三大模块（数据、模型、可视化与交互）如何首尾相连，并围绕用户形成一个多重回路。
数据经由预处理后被送入模型层进行运算，模型结果可进一步投射到可视化。用户在视图上操作时，可跳转至不同分析模型或获取更多数据，形成一个整体的系统生态。{cite}`sacha2014knowledge`
```


## 系统构建的六大关键步骤

**1. 提出可视分析任务**

首先，需要明确我们要通过可视分析来解决哪些问题，满足哪些需求。
这一步通常会结合业务背景或科研目标，从而定义系统需要实现的功能与分析目标。
例如，在医疗影像分析场景中，目标可能是识别和标注疑似病变区域；在地理信息场景中，目标可能是对大范围内的交通流量进行实时监测与预警。

**2. 构建可视分析模型**

在明确任务之后，需要设计并绘制可视分析系统的架构图，形成可视分析模型。
该模型通常基于 Card{cite}`Card1999`于1999 年提出的信息可视化模型（{numref}`fig-visualization-analytics-inform_model`），即从原始数据出发，通过“数据转换”“视觉映射”与“视图转换”等阶段，最终完成用户与可视化视图的交互过程。
可视分析模型的作用在于为系统提供整体思路与流程把控，使后续的可视化设计、实现和评测都能保持一致的目标与逻辑。

**3. 设计可视化方法**

在模型框架的指引下，需要从理论和概念层面设计完成可视分析任务所需的多个视图。
设计内容包括如何进行视觉编码（如采用颜色、大小、位置或纹理等映射数据特征），以及如何支持用户的交互（如刷选、过滤、多视图联动等）。
这一步通常会产出初步的可视化“草图”或“方案文档”，为后续的实现奠定基础。

**4. 实现可视化视图**

接下来，根据先前的设计方案，综合考虑前端技术栈（如 D3.js、WebGL、Canvas 等）和后端数据处理（如数据库、分布式计算框架、API 接口）来构建可视化视图原型。
这一过程需要充分考虑系统响应速度、可用性以及可扩展性等因素。通常会迭代实现并测试多个不同的可视化模块，确保其功能与视觉呈现方式均符合预期。

**5. 完成可视分析原型系统**

在实现了多个可视化视图后，需要使用交互技术（如联动刷选、多窗口同步、动态过滤、缩放漫游等）将各个视图融合成为一个可视分析原型系统。
此时系统应能初步满足既定的可视分析任务，并允许用户以较直观的方式进行探索和数据交互。若需要协同分析或跨平台应用，还需注意网络部署与权限管理等问题。

**6. 进行可视分析评测**

最后，对原型系统进行评价与测试，既包括对系统功能的完整性和可用性的评估，也包括对可视化效果、用户交互体验及分析深度的考量。
此步骤十分关键。如果离开了严谨的评测分析，可视分析系统的设计者将会很难验证系统的有效性和实用性{cite}`plaisant2004challenge`。
案例研究（Case Study）是最常见的一种评估手段，用户访谈（User Interview）和专家评估（Expert Review）和也常常作为辅助性的评估手段出现。
基于评测结果，可进一步迭代完善系统，优化其在实际应用中的效率与可靠性。


```{figure} fig/visualization-analytics-inform_model.png
:name: fig-visualization-analytics-inform_model
经典的信息可视化模型。{cite}`card1999readings`
```


## 可视分析案例


2018年，Wang等人在论文《Towards Easy Comparison of Local Businesses Using Online Reviews》中提出了一种名为E-Comp的可视分析系统{cite}`wang2018towards`，旨在帮助用户通过在线评论（如Yelp、TripAdvisor等平台的评分与文本评论）快速、直观地比较本地商家（如餐馆、酒店、理发店等）。其核心目标是解决传统平台中因评论数据量大、用户评分标准差异大、时间分散等问题导致的信息过载与低效比较问题。
下面将以Wang等人提出的可视分析系统为例，示范如何将可视分析流程应用于现实数据场景。

**提出可视分析任务**

目标：帮助用户快速找出候选商家（初步筛选）；帮助用户深度对比候选商家在具体指标（口味、价格、服务、环境等）和时间趋势方面的差异；弥补不同用户偏好带来的整体评分失真，提供可靠的对比（如使用共同顾客评分差异做更客观的度量）。

具体来说，作者一共提出了6项任务：
1. 支持筛选商户及快速概览（Quick overview for filtering potential candidates）；
2. 提供用户可信赖的商户比较（Reliable comparison between businesses）；
3. 用户评论时序分析（Temporal analysis of user reviews）；
4. 能够洞察重要特征的细节（Insightful details of important features）；
5. 按需探索详细评论（Detailed review exploration on demand）；
6. 直观的可视化设计（Intuitive visual designs）。

**构建可视分析模型**

- 数据源与预处理模块  
  - 来自 Yelp 的在线评论数据（包含：星级评分、评论文本、用户信息、时间戳、“有用”投票数等）。
  - 离线处理：提取“形容词-名词”词对、计算情感值、统计共同顾客的评分差异、归纳价格和评分分布等。

- 可视分析系统（E-Comp）整体结构
  - 数据读入与存储层：存放经过清洗和聚合的业务信息（商家 ID、地理位置、价格等级）、评论统计数据（评分分布、共同顾客关系）、以及文本分析结果（情感词对等）。
  - 分析处理层：
    - 通过算法识别共同顾客、构建 Sankey 图所需的数据；
    - 进行词云布局与分群；
    - 计算每条评论的帮助度 (综合字数、投票、评分极端度)；

- 可视化呈现层： 
  - 地图视图与图元（glyph）用于初步对比；
  - Sankey 图用于评分差异可视化；
  - 时间视图用于查看评论在时间维度的演变；
  - 增强词云视图用于深入对比商家在食物、服务等方面的好坏点。

**设计可视化方法**

{numref}`visualization-analytics-visual_figure`是 E-Comp 的用户界面。
可以看到图中有非常明显的 A、B、C 等字样的字母标记。这也是可视分析论文中常见的标记方法。
```{figure} fig/visualization-analytics-visual_figure.png
:name: visualization-analytics-visual_figure
经典的信息可视化模型。{cite}`card1999readings`
```
其中：
- （A）控制面板（Control Panel）：允许用户过滤数据从而改变其他视图； 
- （B）地图视图（Map View），使用扇形面积表示评论数量（人气），颜色表示好评/差评比例。在图元上叠加价格条、平均星级信息。通过连线粗细显示商家间共同顾客数量，以辅助初步筛选。
- （C）共同顾客比较视图（Common Customer Comparison View），将两个商家相同用户的评分直接相连，并在中间显示差异分组；使用颜色渐变或色标来表示评分高低，或两家在同一用户评分下的差值。
- （D）时序视图（Temporal view），采用堆叠或分层布局表现不同星级评论随时间的变化趋势；用矩形/圆形大小编码评论的“帮助度”，便于快速关注关键评论；鼠标悬停或点击可以在详情面板中查看完整评论文本。
- （E）增强词云视图（Augmented word cloud view），将“形容词-名词”词对聚类，对同一名词的各个形容词按频率排序，并用情感色彩展示；用分块或环形辐射的排布方式来保证高频词优先显示在中心区域，减少遮挡。
- （F）详细评论文本视图（Detailed Review Text View），用于显示在时序视图 (D) 中选中（红色虚线矩形）的评论的详细文本信息；
- （G）商户表（Business Table），列举出了所选地区的商户基本信息。

作者通过这种形式将各个区域划分为不同视图，视图之间可以交互联动，帮助读者更快地了解各个视图的功能。
在之前一些可视分析论文中，作者喜欢明确将视图划分为主视图（入口视图）和辅助视图。
近年来，这种趋势开始有所下降，视图之间的关系开始变得更加扁平。


**实现可视化视图**

- 系统原型使用Web 技术栈（如 D3.js、JavaScript、HTML + CSS）来开发：
- 在实现过程中，需解决图元重叠（通过碰撞检测或人工偏移）、词云排布（利用 Archimedean spiral 等布局算法）等技术细节，以确保可视化可读性。

**完成可视分析原型系统**

E-Comp 将上述视图集成到单页面（Single-Page Application）或 Web 界面中：
- 地图视图：初步筛选 + 点击选择两个待对比商家；
- 共同顾客评分对比视图：查看差异评分；
- 时间视图：察看评论随时间的变化、近几月或历年的趋势；
- 增强词云：多种特征（食物/环境/服务/价格）的好评、差评集群分布；
- 评论详情：对高帮助度评论进行原文查看。

用户交互 & 系统功能：
- 选区过滤：在地图上框选商家或调整侧边栏；
- 联动刷新：任何视图中的操作都会刷新其他视图；
- 帮助度排序：突出重要评论；
- 工具提示：悬停在图元或单词上查看数值信息；



**可视分析评测**

- **案例分析：**

在论文中展示了实地案例：一位用户想在 ASU 附近选餐厅，利用 E-Comp 从地图视图开始，首先导航到 ASU 周围的区域。在看了餐厅的总体分布之后，发现了一个餐厅聚集的区域。
使用「控制面板」过滤掉明显不符合要求的餐馆后，他发现 A 餐厅的评价很多（饼图的深蓝色区域），而且非常受欢迎。

然而，它的价格对这个用户来说有些贵。
不过，他很快注意到，有很多去过 A 餐厅的顾客也喜欢去 另外两家餐厅：Chuck Box 和 Original Chopshop。这两家的价格明显更便宜。同时，这两个餐厅也很受欢迎。 

随后他使用Sankey/时间视图/词云视图进行深度对比，发现虽然 Chuck Box 历史悠久、人气也大，但从共同用户的评分来看，ChopShop 获得更多中高星评价，并且在较短时间内吸引到大量顾客，口碑上升更明显。
综合价格、菜单特色（健康沙拉 vs. 经典汉堡）、用户好评度和最新一段时间的趋势，用户决定更倾向选择 ChopShop。

整个案例展示了可视分析方法如何在最初的“地图概要筛选”、中间的“共同评分对比”、以及“特征词云分析”中层层递进，帮助用户迅速洞察商家差异。

- **用户研究 & 访谈：**

研究人员让多位有真实选餐需求的用户试用 E-Comp，如“比较 Chuck Box 和 Original ChopShop”等；
对比实验：与传统平台（Yelp）对比，用户使用E-Comp的平均决策时间缩短40%，决策信心提升35%。
收集用户反馈：大多数用户认为相比传统的 Yelp 页面或纯文字评论检索，“E-Comp”更能在短时间内帮助他们深入对比评分相似、价格接近的餐厅差异。


- **改进方向：**

优化词云布局，减少视觉重叠；增加图片评论分析模块（如食物图片聚类）；支持移动端触控交互。


可视分析的魅力正源于人机交互与数据洞察的巧妙融合：人能够带着领域经验与创意，向数据提出多样化的问题；机器则借助强大的计算与可视化手段，为关于关联、模式和规律的探索提供高效率的支撑。
这种“人机协同”所形成的分析闭环，既能快速循环迭代，又能给分析者留出充足空间进行深度思考。
最终，可视分析不仅让复杂数据变得可触、可见，更帮助我们突破单纯的自动化计算，以更具创造力和灵活度的方式获得洞察，为决策与创新赋能。