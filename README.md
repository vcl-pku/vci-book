# 可视计算与交互概论 - 在线版

## 本地部署流程

注意：本地部署暂时只支持 Linux 内核的系统（含 Windows Subsystem Linux），使用 Windows 系统会在最后一步出现兼容性问题。

### 环境配置

推荐在 `conda` 环境下配置本地部署所需的依赖项，其中 Python 版本须大于等于 3.9，`conda` 的安装请参考 [miniconda 官方网站](https://docs.anaconda.com/miniconda/)。安装完毕后，以 Python 3.9 为例，应在 `shell` 中依次执行下列语句：
```shell
conda create -n d2l -y python=3.9
conda config --append channels conda-forge
conda activate d2l
conda install -y pandoc==2.17
python3 -m pip install ghp-import bs4
git clone https://github.com/d2l-ai/d2l-book.git
cd d2l-book
python3 -m pip install .
```
上述过程可以在任意目录下完成，例如个人主目录 `~`。环境配置过程只需完成一次。

### 本地部署

将本仓库下载到本地：
```shell
git clone https://github.com/vcl-pku/vci-book.git
```

在环境配置完成后，每当希望本地部署网站以进行预览时，可在本项目主目录 `vci-book` 下，通过 `shell` 依次执行下列语句：
```shell
conda activate d2l
./deploy.sh
```
随后网站将自动进行生成及本地部署。命令执行完毕后可通过 http://localhost:8000 访问网站内容。

## 编纂格式与规范

### 章节结构

本书每一章均对应于若干个 Markdown 文件，这些文件被统一组织在 `doc/[chap_name]` 目录下。每个章节的文件夹中均有 `index.md`，该文件应当包含每一章的导入语以及该章所对应的各节目录。除 `index.md` 外，其余各个 `[sec_name].md` 文件对应于该章的每一节，并应当在 `index.md` 的目录中加以链接。

典型的 `index.md` 内容如下：
`````markdown
# 流体模拟
:label:`chap_fluid-simulation`

````toc
:maxdepth: 2

navier-stokes
sph-method
eulerian-fluid
summary
````
`````
其中，`` :label:`chap_fluid-simulation` `` 用来添加标签以便交叉引用，`navier-stokes`、`sph-method`、`eulerian-method` 是该章各节的 Markdown 文件名（无需添加后缀名）。注意无论是章还是节，最终显示在电子书目录中的名称都是其 Markdown 文件的一级标题。

此外，Markdown 文件名及其对应小节的命名须遵循一定的规范：
1. 每章最后（除引言外）一节为“本章小结”，对应于 `summary.md`，总结、讨论、展望、习题、参考文献等应位于此处。
2. 尽量使得每章各小节（除“本章小结”外）的名称具有独特性。例如，对于“流体模拟”一章的小节，使用“纳维—斯托克斯方程”而非“控制方程”，以避免与其它各章的控制方程混淆。
3. 小节的 Markdown 文件名（除 `summary.md` 外）应与其名称对应，必要时可以使用通行的英文简写。如“纳维—斯托克斯方程”对应于 `navier-stokes.md`，“光滑粒子流体”对应于 `sph-method.md` 等。类似地，小节的 Markdown 文件名也应具有独特性。

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

### Markdown 语法扩展

本项目基于 d2lbook 框架，该框架对 Markdown 的语法进行了大量的扩展，例如：

1. 图像、表格的标题与序号，公式及序号，章节序号；
2. 图像、表格、公式、章节的交叉引用；
3. 引用 `.bib` 文件中的参考文献；
4. 插入 `.svg` 格式的矢量图片。

有关上述扩展的具体语法格式，请参考[官方文档](https://book.d2l.ai/user/markdown.html)。

### 图表

### 数学

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

随后可以使用 `` :cite:`Stam1999` `` 或 `` :citet:`Stam1999` `` 来引用该文献，它们分别等同于 LaTeX 中的 `\citep{Stam1999}` 和 `citet{Stam1999}`。

在每章最后的“本章小结”一节中，应在末尾添加如下语句以产生参考文献列表：

```markdown
## 参考文献

:bibliography:`../../reference.bib`
```
