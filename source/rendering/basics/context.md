# 渲染的定义与发展

所谓渲染，指的是以给定的视角（perspective），在已知的光照（lighting）条件下，观察三维场景中具有特定材质（material）的物体而生成二维图像的过程。渲染作为一门研究课题与图形学一同诞生，自 20 世纪 70 年代以来得到了迅猛的发展，催生了电子游戏、影视特效等行业的诞生，并极大地改变了工业设计的面貌。
根据需求的不同，渲染又可以被分为离线渲染（offline rendering）与实时渲染（realtime rendering）两类，它们的发展脉络既在很大程度上交融，却又具有一定的独立性。

## 离线渲染

在计算机科学中，我们称一个算法为“离线”的，并不是在强调该算法可以在网络连接断开的状态下运行。事实上，它表达的是所指称的算法不具有交互性，可以大量占用计算资源与时间。因此，与实时渲染相对，离线渲染因其能够调用更多的计算力而能产出更加逼真的具有丰富细节的结果。我们在日常生活中所看到的可以以假乱真的建筑和家居概念图、电影中充满丰富想象力却难辨真伪的特效，其背后的技术都可以归于此类。

TODO: 离线渲染技术的发展

## 实时渲染

和离线渲染能够大量占用计算资源不同，实时渲染需要确保渲染画面的可交互性，其典型的应用场景即为电子游戏。一般来说，3D 可交互图形应用程序要求一帧画面包括渲染在内的所有计算过程都在 $1/30$ 秒内完成。