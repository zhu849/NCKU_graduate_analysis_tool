#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mechanicalsoup
from bs4 import BeautifulSoup
from classes import PaperData 
from resultGUI import draw_GUI

#system_ID = []
#paper = []

#檢查是否正確抓到學號(有可能抓到信箱)
def badStudentID(student_ID):
    for i in range(len(student_ID)):
        if student_ID[i] == "@":
            return True
    return False

def deal_data(start_year, end_year, degree, advisor_name):
    system_ID = []
    paper = []
    url = "http://etds.lib.ncku.edu.tw/etdservice/searching?start=1&end=300&amount=300&degree=" + degree + "&language=all&&dfile=all&a_year_end=" +str(end_year)+"&a_year_start=" + str(start_year) + "&query_field1=advisor&query_word1=" + advisor_name
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    page = browser.get_current_page()
    
    #找到所有論文的系統識別碼
    for i in range(len(page.find_all('a'))):
        temp = page.find_all('a')[i]['href'][20:42]
        if temp[0:5] == "U0026":
            system_ID.append(temp)
    
    #開啟每個論文抓資料
    for i in range(len(system_ID)):
        SID_url = "http://etds.lib.ncku.edu.tw/etdservice/view_metadata?etdun=" + system_ID[i]
        browser.open(SID_url)
        page = browser.get_current_page()

        #年份處理
        if (str(page.find_all('td')[31])[22:25])[2] == '<':
            num_Graduate_year = int(str(page.find_all('td')[31])[22:24])
        else:
            num_Graduate_year = int(str(page.find_all('td')[31])[22:25])

        #論文名稱處理
        str_paper_title = str(page.find_all('td')[21])[22:-5]
        str_vec = str_paper_title.split()
        str_paper_title = ""
        for i in range(len(str_vec)):
            str_paper_title = str_paper_title + str_vec[i]
        
        #學號處理
        str_studentID = str(page.find_all('td')[41])[22:-5]
        if badStudentID(str_studentID):
            str_studentID = str(page.find_all('td')[43])[22:-5]
        paper.append(PaperData(num_Graduate_year, str_paper_title, str_studentID))

    #統計結果
    exam_method = 0
    recommend_method = 0
    other_method = 0
    year_data = [0]*15
        
    for i in range(len(paper)):    
        #統計入學方式
        if paper[i].addmission_method == "考試入學":
            exam_method =  exam_method + 1
        elif paper[i].addmission_method == "推甄入學":
            recommend_method = recommend_method + 1
        else:
            other_method = other_method + 1
        #統計畢業時間
        year_data[paper[i].duringSchool] = year_data[paper[i].duringSchool] + 1   
    draw_GUI(paper, year_data, advisor_name, exam_method, recommend_method, other_method)

