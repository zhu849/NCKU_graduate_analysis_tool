#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from classes import PaperData 

#結果介面
def draw_GUI(paper, year_data, advisor_name, exam_method, recommend_method, other_method):     
    second_window = Tk()
    second_window.title('搜尋' + advisor_name + '教授的結果')  
    second_window.geometry('1700x800')
    
    #簡易資料frame
    simple_frame = Frame(second_window) 
    simple_frame.place(x = 200,y = 10, height = 350, width = 1200)
    simple_frame_addmission = Frame(simple_frame, width = 250, background="lightyellow")
    simple_frame_addmission.place(x = 0, y = 0, height = 350, width = 600)
    simple_frame_graduateYear = Frame(simple_frame, background = 'lightgreen')
    simple_frame_graduateYear.place(x = 600, y = 0, height = 350, width = 600)
    label_addmission = Label(simple_frame_addmission, font = 20,text = "入學方式統計結果", background = 'gold')
    label_addmission.pack(side='top',fill = 'x')
    label_graduateYear = Label(simple_frame_graduateYear, font = 20,text = "畢業時間統計結果",background = 'yellowgreen')
    label_graduateYear.pack(side='top', fill = 'x')
    
    #圓餅圖 - 畢業時間
    pieChart_graduate_label = []
    pieChart_graduate_rate = []
    for i in range(1,11):
        if year_data[i]!= 0:
            pieChart_graduate_label.append(str(i) + " years")
            pieChart_graduate_rate.append(year_data[i])

    fig_graduateYear = Figure(facecolor = 'lightgreen')
    ax = fig_graduateYear.add_subplot(111)
    ax.pie(pieChart_graduate_rate, radius=1, labels = pieChart_graduate_label, autopct='%0.2f%%', shadow=True)
    pieChart_graduateYear = FigureCanvasTkAgg(fig_graduateYear, simple_frame_graduateYear)
    pieChart_graduateYear.get_tk_widget().place(x = 5, y = 30, height = 300, width = 420)
    
    #圓餅圖 - 入學方式
    pieChart_addmission_label = ['Exam', 'Recommand', 'Others']
    pieChart_addmission_rate = [exam_method, recommend_method, other_method]
    fig_addmission = Figure(facecolor = 'lightyellow')
    ax = fig_addmission.add_subplot(111)
    ax.pie(pieChart_addmission_rate, radius=1, labels=pieChart_addmission_label, autopct='%0.2f%%', shadow=True)
    pieChart_addmission = FigureCanvasTkAgg(fig_addmission, simple_frame_addmission)
    pieChart_addmission.get_tk_widget().place(x = 5, y = 30, height = 300, width = 420)

    #統計表格 - 畢業時間
    table_graduateYear = ttk.Treeview(simple_frame_graduateYear, selectmode = 'browse')
    table_graduateYear['show'] = 'headings'
    table_graduateYear["columns"] = ("畢業時間","人數")
    table_graduateYear.column("畢業時間",width=80)
    table_graduateYear.column("人數",width=60)
    table_graduateYear.heading("畢業時間",text="畢業時間")
    table_graduateYear.heading("人數",text="人數")
    for i in range(1,11):
        if year_data[i] != 0:
            table_graduateYear.insert("",'end',value=(str(i) + " 年畢業",year_data[i]))
    table_graduateYear.place(x = 440, y = 45, height = 250, width = 150)
    
    #統計表格 - 入學方式
    table_addmission = ttk.Treeview(simple_frame_addmission, selectmode = 'browse')
    table_addmission['show'] = 'headings'
    table_addmission["columns"] = ("入學方式","人數")
    table_addmission.column("入學方式",width=80)
    table_addmission.column("人數",width=60)
    table_addmission.heading("入學方式",text="入學方式")
    table_addmission.heading("人數",text="人數")
    table_addmission.insert("",'end',value = ("考試入學",exam_method))
    table_addmission.insert("",'end',value = ("推甄入學",recommend_method))
    table_addmission.insert("",'end',value = ("其他管道",other_method))
    table_addmission.place(x = 440, y = 45, height = 250, width = 150)
    
    #詳細資料frame&表格
    detail_frame = Frame(second_window)
    detail_frame.place(x = 250, y = 375,width = 1150, height = 350)
    table_detail = ttk.Treeview(detail_frame, selectmode ='browse', height=350)
    scrollbar = ttk.Scrollbar(detail_frame, orient ="vertical", command = table_detail.yview) 
    scrollbar.grid(row=0, column=1, sticky="ns")
    table_detail['yscrollcommand']= scrollbar.set
    scrollbar.pack(side = 'right',fill="y")
    table_detail.configure(yscrollcommand=scrollbar.set)
    table_detail['show'] = 'headings'
    table_detail["columns"] = ("學生編號","畢業年度","入學方式","就學期間","論文名稱")
    table_detail.column("學生編號",width=80)
    table_detail.column("畢業年度",width=80)
    table_detail.column("入學方式",width=80)
    table_detail.column("就學期間",width=80)
    table_detail.column("論文名稱",width=800)
    table_detail.heading("學生編號",text="學生編號")
    table_detail.heading("畢業年度",text="畢業年度")
    table_detail.heading("入學方式",text="入學方式")
    table_detail.heading("就學期間",text="就學期間")
    table_detail.heading("論文名稱",text="論文名稱")
    for i in range(len(paper)):
        table_detail.insert("",'end',value=(i+1,paper[i].graduate_year,paper[i].addmission_method,paper[i].duringSchool,paper[i].paper_title))
    table_detail.pack()
    
    second_window.mainloop() 


# In[ ]:




