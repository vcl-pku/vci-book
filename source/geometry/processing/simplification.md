(sec-geometry-processing-simplification)=
# 网格简化

在游戏、科学可视化等计算机图形学的应用中，渲染效率与渲染质量是要兼顾的。当前大部分的计算机性能还不不能以较快的速度渲染海量三角形。经过精心制作的模型，或者 3D 扫描仪扫描并重构得到的模型一般都有几十万、几百万甚至更多的三角形，
但不是所有时候都需要用最高精度的模型。例如，同样的模型处在远处时，所占屏幕像素数会比较小，必然无法看法，这时候再渲染超多顶点的高精度的模型就会浪费计算性能。这时候如果在远处的能用更低精度的模型渲染，那么在不太影响渲染质量的情况下可以提高效率。这就需要用网格简化算法来生成不同细节层次（Level of Detail，LoD）的模型，于是可以在不同情况下选择不同细节层次的模型来渲染。

```{figure} fig/simple_teaser.png
:name: fig-geometry-processing-simple_teaser
:width: 70%

网格简化。将初始形状（左上）简化到 $25\%$（右上）、$6\%$（左下）以及 $1.5\%$（右下）。
```

网格简化（mesh simplification）的目标是用更少的面片数来表达原有模型，降低模型精度的同时保持模型的整体形状。
网格简化分为静态简化和动态简化两类。静态简化预先计算好一系列不同简化率的模型，在实时运行的程序中可以按照模型离视点(view point)的距离选择不同版本的模型进行渲染。动态简化是静态简化的延伸，在运行过程中按照需要对模型进行简化，一般使用局部的几何变换来实现，从而生成具有连续的具有不同分辨率的近似模型。

简化网格一般可以通过移除顶点或坍缩边来进行，相对来说边坍缩（edge collapsing）算法是更为简单而常用的，它通过删除网格中的边来实现简化的效果，如 {numref}`fig-geometry-processing-collapse` 所示。这类算法的核心是设计一种方法来选出需要被删除的边，并将这条边两端顶点合并成一个点放置在新的位置上。根据不同原则设计出的不同方法直接关系到简化后的模型的质量，不良的处理方法甚至会导致网格模型出现拓扑上的错误。

```{figure} fig/collapse.png
:name: fig-geometry-processing-collapse
:width: 60%

边坍缩算法。
```

为了衡量坍缩某条边对模型造成的影响，我们需要引入一种误差度量的方式，一种最常用的方式是二次误差度量（quadratic error {cite}`Garland1997`）。在删除一条边后，我们需要引入一个新的顶点，通过最小化新的顶点与之前对应的平面的 L2 距离，我们可以得到删除这条边会引入的二次度量误差，于是我们可以选取引入二次度量误差最小的边进行坍缩。而另一方面，使得这条边二次度量误差最小化的顶点，也将被设置为边坍缩后的新顶点，如 {numref}`fig-geometry-processing-quad-metrics` 所示，这种设置方式优于取边中点或局部区域平均，可以更好地保留模型的几何特征。利用这种贪心的思想，通过不断的迭代坍缩，我们就能实现对网格的简化。

```{figure} fig/quad-metrics.png
:name: fig-geometry-processing-quad-metrics
:width: 70%

根据局部邻域平均或根据取最小化二次误差度量来设置新的顶点，黑色代表原网格，蓝色代表经过了边坍缩之后的网格。
```

网格简化是一个复杂的问题，涉及到多种多样的度量方案和评判准则，目前每年仍有很多关于网格简化的文章发表，以期达到普适、高效、鲁棒、简化率高、可交互等目标，或在各目标中寻求平衡。有些研究者将神经网络运用到网格简化中，同样取得了不错的效果，这里我们不再对这个课题更加深入，感兴趣的同学可以自行搜索文献阅读。
