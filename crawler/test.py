import csv

def process_data(file_path):
    # 创建一个字典映射评分值
    score_mapping = {
        '10': '1',
        '20': '1',
        '40': '5',
        '50': '5'
    }

    # 读取CSV文件并进行数据处理
    processed_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            # 获取评分和评论
            score = line[1]
            comment = line[2]

            # 映射评分值
            if score in score_mapping:
                score = score_mapping[score]

            # 格式化数据
            processed_line = [score, comment]
            processed_lines.append(processed_line)

    # 将处理后的数据写回源文件
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(processed_lines)

# 调用函数并传入CSV文件的路径
process_data('test_data.csv')