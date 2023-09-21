import os
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts

def get_chart(cnt: int, number, attr) -> Bar:
    bar = (
        Bar()
        .add_xaxis(xaxis_data=attr)
        .add_yaxis('垃圾种类统计', number)
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"第{cnt}个图片垃圾统计"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts()
        )
    )
    return bar

def modify_html_src(file_path, old_src, new_src='src="https://cdn.bootcdn.net/ajax/libs/echarts/5.4.2/echarts.js"'):
    # 读取HTML文件内容
    with open(file_path, 'r') as f:
        content = f.read()

    # 替换src属性
    new_content = content.replace(old_src, new_src)

    # 将修改后的内容写回文件
    with open(file_path, 'w') as f:
        f.write(new_content)
def save():
    timeline = Timeline()
    attr = ['recyclable waste','hazardous waste','kitchen waste','other waste']

    file_path = "yolov5-7.0\\runs\\detect"
    path_list = os.listdir(file_path)[-1]
    name = path_list
    path = os.path.join(file_path,path_list)
    full_path = os.path.join(path,"labels")
    path = os.listdir(full_path)[0]
    full_path = os.path.join(full_path,path)
    # print(full_path)
    i = 0
    cnt = 1
    with open(full_path,'r') as file:
        number = [0, 0, 0, 0]
        content = file.read()
        content = content.replace("\n",' ')
        # print(content)
        content = content.split(' ')
        content.pop(-1)
        # print(content)
        # print(len(content))
        for i in range(len(content)):
            if i%5 == 0:
                # print(number[i])
                number[int(content[i])] += 1
        # print(number)
        # 添加时间轴
        timeline.add(get_chart(cnt,number,attr), time_point=str(cnt))
    timeline.render(f"{name}.html")
    modify_html_src(f"{name}.html",'src="https://assets.pyecharts.org/assets/v5/echarts.min.js"')


if __name__ == '__main__':
    save()







