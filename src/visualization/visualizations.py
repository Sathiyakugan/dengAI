import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def plotly_scatter(df, x, y, color=None, size=None, hover_name=None, hover_data=None, title=None, labels=None,
                   width=None, height=None):
    """
    Plot a scatter plot using plotly
    :param df: dataframe containing the data
    :param x:  column name of the x-axis
    :param y: column name of the y-axis
    :param color: column name of the color
    :param size: column name of the size
    :param hover_name: column name of the hover name
    :param hover_data:  column name of the hover data
    :param title: title of the plot
    :param labels: dictionary containing the labels of the plot
    :param width: width of the plot
    :param height: height of the plot
    :return: None
    """
    fig = px.scatter(df, x=x, y=y, color=color, size=size, hover_name=hover_name, hover_data=hover_data, title=title,
                     labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_bar(df, x, y, color=None, hover_name=None, hover_data=None, title=None, labels=None, width=None,
               height=None):
    fig = px.bar(df, x=x, y=y, color=color, hover_name=hover_name, hover_data=hover_data, title=title, labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_line(df, x, y, color=None, hover_name=None, hover_data=None, title=None, labels=None, width=None,
                height=None):
    fig = px.line(df, x=x, y=y, color=color, hover_name=hover_name, hover_data=hover_data, title=title, labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_histogram(df, x, color=None, hover_name=None, hover_data=None, title=None, labels=None, width=None,
                     height=None):
    fig = px.histogram(df, x=x, color=color, hover_name=hover_name, hover_data=hover_data, title=title, labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_box(df, x, y, color=None, hover_name=None, hover_data=None, title=None, labels=None, width=None,
               height=None):
    fig = px.box(df, x=x, y=y, color=color, hover_name=hover_name, hover_data=hover_data, title=title, labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_pie(df, values, names, color=None, hover_name=None, hover_data=None, title=None, labels=None, width=None,
               height=None):
    fig = px.pie(df, values=values, names=names, color=color, hover_name=hover_name, hover_data=hover_data, title=title,
                 labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_heatmap(df, x, y, color=None, hover_name=None, hover_data=None, title=None, labels=None, width=None,
                   height=None):
    fig = px.density_heatmap(df, x=x, y=y, color=color, hover_name=hover_name, hover_data=hover_data, title=title,
                             labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_scatter_matrix(df, dimensions, color=None, hover_name=None, hover_data=None, title=None, labels=None,
                          width=None, height=None):
    fig = px.scatter_matrix(df, dimensions=dimensions, color=color, hover_name=hover_name, hover_data=hover_data,
                            title=title, labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()


def plotly_parallel_coordinates(df, dimensions, color=None, hover_name=None, hover_data=None, title=None, labels=None,
                                width=None, height=None):
    fig = px.parallel_coordinates(df, dimensions=dimensions, color=color, hover_name=hover_name, hover_data=hover_data,
                                  title=title, labels=labels)
    fig.update_layout(width=width, height=height)
    fig.show()

