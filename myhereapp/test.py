from bokeh.plotting import figure, output_file, show, curdoc
import pandas as pd
from bokeh.models import HoverTool, ColumnDataSource, GlyphRenderer, Legend
from bokeh.io import output_file, show
from bokeh.models.widgets import Select
from bokeh.layouts import row, column
from bokeh.models.tickers import FixedTicker

graphDic = {
    "TBB backend": "tbb",
    "OpenMP backend": "openmp",
    "Single GPU Data Transfer": "singleGPUData",
    "Single GPU Compute": "singleGPUCompute",
    "Multi GPU Data Transfer": "multiGPUData",
    "Multi GPU Compute": "multiGPUCompute"
}

tools_to_show = 'hover,box_zoom,pan,save,reset,wheel_zoom'
graph = figure(plot_width=800, plot_height=400, title="TBB Backend", x_axis_label='# Particles', y_axis_label='time (ms)', tools=tools_to_show)
colors = ['red', 'blue', 'purple', 'green', 'black', 'pink', 'orange']

def triggerFunction(attr, old, new):
    graph = figure(plot_width=800, plot_height=400, y_axis_label='time (ms)', tools=tools_to_show)
    setHover(graph)
    if ((graphDic[select.value]) == "openmp"):
        OpenMP(graph)
    elif ((graphDic[select.value]) == "tbb"):
        TBB(graph)
    elif ((graphDic[select.value]) == "singleGPUCompute"):
        singleGPUCompute(graph)
    elif ((graphDic[select.value]) == "singleGPUData"):
        singleGPUData(graph)
    elif ((graphDic[select.value]) == "multiGPUCompute"):
        multiGPUCompute(graph)
    elif ((graphDic[select.value]) == "multiGPUData"):
        multiGPUData(graph)
    else:
        raise Exception("WRONG!!!")


select=Select(title="Select Graph:", value="TBB backend",options=["TBB backend", "OpenMP backend","Single GPU Data Transfer", "Single GPU Compute", "Multi GPU Data Transfer", "Multi GPU Compute"])
select.on_change('value', triggerFunction)


def TBB(graph): 
    curdoc().clear()  
    TBB = pd.read_csv("myhereapp/Data/TBB.csv")
    graph.xaxis.ticker = FixedTicker(ticks=[160,320,640,960,1280,1600,1920,2240,2560,2880])
    names = [TBB.columns[i] for i in range(1,8)]
    for i in range(7):
        source = ColumnDataSource(data={
            'particles': TBB['particles'],
            'time': TBB[names[i]],
            'name': [names[i] for j in range(10)]
        })
        graph.line('particles', 'time', source=source, legend=names[i], line_width=2, color=colors[i])
        circle = graph.circle('particles', 'time', source=source, size=6, color=colors[i])
    graph.xaxis.axis_label = "# Particles"
    graph.yaxis.axis_label = "time (ms)"
    graph.legend.location="top_left"
    graph.title.text="TBB Backend"
    curdoc().add_root(column(select, graph))
    

def OpenMP(graph):
    curdoc().clear()
    OpenMP = pd.read_csv("myhereapp/Data/OpenMP.csv")
    graph.xaxis.ticker = FixedTicker(ticks=[160,320,640,960,1280,1600,1920,2240,2560,2880])
    names = [OpenMP.columns[i] for i in range(1,8)]
    for i in range(7):
        source = ColumnDataSource(data={
            'particles': OpenMP['particles'],
            'time': OpenMP[names[i]],
            'name': [names[i] for j in range(10)]
        })
        graph.line('particles', 'time', source=source, legend=names[i], line_width=2, color=colors[i])
        circle = graph.circle('particles', 'time', source=source, size=6, color=colors[i])
    graph.xaxis.axis_label = "# Particles"
    graph.yaxis.axis_label = "time (ms)"
    graph.legend.location="top_left"
    graph.title.text="OpenMP Backend"
    curdoc().add_root(column(select, graph))

def singleGPUCompute(graph):
    curdoc().clear()
    graph = figure(plot_width=800, plot_height=400, y_axis_label='time (ms)', tools=tools_to_show, y_axis_type="log")
    graph.xaxis.ticker = FixedTicker(ticks=[160,320,640,960,1280,1600,1920])
    setHover(graph)
    singleGPUCompute = pd.read_csv("myhereapp/Data/singleGPUCompute.csv")
    names = [singleGPUCompute.columns[i] for i in range(1,5)]
    for i in range(4):
        source = ColumnDataSource(data={
            'particles': singleGPUCompute['particles'],
            'time': singleGPUCompute[names[i]],
            'name': [names[i] for j in range(7)]
        })
        graph.line('particles', 'time', source=source, legend=names[i], line_width=2, color=colors[i])
        circle = graph.circle('particles', 'time', source=source, size=6, color=colors[i])
    
    graph.xaxis.axis_label = "# Particles"
    graph.yaxis.axis_label = "time (ms)"
    graph.legend.location="top_left"
    graph.title.text="Single GPU Compute"
    curdoc().add_root(column(select, graph))

def singleGPUData(graph):
    curdoc().clear()
    graph = figure(plot_width=800, plot_height=400, y_axis_label='time (ms)', tools=tools_to_show, y_axis_type="log")
    graph.xaxis.ticker = FixedTicker(ticks=[160,320,640,960,1280,1600,1920])
    setHover(graph)
    singleGPUData = pd.read_csv("myhereapp/Data/singleGPUData.csv")
    names = [singleGPUData.columns[i] for i in range(1,5)]
    for i in range(4):
        source = ColumnDataSource(data={
            'particles': singleGPUData['particles'],
            'time': singleGPUData[names[i]],
            'name': [names[i] for j in range(7)]
        })
        graph.line('particles', 'time', source=source, legend=names[i], line_width=2, color=colors[i])
        circle = graph.circle('particles', 'time', source=source, size=6, color=colors[i])
    
    graph.xaxis.axis_label = "# Particles"
    graph.yaxis.axis_label = "time (ms)"
    graph.legend.location="top_left"
    graph.title.text="Single GPU Data Transfer"
    curdoc().add_root(column(select, graph))

def multiGPUCompute(graph):
    curdoc().clear()
    graph = figure(plot_width=800, plot_height=400, y_axis_label='time (ms)', tools=tools_to_show)
    graph.xaxis.ticker = FixedTicker(ticks=[160,320,640,960,1280,1600,1920,2240,2560,2880])
    setHover(graph)
    multiGPUCompute = pd.read_csv("myhereapp/Data/multiGPUCompute.csv")
    names = [multiGPUCompute.columns[i] for i in range(1,3)]

    for i in range(2):
        source = ColumnDataSource(data={
            'particles': multiGPUCompute['particles'],
            'time': multiGPUCompute[names[i]],
            'name': [names[i] for j in range(10)]
        })
        graph.line('particles', 'time', source=source, legend=names[i], line_width=2, color=colors[i])
        circle = graph.circle('particles', 'time', source=source, size=6, color=colors[i])
    
    graph.xaxis.axis_label = "# Particles"
    graph.yaxis.axis_label = "time (ms)"
    graph.legend.location="top_left"
    graph.title.text="Multi GPU Compute"
    curdoc().add_root(column(select, graph))

def multiGPUData(graph):
    curdoc().clear()
    graph = figure(plot_width=800, plot_height=400, y_axis_label='time (ms)', tools=tools_to_show)
    graph.xaxis.ticker = FixedTicker(ticks=[160,320,640,960,1280,1600,1920,2240,2560,2880])
    setHover(graph)
    multiGPUData = pd.read_csv("myhereapp/Data/multiGPUData.csv")
    names = [multiGPUData.columns[i] for i in range(1,3)]

    for i in range(2):
        source = ColumnDataSource(data={
            'particles': multiGPUData['particles'],
            'time': multiGPUData[names[i]],
            'name': [names[i] for j in range(10)]
        })
        graph.line('particles', 'time', source=source, legend=names[i], line_width=2, color=colors[i])
        circle = graph.circle('particles', 'time', source=source, size=6, color=colors[i])
    
    graph.xaxis.axis_label = "# Particles"
    graph.yaxis.axis_label = "time (ms)"
    graph.legend.location="top_left"
    graph.title.text="Multi GPU Compute"
    curdoc().add_root(column(select, graph))


def setHover(graph):
    hover = graph.select(dict(type=HoverTool))
    hover.tooltips=[
        ("", '@name'),
        ("# Particles", "@particles"),
        ("time", "@time")
    ]

setHover(graph)
TBB(graph)
curdoc().clear()
curdoc().add_root(column(select, graph))



