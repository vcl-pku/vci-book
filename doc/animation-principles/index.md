# 动画原理
:label:`chap_animation-principles`

在前面的章节中，我们关注的都是如何用计算机表达或显示一个**静态**的场景，而从本章开始我们将带领读者了解图形学的另外一个维度——动画。从现在开始，我们要处理和表达的对象将是一个**动态**的场景序列，这与我们之前关注的问题有很大的不同，因为我们引入了一个时间参数。

本章将介绍基本的动画原理，带领读者了解图形学如何对动画序列进行建模，以及如何将运动学应用到动画当中。我们将从运动学中最基本的数学工具——旋转的表示——讲起（:numref:`sec_rotation-representation`），随后以人物动画为例介绍最基本的运动学原理（:numref:`sec_kinematics`）。

````toc
:maxdepth: 2

rotation-representation
kinematics
summary
````