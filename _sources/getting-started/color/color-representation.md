# 颜色的离散表示

## 色彩空间

回顾上一节的格拉斯曼定律，我们知道任意一种人眼可分辨的颜色可以用 $(R, G, B)$ 三原色坐标唯一表示，并且三原色坐标是可以进行加和运算的。通过这种方式，我们可以把颜色在三维空间中组织起来，构成一个**色彩模型（color model）**。如{numref}`fig-started-color-rgb-model` 所示，假设三原色坐标的分量都归一化到 $[0, 1]$ 之间，那么 RGB 色彩模型就可以用一个立方体来表示，取图中立方体面向我们的六个顶点的颜色，就可以得到右边大家更为熟悉的三原色混合关系。

````{subfigure} AB 
:name: fig-started-color-rgb-model
:width: 100 %

```{image} fig/color-cube.png
:alt: RGB
:width: 100%
```

```{image} fig/rgb-diagram.png
:alt: RGB
:width: 77%
```

RGB色彩模型[^color-cube]
````
[^color-cube]: [Wikipedia: RGB color model](https://en.wikipedia.org/wiki/RGB_color_model)

值得注意的是，尽管看起来我们已经给每个色彩在 RGB 色彩模型中找打了唯一的对应，但是这个“唯一”是需要打引号的，因为我们并没有规定作为基础的三原色，也就是 $(1, 0, 0)$，$(0, 1, 0)$，$(0, 0, 1)$ 这三个坐标对应的到底是哪种颜色。这三个颜色可能有细微的改变，使得它们最终等比例混合起来依然是白色，比如你可以想象我们把{numref}`fig-started-color-rgb-model` 中的立方体绕着 $(1, 1, 1)$ 这个对角线稍微旋转一个角度。这使得即使是相同的色彩模型，由于显示设备的不同，我们最终看到的颜色依然会有差异。设备无关、准确描述颜色的色彩模型称为**绝对色彩模型（absolute color model）**，比如由国际照明委员会在 1976 年定义的 CIELAB 色彩模型。为了保证 RGB 色彩模型显示的颜色能够准确还原色彩，每个显示器、扫描仪、相机、打印机等，都需要在出厂时进行色彩的校准。

由于我们最终需要使用离散的数字表示色彩模型，并且受到显示器硬件条件的限制，那么最终我们只能覆盖所有颜色的一个子集，称为**色域（gamut）**。色域与色彩模型一起构成**色彩空间（color space）**。比如最常用的是 RGB 色彩空间，除此之外根据使用目的和硬件设备的不同，常见的还有 HSV 色彩空间，CMYK 色彩空间等，我们在下面介绍它们的细节。

## RGB 色彩空间

RGB 色彩空间是最常用的色彩空间，因为它最接近人眼识别颜色的原理，并且契合现代显示器显示颜色的原理——红、绿、蓝三色二极管的组合。根据色域的不同，RGB 色彩空间又有不同的变体，比如 Adobe RGB，sRGB等，如{numref}`fig-started-color-gamut` 所示。其中 sRGB 是惠普公司和微软公司在 1996 年推出的标准，是现在互联网使用的标准颜色空间[^sRGB]，也是主流显示器支持的色彩空间。比如，在购买显示器时，我们往往会看到支持 99% sRGB 这样的描述。而 Adobe RGB 则拥有更广的色域，由 Adobe 公司在 1998 年推出，目的是尽可能在彩色印刷中支持更多的颜色，主要集中在青绿色系中[^ARGB]。

[^sRGB]: [Wikipedia: sRGB](https://en.wikipedia.org/wiki/SRGB)
[^ARGB]: [Wikipedia: Adobe RGB color space](https://en.wikipedia.org/wiki/Adobe_RGB_color_space)

```{figure} fig/gamut.png
:name: fig-started-color-gamut
:width: 50%

不同 RGB 色彩空间的色域，可视化 $R+G+B=1$ 的切面[^gamut]
```
[^gamut]: [Wikipedia: Color space](https://en.wikipedia.org/wiki/Color_space#Absolute_color_space)

除了色域的区别，由于我们最终需要对颜色进行离散化，还需要考虑 RGB 的每个通道需要用多少比特的数字来表达，称为**色深（color depth）**。更多的位数意味着可以表达更多的颜色，但储存和计算的开销也会变大。我们常见的 0-255 表达的 RGB 颜色，对应的就是 8 比特色深，或者 24 比特每像素（bit per pixel，bpp），也被称为真彩色。这 24 比特也可以表示为一串 16 进制的数字，写为 #rrggbb ，比如 #ff0000 表示的就是 $R=255$， $G=0$，$B=0$。

## HSL 和 HSV 色彩空间

HSL 和 HSV 都是将 RGB 色彩模型中的点表示在圆柱坐标系中的方法，目的是让人们能更直观地操作颜色。HSL 对应色相、饱和度、亮度（hue，saturation，lightness）。HSV 对应色相、饱和度、明度 （hue，saturation，value），也可以称为 HSB，其中 B 对应 brightness。HSL 和 HSV 的色彩模型如{numref}`fig-started-color-hsl-hsv` 所示。

```{figure} fig/hsl-hsv.png
:name: fig-started-color-hsl-hsv

HSL 与 HSV 的区别[^hsl-hsv]
```
[^hsl-hsv]: [Wikipedia: HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)

使用柱坐标最大的好处，在于符合人们对色彩的经验直觉：色相描述颜色属于“哪一类”，也就是赤橙黄绿青蓝紫的哪一种，对应柱坐标的角度参数；饱和度对应颜色的鲜艳程度，也就是颜色中白色占比的多少，对应柱坐标的半径参数；亮度、明度描述颜色的明亮程度，对应柱坐标的高度。因此，人们可以按顺序选择角度、半径、高度这三个参数来选择想要的颜色，这也是数字绘画软件中最常用的调色盘的模型。但同时，柱坐标是非线性的坐标，因此不满足像 RGB 坐标那样的颜色线性加法模型。

HSL 与 HSV 最大的不同，在于对于颜色亮与暗的处理。在 HSL 中，饱和度分量总是从完全饱和色到等价的灰色，而 HSV 则会过渡到纯白色。这同时涉及到人们对于“饱和度”这一概念的理解，在 HSL 中纯白色也可以是完全饱和的（{numref}`fig-started-color-hsl-hsv` 左边的圆柱顶部），这与一部分人的理解是相悖的。因此在实际应用中，HSL 和 HSV 都很常用。

HSL，HSV 可以与 RGB 之间相互转换，具体的转换公式比较复杂，读者可以参考链接[^hsl-hsv]。这里给出从 RGB 坐标 $(r, g, b)\in [0, 1]^3$ 计算色相 $h$ 的示例。我们令 $max$ 和 $min$ 是 $(r, g, b)$ 中的最大值和最小值，则对应色相为:

$$
h = \left\{ \begin{array}{ll}
  0^\circ, & \text{if } max = min \\
  60^\circ \times \frac{g-b}{max-min} + 0^\circ,& \text{if } max = r \text{ and } g\geq b \\
  60^\circ \times \frac{g-b}{max-min} + 360^\circ,& \text{if } max = r \text{ and } g < b \\
  60^\circ \times \frac{b-r}{max-min} + 120^\circ,& \text{if } max = g \\
  60^\circ \times \frac{r-g}{max-min} + 240^\circ,& \text{if } max = b \\
\end{array} \right.
$$ (eq-started-color-hue)

可以通过公式发现，$h\in [0, 360^\circ)$ 对应圆柱的周角，红、绿、蓝均匀分布在圆周上，并等分圆周。

## CMYK 色彩空间

CMYK 色彩空间主要服务于印刷行业，称为**印刷四分色空间**。C、M、Y、K 分别对应四种打印色料：青色（cyan）、洋红色（magenta）、黄色（yellow）、黑色（key plate，或者 black）。与 RGB 颜色模型不同，CMYK 色彩模型的混色方式正好相反，C、M、Y 三种颜色的混合接近黑色而不是白色。这是因为对于印刷品而言，其显示的颜色对应其吸收颜色的补色。比如红色颜料是因为其本身会吸收主要的蓝色、绿色光，导致其反射自然光之后为红色。由于印刷品和显示屏显色原理上的根本不同，很难做到印刷出来的颜色与显示屏显示的颜色一致。

```{figure} fig/cmyk.png
:name: fig-started-color-cmyk
:width: 40%

比较接近实际 CMY 叠色的示意图[^cmyk]
```
[^cmyk]: [Wikipedia: CMYK color model](https://en.wikipedia.org/wiki/CMYK_color_model)

CMYK 与 RGB 之间也存在转换关系，由下面的公式给出：

$$
\begin{aligned}
  R &= (1 - C)(1 - K) \\
  G &= (1 - M)(1 - K) \\
  B &= (1 - Y)(1 - K)
\end{aligned}
$$ (eq-started-color-CMYK2RGB)

$$
\begin{aligned}
  C &= 1 - \frac{R}{\max (R, G, B)}\\
  M &= 1 - \frac{G}{\max (R, G, B)}\\
  Y &= 1 - \frac{B}{\max (R, G, B)}\\
  K &= 1 - \max (R, G, B)
\end{aligned}
$$ (eq-started-color-RGB2CMYK)