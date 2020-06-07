#!/usr/bin/env python
# coding: utf-8

# In[ ]:

class PaperData():
    #解析學號意義
    def analytics_studentID(self):
        #分析第三碼 - 學生身分
        category_number = int(self.StudentID[2])
        if category_number == 6:
            self.category = "碩士生"
        elif category_number == 8:
            self.category = "博士生"
        else:
            self.category = "其他"
        #分析第四、五碼 - 入學年度
     	#100年前&後個別字串處理
        if int(self.StudentID[3:5]) > 80:
            self.addmission_year = int(self.StudentID[3:5])
        else:
            self.addmission_year = int(self.StudentID[3:5]) + 100
        #計算就學時間 
        #計算方式 = 發表學年度 - 入學年度 + 1
        self.duringSchool = self.graduate_year - self.addmission_year + 1
        #分析第六碼
        addmissionMethod_number = int(self.StudentID[5])
        if addmissionMethod_number == 1:
            self.addmission_method = "考試入學"
        elif addmissionMethod_number == 4:
            self.addmission_method = "推甄入學"
        else:
            self.addmission_method = "其他"
    
    def __init__(self, graduate_year, paper_title, StudentID):
        self.graduate_year = graduate_year
        self.paper_title = paper_title
        self.StudentID = StudentID
        self.category = ""
        self.addmission_year = ""
        self.addmission_method = ""
        self.duringSchool = -1
        self.analytics_studentID()