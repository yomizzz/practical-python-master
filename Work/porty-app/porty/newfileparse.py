# fileparse.py
#
# Exercise 3.3

import csv
import logging # 用于记录诊断信息
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse lines into a list of records
    select：一个列表，选择性地处理一些列
    types：一个列表，规定输出列数据的类型
    has_headers：True代表有表头
    delimiter：代表各列之间数据分隔符
    silence_errors：True则不打印错误信息
    '''
    
    # 如果需要有选择性地输出一些列，但没有表头，则报错
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    
    #csv模块不仅仅可以读取csv文件，也可以读取其他分隔符分隔的数据文件
    rows = csv.reader(lines, delimiter=delimiter)
    
    # Read the file headers if there are headers in CSV file
    headers = next(rows) if has_headers else []
        
    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select] #利用列表表达式来构建列表
        headers = select
                
    records = []
    # 迭代输出元素和对应的索引值，其中索引值用于显示哪一行出现了错误
    for rowno, row in enumerate(rows, 1): 
        if not row:  # Skip rows with no data 跳过空行
            continue
        # Filter the row if specific columns were selected 列表表达式生成新列表
        if select:
            row = [ row[index] for index in indices]
        # Type-conversions
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)] # zip()函数返回元组
            except ValueError as e:
                # 默认是显示错误信息，只有当调用者要求不显示时，才会跳过打印错误信息
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue
                    
        # Making a dictionary if there are headers in CSV file, else Making a tuple
        if headers:
            record = dict(zip(headers, row)) # data in dict are all str type
        else:
            record = tuple(row)
                
        records.append(record)
            
    return records
   
