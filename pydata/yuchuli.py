import PySimpleGUI as sg
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
sg.ChangeLookAndFeel('GreenTan')
menu_def = [['&使用说明', ['&注意']]]
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Frame(layout=[
    [sg.Radio('重复值处理', "RADIO1",size=(15,1),key="dup"),  sg.Radio('缺失值处理', "RADIO1",size=(15,1),key="mis"), sg.Radio('异常值处理', "RADIO1",default=True,key="war")]], title='数据预处理',title_color='green',title_location='n',relief=sg.RELIEF_SUNKEN, tooltip='选择其中一种处理方式' )],
    [sg.Text('文件位置', size=(8, 1), auto_size_text=False, justification='right'),
     sg.InputText(enable_events=True,key="lujing"), sg.Button('浏览',key = 'getf')],
    [sg.Button('查看',key = 'look'),sg.Submit('处理',key = 'handle'), sg.Cancel('关闭')]]

window = sg.Window('特征工程', layout, default_element_size=(40, 1), grab_anywhere=False)
while True:
    event, values = window.read()
    if event == 'getf':
        text = sg.popup_get_file('请点击浏览键或自行填入文件绝对路径',title = '获取文件',file_types = (("Excel Files", "*.xlsx"),("Excel Files", "*.xls"),))
        sg.popup('提示', '是否确认选择文件---', text)
        window['lujing'].update(text)      
    if event == "look":
        if values["lujing"] != None:
            if values['dup'] == True:
                df = pd.read_excel(values['lujing'])
                imfor = df[df.duplicated()]
#                imfor = str(imfor)
                if df[df.duplicated()].empty == False:
                    sg.popup_scrolled(imfor,size=(100,10),title = '重复值信息')
                if df[df.duplicated()].empty == True:
                    sg.popup('所选数据信息中没有重复值！',title = '提示')                                     
            if values['mis'] == True:
                df = pd.read_excel(values['lujing'])
                imfor1 = df.isnull().sum()
                imfor1 = str(imfor1)
                sg.popup_scrolled(imfor1,size=(20,20),title = '每列缺失值统计')
            if values['war'] == True:
                df = pd.read_excel(values['lujing'])
                A = df.boxplot(rot = 45,figsize = (25,25))
                sg.popup_scrolled(image = A)
        if values["lujing"] == None:
             sg.popup('请输入路径！')
    if event == "handle":
        if values["lujing"] != None:
            if values['dup'] == True:
                df = pd.read_excel(values['lujing'])
                df = df.drop_duplicates(inplace = True)
                df.to_excel(values['lujing'])
                sg.popup('重复值处理成功，请在选择路径下查看文件',title = '提示')
            if values['mis'] == True:
                df = pd.read_excel(values['lujing'])
                df.fillna(method = 'pad',inplace = True)
                df.to_excel(values['lujing'])
                sg.popup('缺失值处理成功，请在选择路径下查看文件',title = '提示')
            if values['war'] == True:
                sg.popup('异常值处理主观性较大，请自行解决！',title = '提示')                
        if values["lujing"] == None:
             sg.popup('请输入路径！')        
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break    
    if event == "注意":
        sg.Popup("作用讲解：",
                 "重复值处理方法 ：采用删除重复行的方法",
                 "缺失值处理方法 ：用一列中的缺失值上面的数值替换缺失值",
                 "异常值处理方法 ：异常值处理方法引人而异，这里不设处理",
                 "加载查看与处理 ：用户使用步骤：选择数据文件路径---查看错误---处理错误")            
