# 数据
<!-- :label:`visualization-data` -->

数据可视化的处理对象是各种类型的数据。
数据是可视化的原材料，深入理解数据的特点与结构是实现有效可视化的基础。
本节将从数据的定义与分类、数据的获取与预处理、数据可视化的挑战三个方面，系统地阐述可视化中的数据基础知识。

## 什么是数据

数据是对客观事物的性质、状态以及相互关系的记录。
它是信息的载体，也是可视化的对象。广义上,数据可以使用 "6W" 模型来描述，即 What(数据是什么)、When(数据的时间属性)、Where(数据的空间属性)、Who(数据的对象)、Why(数据产生的原因)、How(数据产生的方式)。
这些属性构成了对数据多方面特性的描述。

按照数据的结构化程度，可以将数据分为结构化数据、半结构化数据和非结构化数据三大类：

**1. 结构化数据（Structured Data）：**
结构化数据具有固定的格式和预定义的数据模型，通常以表格的形式存储在关系型数据库中。每个数据项都有明确的字段和数据类型，不同数据项之间的关系也有明确定义。结构化数据的特点是高度组织化，易于查询、分析和处理。
常见的结构化数据包括：
- 关系型数据库中的数据表，如 MySQL、Oracle、SQL Server 等。 
- 电子表格中的数据，如 Excel、CSV 文件等。 
- 具有固定格式的日志文件，如 Web 服务器日志、应用程序日志等。

**2. 半结构化数据（Semi-structured Data）：**
半结构化数据介于完全结构化和非结构化之间，具有一定的结构和组织，但不如结构化数据严格。半结构化数据通常以树形结构或图形结构来表示，数据项之间的关系相对松散。常见的半结构化数据格式包括 XML、JSON 等。
常见的半结构化数据包括：
- XML 文档，如 Web 服务的响应、配置文件等。
- JSON 数据，如 Web API 的响应、NoSQL 数据库（如 MongoDB）中的文档等。
- 电子邮件，包含结构化的头部信息和非结构化的正文内容。
- HTML 文档，包含结构化的标签和非结构化的文本内容。

**3. 非结构化数据（Unstructured Data）：**
非结构化数据没有预定义的数据模型或组织结构，通常以自由格式存储。非结构化数据的特点是多样性和不可预测性，难以用传统的数据库技术直接处理和分析。非结构化数据占据了当今数据的绝大部分。
常见的非结构化数据包括：
- 文本文档，如 Word 文档、PDF 文件、电子邮件正文等。
- 图像和图形文件，如 JPEG、PNG、BMP 等。
- 音频和视频文件，如 MP3、WAV、MP4、AVI 等。
- 社交媒体数据，如推文、帖子、评论等。
- 传感器数据，如物联网设备采集的原始数据。

随着大数据技术的发展，处理非结构化数据的能力也在不断提高，如使用自然语言处理、计算机视觉等技术从非结构化数据中提取结构化信息。
在进行数据分析和可视化时，需要根据数据的结构化程度选择合适的工具和方法。对于结构化数据，可以使用传统的数据库查询语言（如 SQL）和商业智能工具进行分析和可视化。对于半结构化数据，可以使用特定的查询语言（如 XQuery、JSONiq）和文档数据库进行处理。对于非结构化数据，通常需要先进行预处理和特征提取，再应用机器学习、数据挖掘等技术进行分析和可视化。


从数据类型的角度看，可以将数据分为以下几类：
- 数值型数据：用数字表示的定量数据，包括连续型数据(如长度、温度)和离散型数据(如编号、类别标签)。
- 文本型数据：用自然语言表达的非结构化数据，如新闻报道、用户评论等。
- 图形图像数据：用像素阵列表示的视觉数据，如照片、医学影像、遥感影像等。
- 时空数据：包含时间或空间属性的数据，如轨迹数据、卫星遥感数据等。
- 关系型数据：描述实体之间关联的数据，如社交网络、知识图谱等。

不同类型的数据具有不同的特点，在可视化时需要采取不同的处理与映射方式。
如数值型数据通常可以直接映射到视觉变量如位置、颜色等；文本数据则需要提取关键词、主题等结构化信息才能进行可视化；图像数据可以直接呈现，也可以提取特征进行可视分析；时空数据需要考虑时间和空间尺度、参考系等因素；关系数据的可视化需要合理布局实体和连接。

除了数据类型，在考虑可视化设计时还需要关注数据的以下特征：
- 数据规模：数据量的大小，海量数据对可视化系统的渲染与交互提出更高要求。
- 数据维度：数据包含的属性个数，高维数据给可视化带来表达与感知的挑战。
- 数据分布：数据在各个取值范围内的分布密度，不同分布特征可能蕴含不同的模式。
- 数据质量：数据中噪声、缺失、异常等问题的严重程度，低质量数据可能需要额外的清洗与修复。
- 数据语义：数据所包含的专业、业务语义，可视化的设计需要考虑具体的数据分析任务。


## 数据获取与处理


数据预处理：在创建可视化之前，为了使可视化更有意义和有效，通常需要对数据进行预处理．这些步骤有助于确保可视化结果的准确性、清晰度和可解释性．以下是可视化数据预处理的一些关键方面：
- 数据清洗：删除或修复数据中的错误、异常值或不一致性，以确保可视化结果不会受到数据质量问题的干扰．
- 缺失值处理：如果数据中存在缺失值，需要考虑如何在可视化中处理它们，例如填充缺失值、忽略包含缺失值的数据点或提供额外的信息来表示缺失值．
- 数据转换：根据可视化的需求，可能需要对数据进行转换，例如进行对数变换、标准化或归一化，以使数据更适合可视化．
- 数据筛选：选择与可视化目标相关的数据子集，以减小数据量并聚焦于关键信息．
- 数据聚合：在可视化中使用汇总数据或聚合数据以提供更高层次的概览和趋势．
- 数据标签：确保可视化中的数据点或元素都具有适当的标签，以帮助观众理解图表中的信息．
- 数据排序：对数据进行排序，以突出重要的趋势或模式．
- 数据标尺和单位：确保可视化中的轴标尺和单位是清晰的，以帮助观众理解数据的刻度和度量．
- 数据注释：为了提供更多的上下文和解释，可以在可视化中添加文字注释或标记．


## 数据科学的挑战

大数据为可视化带来的问题：
高维数据可视化，复杂、异构数据可视化，针对海量数据的实时交互设计，分布式协同可视化，以及针对大数据的可视分析流程等。
