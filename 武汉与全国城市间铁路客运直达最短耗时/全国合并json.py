import os
import json

# 获取目标文件夹的路径
filedir = 'E:\\A地图故事\\武汉与全国城市间铁路客运直达最短耗时\\data'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.json文件，如果没有则创建

with open('E:\\A地图故事\\武汉与全国城市间铁路客运直达最短耗时\\data\\全国各市地区.json', "w", encoding="utf-8") as f0:  # 结果文件
    y = 0
    f0.write('[')
    f0.write('\n')
    for filename in filenames:
        # 文件的个数
        filepath = filedir + '\\' + filename  # 使用双斜杠来分隔路径
        # 该文件中line有多少行
        print(filepath + "开始访问...")
        with open(filepath, 'r', encoding='utf-8') as fp1:
            y = y + 1
            print(y)
            x = 0
            for line in fp1.readlines():
                x = x + 1
                s = line  # 一行就是一个JSON对象
                try:
                    b = json.loads(s)  # 直接加载JSON数据
                    f0.write(json.dumps(b, ensure_ascii=False))
                except json.JSONDecodeError as e:
                    print(f"解析JSON出错：{e}")

        print(filepath + "加载入文件完成...")

    f0.close()
