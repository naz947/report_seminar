import matplotlib.pyplot as plt
import numpy as np

def make_plot(plot_data,name):
    p_data=[len(plot_data[plot_data==1]),
    len(plot_data[plot_data<=10])-len(plot_data[plot_data==1]),
        len(plot_data[plot_data<=50])-len(plot_data[plot_data<=10]),
        len(plot_data[plot_data<=100])-len(plot_data[plot_data<=50]),
        len(plot_data[plot_data<=500])-len(plot_data[plot_data<=100]),
        len(plot_data[plot_data>500])]
    x=np.arange(len(p_data))
    plt.figure(figsize=(10,8))
    plt.bar(x, p_data)
    plt.xlabel('Range of samples per class',fontsize=18)
    plt.ylabel('No. of classes',fontsize=18)
    title="Data Imbalance in "+str(name)+" dataset"
    plt.title(title,fontsize=18)
    plt.xticks(x, ('1','1-10','10-50','50-100','100-500','>500'),fontsize=18)
    for i, v in enumerate(p_data):
        val=np.round(np.float(p_data[i])*100/sum(p_data),2)
        val=str(val)+'%'
        plt.text(i-0.35,
                  v/p_data[i],
                val,
                  fontsize=16)

    plt_name=name+'.jpg'
    plt.savefig(plt_name)
    plt.show()
