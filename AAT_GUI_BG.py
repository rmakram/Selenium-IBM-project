# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:12:35 2022

@author: ZZ00I7865
"""
#pip install selenium
#pip install py-getch
#pip install pyinstaller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os
import csv
from datetime import datetime
import webbrowser
import tkinter as tk  
from tkinter import ttk
from tkinter.ttk import Label,Entry,Button
from tkinter import *
from tkinter import Toplevel
import sys

#-------------------------------------------------------------------------------------------------------------------------       
# In[1]:
#First: DOORS:
#------------------------------------------------------------------------------
#1.1 DOORS input data and login functions:
#1.1.1  DOORS input data functions:
#-----------------------------------------

def input_data_Doors_Assignees():
                global new
                global Assignment_Doors                
                Input_Assignment_Doors=Assignees_field.get()
                Assignment_Doors=Input_Assignment_Doors.split(',')
                for x in Assignment_Doors:
                    if str(x).strip()=='':
#                        print("""\nYou must not add any empty input data, please try again later..""")
                        new= Toplevel(win)
                        new.geometry("500x250")
                        new.grab_set()
                        new.title("ERROR")
                        Label(new, text="""User should provide Assignees Full Names""").pack()
                        Button(new, text="Close", command = close_toplevel_window).pack()
                        new.mainloop()
                        break

def input_Doors_Username():
                global new
                global user
                user=str(user_field.get())
#                user_field.delete('0', 'end')
                user=user.lower()
                if "alstomgroup.com" not in user:
                    new= Toplevel(win)
                    new.geometry("500x250")
                    new.grab_set()
                    new.title("ERROR")
                    Label(new, text="Username field is empty or not valid,\nplease enter username again").pack()
                    Button(new, text="Close", command = close_toplevel_window).pack()
                    new.mainloop()
                    
def input_data_Doors_IBM():
                global new
                global sender
                sender=str(ibm_field.get())
#                ibm_field.delete('0', 'end')
                sender=sender.lower()
                if "ibm.com" not in sender:
                    new= Toplevel(win)
                    new.geometry("500x250")
                    new.grab_set()
                    new.title("ERROR")
                    Label(new, text="""User should provide valid IBM Email""").pack()
                    Button(new, text="Close", command = close_toplevel_window).pack()
                    new.mainloop()

def input_Doors_Password():
    global new
    global myPass
    myPass=str(pswrd_field.get())
#    pswrd_field.delete('0', 'end')
    if myPass == "":
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="Password field is empty,\nplease enter password again").pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        new.mainloop()


#if CODE/PIN required:
def input_Doors_code():
        global code_field
        global new
        global browser
        Text = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div""")))
        Text2= WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div""")))
        if "Text" in Text.text:
            Text.click()
        else:
            Text2.click()
            
        new= Toplevel(win)
        new.geometry("250x250")
        new.grab_set()
        new.title("Service Now Code Request")
        Label(new, text="Enter Code").pack()
        code_field=Entry(new,show="*",width=25)
        code_field.pack()
        submit2=Button(new,text='Submit' , command = input_Doors_PIN)
        submit2.pack()
        new.mainloop()
        
def input_Doors_PIN():
        global new2
        global new
        PIN=code_field.get()
        code= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/input""")))
        code.clear()
        code.send_keys(PIN)
        Verify=browser.find_element_by_xpath("""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[6]/div/div/div/div/input""")
        Verify.click()
        try:
            YES= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input""")))
            YES.click()
            
            new2= Toplevel(new)
            new2.geometry("500x250")
            new2.grab_set()
            new2.title("Output")
            Label(new2, text="""Login Succeeded""").pack()
            Button(new2, text="Close", command = close_toplevel_window).pack()
            new2.mainloop()
            
        except:
            new2= Toplevel(new)
            new2.geometry("500x250")
            new2.grab_set()
            new2.title("ERROR")
            Label(new2, text="""Code is incorrect, please enter it again.""").pack()
            Button(new2, text="Close", command = close_toplevel_window2).pack()
            new2.mainloop()
            
#------------------------------------------------------------------------------
#1.1.2 DOORS Login PROGRAM_Function:
#-----------------------------------------
                
def login_Doors():
  global browser
  global DateTimeNow
  global new2
  global new
  DateTimeNow=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  input_Doors_Username()
  input_Doors_Password()
  try:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path="../chromedriver/chromedriver.exe", options=options)
    browser.get("https://alstom.service-now.com/nav_to.do?uri=%2Fhome.do")
    browser.set_window_size(1440, 900)
    try:
        account=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]""")))
        account.click()
    except:
        pass
    try:
        username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]""")))
        username.clear()
    except Exception as e:
#        print("\n"+DateTimeNow,"""ERROR: An error has occured while loading the driver. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured while loading the driver.\nKindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error occured while loading the driver '+str(e)+'\n')
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        browser.quit()
        new.mainloop()
        
    username.send_keys(user)
    next_button=browser.find_element_by_xpath("""//*[@id="idSIButton9"]""")
    next_button.click()
    time.sleep(5)
 
    password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input""")))
    password.clear()
    password.send_keys(myPass)
    SIGNIN=browser.find_element_by_xpath("""//*[@id="idSIButton9"]""")
    SIGNIN.click()
    time.sleep(5)
    
    try:
        input_Doors_code()
    except:
        pass

    YES= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input""")))
    YES.click()
    
    new2= Toplevel(win)
    new2.geometry("500x250")
    new2.grab_set()
    new2.title("Output")
    Label(new2, text="""Login Succeeded""").pack()
    Button(new2, text="Close", command = close_toplevel_window).pack()
    new2.mainloop()
           
  except Exception as e:
#       print("\n"+DateTimeNow,"""ERROR: An error has occured while logging in..,\nFor more details, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
       new2= Toplevel(win)
       new2.geometry("500x250")
       new2.grab_set()
       new2.title("ERROR")
       Label(new2, text="""An error has occured while logging in..,\nFor more details, kindly check the log file\n "Logs/logfile_AAT_DOORS.txt""").pack()
       Button(new2, text="Close", command = close_toplevel_window).pack()
       output11=(DateTimeNow+': Job failed with error: An error has occured while logging in..\n'+str(e)+'\n')
       with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
           f11.write(output11)
           f11.close()
       try:
           browser.quit()
       except:
           pass
       new2.mainloop()

#------------------------------------------------------------------------------
#1.2 DOORS Assign Tasks function:
#1.2.1: DOORS Assign SNOW_Function:
#-----------------------------------------

def assign_doors_tasks(Assignment):
    global new2
    global new
    try:
        j=len(Assignment)        
        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")
        while ARROW:
            try:
                i=0
                while i in range(0,j):
                    Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')     
                    string="DOORS"
                    if string in Summary:
                        Assigned=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""")
                        Assigned.click()
                        Assigned.clear()
                        Assigned.send_keys(str(Assignment[i]).strip())
                        Assigned.send_keys(u'\ue007')
                        time.sleep(3)
                        browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""").click()
                        time.sleep(3)
                        ticket_No=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]""").get_attribute('value')
                        Assignee=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""").get_attribute('value')
                        Assignee=str(Assignee).strip()
                        if  Assignee != "":
                            data=[ticket_No,Assignee,Summary]
                            with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'a', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                                f.close()
                            i=i+1
                        else:
                            with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'r') as f1:
                                No_of_Tasks  = -1
                                for row in f1:
                                    No_of_Tasks+= 1
                                f1.close()
#                            print("\n"+DateTimeNow,"Job Failed, No of Assigned DOORS Tasks= "+str(No_of_Tasks),""", ERROR: One or more of input Assignees is incorrect, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
                            new= Toplevel(win)
                            new.geometry("500x250")
                            new.grab_set()
                            new.title("ERROR")
                            Label(new, text="""Job Failed,\nNo. of Assigned DOORS Tasks= """+str(No_of_Tasks)+""",\nERROR: One or more of input Assignees is incorrect.\n For more details, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
                            Button(new, text="Close", command = close_toplevel_window).pack()
                            e=""" ,ERROR: One or more of input Assignees is incorrect - ARROW."""                            
                            output11=(DateTimeNow+": Job Failed, No of Assigned DOORS Tasks= "+str(No_of_Tasks)+str(e)+'\n')
                            with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
                                f11.write(output11)
                                f11.close()
                            browser.quit()
                            new.mainloop()   

                        time.sleep(3)
                        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")                    
                        ARROW.click()
                        time.sleep(3)
                    else:
                        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")
                        ARROW.click()
                        time.sleep(3)
            except:
                break
    
        try:
            BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
            BACK_ARROW.click()
        except:
            with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'r') as f1:
                No_of_Tasks  = -1
                for row in f1:
                    No_of_Tasks+= 1
                f1.close()
#            print("\n"+DateTimeNow,"Job Completed. No. of Assigned DOORS Tasks= "+str(No_of_Tasks))
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="Job Completed.\nNo. of Assigned DOORS Tasks= "+str(No_of_Tasks)).pack()
            Button(new, text="Close", command = close_toplevel_window).pack()
            output11=(DateTimeNow+": Job Completed. No. of Assigned DOORS Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            new.mainloop()
    
        while BACK_ARROW:
             try:
                time.sleep(3)
                if i>=j:
                    i=0
                while i in range(0,j):
                    Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')     
                    string="DOORS"
                    if string in Summary:
                        Assigned=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""")
                        Assigned.click()
                        Assigned.clear()
                        Assigned.send_keys(str(Assignment[i]).strip())
                        Assigned.send_keys(u'\ue007')
                        time.sleep(3)
                        browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""").click()
                        time.sleep(3)
                        ticket_No=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]""").get_attribute('value')
                        Assignee=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""").get_attribute('value')
                        Assignee=str(Assignee).strip()
                        if  Assignee != "":
                            data=[ticket_No,Assignee,Summary]
                            with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'a', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                                f.close()
                            i=i+1
                        else:
                            with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'r') as f1:
                                No_of_Tasks  = -1
                                for row in f1:
                                    No_of_Tasks+= 1
                                f1.close()
          #                  print("\n"+DateTimeNow,"Job Failed, No. of Assigned DOORS Tasks= "+str(No_of_Tasks),"""ERROR: One or more of input Assignees is incorrect, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
                            new= Toplevel(win)
                            new.geometry("500x250")
                            new.grab_set()
                            new.title("ERROR")
                            Label(new, text="Job Failed,\nNo. of Assigned DOORS Tasks= "+str(No_of_Tasks)+""",\nERROR: One or more of input Assignees is incorrect.\n For more deatils, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
                            Button(new, text="Close", command = close_toplevel_window).pack()
                            e=""" ,ERROR: One or more of input Assignees is incorrect - BACKARROW."""                            
                            output11=(DateTimeNow+": Job Failed, No of Assigned DOORS Tasks= "+str(No_of_Tasks)+str(e)+'\n')
                            with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
                                f11.write(output11)
                                f11.close()
                            browser.quit()
                            new.mainloop()

                        time.sleep(3)                                
                        BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
                        BACK_ARROW.click()
                        time.sleep(3)
                    else:
                        BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")
                        BACK_ARROW.click()
                        time.sleep(3)
             except:
                break
        
        with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'r') as f1:
            No_of_Tasks  = -1
            for row in f1:
                No_of_Tasks+= 1
            f1.close()
           
#        print("\n"+DateTimeNow,"Job Completed. No of Assigned DOORS Tasks= "+str(No_of_Tasks))
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="Job Completed. No of Assigned DOORS Tasks= "+str(No_of_Tasks)).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+": Job Completed. No of Assigned DOORS Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

    except Exception as e: 
 #       print("\n"+DateTimeNow,"""An error has occured, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured.\nFor more details,\nkindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()
        
#------------------------------------------------------------------------------
#1.2.2: DOORS Assign PROGRAM_Function:
#-----------------------------------------

def assigned_doors_tasks():
  global new2
  global new
  input_data_Doors_Assignees()
  try:
    browser.switch_to.parent_frame()
  except: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="You have to login first.").pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    new.mainloop()    
  try:  
    Menu = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
    Menu.click()
    try:
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[8]/div/div/a/div/div""")
        WORK.click()
    except:
        SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
        SD.click()
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[8]/div/div/a/div/div""")
        WORK.click()
        
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
    search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
    search_filter.click()
    search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
    search_Number.click()
    search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
    search_button.click()
    search_button.clear()
    search_button.send_keys("TASK")
#Press_Enter:
    search_button.send_keys(u'\ue007')
    time.sleep(2)
    
  except Exception as e: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""An error has occured.\nFor more details,\nkindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
    with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
        f11.write(output11)
        f11.close()
    new.mainloop()
    
  try:
    tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
    row = tbody.find_elements_by_tag_name("tr")[0]
    t_No = row.find_elements_by_tag_name("td")[2]
    t_No.click()
    
    header=["ticket_No","Assignee","Summary"]
    with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        f.close()

#CALL SNOW FUNCTION:
    assign_doors_tasks(Assignment_Doors)
            
  except Exception as e:
#    print ("""Seems there were no AAT Tasks in the queue or error occured..""")
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""Seems there were no AAT Tasks in the queue or error occured..\nFor more details,\nkindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    output11=(DateTimeNow+""": Seems there were no AAT Tasks in the queue or error occured..\n"""+str(e))
    with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
        f11.write(output11)
        f11.close()
    new.mainloop()
    
    
#------------------------------------------------------------------------------
#1.3 DOORS Extract users' data from tasks function:
#1.3.1: DOORS Extract users' data SNOW_Function:
#-----------------------------------------

def Add_Doors_Users_info_to_CSV():
            global ticket_No
            browser.switch_to.parent_frame()
            browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""").clear()
            T_Number=browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""")
            T_Number.send_keys(ticket_No)
            T_Number.send_keys(u'\ue007')
            time.sleep(5)
            browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
            Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')        
            Doors_DB="IBM Rational Engineering Toolsuite(Rational_DOORS)_SUB || Add Access"
            DCP_DB="DOORS Collaboration platform || Add Access"
            Doors_DB_Leaver="IBM Rational Engineering Toolsuite(Rational_DOORS)_SUB || Leaver"
            Doors_DB_Remove="IBM Rational Engineering Toolsuite(Rational_DOORS)_SUB || Remove Access"
            Doors_DCP_Leaver="DOORS Collaboration platform || Leaver"
            Doors_DCP_Remove="DOORS Collaboration platform || Remove Access"
            time.sleep(3)
            if Doors_DB in Summary:
                Full_Name=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/input""").get_attribute('value')
                browser.find_element_by_xpath("""//*[@id="tabs2_section"]/span[3]/span[1]""").click()
                time.sleep(2)
                email= browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[3]/td/span/div/div[2]/table/tbody/tr/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[6]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID2=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[7]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                Alstom_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/span/div[2]/div[1]/table/tbody/tr[2]/td/div/div/div/div[2]/input[2]""").get_attribute('value')     
                if SSO_ID=="" or SSO_ID.isnumeric():
                    if SSO_ID2=="" or SSO_ID2.isnumeric():
                        SSO_ID=Alstom_ID
                    else:
                        SSO_ID=SSO_ID2
                string="Group"
                Groups=[]
                Description=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[2]/table/tbody/tr[2]/td/div/div/div/div[2]/input""").get_attribute('value')
                for line in Description.split('\n'):
                    line = line.strip('\r')
                    if string in line:
                        sline = line.split()
                        group=sline[1]
                        if group not in Groups:
                            Groups.append(group)
                        groups=''
                        for i in Groups:
                            groups+=i+';'
                        groups=groups.rstrip(';')
                data=[sender,ticket_No,SSO_ID,Full_Name,email,groups]
                with open('../files/DOORS/users_doors.csv', 'a', encoding='UTF8', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(data)
                            f.close()
            elif DCP_DB in Summary:
                Full_Name=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/input""").get_attribute('value')
                browser.find_element_by_xpath("""//*[@id="tabs2_section"]/span[3]/span[1]""").click()
                time.sleep(2)
                email= browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[3]/td/span/div/div[2]/table/tbody/tr/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[6]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID2=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[7]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                Alstom_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/span/div[2]/div[1]/table/tbody/tr[2]/td/div/div/div/div[2]/input[2]""").get_attribute('value')     
                if SSO_ID=="" or SSO_ID.isnumeric():
                    if SSO_ID2=="" or SSO_ID2.isnumeric():
                        SSO_ID=Alstom_ID
                    else:
                        SSO_ID=SSO_ID2
                string="Group: "
                other_groups=["eXchange","AME RM Team","GlobalACL"]
                Groups=[]
                groups=''
                Description=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[2]/table/tbody/tr[2]/td/div/div/div/div[2]/input""").get_attribute('value')                
                for line in Description.split('\n'):
                    line = line.strip('\r')
                    if string in line:
                        line=line.lstrip(string)
                        sline = line.split(' || ')
                        for i in sline:
                            if i[0] == '_' or i in other_groups:
                                if i=="_ROLE_Engineer":
                                    i="_ROLE_ScopeEngineer"
                                elif i=="_DataModelAdministrator":
                                    i="__DataModelAdmins"
                                if i not in Groups:
                                    Groups.append(i)
                for i in Groups:
                    groups+=i+';'
                groups=groups.rstrip(';')
                data=[sender,ticket_No,SSO_ID,Full_Name,email,groups]
                with open('../files/DOORS/users_dcp.csv', 'a', encoding='UTF8', newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow(data)
                                    f.close()
            elif Doors_DB_Leaver in Summary or Doors_DB_Remove in Summary:
                email= browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[3]/td/span/div/div[2]/table/tbody/tr/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[6]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID2=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[7]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                Alstom_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/span/div[2]/div[1]/table/tbody/tr[2]/td/div/div/div/div[2]/input[2]""").get_attribute('value')     
                if SSO_ID=="" or SSO_ID.isnumeric():
                    if SSO_ID2=="" or SSO_ID2.isnumeric():
                        SSO_ID=Alstom_ID
                    else:
                        SSO_ID=SSO_ID2
                data=[ticket_No,SSO_ID,email,Summary]
                with open('../files/DOORS/users_doors_leaver.csv', 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                    f.close()
            elif Doors_DCP_Leaver in Summary or Doors_DCP_Remove in Summary:
                email= browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[3]/td/span/div/div[2]/table/tbody/tr/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[6]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID2=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[7]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                Alstom_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/span/div[2]/div[1]/table/tbody/tr[2]/td/div/div/div/div[2]/input[2]""").get_attribute('value')     
                if SSO_ID=="" or SSO_ID.isnumeric():
                    if SSO_ID2=="" or SSO_ID2.isnumeric():
                        SSO_ID=Alstom_ID
                    else:
                        SSO_ID=SSO_ID2
                data=[ticket_No,SSO_ID,email,Summary]
                with open('../files/DOORS/users_dcp_leaver.csv', 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                    f.close()

#-------------------------------------------------------------
#1.3.2: DOORS Extract users' data PROGRAM_Function:
#-----------------------------------------
      
def AAT_TO_CSV_Doors():
    global new
    global new2
    input_data_Doors_IBM()
    try:
        browser.switch_to.parent_frame()
    except:
#       print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="You have to login first.").pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        new.mainloop()    
    try:
        header1=["sender","ticket_No","SSO_ID","Full_Name","email","groups"]
        header2=["ticket_No","SSO_ID","Email","Summary"]
        with open('../files/DOORS/users_doors.csv', 'w', encoding='UTF8', newline='') as f1:
            writer = csv.writer(f1)
            writer.writerow(header1)
            f1.close()
        with open('../files/DOORS/users_dcp.csv', 'w', encoding='UTF8', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow(header1)
            f2.close()
        with open('../files/DOORS/users_doors_leaver.csv', 'w', encoding='UTF8', newline='') as f3:
            writer = csv.writer(f3)
            writer.writerow(header2)
            f3.close()
        with open('../files/DOORS/users_dcp_leaver.csv', 'w', encoding='UTF8', newline='') as f4:
            writer = csv.writer(f4)
            writer.writerow(header2)
            f4.close()

        Menu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
        Menu.click()
        try:
            WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
            WORK.click()
        except:
            SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
            SD.click()
            WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
            WORK.click()
            
        time.sleep(3)
        browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
        search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
        search_filter.click()
        search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
        search_Number.click()
        search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
        search_button.click()
        search_button.clear()
        search_button.send_keys("TASK")
        search_button.send_keys(u'\ue007')
        time.sleep(2)
        
        tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
        rows = tbody.find_elements_by_tag_name("tr")
        tasks=[]
        while rows:
            try:
                tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
                rows = tbody.find_elements_by_tag_name("tr")
                for row in rows:
                    tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
                    rows = tbody.find_elements_by_tag_name("tr")
                    t_No = row.find_elements_by_tag_name("td")[2].text
                    tasks.append(t_No)
                next_page=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/div[2]/span[2]/button[3]""")
                next_page.click()
                time.sleep(3)
            except:
                break  
        No_of_Tasks=len(tasks)
        if No_of_Tasks == 0:
#            print ("""There is no AAT Tasks in the queue, please try again later..""")
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="""There is no AAT Tasks in the queue..\nFor more details, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
            Button(new, text="Close", command = close_toplevel_window).pack()
            output11=(DateTimeNow+": Job completed, No of requested Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            new.mainloop()
        else:
            global ticket_No
#CALL SNOW FUNCTION:
            for ticket_No in tasks:
                Add_Doors_Users_info_to_CSV()

  #      print("\n"+DateTimeNow,"Job completed, No of Tasks= "+str(No_of_Tasks))
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="Job completed, No of requested Tasks= "+str(No_of_Tasks)+'\n').pack()
            Button(new, text="Close", command = close_toplevel_window).pack()
            output11=(DateTimeNow+": Job completed, No of requested Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            new.mainloop()
            
    except Exception as e: 
#        print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured.\nFor more details, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

#------------------------------------------------------------------------------
#1.4 DOORS Tasks Closure function:
#1.4.1  DOORS CLOSURE SNOW_Function:
#-----------------------------------------
        
def AAT_Doors_closure():
            browser.switch_to.parent_frame()
            browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""").clear()
            T_Number=browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""")
            T_Number.send_keys(ticket_No)
            T_Number.send_keys(u'\ue007')
            time.sleep(3)
            browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
            Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')        
            Doors_DB="IBM Rational Engineering Toolsuite(Rational_DOORS)_SUB || Add Access"
            DCP_DB="DOORS Collaboration platform || Add Access"
            Doors_DB_Leaver="IBM Rational Engineering Toolsuite(Rational_DOORS)_SUB || Leaver"
            Doors_DB_Remove="IBM Rational Engineering Toolsuite(Rational_DOORS)_SUB || Remove Access"
            Doors_DCP_Leaver="DOORS Collaboration platform || Leaver"
            Doors_DCP_Remove="DOORS Collaboration platform || Remove Access"
            try:
                Notes=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[1]/span[1]/span[2]""")
                Notes.click()
            except:
                pass
            global counter2
            if Doors_DB in Summary:
                with open('../files/DOORS/addUserslogFile.txt', 'r') as f:
                    for line in f:
                        if ticket_No in line:
                            line=line.split(',')
                            output=str(line[2]).strip()
                            try:
                                WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/textarea""")
                                WORKNOTES.click()
                                WORKNOTES.send_keys(output)
                            except:
                                WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/textarea""")
                                WORKNOTES.click()
                                WORKNOTES.send_keys(output)
                            Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                            Assigned.select_by_value('2')
                            time.sleep(2)
                            SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                            SAVE.click()
                            time.sleep(2)
                            Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                            Assigned.select_by_value('3')
                            time.sleep(2)
                            RES_INFO=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]""")
                            RES_INFO.click()
                            RES_INFO_INPUT=browser.find_element_by_xpath("""//*[@id="sc_task.close_notes"]""")
                            RES_INFO_INPUT.click()
                            RES_INFO_INPUT2= browser.find_element_by_css_selector("""#sc_task\.close_notes""")
                            RES_INFO_INPUT2.send_keys(output)
                            SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                            SAVE.click()
                            f.close()
                            counter2 += 1
                            break
                    else:
                        data=(ticket_No+" || "+Summary+"\n")
                        with open('../files/DOORS/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                            f.write(data)
                            f.close()
                            
            elif DCP_DB in Summary:
                with open('../files/DOORS/addUserslogFile_DCP.txt', 'r') as f:
                    for line in f:
                        if ticket_No in line:
                            line=line.split(',')
                            output=str(line[2]).strip()
                            try:
                                WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/textarea""")
                                WORKNOTES.click()
                                WORKNOTES.send_keys(output)
                            except:
                                WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/textarea""")
                                WORKNOTES.click()
                                WORKNOTES.send_keys(output)
                            Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                            Assigned.select_by_value('2')
                            time.sleep(2)
                            SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                            SAVE.click()
                            time.sleep(2)
                            Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                            Assigned.select_by_value('3')
                            time.sleep(2)
                            RES_INFO=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]""")
                            RES_INFO.click()
                            RES_INFO_INPUT=browser.find_element_by_xpath("""//*[@id="sc_task.close_notes"]""")
                            RES_INFO_INPUT.click()
                            RES_INFO_INPUT2= browser.find_element_by_css_selector("""#sc_task\.close_notes""")
                            RES_INFO_INPUT2.send_keys(output)
                            SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                            SAVE.click()
                            f.close()
                            counter2 += 1
                            break
                    else:
                        data=(ticket_No+" || "+Summary+"\n")
                        with open('../files/DOORS/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                            f.write(data)
                            f.close()            
                            
            elif Doors_DB_Leaver in Summary or Doors_DB_Remove in Summary:
                with open('../files/DOORS/deletedUserslogFile.txt', 'r') as f:
                    for line in f:
                        if ticket_No in line:
                            if "deleted" in line:                           
                                output="""The mentioned DOORS account has been deleted from production and pre-production Doors environments."""
                                try:
                                    WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/textarea""")
                                    WORKNOTES.click()
                                    WORKNOTES.send_keys(output)
                                except:
                                    WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/textarea""")
                                    WORKNOTES.click()
                                    WORKNOTES.send_keys(output)
                                Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                                Assigned.select_by_value('2')
                                time.sleep(2)
                                SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                                SAVE.click()
                                time.sleep(2)
                                Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                                Assigned.select_by_value('3')
                                time.sleep(2)
                                RES_INFO=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]""")
                                RES_INFO.click()
                                RES_INFO_INPUT=browser.find_element_by_xpath("""//*[@id="sc_task.close_notes"]""")
                                RES_INFO_INPUT.click()
                                RES_INFO_INPUT2= browser.find_element_by_css_selector("""#sc_task\.close_notes""")
                                RES_INFO_INPUT2.send_keys(output)
                                SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                                SAVE.click()
                                f.close()
                                counter2 += 1
                                break
                    else:
                        data=(ticket_No+" || "+Summary+"\n")
                        with open('../files/DOORS/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                            f.write(data)
                            f.close()

            elif Doors_DCP_Leaver in Summary or Doors_DCP_Remove in Summary:
                with open('../files/DOORS/deletedUserslogFile_DCP.txt', 'r') as f:
                    for line in f:
                        if ticket_No in line:
                            if "deleted" in line:                           
                                output="""The mentioned DOORS account has been deleted from Doors DCP environment."""                        
                                try:
                                    WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/textarea""")
                                    WORKNOTES.click()
                                    WORKNOTES.send_keys(output)
                                except:
                                    WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/textarea""")
                                    WORKNOTES.click()
                                    WORKNOTES.send_keys(output)
                                Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                                Assigned.select_by_value('2')
                                time.sleep(2)
                                SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                                SAVE.click()
                                time.sleep(2)
                                Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                                Assigned.select_by_value('3')
                                time.sleep(2)
                                RES_INFO=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]""")
                                RES_INFO.click()
                                RES_INFO_INPUT=browser.find_element_by_xpath("""//*[@id="sc_task.close_notes"]""")
                                RES_INFO_INPUT.click()
                                RES_INFO_INPUT2= browser.find_element_by_css_selector("""#sc_task\.close_notes""")
                                RES_INFO_INPUT2.send_keys(output)
                                SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                                SAVE.click()
                                f.close()
                                counter2 += 1
                                break
                    else:
                        data=(ticket_No+" || "+Summary+"\n")
                        with open('../files/DOORS/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                            f.write(data)
                            f.close()            
            
            else:
                data=(ticket_No+" || "+Summary+"\n")
                with open('../files/DOORS/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                    f.write(data)
                    f.close()
                    
                    
#-----------------------------------------
#1.4.2  DOORS CLOSURE PROGRAM_Function:
#-----------------------------------------
                    
def Ticket_Closure_Doors():                 
  global new
  global new2
  try:
    browser.switch_to.parent_frame()
  except: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="You have to login first.").pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    new.mainloop()
  try:    
    try:
        with open('../files/DOORS/addUserslogFile.txt', 'r') as f1:
            f1.close()
    except:
        with open('../files/DOORS/addUserslogFile.txt', 'w', encoding='UTF8', newline="") as f1:
            f1.close()
    try:
        with open('../files/DOORS/addUserslogFile_DCP.txt', 'r') as f2:
            f2.close()
    except:
        with open('../files/DOORS/addUserslogFile_DCP.txt', 'w', encoding='UTF8', newline="") as f2:
            f2.close()
    try:
        with open('../files/DOORS/deletedUserslogFile.txt', 'r') as f3:
            f3.close()
    except:
        with open('../files/DOORS/deletedUserslogFile.txt', 'w', encoding='UTF8', newline="") as f3:
            f3.close()
    try:
        with open('../files/DOORS/deletedUserslogFile_DCP.txt', 'r') as f4:
            f4.close()
    except:
        with open('../files/DOORS/deletedUserslogFile_DCP.txt', 'w', encoding='UTF8', newline="") as f4:
            f4.close()            
        
    with open('../files/DOORS/to_be_checked.txt', 'w', encoding='UTF8', newline="") as f5:
        f5.close()
    
    time.sleep(5)
    
    Menu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
    Menu.click()
    try:
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
        WORK.click()
    except:
        SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
        SD.click()
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
        WORK.click()
        
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
    search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
    search_filter.click()
    search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
    search_Number.click()
    search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
    search_button.click()
    search_button.clear()
    search_button.send_keys("TASK")
    search_button.send_keys(u'\ue007')
    time.sleep(2)
    
    tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
    rows = tbody.find_elements_by_tag_name("tr")
    tasks=[]
    while rows:
        try:
            tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
            rows = tbody.find_elements_by_tag_name("tr")
            for row in rows:
                tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
                rows = tbody.find_elements_by_tag_name("tr")
                t_No = row.find_elements_by_tag_name("td")[2].text
                tasks.append(t_No)
            next_page=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/div[2]/span[2]/button[3]""")
            next_page.click()
            time.sleep(3)
        except:
            break  
        
    No_of_Tasks=len(tasks)
    global counter2
    counter2=0
    if No_of_Tasks == 0:
#        print ("""There is no AAT Tasks in the queue, please try again later..""")
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="""There is no AAT Tasks in the queue.\nFor more details, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+": Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline="\n") as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

    else:
        global ticket_No
#Calling SNOW function:
        for ticket_No in tasks:
            AAT_Doors_closure()
    
#    print("\n"+DateTimeNow,"Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks))
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks)).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+": Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline="\n") as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

  except Exception as e: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""An error has occured. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """).pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    output11=(DateTimeNow+': Job failed with error: '+str(e)+"\n")
    with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline="") as f11:
        f11.write(output11)
        f11.close()
    new.mainloop()
    
#------------------------------------------------------------------------------
#1.5 DOORS Open file functions:
#-----------------------------------------    
def AAT_DOORS_Logfile():
        with open('../Logs/logfile_AAT_DOORS.txt', 'a', encoding='UTF8', newline="") as f1:
            f1.close()
        webbrowser.open('..\\Logs\\logfile_AAT_DOORS.txt')
    
def AAT_Assigned_Doors_Tasks():
    try:
        with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'r') as f:
            f.close()
        webbrowser.open('..\\files\\DOORS\\Assigned_Doors_Tickets.csv')
    except:
        header=["ticket_No","Assignee","Summary"]
        with open('../files/DOORS/Assigned_Doors_Tickets.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        f.close()
        webbrowser.open('..\\files\\DOORS\\Assigned_Doors_Tickets.csv')      
       
def to_be_checked_Doors():
    try:
        with open('../files/DOORS/to_be_checked.txt', 'r') as f1:
            f1.close()
        webbrowser.open('..\\files\\DOORS\\to_be_checked.txt') 
    except:
        with open('../files/DOORS/to_be_checked.txt', 'w', encoding='UTF8', newline="") as f1:
            f1.close()
        webbrowser.open('..\\files\\DOORS\\to_be_checked.txt')

#-------------------------------------------------------------------------------
        
def Add_Delete_Doors_Tasks():
    header1=["sender","ticket_No","SSO_ID","Full_Name","email","groups"]
    header2=["ticket_No","SSO_ID","Email","Summary"]
    try:
        with open('../files/DOORS/users_doors.csv', 'r') as f1:
            f1.close()
        webbrowser.open('..\\files\\DOORS\\users_doors.csv')
    except:
        with open('../files/DOORS/users_doors.csv', 'w', encoding='UTF8', newline='') as f1:
            writer = csv.writer(f1)
            writer.writerow(header1)
            f1.close()   
        webbrowser.open('..\\files\\DOORS\\users_doors.csv')        
    try:
        with open('../files/DOORS/users_dcp.csv', 'r') as f2:
            f2.close()
        webbrowser.open('..\\files\\DOORS\\users_dcp.csv')         
    except:
        with open('../files/DOORS/users_dcp.csv', 'w', encoding='UTF8', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow(header1)
            f2.close()  
        webbrowser.open('..\\files\\DOORS\\users_dcp.csv')   
    try:
        with open('../files/DOORS/users_doors_leaver.csv', 'r') as f3:
            f3.close()
        webbrowser.open('..\\files\\DOORS\\users_doors_leaver.csv')    
    except:
        with open('../files/DOORS/users_doors_leaver.csv', 'w', encoding='UTF8', newline='') as f3:
            writer = csv.writer(f3)
            writer.writerow(header2)
            f3.close()        
        webbrowser.open('..\\files\\DOORS\\users_doors_leaver.csv')
    try:
         with open('../files/DOORS/users_dcp_leaver.csv', 'r') as f4:
            f4.close()
         webbrowser.open('..\\files\\DOORS\\users_dcp_leaver.csv') 
    except:
        with open('../files/DOORS/users_dcp_leaver.csv', 'w', encoding='UTF8', newline='') as f4:
            writer = csv.writer(f4)
            writer.writerow(header2)
            f4.close()                
        webbrowser.open('..\\files\\DOORS\\users_dcp_leaver.csv')

#-------------------------------------------------------------------------------
#1.6: DOORS Call DXL Scripts:  
#--------------------------------------
def add_users_doors():
    os.system("..\\DXL_Scripts\\add_users_and_validate_DOORS\\addusersfromdxl.bat")

def add_users_doors_validation():
    os.system("..\\DXL_Scripts\\add_users_and_validate_DOORS\\validation.bat")
    
def add_users_doors_validationFailed():
    os.system("..\\DXL_Scripts\\add_users_and_validate_DOORS\\addUsersFromCSV-ValidationFailed.bat")

def add_users_doors_validation_logs():
    try:
        with open('../files/DOORS/ValidationFailed_users.csv') as f:
            f.close()
        webbrowser.open('..\\files\\DOORS\\ValidationFailed_users.csv') 
    except:            
        header90=['sender','ticket_No','SSO_ID','Full_Name','email','groups']
        with open('../files/DOORS/ValidationFailed_users.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header90)
            f.close()
        webbrowser.open('..\\files\\DOORS\\ValidationFailed_users.csv') 

def add_users_doors_logs():
    with open('../files/DOORS/addUserslogFile.txt', 'a', encoding='UTF8', newline="") as f1:
        f1.close()
    webbrowser.open('..\\files\\DOORS\\addUserslogFile.txt')
    
#------------------------------------------------------------------------------
    
def add_users_dcp():
    os.system("..\\DXL_Scripts\\add_users_and_validate_DCP\\addusersfromdxl.bat")

def add_users_dcp_validation():
    os.system("..\\DXL_Scripts\\add_users_and_validate_DCP\\validation.bat")
    
def add_users_dcp_validationFailed():
    os.system("..\\DXL_Scripts\\add_users_and_validate_DCP\\addUsersFromCSV-ValidationFailed.bat")
    
def add_users_dcp_validation_logs():
    try:
        with open('../files/DOORS/ValidationFailed_users_dcp.csv') as f:
            f.close()
        webbrowser.open('..\\files\\DOORS\\ValidationFailed_users_dcp.csv') 
    except:            
        header90=['sender','ticket_No','SSO_ID','Full_Name','email','groups']
        with open('../files/DOORS/ValidationFailed_users_dcp.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header90)
            f.close()
        webbrowser.open('..\\files\\DOORS\\ValidationFailed_users_dcp.csv')

def add_users_dcp_logs():
    with open('../files/DOORS/addUserslogFile_DCP.txt', 'a', encoding='UTF8', newline="") as f1:
        f1.close()
    webbrowser.open('..\\files\\DOORS\\addUserslogFile_DCP.txt')
    
#------------------------------------------------------------------------------
    
def disable_users_doors_PREPROD():
    os.system("..\\DXL_Scripts\\disable_and_delete_user_DOORS\\disableUsersFromCSV-PREPROD.bat")

def delete_users_doors_PREPROD():
    os.system("..\\DXL_Scripts\\disable_and_delete_user_DOORS\\deletingUsersFromCSV-PREPROD.bat")

def disable_users_doors_PREPROD_logs():
    with open('../files/DOORS/disableUserslogFile-PREPROD.txt', 'a', encoding='UTF8', newline="") as f1:
        f1.close()
    webbrowser.open('..\\files\\DOORS\\disableUserslogFile-PREPROD.txt')
 
def delete_users_doors_PREPROD_logs():
        with open('../files/DOORS/deletedUserslogFile-PREPROD.txt', 'a', encoding='UTF8', newline='') as f4:
            f4.close()
        webbrowser.open('..\\files\\DOORS\\deletedUserslogFile-PREPROD.txt') 

#------------------------------------------------------------------------------
        
def disable_users_doors():        
    os.system("..\\DXL_Scripts\\disable_and_delete_user_DOORS\\disableUsersFromCSV.bat")

def delete_users_doors():
    os.system("..\\DXL_Scripts\\disable_and_delete_user_DOORS\\deletingUsersFromCSV.bat")

def disable_users_doors_logs():
    with open('../files/DOORS/disableUserslogFile.txt', 'a', encoding='UTF8', newline="") as f1:
        f1.close()
    webbrowser.open('..\\files\\DOORS\\disableUserslogFile.txt')   

def delete_users_doors_logs():
        with open('../files/DOORS/deletedUserslogFile.txt', 'a', encoding='UTF8', newline='') as f4:
            f4.close()
        webbrowser.open('..\\files\\DOORS\\deletedUserslogFile.txt') 
        

#------------------------------------------------------------------------------
        
def disable_users_dcp():
    os.system("..\\DXL_Scripts\\disable_and_delete_user_DCP\\disableUsersFromCSV.bat")

def delete_users_dcp():
    os.system("..\\DXL_Scripts\\disable_and_delete_user_DCP\\deletingUsersFromCSV.bat")

def disable_users_dcp_logs():
    with open('../files/DOORS/disableUserslogFile_DCP.txt', 'a', encoding='UTF8', newline="") as f1:
        f1.close()
    webbrowser.open('..\\files\\DOORS\\disableUserslogFile_DCP.txt')
    
def delete_users_dcp_logs():
        with open('../files/DOORS/deletedUserslogFile_DCP.txt', 'a', encoding='UTF8', newline='') as f4:
            f4.close()
        webbrowser.open('..\\files\\DOORS\\deletedUserslogFile_DCP.txt')

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------       
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------       
# In[2]:
#Second: Synergy:
#------------------------------------------------------------------------------
#2.1 Synergy Open files function:
#-----------------------------------------
        
def AAT_Synergy_Tasks_log():
        with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline="") as f1:
            f1.close()
        webbrowser.open('..\\Logs\\logfile_AAT_SYNERGY.txt')
    
def Transferring_synergy_tasks_Logs():
    try:
        with open('../files/SYNERGY/Transferred_Tickets.csv', 'r') as f:
            f.close()
        webbrowser.open('..\\files\\SYNERGY\\Transferred_Tickets.csv')
    except:
        header=["ticket_No","Summary"]
        with open('../files/SYNERGY/Transferred_Tickets.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        f.close()
        webbrowser.open('..\\files\\SYNERGY\\Transferred_Tickets.csv')
        
#------------------------------------------------------------------------------
#2.2 Synergy input data functions:
#-----------------------------------------
        
def input_Synergy_Username():
                global user
                global new
                user=str(user_field3.get())
#                user_field3.delete('0', 'end')
                user=user.lower()
                if user == "" or "@alstomgroup.com" not in user:
                    new= Toplevel(win)
                    new.geometry("500x250")
                    new.grab_set()
                    new.title("ERROR")
                    Label(new, text="Username field is empty or not valid,\nplease enter username again").pack()
                    Button(new, text="Close", command = close_toplevel_window).pack()
                    new.mainloop()

def input_Synergy_Password():
    global myPass
    global new
    myPass=str(pswrd_field3.get())
    pswrd_field3.delete('0', 'end')
    if myPass == "":
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="Password field is empty,\nplease enter password again").pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        new.mainloop()
        
def input_Synergy_Code():
        global code_field
        global new
        global browser
        Text = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div""")))
        Text2= WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div""")))
        if "Text" in Text.text:
            Text.click()
        else:
            Text2.click()
            
        new= Toplevel(win)
        new.geometry("250x250")
        new.grab_set()
        new.title("Service Now Code Request")
        Label(new, text="Enter Code").pack()
        code_field=Entry(new,show="*",width=25)
        code_field.pack()
        submit2=Button(new,text='Submit' , command = input_Synergy_PIN_and_Assign)
        submit2.pack()
        new.mainloop()

def input_Synergy_PIN_and_Assign():
        global new2
        global new
        PIN=code_field.get()
        code= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/input""")))
        code.clear()
        code.send_keys(PIN)
        Verify=browser.find_element_by_xpath("""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[6]/div/div/div/div/input""")
        Verify.click()
        try:
            YES= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input""")))
            YES.click()
            close_toplevel_window()
        except:
            new2= Toplevel(new)
            new2.geometry("500x250")
            new2.grab_set()
            new2.title("ERROR")
            Label(new2, text="""Code is incorrect, please enter it again.""").pack()
            Button(new2, text="Close", command = close_toplevel_window2).pack()
            new2.mainloop()
#Call transfer function:      
        Transferring_synergy_tasks()    


#------------------------------------------------------------------------------
#2.3 Synergy login and Transfer tasks functions:
#2.3.1 Synergy Transfer SNOW_Function:
#-----------------------------------------

def transfer_tasks_synergy():
    global new
    global new2
    try:
        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")
        while ARROW:
            try:
                    Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')     
                    string="SYNERGY"
                    if string in Summary:
                        Assigned=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[3]/div[2]/div[2]/input""")
                        Assigned.click()
                        Assigned.clear()
                        Assigned.send_keys(str("""IBM-AS-Identity and access mgmt"""))
                        Assigned.send_keys(u'\ue007')
                        time.sleep(3)
                #save button:
                        browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""").click()
                        time.sleep(3)
                        ticket_No=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]""").get_attribute('value')
                        data=[ticket_No,Summary]
                        with open('../files/SYNERGY/Transferred_Tickets.csv', 'a', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                                f.close()
                        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")                    
                        ARROW.click()
                        time.sleep(3)
                    else:
                        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")
                        ARROW.click()
                        time.sleep(3)
            except:
                break
    
        try:
            BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
            BACK_ARROW.click()
        except:
            with open('../files/SYNERGY/Transferred_Tickets.csv', 'r') as f1:
                No_of_Tasks  = -1
                for row in f1:
                    No_of_Tasks+= 1
                f1.close()
#            print("\n"+DateTimeNow,"Job Completed. No of Tansferred SYNERGY Tasks= "+str(No_of_Tasks))
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="""Job Completed. \nNo. of Tansferred SYNERGY Tasks= """+str(No_of_Tasks)).pack()
            Button(new, text="Close", command = close_toplevel_window).pack()  
            output11=(DateTimeNow+": Job Completed. No of Tansferred SYNERGY Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            browser.quit()
            new.mainloop()
    
        while BACK_ARROW:
            try:
                    Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')     
                    string="SYNERGY"
                    if string in Summary:
                        Assigned=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[3]/div[2]/div[2]/input""")
                        Assigned.click()
                        Assigned.clear()
                        Assigned.send_keys(str("""IBM-AS-Identity and access mgmt"""))
                        Assigned.send_keys(u'\ue007')
                        time.sleep(3)
                        #save button:
                        browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""").click()
                        time.sleep(3)
                        ticket_No=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]""").get_attribute('value')
                        data=[ticket_No,Summary]
                        with open('../files/SYNERGY/Transferred_Tickets.csv', 'a', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                                f.close()
                        BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
                        BACK_ARROW.click()
                        time.sleep(3)
                    else:
                        BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
                        BACK_ARROW.click()
                        time.sleep(3)
            except:
                break
        
        with open('../files/SYNERGY/Transferred_Tickets.csv', 'r') as f1:
            No_of_Tasks  = -1
            for row in f1:
                No_of_Tasks+= 1
            f1.close()
           
#        print("\n"+DateTimeNow,"Job Completed. No of Tansferred SYNERGY Tasks= "+str(No_of_Tasks))
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="""Job Completed. \nNo. of Tansferred SYNERGY Tasks= """+str(No_of_Tasks)).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()  
        output11=(DateTimeNow+": Job Completed. No. of Tansferred SYNERGY Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        browser.quit()
        new.mainloop()

    except Exception as e: 
#        print("\n"+DateTimeNow,"""An error has occured, kindly check the log file "Logs/logfile_AAT_SYNERGY.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""Job Failed,\nNo. of Tansferred SYNERGY Tasks= """+str(No_of_Tasks)).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()        
        output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
        with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        browser.quit()
        new.mainloop()

#-----------------------------------------        
#2.3.2 Synergy Transfer PROGRAM_Function:
#-----------------------------------------

def Transferring_synergy_tasks():
  global new
  global new2
  try:
    Menu = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
    Menu.click()
    try:
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[8]/div/div/a/div/div""")
        WORK.click()
    except:
        SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
        SD.click()
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[8]/div/div/a/div/div""")
        WORK.click()
        
    time.sleep(3)
#Switch_to_frame
    browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
    search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
    search_filter.click()
    search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
    search_Number.click()
    search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
    search_button.click()
    search_button.clear()
    search_button.send_keys("TASK")
#ENTER BUTTON:    
    search_button.send_keys(u'\ue007')
    time.sleep(2)
    try:        
        header=["ticket_No","Summary"]
        with open('../files/SYNERGY/Transferred_Tickets.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        f.close()
        
        tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
        row = tbody.find_elements_by_tag_name("tr")[0]
        t_No = row.find_elements_by_tag_name("td")[2]
        t_No.click()
                        
    except Exception as e:
#        print ("""There is no AAT Tasks in the queue or error occured. For more details, please check the log file ./logfile_AAT_SYNERGY.txt""")
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""There is no AAT Tasks in the queue or error occured.\nFor more details,\nplease check the log file Logs/logfile_AAT_SYNERGY.txt""").pack()
        Button(new, text="Close", command = close_toplevel_window).pack()         
        output11=(DateTimeNow+": Job Completed. No of Tansferred SYNERGY Tasks= 0\n"+str(e)+'\n')
        with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        browser.quit()
        new.mainloop()
        
#Call SNOW Function:
    transfer_tasks_synergy()

  except Exception as e: 
#    print("\n"+DateTimeNow,"""An error has occured.. For more details, Kindly check the log file "Logs/logfile_AAT_SYNERGY.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""An error has occured..\nFor more details,\nKindly check the log file "Logs/logfile_AAT_SYNERGY.txt""").pack()
    Button(new, text="Close", command = close_toplevel_window).pack()         
    output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
    with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
        f11.write(output11)
        f11.close()
    browser.quit()
    new.mainloop()
    
#-----------------------------------------        
#2.3.3 Synergy Login and Call Transfer PROGRAM_Function:
#-----------------------------------------
        
def login_transfer_Synergy():
  global browser
  global DateTimeNow
  global new
  global new2
  DateTimeNow=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  input_Synergy_Username()
  input_Synergy_Password()
  try:
     options = webdriver.ChromeOptions()
     options.add_argument('headless')
     browser = webdriver.Chrome(executable_path="../chromedriver/chromedriver.exe", options=options)
     browser.get("https://alstom.service-now.com/nav_to.do?uri=%2Fhome.do")
     browser.set_window_size(1440, 900)
     try:
        account=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]""")))
        account.click()
     except:
        pass
     try:
        username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]""")))
        username.clear()
     except Exception as e:
#        print("\n"+DateTimeNow,"""ERROR: An error has occured while loading the driver. Kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured while loading the driver. Kindly check the log file "Logs/logfile_AAT_SYNERGY.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error occured while loading the driver '+str(e)+'\n')
        with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        browser.quit()
        new.mainloop()
        
     username.send_keys(user)
     next_button=browser.find_element_by_xpath("""//*[@id="idSIButton9"]""")
     next_button.click()
     time.sleep(5)
   
     password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input""")))
     password.clear()
     password.send_keys(myPass)
     SIGNIN=browser.find_element_by_xpath("""//*[@id="idSIButton9"]""")
     SIGNIN.click()
     time.sleep(5)

     try:
        input_Synergy_Code()
     except:
        pass
                
     try:
        YES= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input""")))
        YES.click()
     except:
        pass

#Call transfer Program function:    
     Transferring_synergy_tasks()
           
  except Exception as e:
#       print("\n"+DateTimeNow,"""ERROR: An error has occured..,\nFor more details, kindly check the log file "Logs/logfile_AAT_DOORS.txt" """)
       new= Toplevel(win)
       new.geometry("500x250")
       new.grab_set()
       new.title("ERROR")
       Label(new, text="""An error has occured..,\nFor more details,\nkindly check the log file\n "Logs/logfile_AAT_SYNERGY.txt""").pack()
       Button(new, text="Close", command = close_toplevel_window).pack()
       output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
       with open('../Logs/logfile_AAT_SYNERGY.txt', 'a', encoding='UTF8', newline='') as f11:
           f11.write(output11)
           f11.close()
       try:
           browser.quit()
       except:
           pass
       new.mainloop()

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------       
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------       
# In[3]:
#Third: Jazz:
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#3.1 JAZZ input data and login functions:
#3.1.1  JAZZ input data functions:
#-----------------------------------------
def input_data_Jazz_Assignees():
                global new
                global Assignment_Jazz               
                Input_Assignment_Jazz=Assignees_field2.get()
                Assignment_Jazz=Input_Assignment_Jazz.split(',')
                for x in Assignment_Jazz:
                    if str(x).strip()=='':
#                        print("""\nYou must not add any empty input data, please try again later..""")
                        new= Toplevel(win)
                        new.geometry("500x250")
                        new.grab_set()
                        new.title("ERROR")
                        Label(new, text="""User should provide Assignees Full Names""").pack()
                        Button(new, text="Close", command = close_toplevel_window).pack()
                        new.mainloop()
                        break

def input_Jazz_Username():
                global new
                global user
                user=str(user_field2.get())
#                user_field.delete('0', 'end')
                user=user.lower()
                if "alstomgroup.com" not in user:
                    new= Toplevel(win)
                    new.geometry("500x250")
                    new.grab_set()
                    new.title("ERROR")
                    Label(new, text="Username field is empty or not valid,\nplease enter username again").pack()
                    Button(new, text="Close", command = close_toplevel_window).pack()
                    new.mainloop()
                    

def input_Jazz_Password():
    global new
    global myPass
    myPass=str(pswrd_field2.get())
#    pswrd_field.delete('0', 'end')
    if myPass == "":
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="Password field is empty,\nplease enter password again").pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        new.mainloop()


#if CODE/PIN required:
def input_Jazz_code():
        global code_field2
        global new
        global browser
        Text = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div""")))
        Text2= WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div""")))
        if "Text" in Text.text:
            Text.click()
        else:
            Text2.click()
            
        new= Toplevel(win)
        new.geometry("250x250")
        new.grab_set()
        new.title("Service Now Code Request")
        Label(new, text="Enter Code").pack()
        code_field2=Entry(new,show="*",width=25)
        code_field2.pack()
        submit2=Button(new,text='Submit' , command = input_Jazz_PIN)
        submit2.pack()
        new.mainloop()
        
def input_Jazz_PIN():
        global new2
        global new
        PIN=code_field2.get()
        code= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/input""")))
        code.clear()
        code.send_keys(PIN)
        Verify=browser.find_element_by_xpath("""/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[6]/div/div/div/div/input""")
        Verify.click()
        try:
            YES= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input""")))
            YES.click()
            
            new2= Toplevel(new)
            new2.geometry("500x250")
            new2.grab_set()
            new2.title("Output")
            Label(new2, text="""Login Succeeded""").pack()
            Button(new2, text="Close", command = close_toplevel_window).pack()
            new2.mainloop()
            
        except:
            new2= Toplevel(new)
            new2.geometry("500x250")
            new2.grab_set()
            new2.title("ERROR")
            Label(new2, text="""Code is incorrect, please enter it again.""").pack()
            Button(new2, text="Close", command = close_toplevel_window2).pack()
            new2.mainloop()      

#------------------------------------------------------------------------------
#3.1.2 JAZZ Login PROGRAM_Function:
#-----------------------------------------
            
def login_Jazz():
  global browser
  global DateTimeNow
  global new2
  global new
  DateTimeNow=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  input_Jazz_Username()
  input_Jazz_Password()
  try:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path="../chromedriver/chromedriver.exe", options=options)
    browser.get("https://alstom.service-now.com/nav_to.do?uri=%2Fhome.do")
    browser.set_window_size(1440, 900)
    try:
        account=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]""")))
        account.click()
    except:
        pass
    try:
        username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]""")))
        username.clear()
    except Exception as e:
#        print("\n"+DateTimeNow,"""ERROR: An error has occured while loading the driver. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured while loading the driver.\nKindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error occured while loading the driver '+str(e)+'\n')
        with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        browser.quit()
        new.mainloop()
        
    username.send_keys(user)
    next_button=browser.find_element_by_xpath("""//*[@id="idSIButton9"]""")
    next_button.click()
    time.sleep(5)
 
    password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input""")))
    password.clear()
    password.send_keys(myPass)
    SIGNIN=browser.find_element_by_xpath("""//*[@id="idSIButton9"]""")
    SIGNIN.click()
    time.sleep(5)
    
    try:
        input_Jazz_code()
    except:
        pass

    YES= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input""")))
    YES.click()
    
    new2= Toplevel(win)
    new2.geometry("500x250")
    new2.grab_set()
    new2.title("Output")
    Label(new2, text="""Login Succeeded""").pack()
    Button(new2, text="Close", command = close_toplevel_window).pack()
    new2.mainloop()
           
  except Exception as e:
#       print("\n"+DateTimeNow,"""ERROR: An error has occured while logging in..,\nFor more details, kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
       new2= Toplevel(win)
       new2.geometry("500x250")
       new2.grab_set()
       new2.title("ERROR")
       Label(new2, text="""An error has occured while logging in..,\nFor more details, kindly check the log file\n "Logs/logfile_AAT_JAZZ.txt""").pack()
       Button(new2, text="Close", command = close_toplevel_window).pack()
       output11=(DateTimeNow+': Job failed with error: An error has occured while logging in..\n'+str(e)+'\n')
       with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
           f11.write(output11)
           f11.close()
       try:
           browser.quit()
       except:
           pass
       new2.mainloop()

#------------------------------------------------------------------------------
#3.2 JAZZ Assign Tasks function:
#3.2.1: JAZZ Assign SNOW_Function:
#-----------------------------------------

def assign_Jazz_tasks(Assignment):
    global new2
    global new
    try:
        j=len(Assignment)
        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")
        while ARROW:
            try:
                i=0
                while i in range(0,j):
                    Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')     
                    string="JAZZ"
                    if string in Summary:
                        Assigned=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""")
                        Assigned.click()
                        Assigned.clear()
                        Assigned.send_keys(str(Assignment[i]).strip())
                        Assigned.send_keys(u'\ue007')
                        time.sleep(3)
                        browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""").click()
                        time.sleep(3)
                        ticket_No=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]""").get_attribute('value')
                        Assignee=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""").get_attribute('value')
                        Assignee=str(Assignee).strip()
                        if  Assignee != "":
                            data=[ticket_No,Assignee,Summary]
                            with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'a', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                                f.close()
                            i=i+1
                        else:
                            with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'r') as f1:
                                No_of_Tasks  = -1
                                for row in f1:
                                    No_of_Tasks+= 1
                                f1.close()
#                            print("\n"+DateTimeNow,"Job Failed, No of Assigned JAZZ Tasks= "+str(No_of_Tasks),""", ERROR: One or more of input Assignees is incorrect, kindly check the log file "./logfile_Assign_Tickets.txt." """)
                            new= Toplevel(win)
                            new.geometry("500x250")
                            new.grab_set()
                            new.title("ERROR")
                            Label(new, text="""Job Failed,\nNo. of Assigned JAZZ Tasks= """+str(No_of_Tasks)+""",\nERROR: One or more of input Assignees is incorrect.\n For more details, kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
                            Button(new, text="Close", command = close_toplevel_window).pack()
                            e=""" ,ERROR: One or more of input Assignees is incorrect - ARROW."""                            
                            output11=(DateTimeNow+": Job Failed, No of Assigned JAZZ Tasks= "+str(No_of_Tasks)+str(e)+'\n')
                            with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
                                f11.write(output11)
                                f11.close()
                            browser.quit()
                            new.mainloop()
                            
                        time.sleep(3)
                        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")                    
                        ARROW.click()
                        time.sleep(3)
                    else:
                        ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[2]""")
                        ARROW.click()
                        time.sleep(3)
            except:
                break
    
        try:
            BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
            BACK_ARROW.click()
        except:
            with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'r') as f1:
                No_of_Tasks  = -1
                for row in f1:
                    No_of_Tasks+= 1
                f1.close()
#            print("\n"+DateTimeNow,"Job Completed, No of Assigned JAZZ Tasks= "+str(No_of_Tasks))
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="Job Completed.\nNo. of Assigned JAZZ Tasks= "+str(No_of_Tasks)).pack()
            Button(new, text="Close", command = close_toplevel_window).pack()
            output11=(DateTimeNow+": Job Completed. No. of Assigned JAZZ Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            new.mainloop()
    
        while BACK_ARROW:
             try:
                time.sleep(3)
                if i>=j:
                    i=0
                while i in range(0,j):
                    Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')     
                    string="JAZZ"
                    if string in Summary:
                        Assigned=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""")
                        Assigned.click()
                        Assigned.clear()
                        Assigned.send_keys(str(Assignment[i]).strip())
                        Assigned.send_keys(u'\ue007')
                        time.sleep(3)
                        browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""").click()
                        time.sleep(3)
                        ticket_No=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]""").get_attribute('value')
                        Assignee=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[2]/div[6]/div[2]/div[2]/input""").get_attribute('value')
                        Assignee=str(Assignee).strip()
                        if  Assignee != "":
                            data=[ticket_No,Assignee,Summary]
                            with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'a', encoding='UTF8', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(data)
                                f.close()
                            i=i+1
                        else:
                            with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'r') as f1:
                                No_of_Tasks  = -1
                                for row in f1:
                                    No_of_Tasks+= 1
                                f1.close()
#                            print("\n"+DateTimeNow,"Job Failed, No of Assigned JAZZ Tasks= "+str(No_of_Tasks),"""ERROR: One or more of input Assignees is incorrect, kindly check the log file "./logfile_Assign_Tickets.txt." """)
                            new= Toplevel(win)
                            new.geometry("500x250")
                            new.grab_set()
                            new.title("ERROR")
                            Label(new, text="Job Failed,\nNo. of Assigned JAZZ Tasks= "+str(No_of_Tasks)+""",\nERROR: One or more of input Assignees is incorrect.\n For more deatils, kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
                            Button(new, text="Close", command = close_toplevel_window).pack()
                            e=""" ,ERROR: One or more of input Assignees is incorrect - BACKARROW."""                            
                            output11=(DateTimeNow+": Job Failed, No of Assigned JAZZ Tasks= "+str(No_of_Tasks)+str(e)+'\n')
                            with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
                                f11.write(output11)
                                f11.close()
                            browser.quit()
                            new.mainloop()

                        time.sleep(3)                                
                        BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")                    
                        BACK_ARROW.click()
                        time.sleep(3)
                    else:
                        BACK_ARROW=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/div[2]/button[1]""")
                        BACK_ARROW.click()
                        time.sleep(3)
             except:
                break
        
        with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'r') as f1:
            No_of_Tasks  = -1
            for row in f1:
                No_of_Tasks+= 1
            f1.close()
           
#        print("\n"+DateTimeNow,"Job Completed, No of Assigned JAZZ Tasks= "+str(No_of_Tasks))
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="Job Completed. No of Assigned JAZZ Tasks= "+str(No_of_Tasks)).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+": Job Completed. No of Assigned JAZZ Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_jAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

    except Exception as e: 
#        print("\n"+DateTimeNow,"""An error has occured, kindly check the log file "./logfile_Assign_Tickets.txt." """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured.\nFor more details,\nkindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
        with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()


#------------------------------------------------------------------------------
#3.2.2: JAZZ Assign PROGRAM_Function:
#-----------------------------------------

def assigned_Jazz_tasks():
  global new2
  global new
  input_data_Jazz_Assignees()
  try:
    browser.switch_to.parent_frame()
  except: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="You have to login first.").pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    new.mainloop()    
  try:  
    Menu = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
    Menu.click()
    try:
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[8]/div/div/a/div/div""")
        WORK.click()
    except:
        SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
        SD.click()
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[8]/div/div/a/div/div""")
        WORK.click()
        
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
    search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
    search_filter.click()
    search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
    search_Number.click()
    search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
    search_button.click()
    search_button.clear()
    search_button.send_keys("TASK")
#Press_Enter:
    search_button.send_keys(u'\ue007')
    time.sleep(2)
    
  except Exception as e: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""An error has occured.\nFor more details,\nkindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
    with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
        f11.write(output11)
        f11.close()
    new.mainloop()
    
  try:
    tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
    row = tbody.find_elements_by_tag_name("tr")[0]
    t_No = row.find_elements_by_tag_name("td")[2]
    t_No.click()
    
    header=["ticket_No","Assignee","Summary"]
    with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        f.close()

#CALL SNOW FUNCTION:
    assign_Jazz_tasks(Assignment_Jazz)
            
  except Exception as e:
#    print ("""Seems there were no AAT Tasks in the queue or error occured..""")
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""Seems there were no AAT Tasks in the queue or error occured..\nFor more details,\nkindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    output11=(DateTimeNow+""": Seems there were no AAT Tasks in the queue or error occured..\n"""+str(e))
    with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
        f11.write(output11)
        f11.close()
    new.mainloop()


#------------------------------------------------------------------------------
#3.3 JAZZ Extract users' data from tasks function:
#3.3.1: JAZZ Extract users' data SNOW_Function:
#-----------------------------------------

def Add_Jazz_Users_info_to_CSV():
            global ticket_No
            browser.switch_to.parent_frame()
#search:
            browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""").clear()
            T_Number=browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""")
            T_Number.send_keys(ticket_No)
            T_Number.send_keys(u'\ue007')
            time.sleep(5)
            browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
            Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')        
            Jazz_DB="(Rational_JAZZ)_SUB || Add Access"
            Jazz_DB_Leaver="(Rational_JAZZ)_SUB || Leaver"
            Jazz_DB_Leaver2="(Rational_JAZZ)_SUB || Remove Access"
#edit the old with new license
            license1="DOORS Next Generation - Contributor - Token"
            license2="DOORS Next Generation - analyst - Token"
            license3="Quality Manager - Quality Professional - Token"
            license4="Quality Manager - Contributor - Token"
            license5="Team Concert - Stakeholder - Token"
            license6="Team Concert - Contributor - Token"
            license7="Team Concert - Developer - Token"

            Newlic1="com.ibm.team.rrc.reviewer.token"
            Newlic2="com.ibm.team.rrc.analyst.token"
            Newlic3="com.ibm.rqm.qualityprofessional.token"
            Newlic4="com.ibm.rqm.viewer.token"
            Newlic5="com.ibm.team.rtc.stakeholder.token"
            Newlic6="com.ibm.team.rtc.contributor.token"
            Newlic7="com.ibm.team.rtc.developer.token"
            
            time.sleep(3)
            if Jazz_DB in Summary:
                Full_Name=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[5]/div[2]/div[2]/input""").get_attribute('value')
                #click on variables
                browser.find_element_by_xpath("""//*[@id="tabs2_section"]/span[3]/span[1]""").click()
                time.sleep(2)
                email= browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[3]/td/span/div/div[2]/table/tbody/tr/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[6]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID2=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[7]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                Alstom_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/span/div[2]/div[1]/table/tbody/tr[2]/td/div/div/div/div[2]/input[2]""").get_attribute('value')     
                if SSO_ID=="" or SSO_ID.isnumeric():
                    if SSO_ID2=="" or SSO_ID2.isnumeric():
                        SSO_ID=Alstom_ID
                    else:
                        SSO_ID=SSO_ID2
                         
                string="import"
                Groups=[]
                Description=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[2]/table/tbody/tr[2]/td/div/div/div/div[2]/input""").get_attribute('value')
                for line in Description.split('\n'):
                      line = line.strip('\r')
                      if string in line:
                          sline = line.split('Rational ')
                          group=sline[1]
                          
                          if license1 in group:
                              group=Newlic1
                          elif license2 in group:
                              group=Newlic2
                          elif license3 in group:
                              group=Newlic3
                          elif license4 in group:
                              group=Newlic4
                          elif license5 in group:
                              group=Newlic5
                          elif license6 in group:
                              group=Newlic6
                          elif license7 in group:
                              group=Newlic7
                              
                          if group not in Groups:
                              Groups.append(group)

                          licenses=''
                          for i in Groups:
                              i=i.rstrip('.')
                              licenses+=i+';'
                          licenses=licenses.rstrip(';')
                data=[SSO_ID,Full_Name,email,'['+licenses+']','[JazzUsers]',0]
                with open('../files/JAZZ/users_Jazz.csv', 'a', encoding='UTF8', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(data)
                            f.close()

            elif Jazz_DB_Leaver in Summary or Jazz_DB_Leaver2 in Summary:
                email= browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[3]/td/span/div/div[2]/table/tbody/tr/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[6]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                SSO_ID2=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[4]/td/span/div[2]/div[1]/table/tbody/tr[7]/td/div/div/div/div[2]/input[2]""").get_attribute('value')
                Alstom_ID=browser.find_element_by_xpath("""/html/body/div[2]/form/span[4]/span/div/div/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/span/div[2]/div[1]/table/tbody/tr[2]/td/div/div/div/div[2]/input[2]""").get_attribute('value')     
                if SSO_ID=="" or SSO_ID.isnumeric():
                    if SSO_ID2=="" or SSO_ID2.isnumeric():
                        SSO_ID=Alstom_ID
                    else:
                        SSO_ID=SSO_ID2
                data=[ticket_No,SSO_ID,email,Summary]
                with open('../files/JAZZ/users_JAZZ_leaver.csv', 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                    f.close()

#-------------------------------------------------------------
#3.3.2: JAZZ Extract users' data PROGRAM_Function:
#-----------------------------------------
      
def AAT_TO_CSV_Jazz():
    global new
    global new2
    try:
        browser.switch_to.parent_frame()
    except:
#       print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="You have to login first.").pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        new.mainloop()    
    try:
#        header1=["sender","ticket_No","SSO_ID","Full_Name","email","groups"]
        header2=["ticket_No","SSO_ID","Email","Summary"]
        with open('../files/JAZZ/users_Jazz.csv', 'w', encoding='UTF8', newline='') as f1:
            writer = csv.writer(f1)
#            writer.writerow(header1)
            f1.close()
        with open('../files/JAZZ/users_Jazz_leaver.csv', 'w', encoding='UTF8', newline='') as f3:
            writer = csv.writer(f3)
            writer.writerow(header2)
            f3.close()

        Menu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
        Menu.click()
        try:
            WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
            WORK.click()
        except:
            SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
            SD.click()
            WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
            WORK.click()
            
        time.sleep(3)
        browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
        search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
        search_filter.click()
        search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
        search_Number.click()
        search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
        search_button.click()
        search_button.clear()
        search_button.send_keys("TASK")
        search_button.send_keys(u'\ue007')
        time.sleep(2)
        
        tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
        rows = tbody.find_elements_by_tag_name("tr")
        tasks=[]
        while rows:
            try:
                tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
                rows = tbody.find_elements_by_tag_name("tr")
                for row in rows:
                    tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
                    rows = tbody.find_elements_by_tag_name("tr")
                    t_No = row.find_elements_by_tag_name("td")[2].text
                    tasks.append(t_No)
                next_page=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/div[2]/span[2]/button[3]""")
                next_page.click()
                time.sleep(3)
            except:
                break  
        No_of_Tasks=len(tasks)
        if No_of_Tasks == 0:
#            print ("""There is no AAT Tasks in the queue, please try again later..""")
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="""There is no AAT Tasks in the queue..\nFor more details, kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
            Button(new, text="Close", command = close_toplevel_window).pack()
            output11=(DateTimeNow+": Job completed, No of requested Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            new.mainloop()
        else:
            global ticket_No
#CALL SNOW FUNCTION:
            for ticket_No in tasks:
                Add_Jazz_Users_info_to_CSV()

  #      print("\n"+DateTimeNow,"Job completed, No of Tasks= "+str(No_of_Tasks))
            new= Toplevel(win)
            new.geometry("500x250")
            new.grab_set()
            new.title("Output")
            Label(new, text="Job completed, No of requested Tasks= "+str(No_of_Tasks)+'\n').pack()
            Button(new, text="Close", command = close_toplevel_window).pack()
            output11=(DateTimeNow+": Job completed, No of requested Tasks= "+str(No_of_Tasks)+"\n")
            with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
                f11.write(output11)
                f11.close()
            new.mainloop()
            
    except Exception as e: 
#        print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("ERROR")
        Label(new, text="""An error has occured.\nFor more details, kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+': Job failed with error: '+str(e)+'\n')
        with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline='') as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

#------------------------------------------------------------------------------
#3.4 JAZZ Tasks Closure function:
#3.4.1  JAZZ CLOSURE SNOW_Function:
#-----------------------------------------
        
def AAT_closure_Jazz():
            browser.switch_to.parent_frame()
            browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""").clear()
            T_Number=browser.find_element_by_xpath("""/html/body/div/div/div/header/div[1]/div/div[2]/div/div[4]/form/div/input""")
            T_Number.send_keys(ticket_No)
            T_Number.send_keys(u'\ue007')
            time.sleep(3)
            browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
            Summary=browser.find_element_by_xpath("""/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[1]/div[2]/input""").get_attribute('value')        
            JAZZ_DB="IBM Rational Engineering Toolsuite(Rational_JAZZ)_SUB || Add Access"
            JAZZ_DB_Leaver="IBM Rational Engineering Toolsuite(Rational_JAZZ)_SUB || Leaver"
            JAZZ_DB_Remove="IBM Rational Engineering Toolsuite(Rational_JAZZ)_SUB || Remove Access"
            try:
                Notes=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[1]/span[1]/span[2]""")
                Notes.click()
            except:
                pass
            global counter2
            if JAZZ_DB in Summary:
                with open('../files/JAZZ/addUserslogFile.txt', 'r') as f: 
                    for line in f:
                        if ticket_No in line:
                            line=line.split(',')
                            output=str(line[2]).strip()
                            try:
                                WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/textarea""")
                                WORKNOTES.click()
                                WORKNOTES.send_keys(output)
                            except:
                                WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/textarea""")
                                WORKNOTES.click()
                                WORKNOTES.send_keys(output)
                            Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                            Assigned.select_by_value('2')
                            time.sleep(2)
                            SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                            SAVE.click()
                            time.sleep(2)
                            Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                            Assigned.select_by_value('3')
                            time.sleep(2)
                            RES_INFO=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]""")
                            RES_INFO.click()
                            RES_INFO_INPUT=browser.find_element_by_xpath("""//*[@id="sc_task.close_notes"]""")
                            RES_INFO_INPUT.click()
                            RES_INFO_INPUT2= browser.find_element_by_css_selector("""#sc_task\.close_notes""")
                            RES_INFO_INPUT2.send_keys(output)
                            SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                            SAVE.click()
                            f.close()
                            counter2 += 1
                            break
                    else:
                        data=(ticket_No+" || "+Summary+"\n")
                        with open('../files/JAZZ/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                            f.write(data)
                            f.close()
                                                   
            elif JAZZ_DB_Leaver in Summary or JAZZ_DB_Remove in Summary:
                with open('../files/JAZZ/deletedUserslogFile.txt', 'r') as f:
                    for line in f:
                        if ticket_No in line:
                            if "deleted" in line:                           
                                output="""The mentioned JAZZ account has been deleted from JAZZ environments."""
                                try:
                                    WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/textarea""")
                                    WORKNOTES.click()
                                    WORKNOTES.send_keys(output)
                                except:
                                    WORKNOTES=browser.find_element_by_xpath("""/html/body/div[2]/form/span[2]/span/div/div[2]/div/div[3]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div/textarea""")
                                    WORKNOTES.click()
                                    WORKNOTES.send_keys(output)
                                Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                                Assigned.select_by_value('2')
                                time.sleep(2)
                                SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                                SAVE.click()
                                time.sleep(2)
                                Assigned=Select(browser.find_element_by_xpath("""//*[@id="sc_task.state"]"""))
                                Assigned.select_by_value('3')
                                time.sleep(2)
                                RES_INFO=browser.find_element_by_xpath("""/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]""")
                                RES_INFO.click()
                                RES_INFO_INPUT=browser.find_element_by_xpath("""//*[@id="sc_task.close_notes"]""")
                                RES_INFO_INPUT.click()
                                RES_INFO_INPUT2= browser.find_element_by_css_selector("""#sc_task\.close_notes""")
                                RES_INFO_INPUT2.send_keys(output)
                                SAVE=browser.find_element_by_xpath("""/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]""")
                                SAVE.click()
                                f.close()
                                counter2 += 1
                                break
                    else:
                        data=(ticket_No+" || "+Summary+"\n")
                        with open('../files/JAZZ/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                            f.write(data)
                            f.close()      
            
            else:
                data=(ticket_No+" || "+Summary+"\n")
                with open('../files/JAZZ/to_be_checked.txt', 'a', encoding='UTF8', newline="") as f:
                    f.write(data)
                    f.close()
                    
                    
#-----------------------------------------
#3.4.2  JAZZ CLOSURE PROGRAM_Function:
#-----------------------------------------
                    
def Ticket_Closure_Jazz():                 
  global new
  global new2
  try:
    browser.switch_to.parent_frame()
  except: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="You have to login first.").pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    new.mainloop()
  try:    
    try:
        with open('../files/JAZZ/addUserslogFile.txt', 'r') as f1:
            f1.close()
    except:
        with open('../files/JAZZ/addUserslogFile.txt', 'w', encoding='UTF8', newline="") as f1:
            f1.close()
    try:
        with open('../files/JAZZ/deletedUserslogFile.txt', 'r') as f3:
            f3.close()
    except:
        with open('../files/JAZZ/deletedUserslogFile.txt', 'w', encoding='UTF8', newline="") as f3:
            f3.close()         
        
    with open('../files/JAZZ/to_be_checked.txt', 'w', encoding='UTF8', newline="") as f5:
        f5.close()
    
    time.sleep(5)
    
    Menu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div/nav/div/div[2]/div/div/a[1]""")))
    Menu.click()
    try:
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
        WORK.click()
    except:
        SD=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/a/span""")
        SD.click()
        WORK=browser.find_element_by_xpath("""/html/body/div/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[13]/ul/li[5]/div/div/a/div/div""")
        WORK.click()
        
    time.sleep(3)
    browser.switch_to.frame(browser.find_element_by_xpath("""//*[@id="gsft_main"]"""))
    search_filter=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span""")
    search_filter.click()
    search_Number=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/span[1]/span/select/option[2]""")
    search_Number.click()
    search_button=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/span/div/div/input""")
    search_button.click()
    search_button.clear()
    search_button.send_keys("TASK")
    search_button.send_keys(u'\ue007')
    time.sleep(2)
    
    tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
    rows = tbody.find_elements_by_tag_name("tr")
    tasks=[]
    while rows:
        try:
            tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
            rows = tbody.find_elements_by_tag_name("tr")
            for row in rows:
                tbody = browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[5]/table/tbody/tr/td/div/table/tbody""")
                rows = tbody.find_elements_by_tag_name("tr")
                t_No = row.find_elements_by_tag_name("td")[2].text
                tasks.append(t_No)
            next_page=browser.find_element_by_xpath("""/html/body/div[1]/div[1]/span/div/div[1]/div/div[2]/span[2]/button[3]""")
            next_page.click()
            time.sleep(3)
        except:
            break  
        
    No_of_Tasks=len(tasks)
    global counter2
    counter2=0
    if No_of_Tasks == 0:
#        print ("""There is no AAT Tasks in the queue, please try again later..""")
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="""There is no AAT Tasks in the queue.\nFor more details, kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+": Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline="\n") as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

    else:
        global ticket_No
#Calling SNOW function:
        for ticket_No in tasks:
            AAT_closure_Jazz()
    
#    print("\n"+DateTimeNow,"Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks))
        new= Toplevel(win)
        new.geometry("500x250")
        new.grab_set()
        new.title("Output")
        Label(new, text="Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks)).pack()
        Button(new, text="Close", command = close_toplevel_window).pack()
        output11=(DateTimeNow+": Job completed, No of closed incidents="+str(counter2)+", No of total Tasks= "+str(No_of_Tasks)+"\n")
        with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline="\n") as f11:
            f11.write(output11)
            f11.close()
        new.mainloop()

  except Exception as e: 
#    print("\n"+DateTimeNow,"""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """)
    new= Toplevel(win)
    new.geometry("500x250")
    new.grab_set()
    new.title("ERROR")
    Label(new, text="""An error has occured. Kindly check the log file "Logs/logfile_AAT_JAZZ.txt" """).pack()
    Button(new, text="Close", command = close_toplevel_window).pack()
    output11=(DateTimeNow+': Job failed with error: '+str(e)+"\n")
    with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline="") as f11:
        f11.write(output11)
        f11.close()
    new.mainloop()



#------------------------------------------------------------------------------
#3.5 JAZZ Open file functions:
#-----------------------------------------
    
def AAT_Jazz_Logfile():
        with open('../Logs/logfile_AAT_JAZZ.txt', 'a', encoding='UTF8', newline="") as f1:
            f1.close()
        webbrowser.open('..\\Logs\\logfile_AAT_JAZZ.txt')
    
def AAT_Assigned_Jazz_Tasks():
    try:
        with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'r') as f:
            f.close()
        webbrowser.open('..\\files\\JAZZ\\Assigned_Jazz_Tickets.csv')
    except:
        header=["ticket_No","Assignee","Summary"]
        with open('../files/JAZZ/Assigned_Jazz_Tickets.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        f.close()
        webbrowser.open('..\\files\\JAZZ\\Assigned_Jazz_Tickets.csv')      
       
def to_be_checked_Jazz():
    try:
        with open('../files/JAZZ/to_be_checked.txt', 'r') as f1:
            f1.close()
        webbrowser.open('..\\files\\JAZZ\\to_be_checked.txt') 
    except:
        with open('../files/JAZZ/to_be_checked.txt', 'w', encoding='UTF8', newline="") as f1:
            f1.close()
        webbrowser.open('..\\files\\JAZZ\\to_be_checked.txt')

      
def Add_Delete_Jazz_Tasks():
#    header1=["sender","ticket_No","SSO_ID","Full_Name","email","groups"]
    header2=["ticket_No","SSO_ID","Email","Summary"]
    try:
        with open('../files/JAZZ/users_Jazz.csv', 'r') as f1:
            f1.close()
        webbrowser.open('..\\files\\JAZZ\\users_Jazz.csv')
    except:
        with open('../files/JAZZ/users_Jazz.csv', 'w', encoding='UTF8', newline='') as f1:
            writer = csv.writer(f1)
 #           writer.writerow(header1)
            f1.close()   
        webbrowser.open('..\\files\\JAZZ\\users_Jazz.csv')        

    try:
        with open('../files/JAZZ/users_Jazz_leaver.csv', 'r') as f3:
            f3.close()
        webbrowser.open('..\\files\\JAZZ\\users_Jazz_leaver.csv')    
    except:
        with open('../files/JAZZ/users_Jazz_leaver.csv', 'w', encoding='UTF8', newline='') as f3:
            writer = csv.writer(f3)
            writer.writerow(header2)
            f3.close()        
        webbrowser.open('..\\files\\JAZZ\\users_Jazz_leaver.csv')


def add_users_Jazz_logs():
    with open('../files/JAZZ/addUserslogFile.txt', 'a', encoding='UTF8', newline="") as f1:
        f1.close()
    webbrowser.open('..\\files\\JAZZ\\addUserslogFile.txt')  
    
def delete_users_Jazz_logs():
        with open('../files/JAZZ/deletedUserslogFile.txt', 'a', encoding='UTF8', newline='') as f4:
            f4.close()
        webbrowser.open('..\\files\\JAZZ\\deletedUserslogFile.txt')


#-------------------------------------------------------------------------------
#3.6: JAZZ Call REPO TOOLS Scripts:  
#--------------------------------------

def add_users_Jazz():
    os.system("..\\REPO_Tools\\addusersfromCSV.bat")    

def delete_users_Jazz():
    os.system("..\\REPO_Tools\\deletingUsersFromCSV.bat")
        

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------       
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

# In[4]:
#4. GUI CONFIGURATION:
#--------------------------------------------------
#4.1 General Configurtaions for App window and Tabs:
#--------------------------------------------------    
try:
#copy file tk8.6 from path: "C:\Users\<userID>\Anaconda3\Library\lib" to this path: "\AAT_GUI\lib"
#and edit in file "tk.tcl", to adjust the version in line: package require -exact Tk  8.6.9


    DateTimeNow=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    base = None

    if sys.platform=='win32':
        base = "Win32GUI"

    os.environ.__setitem__('DISPLAY', '169.254.79.152:0.0')
    #os.environ.get('DISPLAY')
    win = tk.Tk()# Create instance
    win.title("AAT Tickets")        # Add a title 
    Label(win, text="""Welcome""",font = "Helvetica 16 bold italic",fg = "dark blue", bg="yellow").pack()

    win.configure(background='yellow')
    tabControl = ttk.Notebook(win)          # Create Tab Control

    tab0 = ttk.Frame(tabControl)            # Create a tab
    tab1 = ttk.Frame(tabControl)            # Create a tab
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)

    def close_window():
        try:
            browser.quit()
            win.destroy()
            os.system("TASKKILL /IM AAT_GUI_BG.exe")
        except:
            win.destroy()
            os.system("TASKKILL /IM AAT_GUI_BG.exe") 
        
    def close_toplevel_window():
        global new2
        global new
        try:
            new2.destroy()
        except:
            pass
        try:
            new.destroy()
        except:
            pass
        
    def close_toplevel_window2():
        global new2
        try:
            new2.destroy()
        except:
            pass      

    tabControl.add(tab1, text='DOORS')
    tabControl.add(tab2, text='JAZZ')
    tabControl.add(tab3, text='SYNERGY')

#------------------------------------------------------------------------------
#4.2 DOORS GUI:
#----------------------------
#    ttk.Label(tab1,text='                           ').grid(column=0)
#    ttk.Label(tab1,text='').grid(row=0)
    ttk.Label(tab1,text='\n------- TASKS -------\n ',font="Helvetica 9 bold").grid(row=0,column=1)
#    ttk.Label(tab1,text='----------------------------------------\n ',font="Helvetica 9 bold").grid(row=0,column=2)
#    ttk.Label(tab1,text='----------------------------------------\n ',font="Helvetica 9 bold").grid(row=0,column=3)
    ttk.Label(tab1,text='\n------- OUTPUT -------\n ',font="Helvetica 9 bold").grid(row=0,column=4)    
    
    #    InputDataFile.grid(row=1, column=1)

    inputSNOWemail=ttk.Label(tab1,text='Service-Now Email',font="Helvetica 9 bold")
    inputSNOWemail.grid(row=1, column=1)
    user_field=ttk.Entry(tab1,width=30)
    user_field.grid(row=1, column=2)

    inputPassword=ttk.Label(tab1,text='Service-Now Password',font="Helvetica 9 bold")
    inputPassword.grid(row=2, column=1)
    pswrd_field=ttk.Entry(tab1,show="*",width=30)
    pswrd_field.grid(row=2, column=2)

#    submit=ttk.Button(tab1,text='Submit',command = input_Doors_Password, width=15)
#    submit.grid(row=2, column=3)
    
 #   ttk.Label(tab1,text='Log Files',font = "Helvetica 10 bold").grid(row=4, column=4)

    logintoSNOW=ttk.Button(tab1,text='Login to Service Now' , command = login_Doors, width=25)
    logintoSNOW.grid(row=2, column=3)

#    ttk.Label(tab1,text='').grid(row=5)    
    ttk.Label(tab1,text='--------------------------------------------').grid(row=3,column=1)
    ttk.Label(tab1,text='----------------------------------------').grid(row=3,column=2)
    ttk.Label(tab1,text='----------------------------------------').grid(row=3,column=3)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=3,column=4)
    
    inputAssigneers=ttk.Label(tab1,text='Assignees Full Names\n(comma seperated)',font="Helvetica 9 bold")
    inputAssigneers.grid(row=4, column=1)
    Assignees_field=ttk.Entry(tab1,width=30)
    Assignees_field.grid(row=4, column=2)

    AssignedTasks=ttk.Button(tab1, text='Assign Tasks on SNOW' , command = assigned_doors_tasks, width=35)
    AssignedTasks.grid(row=5, column=1)

    ttk.Button(tab1, text='Assigned Tasks Output', command=AAT_Assigned_Doors_Tasks, width=35).grid(row=5, column=4)
    
#    ttk.Label(tab1,text='').grid(row=7)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=6,column=1)
    ttk.Label(tab1,text='----------------------------------------').grid(row=6,column=2)
    ttk.Label(tab1,text='----------------------------------------').grid(row=6,column=3)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=6,column=4)
    
    
    inputIBMemail=ttk.Label(tab1,text='Enter your IBM Email',font="Helvetica 9 bold")
    inputIBMemail.grid(row=7, column=1)
    ibm_field=ttk.Entry(tab1,width=30)
    ibm_field.grid(row=7, column=2)

    AATTOCSV=ttk.Button(tab1,text="""Extract info from Tasks on SNOW""" , command = AAT_TO_CSV_Doors, width=35 )
    AATTOCSV.grid(row=8, column=1)

    ttk.Button(tab1,text="""Add-Delete DOORS Tasks""" , command = Add_Delete_Doors_Tasks, width=35).grid(row=8, column=4)
    
#    ttk.Label(tab1,text='').grid(row=9)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=9,column=1)
    ttk.Label(tab1,text='----------------------------------------').grid(row=9,column=2)
    ttk.Label(tab1,text='----------------------------------------').grid(row=9,column=3)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=9,column=4)
    
    add_users_doors=ttk.Button(tab1,text="""Add Users to DOORS""" , command = add_users_doors, width=35 )
    add_users_doors.grid(row=10, column=1)
    add_users_doors_validation=ttk.Button(tab1,text="""Validate Added DOORS Users""" , command = add_users_doors_validation, width=35 )
    add_users_doors_validation.grid(row=11, column=1)
    add_users_doors_validationFailed=ttk.Button(tab1,text="""Add Failed-Validated DOORS Users""" , command = add_users_doors_validationFailed, width=35 )
    add_users_doors_validationFailed.grid(row=12, column=1)
    add_users_doors_validation_logs=ttk.Button(tab1,text="""Failed-Validated DOORS Users""" , command= add_users_doors_validation_logs, width=35 )
    add_users_doors_validation_logs.grid(row=11, column=4)
    add_users_doors_logs=ttk.Button(tab1,text="""Add DOORS Users Logs""" , command = add_users_doors_logs, width=35 )
    add_users_doors_logs.grid(row=12, column=4)
    
    ttk.Label(tab1,text='').grid(row=13)
    
    add_users_dcp=ttk.Button(tab1,text="""Add Users to DCP""" , command = add_users_dcp, width=35 )
    add_users_dcp.grid(row=14, column=1)
    add_users_dcp_validation=ttk.Button(tab1,text="""Validate Added DCP Users""" , command = add_users_dcp_validation, width=35 )
    add_users_dcp_validation.grid(row=15, column=1)
    add_users_dcp_validationFailed=ttk.Button(tab1,text="""Add Failed-Validated DCP Users""" , command = add_users_dcp_validationFailed , width=35)
    add_users_dcp_validationFailed.grid(row=16, column=1)
    add_users_dcp_validation_logs=ttk.Button(tab1,text="""Failed-Validated DCP Users""" , command = add_users_dcp_validation_logs, width=35 )
    add_users_dcp_validation_logs.grid(row=15, column=4)
    add_users_dcp_logs=ttk.Button(tab1,text="""Add DCP Users Logs""" , command = add_users_dcp_logs, width=35 )
    add_users_dcp_logs.grid(row=16, column=4)  
    
    ttk.Label(tab1,text='').grid(row=17)
    
    disable_users_doors_PREPROD=ttk.Button(tab1,text="""Disable DOORS PREPROD Users""" , command = disable_users_doors_PREPROD, width=35 )
    disable_users_doors_PREPROD.grid(row=18, column=1)
    delete_users_doors_PREPROD=ttk.Button(tab1,text="""Delete DOORS PREPROD Users""" , command = delete_users_doors_PREPROD , width=35)
    delete_users_doors_PREPROD.grid(row=19, column=1)
    disable_users_doors_PREPROD_logs=ttk.Button(tab1,text="""Disabled DOORS PREPROD Users Logs""" , command = disable_users_doors_PREPROD_logs, width=35 )
    disable_users_doors_PREPROD_logs.grid(row=18, column=4)
    delete_users_doors_PREPROD_logs=ttk.Button(tab1,text="""Deleted DOORS PREPROD Users Logs""" , command = delete_users_doors_PREPROD_logs , width=35)
    delete_users_doors_PREPROD_logs.grid(row=19, column=4)
    
    disable_users_doors=ttk.Button(tab1,text="""Disable DOORS PROD Users""" , command = disable_users_doors, width=35 )
    disable_users_doors.grid(row=20, column=1)
    delete_users_doors=ttk.Button(tab1,text="""Delete DOORS PROD Users""" , command = delete_users_doors, width=35 )
    delete_users_doors.grid(row=21, column=1)
    disable_users_doors_logs=ttk.Button(tab1,text="""Disabled DOORS PROD Users Logs""" , command = disable_users_doors_logs, width=35 )
    disable_users_doors_logs.grid(row=20, column=4)
    delete_users_doors_logs=ttk.Button(tab1,text="""Deleted DOORS PROD Users Logs""" , command = delete_users_doors_logs, width=35 )
    delete_users_doors_logs.grid(row=21, column=4)
    
    ttk.Label(tab1,text='').grid(row=22)
    
    disable_users_dcp=ttk.Button(tab1,text="""Disable DCP Users"""  , command = disable_users_dcp, width=35 )
    disable_users_dcp.grid(row=23, column=1)
    delete_users_dcp=ttk.Button(tab1,text="""Delete DCP Users""" , command = delete_users_dcp, width=35 )
    delete_users_dcp.grid(row=24, column=1)
    disable_users_dcp_logs=ttk.Button(tab1,text="""Disabled DCP Users Logs""" , command = disable_users_dcp_logs, width=35 )
    disable_users_dcp_logs.grid(row=23, column=4)
    delete_users_dcp_logs=ttk.Button(tab1,text="""Deleted DCP Users Logs""" , command = delete_users_dcp_logs, width=35 )
    delete_users_dcp_logs.grid(row=24, column=4)

#    ttk.Label(tab1,text='').grid(row=25)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=25,column=1)
    ttk.Label(tab1,text='----------------------------------------').grid(row=25,column=2)
    ttk.Label(tab1,text='----------------------------------------').grid(row=25,column=3)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=25,column=4)
    
    TicketClosure=ttk.Button(tab1,text='Close Tasks on SNOW' , command = Ticket_Closure_Doors, width=35)
    TicketClosure.grid(row=26, column=1)

    ttk.Button(tab1,text='Remaining Tasks' , command = to_be_checked_Doors, width=35).grid(row=26, column=4)

#    ttk.Label(tab1,text='').grid(row=27)    
    ttk.Label(tab1,text='--------------------------------------------').grid(row=27,column=1)
    ttk.Label(tab1,text='----------------------------------------').grid(row=27,column=2)
    ttk.Label(tab1,text='----------------------------------------').grid(row=27,column=3)
    ttk.Label(tab1,text='--------------------------------------------').grid(row=27,column=4)
    

    ttk.Button(tab1, text='DOORS LogFile', command=AAT_DOORS_Logfile, width=15).grid(row=28, column=4)
    ttk.Button(tab1,text='Quit',command=close_window, width=15).grid(row=29, column=4)

#------------------------------------------------------------------------------
#4.3 SYNERGY GUI:
#----------------------------
    ttk.Label(tab3,text='                 ').grid(column=0)    
    ttk.Label(tab3,text='').grid(row=0)  
    
    inputUsername3=ttk.Label(tab3,text='Service-Now Email',font="Helvetica 9 bold")
    inputUsername3.grid(row=1, column=1)
    user_field3=ttk.Entry(tab3,width=40)
    user_field3.grid(row=1, column=2)
    
    inputPassword3=ttk.Label(tab3,text='Service-Now Password',font="Helvetica 9 bold")
    inputPassword3.grid(row=2, column=1)
    pswrd_field3=ttk.Entry(tab3,show="*",width=40)
    pswrd_field3.grid(row=2, column=2)

    ttk.Label(tab3,text='').grid(row=3)  
    
    logintoSNOW3=ttk.Button(tab3,text='Login to Service Now\n and Transfer Tasks' , command = login_transfer_Synergy, width=35)
    logintoSNOW3.grid(row=4, column=1)
        
    logintoSNOW3=ttk.Button(tab3,text='Transferred Tasks' , command = Transferring_synergy_tasks_Logs, width=20)
    logintoSNOW3.grid(row=4, column=2)
    
    logintoSNOW3=ttk.Button(tab3,text='SYNERGY Logfile' , command = AAT_Synergy_Tasks_log, width=20)
    logintoSNOW3.grid(row=4, column=3)
    
    ttk.Button(tab3,text='Quit',command=close_window, width=20).grid(row=5, column=3)


#-----------------------------------------------------------------------------------------------------------
#4.4 JAZZ GUI:
#-----------------------------------------------------------------------------
    ttk.Label(tab2,text='\n------- TASKS -------\n ',font="Helvetica 9 bold").grid(row=0,column=1)
    ttk.Label(tab2,text='\n------- OUTPUT -------\n ',font="Helvetica 9 bold").grid(row=0,column=4)    
    
    inputSNOWemail2=ttk.Label(tab2,text='Service-Now Email',font="Helvetica 9 bold")
    inputSNOWemail2.grid(row=1, column=1)
    user_field2=ttk.Entry(tab2,width=30)
    user_field2.grid(row=1, column=2)

    inputPassword2=ttk.Label(tab2,text='Service-Now Password',font="Helvetica 9 bold")
    inputPassword2.grid(row=2, column=1)
    pswrd_field2=ttk.Entry(tab2,show="*",width=30)
    pswrd_field2.grid(row=2, column=2)

    logintoSNOW2=ttk.Button(tab2,text='Login to Service Now' , command = login_Jazz, width=25)
    logintoSNOW2.grid(row=2, column=3)

#    ttk.Label(tab1,text='').grid(row=5)    
    ttk.Label(tab2,text='--------------------------------------------').grid(row=3,column=1)
    ttk.Label(tab2,text='----------------------------------------').grid(row=3,column=2)
    ttk.Label(tab2,text='----------------------------------------').grid(row=3,column=3)
    ttk.Label(tab2,text='--------------------------------------------').grid(row=3,column=4)


    inputAssigneers2=ttk.Label(tab2,text='Assignees Full Names\n(comma seperated)',font="Helvetica 9 bold")
    inputAssigneers2.grid(row=4, column=1)
    Assignees_field2=ttk.Entry(tab2,width=30)
    Assignees_field2.grid(row=4, column=2)

    AssignedTasks2=ttk.Button(tab2, text='Assign Tasks on SNOW' , command = assigned_Jazz_tasks, width=35)
    AssignedTasks2.grid(row=5, column=1)

    ttk.Button(tab2, text='Assigned Tasks Output', command=AAT_Assigned_Jazz_Tasks, width=35).grid(row=5, column=4)
    
#    ttk.Label(tab1,text='').grid(row=7)
    ttk.Label(tab2,text='--------------------------------------------\n').grid(row=6,column=1)
    ttk.Label(tab2,text='----------------------------------------\n').grid(row=6,column=2)
    ttk.Label(tab2,text='----------------------------------------\n').grid(row=6,column=3)
    ttk.Label(tab2,text='--------------------------------------------\n').grid(row=6,column=4)

    AATTOCSV2=ttk.Button(tab2,text="""Extract info from Tasks on SNOW""" , command = AAT_TO_CSV_Jazz, width=35 )
    AATTOCSV2.grid(row=7, column=1)

    ttk.Button(tab2,text="""Add-Delete JAZZ Tasks""" , command = Add_Delete_Jazz_Tasks, width=35).grid(row=7, column=4)
    
#    ttk.Label(tab1,text='').grid(row=9)
    ttk.Label(tab2,text='\n--------------------------------------------').grid(row=8,column=1)
    ttk.Label(tab2,text='\n----------------------------------------').grid(row=8,column=2)
    ttk.Label(tab2,text='\n----------------------------------------').grid(row=8,column=3)
    ttk.Label(tab2,text='\n--------------------------------------------').grid(row=8,column=4)

    add_users_Jazz=ttk.Button(tab2,text="""Add Users to JAZZ""" , command = add_users_Jazz, width=35 )
    add_users_Jazz.grid(row=9, column=1)
    add_users_Jazz_logs=ttk.Button(tab2,text="""Add JAZZ Users Logs""" , command = add_users_Jazz_logs, width=35 )
    add_users_Jazz_logs.grid(row=9, column=4)
    
    ttk.Label(tab2,text='').grid(row=10)

    delete_users_Jazz=ttk.Button(tab2,text="""Delete JAZZ PROD Users""" , command = delete_users_Jazz, width=35 )
    delete_users_Jazz.grid(row=11, column=1)
    delete_users_Jazz_logs=ttk.Button(tab2,text="""Deleted JAZZ PROD Users Logs""" , command = delete_users_Jazz_logs, width=35 )
    delete_users_Jazz_logs.grid(row=11, column=4)
        
#    ttk.Label(tab1,text='').grid(row=25)
    ttk.Label(tab2,text='--------------------------------------------\n').grid(row=12,column=1)
    ttk.Label(tab2,text='----------------------------------------\n').grid(row=12,column=2)
    ttk.Label(tab2,text='----------------------------------------\n').grid(row=12,column=3)
    ttk.Label(tab2,text='--------------------------------------------\n').grid(row=12,column=4)
    
    TicketClosure2=ttk.Button(tab2,text='Close Tasks on SNOW' , command = Ticket_Closure_Jazz, width=35)
    TicketClosure2.grid(row=14, column=1)

    ttk.Button(tab2,text='Remaining Tasks' , command = to_be_checked_Jazz, width=35).grid(row=14, column=4)

#    ttk.Label(tab1,text='').grid(row=27)    
    ttk.Label(tab2,text='\n--------------------------------------------').grid(row=15,column=1)
    ttk.Label(tab2,text='\n----------------------------------------').grid(row=15,column=2)
    ttk.Label(tab2,text='\n----------------------------------------').grid(row=15,column=3)
    ttk.Label(tab2,text='\n--------------------------------------------').grid(row=15,column=4)
    

    ttk.Button(tab2, text='JAZZ LogFile', command=AAT_Jazz_Logfile, width=15).grid(row=16, column=4)
    ttk.Button(tab2,text='Quit',command=close_window, width=15).grid(row=17, column=4)
    
    
#------------------------------------------------------------------------------
#4.5 IN GENERAL:
#----------------------------    
    tabControl.pack(expand=1, fill="both")  #Pack to make visible
    win.mainloop()

except Exception as e:
    DateTimeNow=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    base = None

    if sys.platform=='win32':
        base = "Win32GUI"

    os.environ.__setitem__('DISPLAY', '169.254.79.152:0.0')
    win = tk.Tk()# Create instance
    win.title("AAT Tickets")
    win.geometry("500x250")
    Label(win, text="""An error has occured while Loading the application.\nKindly check the log file "Logs/logfile_GUI_DOORS.txt" """).pack()
    Button(win, text="Close", command = close_window).pack()
    output11=(DateTimeNow+': Job failed with error: '+str(e)+"\n")
    with open('../logs/logfile_AAT_GUI.txt', 'a', encoding='UTF8', newline="") as f11:
        f11.write(output11)
        f11.close()
    win.mainloop()