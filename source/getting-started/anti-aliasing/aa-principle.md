# 反走样

## 反走样基本原理

走样发生的原因在于采样频率不足，不满足奈奎斯特-香农采样定理的要求：$f_s > 2f_0$。自然，反走样就有两种思路，一是尽可能提高采样频率，二是降低信号本身的频率。下面我们介绍使用这两种思路的现在常用的反走样方法[^aa]。

[^aa]: [Anti-Aliasing in Gaming: The Battle for Perfect Graphics](https://vokigames.com/anti-aliasing-in-gaming-the-battle-for-perfect-graphics/)

## SSAA

SSAA 全称是**超采样反走样（super sample anti aliasing，SSAA）**，顾名思义，其核心是对像素进行超采样。本来我们只需要在每个像素的中心点计算一个颜色，超采样就是在像素内部的不同位置计算多次颜色然后取平均值。