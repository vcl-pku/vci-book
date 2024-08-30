# 颜色感知与心理

在实际中，人眼所感知到的颜色可能还会受到心理因素的影响，使得我们最终感受到的颜色并不是实际显示的颜色，产生一些有趣的效应。而这些颜色感知的心理现象也会被用到可视化领域中，用于突出传达某些信息。我们下面举出一些例子。

## 色彩立体效应

````{subfigure} AB 
:name: fig-started-color-chromostereopsis
:width: 100 %

```{image} fig/blue-red.png
:width: 100%
```

```{image} fig/stained-glass.jpg
:width: 56%
```

色彩立体效应[^chromostereopsis]
````
[^chromostereopsis]: [Wikipedia: Chromostereopsis](https://en.wikipedia.org/wiki/Chromostereopsis)

观察上面的{numref}`fig-started-color-chromostereopsis`，你是否觉得画面中的红色和蓝色处在不同的深度？红色的部分感觉突出画面，而蓝色在背景里，或者正好相反。这种现象称为**色彩立体效应（chromostereopsis）**。当光线通过角膜时，会发生轻微衍射．眼睛通常能够将黄色波长的光（598nm）调到最清晰的焦点，从而使得波长较长的红色光波会聚在视网膜后面．波长较短的绿色和蓝色光波会聚在视网膜前面．因此，人眼产生了一种视觉假象，即长波长的光会被认为比波长短的光来自更近的地方，也有些人会产生相反的感觉。因此我们可以只从颜色感知出不同的深度，可以被用来突出画面中的某些内容。

## 颜色恒常特性


````{subfigure} AB 
:name: fig-started-color-checker
:width: 100 %

```{image} fig/checker.png
:width: 100%
```

```{image} fig/checker2.png
:width: 100%
```

棋盘阴影错觉[^checker]
````
[^checker]: [Wikipedia: Checker shadow illusion](https://en.wikipedia.org/wiki/Checker_shadow_illusion)

{numref}`fig-started-color-checker` 中展示了经典的棋盘阴影错觉：在左边的图中，A 和 B 看起来的颜色并不相同，A 要更深一些，但是从右边的图可以看出，二者在图片中的灰度其实是一样的。这一现象反应了视觉的**颜色恒常特性（color constancy）**：我们能够在不同的照明条件下保持对颜色的感知较为恒定的能力。人类视觉的这种特性有助于我们在复杂光照条件下对物体的识别，因此也是计算机视觉（computer vision）算法追求的目标。从图片中的颜色将环境光照与物体本来的颜色分离开，这样的算法称为视网膜算法（retinex algorithm）。

## 色诱导

````{subfigure} A|B 
:name: fig-started-color-induction
:width: 100%

```{image} fig/induction-1.jpg
:width: 100%
```

```{image} fig/induction-2.png
:width: 74%
```

色诱导[^induction]
````
[^induction]: [一条裙子背后的颜色故事](https://www.nim.ac.cn/node/259)

**色诱导（color induction）** 是与颜色恒常特性密切相关的心理现象。如{numref}`fig-started-color-induction` 所示，黄色和蓝色背景中的魔方感觉上颜色是一样的，但是当我们把左边的蓝色色块与右边的黄色色块连起来时，你会发现二者其实都是一样的灰色。这是因为颜色恒常特性的存在，人们在感知颜色时会自动在脑中扣除环境光的影响，因此在黄色环境中灰色会被识别为补色蓝色，而蓝色背景中灰色就会被识别为补色黄色。因此，环境光在很大程度上会影响人们对于颜色的判断。

关于颜色恒常特性和色诱导所引发的现象，在2015年的互联网上还存在一个有意思的争论[^induction]：{numref}`fig-started-color-dress` 是白金色还是黑蓝色？

```{figure} fig/dress.jpg
:name: fig-started-color-dress
:width: 40%

这条裙子是白金还是黑蓝？[^induction]
```

## 颜色感知缺陷

**色盲（color blindness）**，或者**色觉辨认障碍（color vision deficiency，CVD）** 是指能看见及辨别颜色的能力低于常人的状况。它并不是一种心理现象，最常见的原因是视锥细胞缺陷。当眼睛中只有一种或者没有视锥细胞时，便会造成全色盲（Monochromatism），即只能感知明暗以及不同程度的灰色。当眼睛中只有两种视锥细胞时，会造成三种主要的双色视觉：患有红色盲
（Protanopia）的人无法看到红色光，患有绿色盲（Deuteranopia）的人无法看到绿色光，患有黄蓝色盲（Tritanopia）的人无法看到蓝色光。此外，也有一些人的眼睛尽管有三种视锥细胞，但是其看到的颜色和正常的人眼不一样。由于色盲很难被治愈，在游戏、软件开发时也应该尽量照顾到色盲人群，避免完全用彩色传达最重要的信息，提供相应的无障碍模式。