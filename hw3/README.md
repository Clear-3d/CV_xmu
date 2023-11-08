记录一份作业

这是一份关于训练transformer完成英文到中文翻译的任务。

用卡3090*3 ,epoch=20, batchsize=150, 训练用时5h（做了代码调整，减轻了测试负担，test_bleu花费时间很大。。）

一些可关注的点：

1.需要自己训一个分词器，cpu训，15min左右。

2.使用gpu要求改对应的map关系，如

```
os.environ['CUDA_VISIBLE_DEVICES'] = '4,5,6'
```

对应config要修改

```
gpu_id = '0',
device_id = [0,1,2],
```

3.调参技巧：

3.1 第一个epoch跑bleu指标非常的慢，之后会快一些，所有我直接修改了test的流程，使得训练更快节约资源；

3.2 4卡不一定比3卡快，可能由于IO问题把，这很玄学，我一个测试的比较好的例子是一张卡50batch，可能是由于不同的batch设置会导致test分测试集batch的时候会分出一些比较慢的batch。

3.3 训练大约在epoch10-14阶段达到最佳性能，本文提供两个模型model_bleu26.pth、model_bleu28.pth给可能有需要的人测试使用，点击这里[下载](https://www.dropbox.com/scl/fo/2eqotgw9xxdwho5k8uee3/h?rlkey=p0dg3see1eiw8s6vr7rgl18yd&dl=0)

最后, If you find this work useful, a star would be greatly appreciated.
