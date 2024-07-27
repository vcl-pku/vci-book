# 可视计算与交互概论 - 在线版

## 本地部署流程

本地部署在 Linux、Windows 上均测试通过，无操作系统要求。

### 环境配置

推荐在 `conda` 环境下配置本地部署所需的依赖项，其中 Python 版本须大于等于 3.10，`conda` 的安装请参考 [miniconda 官方网站](https://docs.anaconda.com/miniconda/)。安装完毕后，以 Python 3.10 为例，应在 `shell` 中依次执行下列语句：
```shell
conda create -n sphinx -y python=3.10
conda activate sphinx
```
随后将本仓库下载到本地，并安装相应依赖项：
```shell
git clone https://github.com/vcl-pku/vci-book.git
cd vci-book
pip install -r requirements.txt
pip install sphinx-autobuild
```

### 本地部署

在环境配置完成后，每当希望本地部署网站以进行预览时，可在本项目主目录 `vci-book` 下，通过 `shell` 依次执行下列语句：
```shell
conda activate sphinx
sphinx-autobuild source build/html
```
随后，网站内容将被部署到[本地](http://127.0.0.1:8000)，`sphinx-autobuild` 会自动检测对源码的修改，动态更新本地所部署的网站。

## 编纂格式与规范

### 章节结构

本书会显示在各级目录中的标题有 *Part*、*Chapter*、*Section*、*Subsection* 共四层结构，它们满足下列约束：
- “引言”是一个 *Chapter*，对应于 `source/introduction` 目录。
- “二维图形”、“几何建模”、“场景渲染”、“动态生成”是四个 *Part*，分别对应于 `source/getting-started`、`source/geometry`、`source/rendering`、`source/animation` 目录。
- “可视化与交互”是一个 *Part*，对应于 `source/visualization` 与 `source/interaction` 目录。
- 每个 *Part* 下有若干 *Chapter*，都对应于一个 `source/[part_name]/[chap_name]` 目录。
- `source/introduction` 或每个 `source/[part_name]/[chap_name]` 目录下都有若干个 Markdown 文件。
- 以 `index.md` 命名的 Markdown 文件应当包含每个 *Chapter* 的导入语和该 *Chapter* 的目录。
- 以 `[sec_name].md` 命名的 Markdown 文件都代表该 *Chapter* 的某个 *Section*，它们应在 `index.md` 的目录中加以链接。

典型的 `index.md` 内容如下：
`````markdown
(chap-rendering-basics)=
# 场景渲染基础

```{toctree}
:maxdepth: 2

rasterization
ray-tracing
summary
```
`````
其中，`(chap-rendering-basics)=` 用来向各级标题添加标签以便交叉引用，`rasterization`、`ray-tracing` 是该 *Chapter* 各 *Section* 的 Markdown 文件名（无需添加后缀名）。注意无论是 *Chapter* 还是 *Section*，最终显示在电子书目录中的名称都是其 Markdown 文件的一级标题。

此外，各个 *Chapter* 及 *Section* 以及它们对应的目录或文件名也须遵循一定的规范：
1. 每个 *Chapter* 的命名应完整、准确，如使用“几何变换”而非“变换”。
2. 每个 *Chapter* 的目录名应在考虑 *Part* 目录名的基础上精炼、准确，如使用 `geometry/transformation` 而非 `geometry/geometric-transformation`。
3. 每个 *Chapter* 的最后一个 *Section* 必须为“本章小结”，对应于 `summary.md`，总结、讨论、展望、本章引用信息、习题、参考文献等应位于此处。
4. 每个 *Section* 的 Markdown 文件名应与其名称对应，但略去 *Part* 和 *Chapter* 中已有的内容。必要时使用通行的英文缩写。如“基于点云的表面重建”对应于 `geometry/reconstruction/point-cloud.md`，“光滑粒子流体”对应于 `sph-method.md` 等。
5. 各级标题的标签命名由小写字母、数字和短横线组成，不使用下划线。
6. 各级标题的标签命名应完整、准确，包含 `part_name` 和 `chap_name`，方便索引，避免冲突。如 `chap-[part_name]-[chap_name]`、`sec-[part_name]-[chap_name]-[sec_name]`、`subsec-[part_name]-[chap_name]-[subsec_name]`。

### 术语和人名

对于不含人名的学术名词，应当使用中文，并在首次（不含各级标题，下同）出现时，括弧标注其英文形式，必要时可以逗号标注简写。注意标点符号均应使用中文模式（全角）。例如：
> - 幺正矩阵（unitary matrix），又译为酉矩阵。
> - 光滑粒子流体动力学（smoothed particle hydrodynamics，SPH）是图形学中经典的流体模拟方法。

对于人名的标注，分情况讨论：
1. 有汉字书写的姓名者（如中国大陆、港澳台、新马泰、朝韩、日本、越南等国公民及其海外族裔），应使用规范简体汉字标注，必要时可在首次出现时括弧标注西文。西文姓、名顺序应与中文相同，中间加逗号。
2. 已经成名的西方学者或其他名人，使用规范简体汉字标注，视翻译的通行性决定是否需要在首次出现时标注英文。
3. 其它西方人名，应尽量选用通行翻译的简体汉字标注，并在首次出现时标注英文。
4. 引用文献时的人名标注由命令自动产生，参见[后文](#参考文献)。

例如：
> - 汤川秀树（Yukawa Hideki）提出了一种用以描述粒子之间短程相互作用的势能模型。
> - 对于张量运算，常使用爱因斯坦求和标记。
> - 冯·诺依曼提出了经典的计算机模型。
> - 美国物理学家理查德·费恩曼（Richard Feynman）写过一本著名的讲义。
> - 尤斯·斯塔姆（Jos Stam）博士曾获得过三次奥斯卡技术奖。

对于含人名的学术名词，应当遵循前述规范，同时在标注英文时尽量整体标注，例如：
> - 牛顿第二定律（Newton's second law）
> - 麦克斯韦方程组（Maxwell's equations）
> - 柯西应力张量（Cauchy stress tensor）

除上述标注规范外，本书计划设立专门的术语及人名对照表。

### 图表

TODO: 添加图表的编写及引用格式。

### 数学

TODO: 添加数学公式的编写及引用格式。

### 参考文献

参考文献条目位于 `reference.bib` 中，条目语法与 BibTeX 相同，例如：

```bibtex
@inproceedings{Stam1999,
  author = {Stam, Jos},
  title = {Stable Fluids},
  year = {1999},
  publisher = {ACM Press/Addison-Wesley Publishing Co.},
  address = {USA},
  booktitle = {Proceedings of the 26th Annual Conference on Computer Graphics and Interactive Techniques},
  pages = {121--128},
  numpages = {8},
  series = {SIGGRAPH '99}
}
```

TODO: 添加参考文献的引用格式。

在每章最后的“本章小结”一节中，应在末尾添加如下语句以产生参考文献列表：

```markdown
## 参考文献

:bibliography:`../../reference.bib`
```
