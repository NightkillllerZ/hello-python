# 词频统计器

# 读取文章内容
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# 统计词频
def count_words(text):
    words = text.lower().split()  # 将文本转为小写，并按空格分割成单词
    word_count = {}  # 存储每个单词的出现次数

    for word in words:
        word = word.strip('.,!?()[]{}":;')  # 去掉标点符号
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


# 打印词频
def print_word_count(word_count):
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)  # 按频率排序
    for word, count in sorted_word_count:
        print(f'{word}: {count}')


# 主函数
def main():
    file_path = 'article.txt'  # 文章文件路径
    text = read_file(file_path)  # 读取文件内容
    word_count = count_words(text)  # 统计词频
    print_word_count(word_count)  # 打印结果


# 调用主函数
if __name__ == "__main__":
    main()
