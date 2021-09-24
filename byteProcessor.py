# -*- coding: utf-8 -*-
# python 3.9
# Author: By 空道
# Created on 10:19 2020/12/5

from sqlite3.dbapi2 import connect
from tkinter import *
import hashlib,gzip,zlib
import time
import struct
import re
import os
import pyperclip
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

LOG_LINE_NUM = 0


def stringTobytes(str):
    return bytes(str,encoding='utf8')
def bytesToString(bs):
    return bytes.decode(bs,encoding='utf8')
def hexStringTobytes(str):
    str = str.replace(" ", "")
    return bytes.fromhex(str)
    # return a2b_hex(str)
def bytesToHexString(bs):
    # hex_str = ''
    # for item in bs:
    #     hex_str += str(hex(item))[2:].zfill(2).upper() + " "
    # return hex_str
    return ''.join(['%02X' % b for b in bs])
def stringToHexString(str):
    strbyte = stringTobytes(str)
    return bytesToHexString(strbyte)
def hexStringToString(hexstr):
    bytesstr = hexStringTobytes(hexstr)
    return bytesstr.decode(encoding='utf-8')
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    def allSelectText(self,text_obj):
        text_obj.tag_add('sel', '1.0', 'end')
    def text_undo(self,text_obj):
        text_obj.edit_undo() 
    def text_redo(self,text_obj):
        text_obj.edit_redo() 
    def callback(self,text_obj):
        text_obj.edit_separator()
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("空道 字节处理器_v1.5")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.init_window_name.geometry('1068x700+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=13)
        #文本框
        self.init_data_Text = Text(self.init_window_name, bd=5,relief=RIDGE,width=67, height=35,autoseparators=False,undo=True)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.init_data_Text.focus_set()
        self.result_data_Text = Text(self.init_window_name, bd=5,relief=RIDGE, width=67, height=35,autoseparators=False,undo=True)  #处理结果展示
        self.init_data_Text.bind("<Command-a>", lambda event:self.allSelectText(text_obj=self.init_data_Text))
        self.init_data_Text.bind("<Key>", lambda event:self.callback(text_obj=self.init_data_Text))
        #self.init_data_Text.bind("<Command-z>", lambda event:self.text_undo(text_obj=self.init_data_Text))
        self.init_data_Text.bind("<Command-y>", lambda event:self.text_redo(text_obj=self.init_data_Text))
        ###//将接口设为只读 
        #self.result_data_Text.bind("<Key>", lambda a: "break")
        self.result_data_Text.grid(row=1, column=13, rowspan=15, columnspan=10)
        self.result_data_Text.bind("<Command-a>", lambda event:self.allSelectText(text_obj=self.result_data_Text))
        self.result_data_Text.bind("<Key>", lambda event:self.callback(text_obj=self.result_data_Text))
        #self.result_data_Text.bind("<Command-z>", lambda event:self.text_undo(text_obj=self.result_data_Text))
        self.result_data_Text.bind("<Command-y>", lambda event:self.text_redo(text_obj=self.result_data_Text))
        #按钮
        self.CheckClipValue = IntVar(value=1)
        self.check_send_clip = Checkbutton(self.init_window_name, text = "将结果发送剪贴板", variable = self.CheckClipValue, onvalue=1, offvalue=0)
    #    self.check_send_clip.select()
        self.check_send_clip.grid(row=1, column=11)
        self.bytes_to_hex_btn = Button(self.init_window_name, text="Bytes转Hex", bg="lightblue", width=10,command=self.bytes_memory_hex)  # 调用内部方法  加()为直接调用
        self.bytes_to_hex_btn.grid(row=2, column=11)
        self.unicdoe_to_str_btn = Button(self.init_window_name, text="unicode转字符", bg="lightblue", width=10,command=self.unicode_to_str_func)  # 调用内部方法  加()为直接调用
        self.unicdoe_to_str_btn.grid(row=3, column=11)
        self.bytes_to_hex_btn = Button(self.init_window_name, text="Hex转JavaByte", bg="lightblue", width=10,command=self.hexStrToJavaBytesStr)  # 调用内部方法  加()为直接调用
        self.bytes_to_hex_btn.grid(row=4, column=11)
        self.hex_to_utf8_btn = Button(self.init_window_name, text="hex转utf8", bg="lightblue", width=10,command=self.hex_to_utf8_func)  # 调用内部方法  加()为直接调用
        self.hex_to_utf8_btn.grid(row=5, column=11)
        self.hex_to_utf16_btn = Button(self.init_window_name, text="hex转utf16", bg="lightblue", width=10,command=self.hex_to_utf16_func)  # 调用内部方法  加()为直接调用
        self.hex_to_utf16_btn.grid(row=6, column=11)
        self.gzip_compression_btn = Button(self.init_window_name, text="Gzip压缩", bg="lightblue", width=10,command=self.gzip_compression)  # 调用内部方法  加()为直接调用
        self.gzip_compression_btn.grid(row=7, column=11)
        self.gzip_decompression_btn = Button(self.init_window_name, text="Gunzip解压", bg="lightblue", width=10,command=self.gzip_decompression)  # 调用内部方法  加()为直接调用
        self.gzip_decompression_btn.grid(row=8, column=11)
        self.zlib_compression_btn = Button(self.init_window_name, text="zlib压缩", bg="lightblue", width=10,command=self.zlib_compression)  # 调用内部方法  加()为直接调用
        self.zlib_compression_btn.grid(row=9, column=11)
        self.zlib_decompression_btn = Button(self.init_window_name, text="unZlib解压", bg="lightblue", width=10,command=self.zlib_decompression)  # 调用内部方法  加()为直接调用
        self.zlib_decompression_btn.grid(row=10, column=11)
        self.utf8_to_hex_btn = Button(self.init_window_name, text="utf8转hex", bg="lightblue", width=10,command=self.utf8_to_hex_func)  # 调用内部方法  加()为直接调用
        self.utf8_to_hex_btn.grid(row=2, column=12)
        self.slip_to_point_btn = Button(self.init_window_name, text="/转.", bg="lightblue", width=10,command=self.slip_to_point_func)  # 调用内部方法  加()为直接调用
        self.slip_to_point_btn.grid(row=3, column=12)
        self.lower_to_upper_btn = Button(self.init_window_name, text="upper", bg="lightblue", width=10,command=self.lower_to_upper_func)  # 调用内部方法  加()为直接调用
        self.lower_to_upper_btn.grid(row=4, column=12)
        self.upper_to_lower_btn = Button(self.init_window_name, text="lower", bg="lightblue", width=10,command=self.upper_to_lower_func)  # 调用内部方法  加()为直接调用
        self.upper_to_lower_btn.grid(row=5, column=12)
        self.charles_hex_to_hex_btn = Button(self.init_window_name, text="charles转hex", bg="lightblue", width=10,command=self.charles_hex_to_hex_func)  # 调用内部方法  加()为直接调用
        self.charles_hex_to_hex_btn.grid(row=6, column=12)
        self.compact_hex_to_hex_btn = Button(self.init_window_name, text="compactHex", bg="lightblue", width=10,command=self.compact_hex_to_hex_func)  # 调用内部方法  加()为直接调用
        self.compact_hex_to_hex_btn.grid(row=7, column=12)
        self.python_hex_to_hex_btn = Button(self.init_window_name, text="PyHexToHex", bg="lightblue", width=10,command=self.python_hex_to_hex_func)  # 调用内部方法  加()为直接调用
        self.python_hex_to_hex_btn.grid(row=8, column=12)

    
        ####初始化字符串用于测试
        ##self.init_data_Text.insert(1.0,'7b22726573756c74223a2274727565222c22737461747573436f6465223a223fc4fe22c2270726f6d707431223a22e8afbf1ffe8aebae68890e58a')

    def listToStr(self, listbyte):
        retstr=bytes()
        for i in listbyte:
            retstr += struct.pack("B",i &0xff)
        return retstr.hex()
    def hexStrToJavaBytesStr(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            outstr="byte data[] = {\n"
            for i in range(int(len(src) / 2)):
                outstr += ("(byte)0x%x,"%(bytes.fromhex(src)[i]&0xff))
            outstr +="\n};"
            self.return_outcome(outstr)
            return
        self.result_data_Text.insert(1.0,"hex to java bytes failed")
    def gzip_compression(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                packbytes = gzip.compress(bytes.fromhex(src))
                self.return_outcome(packbytes.hex())
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"gzip compression failed")
    def gzip_decompression(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                unpackbytes = gzip.decompress(bytes.fromhex(src))
                self.return_outcome(unpackbytes.hex())
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"gzip decompression failed")
    def zlib_compression(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                packbytes = zlib.compress(bytes.fromhex(src))
                self.return_outcome(packbytes.hex())
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"gzip compression failed")
    def zlib_decompression(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                unpackbytes = zlib.decompress(bytes.fromhex(src))
                self.return_outcome(unpackbytes.hex())
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"zlib decompression failed")
    def hex_to_utf8_func(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                self.return_outcome('%s'%bytes.fromhex(src).decode('utf-8'))
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"Exception: %s" %ex)
        self.result_data_Text.insert(1.0,"hex_to_utf8_func failed\n")
        
    def hex_to_utf16_func(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                ###//这里有时候会多一个字节出来,容易出错
                if(len(src) % 4 > 0):
                    src=src[0:len(src) -2]
                self.return_outcome('%s'%bytes.fromhex(src).decode('utf-16'))
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"hex_to_utf16 failed")
    def unicode_to_str_func(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                self.return_outcome(src.encode('utf-8').decode('unicode_escape'))
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"unicode_to_str failed")
    def utf8_to_hex_func(self):
        src = self.init_data_Text.get(1.0,END)
        ### 删除最后自动添加的 回车
        src = src[:-1]
        if src:
            try:
                self.return_outcome(stringToHexString(src))
                return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"utf8_to_hex failed")
    def return_outcome(self, msgstr):
        self.result_data_Text.delete(1.0,'end')
        self.result_data_Text.insert(1.0, msgstr)
        if(self.CheckClipValue.get()):
            pyperclip.copy(self.result_data_Text.get(1.0,END).strip())
    #将 10进制数组 转化为  16进制字符串
    def bytes_memory_hex(self):
        src = self.init_data_Text.get(1.0,END).strip()
        liststr= src.split(",")
        for i in range(len(liststr)):
            if(liststr[i].find('(byte)') >= 0):
                liststr[i] = int(liststr[i].replace('(byte)',''), 16)
            else:
                liststr[i] = int(liststr[i], 10)
        if src:
            try:
                self.return_outcome(self.listToStr(liststr))
                return
            except:
                self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0,"byte to hex failed")
    def slip_to_point_func(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        if src:
            try:
                ###//这里有时候会多一个字节出来,容易出错
                if(len(src) > 0):
                    self.return_outcome(src.replace('/','.'))
                    return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"slip_to_point failed")
    def lower_to_upper_func(self):
        src = self.init_data_Text.get(1.0,END)
        if src:
            try:
                ###//这里有时候会多一个字节出来,容易出错
                if(len(src) > 0):
                    self.return_outcome(src.upper())
                    return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"lower_to_upper failed")
    def upper_to_lower_func(self):
        src = self.init_data_Text.get(1.0,END)
        if src:
            try:
                ###//这里有时候会多一个字节出来,容易出错
                if(len(src) > 0):
                    self.return_outcome(src.lower())
                    return
            except Exception as ex:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"\nException: %s" %ex)
        self.result_data_Text.insert(1.0,"lower_to_upper failed")
    def charles_hex_to_hex_func(self):
        src = self.init_data_Text.get(1.0,END).strip()
        data_list = src.split('\n')
        des = ""
        for hang in data_list:
            if(len(hang) > 0x39):
                hang =hang.strip()
                tlist = hang.split('\x20\x20')
                if(len(tlist) < 2):
                    self.result_data_Text.insert(1.0,"charles_hex_to_hex failed")
                    return 
                des += tlist[1]
        self.return_outcome(des.replace(' ','').replace('\n','').replace('\r','').replace('\t',''))
    def compact_hex_to_hex_func(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        self.return_outcome(src)
    def python_hex_to_hex_func(self):
        src = self.init_data_Text.get(1.0,END).strip().replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        listx = src.split(r'\x')
        strout = ""
        for str in listx:
            if(len(str) < 1):
                connect
            elif(len(str) < 2):
                strout += '0' + str
            else:
                strout +=str
        self.return_outcome(strout)
def center_window(root, w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
def main():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    #### //将窗口显示在最前面
    init_window.lift()
    init_window.attributes('-topmost',True)
    init_window.after_idle(init_window.attributes,'-topmost',False)
    ##### //将主窗口居中
    init_window.update()
    center_window(init_window,init_window.winfo_width(), init_window.winfo_height())
    ###//程序启动获取焦点
    app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
    app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


main()