(chap-getting-started-images)=
# 图像处理

```{figure} fig/stipple-engaving.jpg
:name: fig-started-images-stipple-engaving
:width: 70%

Bartolozzi, Francesco. detail of "Cupid and Psyche with an Arrow". 1793[^stipple]
```
[^stipple]: [Wikipedia: Francesco Bartolozzi](https://en.wikipedia.org/wiki/Francesco_Bartolozzi)

在之前的部分我们主要讨论的是如何在计算机中生成图形，而**图像处理（image processing）** 是相反的过程：我们已经有了一张生成的或者拍摄的图片，需要对图像进行处理和理解。图形学渲染中的后处理、照片的滤镜、计算机视觉（computer vision）的图像分割、分类、理解等都是图像处理的内容。因此，我们不可能在一节的内容里完整介绍图像处理的方方面面，只能浅尝辄止做一些基础性介绍。对于近年来蓬勃发展的深度学习图像处理领域我们也只能点到为止。在本节中，我们会分图像处理中的几个专题，介绍相应的基础算法。

```{toctree}
:maxdepth: 2

filtering
poisson
segmentation
dithering
seam
summary
```