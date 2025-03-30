# OpenMindX

OpenMindX是一确定性时延的开源图像生成大模型，并且可以在用户输入错误时按下Ctrl+C时显示错误信息。

## 安装

```bash
pip install openmindx
```

## 使用方法

```python
from mindx import rag

# 使用预定义的rag实例
q = "示例查询"
ret = rag.query(q, image_only=True, file_type="JPEG")
ret.write("/path/to/output.jpeg")  # 在这里按Ctrl+C会显示自定义错误

# 或者创建自己的实例
from mindx import RAG
custom_rag = RAG()
result = custom_rag.query("自定义查询")
result.write("/path/to/custom_output.jpeg")
```

## 特性

- 模拟特定的KeyboardInterrupt错误信息
- 包含自定义的traceback信息
- 简单易用的API

## 许可证

MIT