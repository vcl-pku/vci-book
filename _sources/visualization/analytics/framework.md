# 可视分析框架与过程

**可视分析的一般框架**

尽管可视分析在不同领域有不同的表现形式，但其基本框架是相通的。一个典型的可视分析框架包括以下几个部分：
<!-- (如图X.1所示): -->
<!-- ![[图X.1 可视分析的一般框架]] -->

- 数据层

负责数据的存储、检索、预处理等，为上层分析提供数据支持。

- 分析层

负责数据的转换、集成、挖掘等，提取数据中有价值的信息和模式。该层主要依赖机器的计算能力，同时需要人的参与和引导。

- 可视层

负责将分析结果转化为直观的视觉表示，供用户观察和理解。该层需要综合考虑数据类型、分析任务、认知原则等，设计合理的视觉编码和布局。

- 交互层

负责解释用户的交互意图，并将其传递给其他层作出响应。一方面，用户通过交互操纵可视视图，调整分析参数；另一方面，系统根据交互生成新的可视视图，激发用户新的洞见。

- 用户层

强调用户的中心地位，用户的知识、经验、洞察力贯穿整个分析过程。用户凭借对数据的理解和对任务的把握，主动探索数据空间，发现新的问题和线索，不断迭代优化分析模型。

以上各层并非简单的线性关系，而是相互交织、循环反馈的。可视分析的本质是人机智能的协同，既发挥机器在数据处理和计算上的优势，又发挥人在知识经验和创新思维上的优势，两者相辅相成，最终达到放大认知(Augmenting Cognition)的目的。


**可视分析的一般过程**

可视分析是一个迭代、循环、渐进的过程。我们可以将其归纳为以下四个基本步骤：
<!-- (如图X.2所示): -->
<!-- ![[图X.2 可视分析的一般过程]] -->

- 数据准备

将原始、杂乱的数据集成到统一的数据空间，并进行清洗、变换等预处理，使其满足后续分析和可视化的需求。数据准备往往占据可视分析时间的大部分，但却是必不可少的基础工作。

- 初始可视化

利用各种视觉隐喻，将处理后的数据映射到可视化视图。初始可视化提供了对数据的第一印象，帮助用户迅速把握数据的整体分布、突出特征等，启发后续分析方向，也可作为后续分析的参照和对比基准。

- 交互探索

用户通过交互操作，如缩放、平移、筛选、链接等，深入探索可视化视图，发现其中的规律与异常。交互探索是可视分析的关键环节，其频繁的人机对话、迭代求精，使用户对数据的理解不断深入，洞见不断涌现。

- 分析建模

对交互探索中发现的特征、规律等进行提炼、抽象，形成数据分析模型。分析模型凝结了用户对数据的理解和认知，指导后续的机器计算和可视分析。同时，分析建模也常会提出新的问题和假设，引发新一轮的交互探索。

以上四步在实践中往往交叉进行，螺旋上升。整个过程并非机器主导，而是以用户为中心，用户的领域知识、分析意图始终引领着分析方向。因此，一套成功的可视分析解决方案，应该为用户营造一个自然流畅、启发探索、迭代优化的分析体验。