# 颜色显示

## 颜色显示原理

对于现在大多的显示设备，颜色显示的原理都是一样的：通过对红、绿、蓝三种颜色的色光混合出 RGB 颜色空间里的颜色，区别仅在于物理实现的方法不一样。比如对于 {numref}`chap-getting-started-basics-pixel-vector` 中介绍的 CRT 显示器而言，我们可以使用三个电子枪分别打在三种颜色的荧光点上，对应红绿蓝三种颜色的像素。液晶显示屏（liquid-crystal display，LCD）使用电压控制偏振光的偏转角度，从而控制白光透过偏振片的强弱，在经过红绿蓝三种颜色的滤光片之后混合出想要的颜色。有机发光二极管（organic light-emitting diode，OLED）屏幕则直接使用红绿蓝三种颜色的有机二极管发出对应颜色的光，并直接控制每种色光的强弱。这些不同的显色原理的区别主要体现在成本、色域、色深、明暗对比度、刷新率等方面。一般来说，OLED的显示效果最好，但成本也是最高的。

````{subfigure} ABC
:name: fig-started-color-display
:width: 100 %
:gap: 8px

```{image} fig/color-crt.png
:alt: CRT
:width: 95%
```

```{image} fig/lcd.jpg
:alt: LCD
:width: 100%
```

```{image} fig/oled.png
:alt: OLED
:width: 80%
```

彩色 CRT[^crt]，LCD[^lcd]，OLED[^oled] 屏幕的显色原理
````
[^crt]: [Wikipedia: Cathode-ray tube](https://en.wikipedia.org/wiki/Cathode-ray_tube)
[^lcd]: [Wikipedia: LCD RGB Subpixel](https://commons.wikimedia.org/wiki/Category:Liquid_crystal_displays#/media/File:LCD_RGB_subpixel.jpg)
[^oled]: [Wikipedia: TOLED Structure](https://commons.wikimedia.org/wiki/File:TOLED_Structure.png)

尽管 CRT 显示器已经淡出了历史，但是与我们下面介绍的伽马校正密切相关，这一概念对现代图形应用依然十分重要。

## 伽马校正

我们假设这样一个工作流程：拿数码相机拍摄一张照片，将其显示在屏幕上，然后比较屏幕上显示的照片和现实世界肉眼观察的效果。我们自然期待照片和现实世界是差不多的，然而如果我们没有考虑**伽马校正（gamma correction）**，最终的结果可能如{numref}`fig-started-color-gamma` 所示存在一些偏差：屏幕上的照片看起来暗部与亮部的对比更强烈，像是直接光照更强。

````{subfigure} AB
:name: fig-started-color-gamma
:width: 100 %
:gap: 8px

```{image} fig/gamma1.jpg
:width: 100%
```

```{image} fig/gamma45.jpg
:width: 100%
```

肉眼观察（左）的结果与屏幕显示结果（右）的区别[^gamma]
````
[^gamma]: [What and Why is Gamma Correction in Photo Images?](https://www.scantips.com/lights/gamma2.html)

这个问题主要出在早期的 CRT 显示器上。相机传感器产生的电信号与接收的光强是成正比的，因此保存下来的图像其实是正确反应了自然界的光照。但是当图像上的数值转化为 CRT 显示器的电压信号之后，最后显示屏的亮度 $I$ 与电压 $V$ 之间并不是线性关系，而是满足接近幂函数的关系：

$$
I \propto V^\gamma
$$ (eq-started-color-crt-gamma)

这里的 $\gamma$ 一般在 2.2 左右。在{numref}`fig-started-color-gamma-curve` 中我们绘制出了 $y=x^\gamma$ 这条曲线。可以发现，这条曲线会压低暗部，本来 $50\%$ 亮度的地方现在亮度只有 $21.8\%$，而最亮的部分和之前是一样的，所以我们才会在{numref}`fig-started-color-gamma` 中感觉显示出的明暗对比更为强烈。

```{figure} fig/gamma400.png
:name: fig-started-color-gamma-curve
:width: 50%

$\gamma=2.2$ 的 CRT 显示曲线和伽马校正曲线 [^gamma]
```

为了解决这个问题，我们需要在显示图片之前，先把图片的颜色做一次相反的变换，也就是对于图片的每个像素颜色 $c$ 做：

$$
c\rightarrow c^{1/\gamma}, \ 1/\gamma = 1/2.2 \approx 0.45
$$ (eq-started-color-crt-gamma-correction)

这样我们会先把图片变亮一些，然后显示出来就是正确的结果了。这样的过程就被称为伽马校正。尽管 CRT 显示器后面被逐渐淘汰了，后面的 LCD 显示器和 OLED 显示器也不再具有这样的亮度-电压性质，伽马校正的步骤已经被标准化在了数字图像处理的过程里，因此也就被沿用了下来。尽管不同的显示器硬件有不同的 $\gamma$ 值，我们上一节提到的 sRGB 颜色空间的在标准中直接规定 $\gamma=2.2$，各种显示器就需要模拟{numref}`fig-started-color-gamma-curve` 中的曲线来适配这个标准。因此，现在我们也经常将 sRGB 颜色空间称为伽马颜色空间，与之相对的就是线性颜色空间。

上面我们考虑的是从现实世界中拍照的情况，那如果是在虚拟世界中生成结果呢？比如我们后面需要学习的渲染部分{numref}`chap-rendering-basics`。由于渲染是在模拟现实世界的光照，因此使用线性颜色空间是最合适的。这就要求我们直到画面显示到屏幕的最后一刻，才开始做伽马校正。庆幸的是，很多图形 API 提供了这样的命令可以一键完成这个任务，比如 OpenGL[^opengl] 提供的`glEnable(GL_FRAMEBUFFER_SRGB)`命令（你现在应该也可以明白其中的`FRAMEBUFFER`和`SRGB`分别代表什么含义）。如果在渲染算法中使用了任何图片作为贴图或者背景，也要注意这些图片是在哪个颜色空间下的。如果我们直接使用了伽马颜色空间中的图片，就意味着这张图片已经进行了伽马校正，最后经过渲染的管线之后还会再做一次伽马校正，这就会导致问题。因此，渲染中使用的任何图片也应该保存在线性颜色空间中。
[^opengl]: [OpenGL](https://www.opengl.org/)
