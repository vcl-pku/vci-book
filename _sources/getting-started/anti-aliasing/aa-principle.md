# 反走样

## 反走样基本原理

走样发生的原因在于采样频率不足，不满足奈奎斯特-香农采样定理的要求：$f_s > 2f_0$。自然，反走样的精髓就在于提高采样频率。下面我们介绍现在常用的反走样方法[^aa]。如{numref}`fig-started-aa-genshin` 所示，你可以在很多游戏中找到这些算法的选项。

[^aa]: [Anti-Aliasing in Gaming: The Battle for Perfect Graphics](https://vokigames.com/anti-aliasing-in-gaming-the-battle-for-perfect-graphics/)

```{figure} fig/genshin-aa.png
:name: fig-started-aa-genshin
:width: 100%

《原神》[^genshin]（5.0版本）中可选的反走样算法
```

[^genshin]: [《原神》官网](https://ys.mihoyo.com/)

## SSAA

SSAA 全称是**超采样反走样（super sample anti aliasing，SSAA）**，顾名思义，其核心是对像素进行超采样。本来我们只需要在每个像素的中心点计算一个颜色，超采样就是在像素内部的不同位置计算多次颜色然后取平均值。因为采样频率增加了，光栅化过程中的走样就减轻了。最后再降采样到屏幕上时，我们只进行了低通滤波，抹去了高频细节，因此不会产生额外的走样。SSAA 最简单的实现是先光栅化到一个 2 倍，4 倍分辨率的帧缓存，然后再计算屏幕上每个像素的平均颜色。除此之外，还有如{numref}`fig-started-aa-ssaa` 所示的各种超采样方式。比如 $2\times 2$ grid 和 $2\times 2$ RGSS 都是每个像素用了 4 个采样点，但是排布不一样，结果是在这个例子中 $2\times 2$ RGSS 的效果更好一些。

```{figure} fig/ssaa.png
:name: fig-started-aa-ssaa
:width: 60%

SSAA 不同采样模式结果图 from Real-Time Rendering, 3rd Edition, A K Peters 2008
```

SSAA 是反走样效果最好的算法，但是开销也是最大的，因为本质上我们是先将图形光栅化到了一个分辨率更高的屏幕上。

## MSAA

MSAA 全称是**多重采样反走样（multi sample anti aliasing，MSAA）**，可以看成是轻量版的 SSAA。MSAA 与 SSAA 最大的不同，在于对于每个三角形，MSAA 最终每个像素还是只会计算一遍颜色，而 SSAA 需要每个采样点计算一个颜色，因此 MSAA 的开销会更低。在实现中，如果一个像素的中心不在三角形内部，但是其中的某一个采样点在三角形内部，按照没有反走样的判断方式这个像素不需要计算颜色，但是 MSAA 会标记这个像素也需要计算颜色。而 MSAA 又与 SSAA 不同，SSAA 的每个采样点都需要单独计算颜色；MSAA 如何发现一个像素被标记了，就只选择其中被覆盖的一个采样点计算颜色，然后乘以采样点被覆盖的比例作为当前像素的颜色。通过这种方式，MSAA 对于三角形内部的像素处理方式和没有反走样是一样的，本来三角形内部也不是走样的重灾区；在三角形的边界上 MSAA 的效果接近于 SSAA，可以实现比较好的反走样效果。

```{figure} fig/msaa-edges.png
:name: fig-started-aa-msaa
:width: 60%

MSAA 效果示意图[^msaa]
```

[^msaa]: [A Quick Overview of MSAA](https://mynameismjp.wordpress.com/2012/10/24/msaa-overview/)

在早期，MSAA 是最常用的反走样算法。然而随着现代游戏渲染场景的复杂化，场景三角形的个数的显著增多，半透明物体、复杂纹理、特效的广泛使用，MSAA 在计算开销上的优势被抹平，逐渐被其他更快的反走样算法所代替。

## TAA

TAA 全称是**时域反走样（temporal anti-aliasing，TAA）**，其核心思想在于把 SSAA 和 MSAA 中的采样点分配到不同帧上。在实现中，每个像素用于计算颜色的采样点会在不同帧之间按照一定规律抖动（jitter），计算得到的颜色会使用滑动窗口与历史像素颜色进行混合平滑。在绘制完全静态的场景时，我们相当于用前几帧的数据合成得到了超采样的结果，因此 TAA 在每一帧的时间开销其实并没有增加多少。然而一旦碰到动态场景，TAA 就可能产生拖影、闪烁的不自然结果。我们可以通过各种方法尝试将之前的颜色信息变形映射到当前帧来减轻这些问题，但是这又增加了一定的时间开销。总的来说，TAA 依然是一种平衡了开销和效果的反走样算法，也被实现在了主流游戏引擎比如虚幻引擎[^ue]中。

[^ue]: [Unreal Engine: 抗锯齿和上采样](https://dev.epicgames.com/documentation/zh-cn/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine)

## 深度学习方法

近年来深度学习方法快速发展，出现了像 DLSS[^dlss]（deep learning super sampling），FSR[^fsr]（FidelityFX super resolution） 这样的基于深度学习的反走样方法。这些方法在本质上并不是反走样方法，而是超分辨率方法，也就是先渲染出低分辨率的图像，然后再通过神经网络放大图像，这样我们就可以通过更低的渲染代价生成更高质量的图像。在从低分辨率放大的过程中，自然会出现很多的锯齿走样现象，神经网络就必须具备合成逼真细节的能力，而这项能力自然就能被运用到反走样之中。所以在{numref}`fig-started-aa-genshin` 中，我们能看到 FSR 2 被作为反走样的选项。感兴趣的读者可以深入了解神经网络超采样背后的细节，这里就不多展开了。

[^dlss]: [Nvidia: DLSS](https://www.nvidia.com/en-us/geforce/technologies/dlss/)
[^fsr]: [AMD: FSR](https://www.amd.com/en/products/graphics/technologies/fidelityfx/super-resolution.html)

## 其他方法

除了上面提到的方法，常见的抗锯齿算法还有 FXAA（fast-approximate anti aliasing），MLAA（morphological anti aliasing），SMAA（subpixel morphological anti aliasing），CSAA（coverage-sampling anti aliasing）等等，可以服务于不同硬件性能，不同渲染场景，不同效果要求，感兴趣的读者可以继续深入了解。不过近年来，颇有深度学习方法压倒一切的趋势。我们可以发现 DLSS 和 FSR 已经成了很多游戏，比如《黑神话：悟空》[^black-myth]，的默认选项了。

```{figure} fig/black-myth.png
:name: fig-started-aa-black-myth
:width: 100%

《黑神话：悟空》游戏设置截图
```

[^black-myth]: [《黑神话：悟空》官网](https://www.heishenhua.com/)