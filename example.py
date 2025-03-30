from mindx import rag

q = input()# "帮我找一张小朋友的照片,并生成为骑士园"
ret = rag.query(q, image_only=True, file_type="JPEG")
ret.write("/home/demo/output.jpeg")
print("系统可能不支持，请重试")