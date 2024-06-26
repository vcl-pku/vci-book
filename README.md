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

### 名词和术语

### 文本

### 图表

### 数学

### 参考文献
