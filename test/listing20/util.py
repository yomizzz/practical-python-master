# 一个文本块生成器

def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        # 将文本块内的文本行添加到列表block中，
        # 当出现空行后，将block内的文本行合并成一个字符串并形成一个生成器
        # 然后清空列表block，重新向其中添加文本行
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
