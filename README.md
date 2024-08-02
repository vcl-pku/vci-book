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
- “可视计算入门”、“几何建模”、“渲染”、“动态生成”是四个 *Part*，分别对应于 `source/getting-started`、`source/geometry`、`source/rendering`、`source/animation` 目录。
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
2. 每个 *Chapter* 的目录名应在考虑 *Part* 目录名的基础上精炼、准确，如使用 `geometry/transformation` 而非 `geometry/geometric-transformation`，使用 `rendering/textures` 而非 `rendering/texture-mapping`。
3. 每个 *Chapter* 的最后一个 *Section* 必须为“本章小结”，对应于 `summary.md`，其中选择性包含“拓展阅读”、“开源与商业软件”、“总结与展望”、“习题”、“引用”、“参考文献”等内容。
4. 每个 *Section* 的 Markdown 文件名应与其名称对应，但略去 *Part* 和 *Chapter* 中已有的内容，必要时使用通行的英文缩写。如“基于点云的表面重建”对应于 `geometry/reconstruction/point-cloud.md`，“光滑粒子流体”对应于 `animation/fluids/sph.md` 等。
5. 各级标题的标签命名由小写字母、数字和短横线组成，不使用下划线。
6. 各级标题的标签命名应完整、准确，包含 `part_name` 和 `chap_name`，用短横线连接，方便索引，避免冲突。如 `chap-[part_name]-[chap_name]`、`sec-[part_name]-[chap_name]-[sec_name]`、`subsec-[part_name]-[chap_name]-[subsec_name]`。允许 `part_name`、`chap_name`、`sec_name` 或 `subsec_name` 本身包含短横线，无需省略或用别的符号代替。

### 中英文混排

无论是标题还是正文，请在中文（不含标点）与拉丁字母、希腊字母、公式、数字之间增加空格。使用标点符号的场合（包括公式末尾），请一律使用中文标点。例如：
> - 第一台电子计算机是发明于 1946 年的 ENIAC。
> - 计算机图形学的顶级会议包括 SIGGRAPH 和 SIGGRAPH Asia。

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

### 图片

请将各 *Chapter* 的图片文件存放于 `source/[part_name]/[chap_name]/fig` 目录下，并以 `[part_name]-[chap_name]-[fig_name].[extension]` 的格式命名以避免冲突（在编译时，所有的图片将被统一复制到相同的目录中）。

插入带标题图片的详细格式请参考 `MysT Parser` 的[官方文档](https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html#figures-images-with-captions)。Markdown 文件中常用的图片插入方式如下：
````markdown
```{figure} fig/fun-fish.png
:scale: 50 %
:name: fig-[part_name]-[chap_name]-[fig_name]

图片的标题（甚至可以是一段话）。
```
````
其中 `:scale:` 用以控制图片的缩放比例，可以用 `:width:` 或 `:height:` 替代。`:name:` 指定图片的标签，用以进行交叉引用。

#### 子图

子图是通过 `subfigure` 环境插入的，如下方例子所示：
`````markdown
````{subfigure} AB|CD|EF
:layout-sm: A|B|C|D|E|F
:gap: 8px
:subcaptions: below
:name: fig-animation-basics-physics_demo
:width: 100 %

```{image} fig/animation-basics-rigid_demo.png
:alt: 刚体模拟
```

```{image} fig/animation-basics-elastic_demo.png
:alt: 弹性体模拟
```

```{image} fig/animation-basics-thinshell_demo.png
:alt: 布料模拟
```

```{image} fig/animation-basics-fluid_demo.png
:alt: 烟雾模拟
```

```{image} fig/animation-basics-magnetic_demo.png
:alt: 磁流体模拟
```

```{image} fig/animation-basics-surfacetension_demo.png
:alt: 流体表面现象模拟
```

各种物理现象的模拟
````
`````
其中在 `{subfigure}` 后跟的字符串指定了子图的排布方式，字符串中的每一个大写字母对应于一张子图，同一个大写字母可以出现多次，表明对应的子图所覆盖的区域，`|` 代表换行符；`:layout-sm:` 为额外指定的针对小屏幕的排布方式，格式与 `{subfigure}` 后跟的字符串相同；`:gap:` 用于指定子图的间距；`:subcaptions:` 可以是 `below` 或 `above`，分别表示子图的标题在图片的下方或上方；`:name:` 指定整个图片的标签；`:width:` 指定整个图片的宽度，可以以像素为单位，也可以是百分比，当是百分比时表示的是整个图片的宽度占屏幕宽度的比例。更多参数的含义可见 [sphinx subfigures 文档](https://sphinx-subfigure.readthedocs.io/en/latest/)。

在参数之后跟有若干个嵌套的 `image` 环境，与 `figure` 环境类似，但其只能包含用于指定子图标题的 `:alt:` 参数，此外不能有任何多余信息。这也导致我们无法直接交叉引用一个子图，一个简单的解决办法是在子图标题前手动加入 `(a)`、`(b)`、`(c)` 等序号，并在交叉引用整张图片后手动打出相应的子图序号。

最后是整张图片的标题，与 `figure` 环境一样，也可以是任何使用 markdown 语法的一段话。

### 表格

插入带标题表格的详细格式请参考 `MysT Parser` 的[官方文档](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#table-with-captions)。Markdown 文件中常用的表格插入方式如下：
````markdown
```{table} 表格的标题
:widths: auto
:align: center
:name: tab-[part_name]-[chap_name]-[code_name]

| foo | bar |
| --- | --- |
| baz | bim |
```
````
其中 `:widths: auto` 指定表格的宽度为自动，`:align:` 标记表格的位置为居中。`:name:` 指定表格的标签，用以进行交叉引用。

### 代码块

插入带标题代码块的详细格式请参考 `MysT Parser` 的[官方文档](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html#adding-a-caption)。Markdown 文件中常用的代码块插入方式如下：
````markdown
```{code-block} python
:caption: 代码块的标题
:lineno-start: 1
:emphasize-lines: 2,3
:name: `code-[part_name]-[chap_name]-[code_name]`

a = 1
b = 2
c = 3
```
````
其中 `:lineno-start:` 启用行号并设置起始值，`:emphasize-lines:` 用以标记需要高亮的行（用逗号隔开）。`:name:` 指定代码块的标签，用以进行交叉引用。

### 交叉引用

图片、表格、代码块、章节均可进行交叉引用。其引用格式均为 `` {numref}`ref_name` ``，`ref_name` 可以是上述对象的标签名，在遵循本规范的前提下，也即 `chap-`、`sec-`、`fig-`、`tab-`、`code-` 开头的各类 `name`。

使用 `` {numref}`ref_name` `` 产生的引用链接会自动包含“图”、“表”等前缀，无需自行输入。但请注意依照中英文混排的要求，必要时在引用之后加入空格。

### 数学

插入数学的详细格式请参考 `MysT Parser` 的[官方文档](https://myst-parser.readthedocs.io/en/latest/syntax/math.html)。推荐使用 `$...$` 插入行内公式，使用下列方式插入行间公式：
```markdown
$$
(a + b)^2  &=  (a + b)(a + b) \\
           &=  a^2 + 2ab + b^2
$$ ([part_name]-[chap_name]-[eq_name])
```
无需使用 `aligned` 环境即可实现简单的对齐功能。末尾括号中的内容指定的是公式的标签。尽管公式标签可以省略，但请注意，只有有标签的公式才会被编号。因此一般而言建议对所有公式增加标签。

公式的标签是独立于前述图、表、章节、代码块的，因此无需增加 `eq-` 作为前缀，也不使用 `{numref}` 进行引用。直接使用 `` {eq}`ref_name` `` 即可。

此外，请使用 `\boldsymbol{}` 标记所有矢量与张量，使用 `\mathrm{}` 标记涉及英文字母的常量（如自然底数等）、数学运算（如取最大值或转置等），以及非表示变量的上下标（例如 `$E_{\mathrm{p}}` 表示势能）。

### 参考文献

参考文献条目位于 `source/[part_name]/[chap_name]/ref.bib` 中，条目语法与 BibTeX 相同，例如：

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
并使用 `` {cite}`Stam1999` `` 加以引用。请注意引用与中文（除标点符号外）之间应有空格隔开。

在每个 *Chapter* 最后的 *Section*（本章小结）中，应在末尾添加如下语句以产生参考文献列表：
````markdown
## 参考文献

```{bibliography} ref.bib
:filter: {"doc1", "doc2"} & docnames
```
````
其中 `:filter:` 语句中的 `doc1`、`doc2` 等请使用本 `Chapter` 的 `Markdown` 文件名替代（不含后缀名）。

### 定理环境

请参考 `sphinx-proof` 插件的[官方文档](https://sphinx-proof.readthedocs.io/en/latest/)，注意标签在命名时应遵循类似图表的规则。即 `thm-{part_name}-{sec_name}-{thm_name}`、`prf-{part_name}-{sec_name}-{prf_name}` 等。
证明、定理、公理、引理、定义、准则、评注、猜想、推论、算法、示例、性质、观察、命题、假设的前缀分别为 `prf-`、`thm-`、`axm-`、`lem-`、`def-`、`crt-`、`rmk-`、`conj-`、`cor-`、`alg-`、`exa-`、`prop-`、`obs-`、`prps-`、`asm-`。

请注意，`sphinx-proof` 插件尚不支持中文本地化，因此产生的引用文本仍为英文，请遵循中英文混排规则。

### 提示环境

请参考 `MysT Parser` 的[官方文档](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html)。可以实现彩色的提示块、折叠块、选项卡等功能。