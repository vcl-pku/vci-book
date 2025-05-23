(chap-getting-started-basics-pixel-vector)=
# 像素与矢量

如果我们将 **显示（display）** 的问题用数学的语言表达出来，我们可以在矩形的屏幕上建立一个直角坐标系，然后说“请在点 $(x_1, y_1)$ 和点 $(x_2, y_2)$ 之间画一条直线”，“请以点 $(x, y)$ 为圆心画一个半径为 $r$ 的圆”之类的话。问题在于，显示的硬件设备应该如何执行这样的描述呢？

## 矢量显示

在早期的显示设备中[^history]，我们其实是在物理层面上实现了上面的数学描述。以{numref}`fig-started-basic-crt` 中当时最常见的阴极射线管（cathode-ray tube，CRT）显示设备为例，后端发射的电子束在经过磁场的偏折后打到涂有荧光层的屏幕上时，就会在屏幕上显示为一个亮点。控制磁场的方向和强度，我们就能控制电子束偏折的角度，从而控制亮点在屏幕上的位置。因此，我们可以控制亮点按照给定的轨迹进行快速移动，在视觉上看来就绘制出我们想要的图形了。这样的显示方式我们称之为**矢量显示（vector display）**。
[^history]:[Wikipedia: History of display technology](https://en.wikipedia.org/wiki/History_of_display_technology)

````{subfigure} AB 
:name: fig-started-basic-crt
:width: 100 %

```{image} fig/crt2.jpg
:alt: CRT
```

```{image} fig/crt.png
:alt: CRT
```

阴极射线管显示器及其原理图[^crt]
````
[^crt]:[Wikipedia: Cathode-ray tube](https://en.wikipedia.org/wiki/Cathode-ray_tube)


尽管矢量显示在早期的显示设备中被广泛使用，其最大的问题在于绘制图形的复杂度非常受限。可以想象，如果我们想要绘制非常复杂的图形，我们需要给出每一段直线、曲线的数学描述，然后控制控制电子束的移动来绘制图形，这往往需要比较长的时间进行绘制。“给绘制的几何体内部填充颜色”这样一个看似简单的任务实现起来也并不直接。此外，控制显示的颜色也是一个难题。因此，矢量显示设备最终就被慢慢淘汰掉了，只有在特定的医疗、工业、军事领域发挥作用。

```{figure} fig/Oscilloscope_clock.jpg
:name: fig-started-basic-crt-clock
:width: 70%

阴极射线管示波器显示的时钟[^crt-clock]
```
[^crt-clock]:[Wikipedia: Vector monitor](https://en.wikipedia.org/wiki/Vector_monitor)


## 像素显示

**像素显示（vector display）** 的基本思想，是将屏幕空间划分为一个个离散的像素，每个像素都有独立的开关，我们通过控制每个像素的开关来显示图形。在这种方式下，不管我们显示的图形简单或者复杂，我们都需要决定所有像素的开关与颜色，显示的开销是不变的。因此，像素显示相比于矢量显示更善于处理复杂的图形，因此也成为了当下主流的显示方式。

````{subfigure} AB 
:name: fig-pixel
:width: 70 %
:gap: 8px

```{image} fig/raster_representation.png
:alt: Rasterization
```

```{image} fig/vector_representation.png
:alt: Vector
```
左：像素显示示意图；右：矢量显示示意图
````

像素显示的思想可以被实现到不同的硬件中。对于上面提到的 CRT 显示器，我们可以通过逐行扫描的方式，将其改造为像素显示。具体来说，电子束不再是追踪每一个图形笔画，而是逐行扫描覆盖整个屏幕，整个图像被编码到了扫描过程中电子束的强度变化之中。更进一步，CRT 显示器可以使用隔行扫描的技术：如{numref}`fig-started-basic-crt-monitor` 所示那样，电子束一次只扫描奇数行上的像素点，一次只扫描偶数行上的像素点，这样交替更新画面。相比于每次扫描整个画面，这样做每次只需要更新屏幕上的一半像素，因此可以提高屏幕的刷新频率，同时奇偶交替更新避免了整个屏幕的撕裂。早年带有“大屁股”的电视、电脑显示器使用的都是这个原理。而之后出现的液晶显示器等都不再使用电子束轰击屏幕荧光层的方式发光，而是使用发光二极管作为光源，通过在屏幕上规律排布很多个发光控制元件来模拟像素，因此可以做得更薄。屏幕上能显示的像素个数称为屏幕的**分辨率（resolution）**，或者称为**解析度**。常见的分辨率类型有：720p（1280 x 720），1080p（1920 x 1080），4K（3840 x 2160）等。


````{subfigure} AB 
:name: fig-started-basic-crt-monitor
:width: 80 %
:gap: 8px

```{image} fig/CRT_image_creation_animation.png
:alt: CRT
```

```{image} fig/crt-monitor.jpg
:alt: CRT
```
左：使用隔行扫描的 CRT 显示器原理示意图；右：Trinitron CRT 显示器[^crt]
````

当然，像素显示方法也不是完美的。其最大的问题在于我们使用离散的像素近似了本来应该连续的图形，这使得最终显示的质量受制于像素的密度，并且在放大图片时不可避免会出现锯齿的现象。简单使用更多的像素可以缓解锯齿问题，但将不可避免地增大计算和储存的开销。我们在后面的反走样章节 {numref}`chap-getting-started-anti-aliasing` 中将会深入讨论如何解决锯齿的问题。

## 矢量 VS 像素

我们可以看到，矢量显示和像素显示是完全不同的两条路径，对图形的表示、计算、显示有着完全不同的要求。并且，两种方法都有各自的问题，没有完美的解决方案。因此，尽管现在像素显示是绝对的主流，但是矢量图形的表示和算法依然发挥着巨大作用。对于很多图形工作者而言，在像素显示器上处理矢量表示的图形是非常常见的工作流程。就本书而言，我们后面学习的主要内容将在像素的框架下进行，而仅将矢量图形的部分作为补充。