# 本章小结

在本章中，我们了解了图形表示与显示的大致原理，其中重点的概念是像素与矢量、帧缓存、图形处理器。在本部分的剩下内容中，我们将深入其中的细节，并了解二维图形绘制与处理的算法。

## 三重缓冲

在{numref}`chap-getting-started-basics-hardware` 中我们介绍了双缓冲的机制，现在假设硬件提供了三个帧缓存，那么可以设计怎样的三重缓冲机制？这相比于双重缓冲有怎样的好处？在思考完成之后，你可以对照图形 API Vulkan 的文档[^vulkan-tutorial][^vulkan-manual]，看看现代图形 API 对于缓冲机制的抽象。

[^vulkan-tutorial]: [Vulkan 编程指南：呈现模式](https://zeromake.github.io/VulkanTutorialCN/47-%E5%91%88%E7%8E%B0%E6%A8%A1%E5%BC%8F.html)
[^vulkan-manual]: [VkPresentModeKHR(3) Manual Page](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkPresentModeKHR.html)

<!-- ## 习题

## 参考文献 -->
