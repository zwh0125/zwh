# 打开文件并读取内容
with open('file_to_read.txt', 'r') as f:
    text = f.read()

# 统计 terrible 出现的次数，并输出结果
terrible_count = text.count('terrible')
print("The word 'terrible' appears {} times.".format(terrible_count))

# 将奇偶位置的 terrible 替换为 marvellous 和 pathetic
text_list = text.split()
for i in range(len(text_list)):
    if text_list[i] == 'terrible':
        if text_list[:i].count('terrible') % 2 == 1:
            text_list[i] = 'pathetic'
        else:
            text_list[i] = 'marvellous'
new_text = ' '.join(text_list)

# 将新文本写入 result.txt 文件
with open('result.txt', 'w') as f:
    f.write(new_text)
