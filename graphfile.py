import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
from matplotlib.ticker import StrMethodFormatter

# three bars in bar graph
def bar_graph3(arg_list):   
    labels, bar1, bar2, bar3, ylabel, title = [arg_list[i] for i in range(6)]
    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 5))
    rects1 = ax.bar(x - width, bar1, width, label=bar1.name, color='blue')
    rects2 = ax.bar(x, bar2, width, label=bar2.name, color='gold')
    rects3 = ax.bar(x + width, bar3, width, label=bar3.name, color='aqua')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    labels_formatted = ['{:.0f}'.format(elem) for elem in labels] 
    ax.set_xticklabels(labels_formatted)
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
    
    
# two bars in bar graph    
def bar_graph(arg_list):   
    labels, bar1, bar2, ylabel, title = [arg_list[i] for i in range(5)]
    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 5))
    rects1 = ax.bar(x - width/2, bar1, width, label=bar1.name, color='blue')
    rects2 = ax.bar(x + width/2, bar2, width, label=bar2.name, color='gold')
 
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.5));

    def autolabel_bar(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{0:.1f}'.format(height), # text -- number with one digit after the decimal
                    (rect.get_x() + rect.get_width()*2 / 3, height),
                    xytext=(0, 3),  # 3 points vertical offset from text to bar
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center
      
    autolabel_bar(rects1)
    autolabel_bar(rects2)
            

# two bars in bar graph -- for education  
def bar_graph2(arg_list):   
    labels, bar1, bar2, ylabel, title = [arg_list[i] for i in range(5)]
    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 5))
    rects1 = ax.bar(x - width/2, bar1, width, label=bar1.name, color='green')
    rects2 = ax.bar(x + width/2, bar2, width, label=bar2.name, color='purple')
 
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    labels = [ '\n'.join(wrap(l, 12)) for l in labels ] # wrap label text 
    ax.set_xticklabels(labels)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.5));

    def autolabel_bar(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{0:.1f}'.format(height), # text -- number with one digit after the decimal
                    (rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset from text to bar
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center
      
    autolabel_bar(rects1)
    autolabel_bar(rects2)
            

# two lines in line graph
def line_graph(arg_list):   
    labels, line1, line2, ylabel, title = [arg_list[i] for i in range(5)]
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, line1, 'o-', label=line1.name, color='blue')
    ax.plot(x, line2, 'o-', label=line2.name, color='gold')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    labels_formatted = ['{:.0f}'.format(elem) for elem in labels] 
    ax.set_xticklabels(labels_formatted)
    #ax.set_xticklabels(labels)
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
  
    
# three lines in line graph
def line_graph3(arg_list):   
    labels, line1, line2, line3, ylabel, title = [arg_list[i] for i in range(6)]
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, line1, 'o-', label=line1.name, color='blue')
    ax.plot(x, line2, 'o-', label=line2.name, color='gold')
    ax.plot(x, line3, 'o-', label=line3.name, color='aqua')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    labels_formatted = ['{:.0f}'.format(elem) for elem in labels] 
    ax.set_xticklabels(labels_formatted)
    #ax.set_xticklabels(labels)
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
    
# three lines in line graph, whole numbers for text labels
def line_graph1(arg_list):   
    labels, line1, line2, line3, ylabel, title = [arg_list[i] for i in range(6)]
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, line1, 'o-', label=line1.name, color='blue')
    ax.plot(x, line2, 'o-', label=line2.name, color='gold')
    ax.plot(x, line3, 'o-', label=line3.name, color='aqua')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.8));

    def autolabel_line(xs, ys):
        """Attach a text label above each dot in line graph, displaying its value."""
        for x,y in zip(xs, ys):
            ax.annotate('{:,.0f}'.format(y), # text label -- number with one digit after the decimal
                    (x,y), # the point to label
                    xytext=(0, 3),  # 3 points vertical offset from text to seg
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center

    autolabel_line(x, line1)
    autolabel_line(x, line2)
    autolabel_line(x, line3)
    

# whole numbers for text label above each dot in line graph -- 2 lines
def line_graph2(labels, line1, line2, ylabel, title):
    x = np.arange(len(labels))  # the label locations
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, line1, 'o-', label=line1.name, color='blue')
    ax.plot(x, line2, 'o-', label=line2.name, color='gold')

    # Add some text for labels, title and custom x-axis tick labels, etc. 
    ax.set_ylabel(ylabel)
    ax.set_xlabel(labels.name)
    ax.set_title(title)
    ax.set_xticks(x)
    labels_formatted = ['{:.0f}'.format(elem) for elem in labels] 
    ax.set_xticklabels(labels_formatted)
    ax.legend(loc=1, bbox_to_anchor=(1, 0.8));

    def autolabel_line(xs, ys):
        """Attach a text label above each dot in line graph, displaying its value."""
        for x,y in zip(xs, ys):
            ax.annotate('{:,.0f}'.format(y), # text label -- number with zero digit after the decimal
                    (x,y), # the point to label
                    xytext=(0, 3),  # 3 points vertical offset from text to seg
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center

    autolabel_line(x, line1)
    autolabel_line(x, line2)

    
# two bars in horizontal bar graph    
def barh_graph(arg_list):   
    labels, bar1, bar2, xlabel, title = [arg_list[i] for i in range(5)]
    y = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 5))
    rects1 = ax.barh(y + width/2, bar1, width, label=bar1.name, color='blue')
    rects2 = ax.barh(y - width/2, bar2, width, label=bar2.name, color='gold')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(labels.name)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_yticks(y)
    labels_formatted = ['{:.0f}'.format(elem) for elem in labels] 
    ax.set_yticklabels(labels_formatted)
    ax.legend(loc=0, bbox_to_anchor=(1, 0.5));

    def autolabel_bar(rects):
        """Attach a text label to the right of each bar in *rects*, displaying its width."""
        for rect in rects:
            rec_width = rect.get_width()
            ax.annotate('{0:.1f}'.format(rec_width), # text -- number with one digit after the decimal
                    (rec_width, rect.get_y()),
                    xytext=(25, 0),  # 25 points vertical offset from text to bar
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center
      
    autolabel_bar(rects1)
    autolabel_bar(rects2)
    
    
# three bars in horizontal bar graph    
def barh_graph3(arg_list):   
    labels, bar1, bar2, bar3, xlabel, title = [arg_list[i] for i in range(6)]
    y = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 5))
    rects1 = ax.barh(y + width, bar1, width, label=bar1.name, color='blue')
    rects2 = ax.barh(y, bar2, width, label=bar2.name, color='gold')
    rects3 = ax.barh(y - width, bar3, width, label=bar3.name, color='aqua')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(labels.name)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_yticks(y)
    labels_formatted = ['{:.0f}'.format(elem) for elem in labels] 
    ax.set_yticklabels(labels_formatted)
    ax.legend(loc=0, bbox_to_anchor=(1, 0.5));

    def autolabel_bar(rects):
        """Attach a text label to the right of each bar in *rects*, displaying its width."""
        for rect in rects:
            rec_width = rect.get_width()
            ax.annotate('{0:.1f}'.format(rec_width), # text -- number with one digit after the decimal
                    (rec_width, rect.get_y()),
                    xytext=(25, 0),  # 25 points vertical offset from text to bar
                    textcoords="offset points",
                    ha='center', va='bottom') # horizontal alignment is center
      
    autolabel_bar(rects1)
    autolabel_bar(rects2)
    autolabel_bar(rects3)