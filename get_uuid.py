import uuid

def generate_uuid():
    length = 5
    # 生成 UUID
    generated_uuid = uuid.uuid4()

    # 将 UUID 转换为字符串
    uuid_str = str(generated_uuid).replace("-", "")

    # 截取指定长度
    fixed_length_uuid = uuid_str[:length]
    
    return fixed_length_uuid