(chap-getting-started-anti-aliasing)=
# 反走样

```{figure} fig/Melencolia.jpg
:name: fig-started-aa-Melencolia
:width: 60%

Dürer, Albrecht. "Melencolia I". 1514, Minneapolis Institute of Art[^Melencolia]
```
[^Melencolia]: [Wikipedia: Melencolia I](https://en.wikipedia.org/wiki/Melencolia_I)

在继续了解如何绘制曲线之前，我们来关注一个细节问题。使用上一节介绍的方法绘制直线和三角形，我们总是在边缘处看到大量的锯齿，如{numref}`fig-started-aa-jaggie` 所示。在像素密度很高时，这些锯齿可能不明显；但是一旦像素密度不高，或者放大来看，锯齿就非常影响观感。本质上，这是由于我们使用离散的像素近似连续图形导致的。出于相同的原因，如果我们把一张照片先缩小分辨率，再放大观察，就可能发现{numref}`fig-started-aa-moire` 中的**摩尔纹（Moire pattern）**，也就是不属于原图像的错误条纹。这些锯齿、摩尔纹的不自然结果统称为**走样（aliasing）**。与之对应的，为了减轻或避免走样现象的技术就称为**反走样（anti aliasing，AA）**。

```{figure} fig/jaggie.jpg
:name: fig-started-aa-jaggie
:width: 80%

画图的锯齿
```

```{figure} fig/moire.jpg
:name: fig-started-aa-moire
:width: 80%

照片中的摩尔纹
```


````{toctree}
:maxdepth: 2

signal-theory
aa-principle
aa-method
summary
````