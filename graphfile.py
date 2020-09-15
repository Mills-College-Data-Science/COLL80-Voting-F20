import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

def bar_graph(labels, bar1, bar1_name, bar2, bar2_name, bar3, bar3_name, title):
    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(14, 6))
    rects1 = ax.bar(x - width, bar1, width, label=bar1_name, color='blue')
    rects2 = ax.bar(x, bar2, width, label=bar2_name, color='gold')
    rects3 = ax.bar(x + width, bar3, width, label=bar3_name, color='aqua')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percent')
    ax.set_xlabel('Year')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.5));

    def autolabel_bar(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{0:.1f}'.format(height), # text -- number with one digit after the decimal
                    (rect.get_x() + rect.get_width() / 3, height),
                    xytext=(0, 3),  # 3 points vertical offset from text to bar
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center
      
    autolabel_bar(rects1)
    autolabel_bar(rects2)
    autolabel_bar(rects3)
            

def line_graph(labels, line1, line1_name, line2, line2_name, line3, line3_name, title):
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(x, line1, 'o-', label=line1_name, color='blue')
    ax.plot(x, line2, 'o-', label=line2_name, color='gold')
    ax.plot(x, line3, 'o-', label=line3_name, color='aqua')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percent')
    ax.set_xlabel('Year')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.8));

    def autolabel_line(xs, ys):
        """Attach a text label above each dot in line graph, displaying its value."""
        for x,y in zip(xs, ys):
            ax.annotate('{:.1f}'.format(y), # text label -- number with one digit after the decimal
                    (x,y), # the point to label
                    xytext=(0, 3),  # 3 points vertical offset from text to seg
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center

    autolabel_line(x, line1)
    autolabel_line(x, line2)
    autolabel_line(x, line3)
    
def bar_graph2(labels, bar1, bar1_name, bar2, bar2_name, title):
    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(14, 6))
    rects1 = ax.bar(x - width/2, bar1, width, label=bar1_name, color='green')
    rects2 = ax.bar(x + width/2, bar2, width, label=bar2_name, color='purple')
 

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percent')
    ax.set_xlabel('Education')
    ax.set_title(title)
    ax.set_xticks(x)
    labels = [ '\n'.join(wrap(l, 12)) for l in labels ]
    ax.set_xticklabels(labels)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.5));

    def autolabel_bar(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{0:.1f}'.format(height), # text -- number with one digit after the decimal
                    (rect.get_x() + rect.get_width() / 3, height),
                    xytext=(0, 3),  # 3 points vertical offset from text to bar
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center
      
    autolabel_bar(rects1)
    autolabel_bar(rects2)
    
            