(chap-getting-started-basics-hardware)=
# 显示原理

在上一节，我们对像素这一概念有了基本了解。而一张图片在最开始的时候只是保存在硬盘中的一串数字。这串数字如何经历转化最终显示到屏幕上，就是这一节我们要了解的内容。

## 显示器

为了能够实时显示动态内容，显示器总是在以固定的频率不断刷新屏幕上的所有像素，这一频率就是显示器的**刷新频率（refresh rate）**。屏幕的刷新频率由物理硬件所决定。比如对于 CRT 显示器而言，一个脉冲信号的电子束轰击荧光屏有逐渐点亮再逐渐熄灭的过程，这一过程需要耗费一定的时间，并且电子束在磁场控制下扫描整个屏幕也需要时间，这些时间决定了显示器刷新频率的上限。对于其他显示器，也会存在其他物理因素的制约刷新率。更高的刷新率意味着画面更连续，更流畅，比如当下主流的高刷新率屏幕可以达到144Hz，也就是每秒更新144次。

显示器总是以固定的频率刷新页面，刷新的内容从**帧缓存（frame buffer）** 中读取。帧缓存是一片内存空间，软件更新帧缓存的内容就可以更新屏幕显示的内容。不同于显示器以固定的频率读取帧缓存，软件更新帧缓存的频率是不一定的。比如，如果我们观看一部 24Hz 拍摄的电影，那么帧缓存就会每秒更新24次；如果我们玩一部帧率为60的游戏，那么帧缓存就会每秒更新60次，甚至由于计算开销过大帧率还可能存在波动。这意味着帧缓存的更新和读取是异步进行的，如果处理不当，就可能存在画面的**撕裂（screen tearing）**，如{numref}`fig-started-basic-tearing`所示。

```{figure} fig/tearing.jpg
:name: fig-started-basic-tearing
:width: 70%

画面撕裂[^tearing]
```
[^tearing]:[Wikipedia: Screen tearing](https://en.wikipedia.org/wiki/Screen_tearing)

解决撕裂问题的最常见方法是使用**多重缓冲（multiple buffering）** 技术。多重缓冲技术使用多个帧缓存，将更新和读取分开，最简单的做法是**双缓冲（double buffering）**。假设显示器正在显示帧缓存 A 中的内容，那么软件更新只会更新帧缓存 B 中的内容。假设显示器下次刷新时 B 中的内容还未更新完全，那么显示器会继续读取 A 中的内容显示到屏幕上。直到 B 中的内容更新完毕，显示器就会切换到 B 中的内容进行显示，而软件则会切换到更新 A 中的内容，如此往复。注意显示器在这个过程中的模式称为**垂直同步（V-sync）** 模式。如果垂直同步模式被设置为关闭，那么显示器则不会等到软件写完再去读取帧缓存 B，这时屏幕撕裂依然存在。使用更多的帧缓存能进一步提高同步的效率，比如可能存在软件更新的频率超过屏幕刷新频率的情况。而这一同步过程往往也不用程序员来操心，一般由专门的图形硬件和驱动来解决，也就是我们下面介绍的图形处理器 GPU。

```{figure} fig/gpu-double-buffer.png
:name: fig-started-basic-double-buffer
:width: 100%

双缓冲原理示意图[^double-buffer]
```
[^double-buffer]:[计算机那些事(8)——图形图像渲染原理](https://chuquan.me/2018/08/26/graphics-rending-principle-gpu/)

## GPU

在早期的计算机中，并不存在专门处理图形的硬件，显示器显示的内容由中央处理器（central processing unit，CPU）直接生成。而随着显示分辨率的提高，专门处理图形计算和显示的硬件出现了，也就是**图形处理器（graphics processing unit，GPU）**。GPU 与 CPU 最大的不同，在于 GPU 有大量简单的计算单元，因此非常适合处理高度并行的程序，比如计算每个像素的颜色。如{numref}`fig-started-basic-cpu-gpu` 所示，CPU 在收到显示的指令之后，比如显示一张图片，播放一段视频，会将需要的资源通过总线发到到 GPU 的内存（也就是“显存”）中，然后发送指令让 GPU 执行显示的程序，并由 GPU 完成与显示器的同步。

```{figure} fig/ios-renderIng-gpu-internal-structure.png
:name: fig-started-basic-cpu-gpu
:width: 70%

GPU 与 CPU 协同工作示意图[^double-buffer]
```

随着图形技术的发展，GPU 的重要性在逐渐提高。首先，通过 OpenGL[^opengl]，DirectX[^directx] 等可编程的图形 API，我们可以像编写 CPU 程序一样编写 GPU 程序，来生成我们想要的 2D、3D 内容，这是现代实时图形技术的基础。GPU 的高度并行性也可以应用到其他非图形的领域。比如 CUDA[^cuda] 作为通用的 GPU 编程框架，可以让用户编写运行在 GPU 上的并行计算程序，广泛应用于科学计算、深度学习等领域中。在后面的渲染章节{numref}`chap-rendering-shading` 中，我们还会进一步学习 GPU 的内部细节。

[^opengl]: [OpenGL](https://www.opengl.org/)
[^directx]: [DirectX](https://learn.microsoft.com/zh-cn/windows/win32/directx)
[^cuda]: [CUDA](https://developer.nvidia.com/cuda-toolkit)