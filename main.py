#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
from deal_data import deal_data, badStudentID

print("程式開啟中，請稍後....")

main_window = Tk()
main_window.title('成大畢業時間分析工具')  
main_window.geometry('450x350')
main_window.resizable(0, 0)

text_advisorName = Label(main_window, text = "指導教授姓名", font = 15)
text_advisorName.place(x=20, y=50)

entry_AdvisorName = Entry(main_window, width = 10,font = 15)
entry_AdvisorName.place(x=150, y=50)

text_wantedYear = Label(main_window,text = "想要搜尋的學年度", font = 15)
text_wantedYear.place(x=20, y=100)

entry_startyear = Entry(main_window, width = 5,font = 15)
entry_startyear.place(x=170, y=100)

text_dash = Label(main_window,text = "到", font = 25)
text_dash.place(x=228,y=100)

entry_endyear = Entry(main_window, width = 5,font = 15)
entry_endyear.place(x=270,y=100)

text_year = Label(main_window, text = "年(畢業年度)", font = 25)
text_year.place(x=320,y=100)

text_studentCategory = Label(main_window, text = "選擇學生類別", font = 15)
text_studentCategory.place(x=20,y=180)

category_select = IntVar()
radio_studentCategory_master = Radiobutton(main_window, text="碩士", variable = category_select, value=1, font = 15) 
radio_studentCategory_doctor = Radiobutton(main_window, text="博士", variable = category_select, value=2, font = 15)
radio_studentCategory_master.place(x=150, y=180)
radio_studentCategory_doctor.place(x=250, y=180)

#submit function
def submit():
    if category_select.get() == 1:
        student_Category = "碩士"
    else:
        student_Category = "博士"
    start_year = entry_startyear.get()
    end_year = entry_endyear.get()
    if int(entry_startyear.get()) > int(entry_endyear.get()):
        start_year = entry_endyear.get()
        end_year = entry_startyear.get()
        
    deal_data(start_year, end_year, student_Category, entry_AdvisorName.get())
    
button_search = Button(main_window, text="搜尋", height = 2, width = 10, font = 30, command = submit)
button_search.place(x=300, y=220)

text_wait = Label(main_window, text = "(搜尋會需要一些時間，請耐心等候)", font = 25)
text_wait.place(x=150, y=280)

main_window.mainloop()                


# In[ ]:




