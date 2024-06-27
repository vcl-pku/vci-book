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

在环境配置完成后，每当希望本地部署网站以进行预览时，可在本项目主目录 `vci-book` 下，通过 `shell` 依次执行下列语句：
```shell
conda activate d2l
./deploy.sh
```
随后网站将自动进行生成及本地部署。命令执行完毕后可通过 https://localhost:8000 访问网站内容。

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
````
`````
其中，`` :label:`chap_fluid-simulation` `` 用来添加标签以便交叉引用，`navier-stokes`、`sph-method`、`eulerian-method` 是该章各节的 Markdown 文件名（无需添加后缀名）。注意无论是章还是节，最终显示在电子书目录中的名称都是其 Markdown 文件的一级标题。

此外，Markdown 文件名及其对应小节的命名须遵循一定的规范：
1. 尽量使得每章各小节的名称具有独特性。例如，对于“流体模拟”一章的小节，使用“纳维—斯托克斯方程”而非“控制方程”，以避免与其它各章的控制方程混淆。
2. 小节的 Markdown 文件名应与其名称对应，必要时可以使用通行的英文简写。如“纳维—斯托克斯方程”对应于 `navier-stokes.md`，“光滑粒子流体”对应于 `sph-method.md` 等。类似地，小节的 Markdown 文件名也应具有独特性。

### 名词和术语

### 文本

### 图表

### 数学

### 参考文献
