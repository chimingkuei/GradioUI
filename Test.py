import gradio as gr

# 定义第一个 Interface
def greet(name):
    return f"Hello, {name}!"

iface1 = gr.Interface(fn=greet, inputs="text", outputs="text", title="Greet Interface")

# 定义第二个 Interface
def square(x):
    return x ** 2

iface2 = gr.Interface(fn=square, inputs="number", outputs="number", title="Square Interface")

# 将两个 Interface 组合在一起
demo = gr.TabbedInterface([iface1, iface2], tab_names=["Greeting", "Square"])

# 运行 Gradio 应用
demo.launch()
