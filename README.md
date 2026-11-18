# pairwise-foveated-render

VR 转头时边缘糊成马赛克、注视点跳、左右眼清晰区不一致：注视点按屏幕中心；渲染分辨率固定；边缘压缩比固定；眼动延迟不补偿；双眼注视点独立算；FOV 变化不重算；中心区和边缘区硬切；动态分辨率不随 GPU 负载；UI 也被降采样；重投影用旧注视点。render/foveated_render.py 是核心，tests/test_foveated_render.py 15个红。要修的是：眼动预测；可变分辨率；按偏心率压缩；延迟补偿；双眼共享注视；FOV 重算；渐变过渡；负载自适应；UI 全分辨率；当前注视重投影。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
