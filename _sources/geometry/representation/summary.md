# 本章小结

## 思考题

1. 从并行性、几何信息保留程度出发，对比 {numref}`sec-geometry-representation-downsample` 中提及的几种点云下降样技术。
2. 行进立方体算法中存在歧义情况（见 {numref}`fig-geometry-representation-marching_cubes-table` 第三行第四列），试对此进行解释并讨论可能产生的影响。
3. 行进立方体算法对规则网格下的符号距离场做出了哪些假设？是否有其他提取网格表面的方式？

    ```{admonition} 补充阅读
    :class: hint

    Dual Marching Cubes 方法（[https://www.cs.rice.edu/~jwarren/papers/dmc.pdf](https://www.cs.rice.edu/~jwarren/papers/dmc.pdf)）。
    ```

## 习题

1. 倒角距离满足三角不等式吗？即，对于任意点云 $P_1,P_2,P_3$，是否有 $\mathrm{CD}(P_1,P_2)+\mathrm{CD}(P_2,P_3)\ge \mathrm{CD}(P_1,P_3)$？证明你的结论。
2. 试提出具体的算法流程，将有符号距离场转换为体素表达。
