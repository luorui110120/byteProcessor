#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: By 空道
# Created on 10:19 2020/11/12
import os
import sys
sys.dont_write_bytecode = True

import hashlib,gzip,zlib
import time
import struct,sys
import re
import os
import pyperclip,subprocess
import chardet

# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from ui.login import Ui_Form
import parseProtobuf


LOG_LINE_NUM = 0
g_README = r"""软件使用说明:
在输入框中留空,点击对应功能按钮,可展示说明;
软件作者: 空道
"""

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
def byteToList(bs):
    if sys.version > '3':
        return list(bs)
    else:
        strByteList=[]
        for i in bs:
            strByteList.append(ord(i))
        return strByteList
    #return list(bs)
def listToBytes(l):
    if sys.version > '3':
        newlist=[]
        for i in l:
            newlist.append(i &0xff)
        return bytes(newlist)
    else:
        retstr=bytes()
        for i in l:
            retstr += struct.pack("B",i &0xff)
        return retstr
def listToStr(listbyte):
    retstr=bytes()
    for i in listbyte:
        retstr += struct.pack("B", i &0xff)
    return retstr.hex()
def protocDecode(protocPath, data):
    process = subprocess.Popen([protocPath, '--decode_raw'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    output = error = None
    try:
        output, error = process.communicate(data)
    except OSError:
        pass
    finally:
        if process.poll() != 0:
            process.wait()
    return output
####将pb 中的 8进制转为字符串
def strOctToStr(data):
    newlist = []
    bytelist = byteToList(data)
    i = 0
    listsize = len(bytelist)
    while(i < listsize):
        if('\\' == bytelist[i]):
            pass
            newlist.append(int(bytelist[i + 1] + bytelist[i + 2] + bytelist[i + 3], 8))
            i = i + 3
        else:
            newlist.append(int.from_bytes(bytes(bytelist[i], encoding = "utf8"), byteorder='big'))
        i = i + 1
    newbytes = listToBytes(newlist)
    return (bytes.decode(newbytes,encoding=chardet.detect(newbytes)['encoding']))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.btn_bytes_memory_hex.clicked.connect(self.bytes_memory_hex_func)
        self.btn_unicode_to_str.clicked.connect(self.unicode_to_str_func)
        self.btn_hex_to_java_bytes.clicked.connect(self.hex_to_java_bytes_func)
        self.btn_hex_to_utf8.clicked.connect(self.hex_to_utf8_func)
        self.btn_hex_to_utf16.clicked.connect(self.hex_to_utf16_func)
        self.btn_gzip_compression.clicked.connect(self.gzip_compression_func)
        self.btn_gzip_decompression.clicked.connect(self.gzip_decompression_func)
        self.btn_zlib_compression.clicked.connect(self.zlib_compression_func)
        self.btn_zlib_decompression.clicked.connect(self.zlib_decompression_func)
        self.btn_slip_to_point.clicked.connect(self.slip_to_point_func)
        self.btn_lower_to_upper.clicked.connect(self.lower_to_upper_func)
        self.btn_upper_to_lower.clicked.connect(self.upper_to_lower_func)
        self.btn_utf8_to_hex.clicked.connect(self.utf8_to_hex_func)
        self.btn_charles_hex_to_hex.clicked.connect(self.charles_hex_to_hex_func)
        self.btn_compact_hex_to_hex.clicked.connect(self.compact_hex_to_hex_func)
        self.btn_python_hex_to_hex.clicked.connect(self.python_hex_to_hex_func)
        self.btn_pb_bin_to_str.clicked.connect(self.pb_bin_to_str_func)
        self.btn_proto_decode.clicked.connect(self.proto_decode_func)
        self.btn_proto_encode.clicked.connect(self.proto_encode_func)



        self.textEdit_output.setText(g_README)

    def bytes_memory_hex_func(self):
        src = self.textEdit_input.toPlainText().strip().replace('{', '').replace('}', '')
        if src:
            try:
                liststr = src.split(",")
                for i in range(len(liststr)):
                    if (liststr[i].find('(byte)') >= 0):
                        liststr[i] = int(liststr[i].replace('(byte)', ''), 16)
                    else:
                        liststr[i] = int(liststr[i], 10)
                self.return_outcome(listToStr(liststr))
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome("""
说明:
下面这个样的java数组, 转化为  hex输出
输入:
{101,32,42,12,44,(byte)0xe0,-91}   
输出:
65202a0c2ce0a5
        """, False)

    def unicode_to_str_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                self.return_outcome(src.encode('utf-8').decode('unicode_escape'))
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        #self.return_outcome("unicode_to_str failed!!!", False)
        else:
            self.return_outcome(r"""
说明:
可输入  \u7a7a\u9053 \u8ba1\u7b97\u5668  输出对应中文  "空道计算器"
                        """, False)

    def hex_to_java_bytes_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                outstr = "byte data[] = {\n"
                for i in range(int(len(src) / 2)):
                    outstr += ("(byte)0x%x," % (bytes.fromhex(src)[i] & 0xff))
                outstr += "\n};"
                self.return_outcome(outstr)
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        #self.return_outcome("hex to java bytes failed", False)
        else:
            self.return_outcome(r"""
说明:
可输入 Hex 数据, 输出 java 的 bytes 数组定义,比如:
输入:123123
输出:byte data[] = {
(byte)0x12,(byte)0x31,(byte)0x23,
};
                            """, False)

    def hex_to_utf8_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                self.return_outcome('%s' % bytes.fromhex(src).decode('utf-8'))
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        #self.return_outcome("hex to utf8 failed", False)
        else:
            self.return_outcome(r"""
说明:
可输入 Hex 数据, 输出 utf8 字符串
                            """, False)

    def hex_to_utf16_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                ###//这里有时候会多一个字节出来,容易出错
                if (len(src) % 4 > 0):
                    src = src[0:len(src) - 2]
                self.return_outcome('%s' % bytes.fromhex(src).decode('utf-16'))
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome(r"""
说明:
可输入 Hex 数据, 输出 utf16 字符串
""", False)

    def gzip_compression_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                packbytes = gzip.compress(bytes.fromhex(src))
                self.return_outcome(packbytes.hex())
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome("""
说明:
输入Hex 数据进行gzip压缩 
            """, False)

    def gzip_decompression_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                unpackbytes = gzip.decompress(bytes.fromhex(src))
                self.return_outcome(unpackbytes.hex())
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome("""
说明:
输入Hex 数据进行gzip解压
                """, False)

    def zlib_compression_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                packbytes = zlib.compress(bytes.fromhex(src))
                self.return_outcome(packbytes.hex())
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome("""
说明:
输入Hex 数据进行zlib压缩 
            """, False)

    def zlib_decompression_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                unpackbytes = zlib.decompress(bytes.fromhex(src))
                self.return_outcome(unpackbytes.hex())
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome("""
说明:
输入Hex 数据进行zlib解压
                """, False)
    def slip_to_point_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                if (len(src) > 0):
                    self.return_outcome(src.replace('/', '.'))
                    return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome("""
说明:
将所有的 / 替换为 .
                            """, False)

    def lower_to_upper_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                if (len(src) > 0):
                    self.return_outcome(src.upper())
                    return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome("""
说明:
将所有的小写字母改为大写
                            """, False)
    def upper_to_lower_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                if (len(src) > 0):
                    self.return_outcome(src.lower())
                    return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome("""
说明:
将所有的大写字母改为小写
                                    """, False)

    def utf8_to_hex_func(self):
        src = self.textEdit_input.toPlainText().strip()
        if src:
            try:
                self.return_outcome(stringToHexString(src))
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome("""
说明:
将utf8 字符串转为 Hex
                                                """, False)
    def charles_hex_to_hex_func(self):
        src = self.textEdit_input.toPlainText().strip()
        if src:
            try:
                data_list = src.split('\n')
                des = ""
                for hang in data_list:
                    hang = hang.strip()
                    tlist = hang.split('\x20\x20')
                    if (len(tlist) < 2):
                        self.return_outcome("charles_hex_to_hex failed", False)
                        return
                    des += tlist[1]
                self.return_outcome(des.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', ''))
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome("""
说明:
输入重charles 直接复制出来的数据格式如下,可直接自动提取中间的hex值;
00000000  0a 06 38 c6 a5 b2 97 06 12 c7 02 0a b4 01 09 00     8             
00000010  00 00 00 a1 d8 33 41 11 00 00 00 00 2f f9 36 41        3A     / 6A
00000020  20 50 28 96 06 30 f7 09 38 92 01 40 64 58 01 68    P(  0  8  @dX h
00000030  50 f0 01 e8 07 9a 02 11 08 01 10 08 21 00 00 00   P           !   
00000040  00 00 86 a2 40 28 02 30 01 9a 02 0f 08 02 10 08       @( 0        
00000050  21 00 00 00 00 00 86 a2 40 28 01 9a 02 11 08 05   !       @(      
00000060  10 08 21 00 00 00 00 00 86 a2 40 28 01 30 01 9a     !       @( 0  
00000070  02 11 08 07 10 08 21 00 00 00 00 00 86 a2 40 28         !       @(
00000080  02 30 01 9a 02 11 08 0a 10 08 21 00 00 00 00 00    0        !     
                            """, False)

    def compact_hex_to_hex_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            self.return_outcome(src)
        else:
            self.return_outcome(r"""
说明:
将输入框中的 空格,回车,Table 全部除去,变成紧凑的格式,比如:
AB CC DD ED      ->    AACCDDED
                            """, False)

    def python_hex_to_hex_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                listx = src.split(r'\x')
                strout = ""
                for strsub in listx:
                    if (len(strsub) < 1):
                        continue
                    elif (len(strsub) < 2):
                        strout += '0' + strsub
                    else:
                        strout += strsub
                self.return_outcome(strout)
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome(r"""
说明:
将python 中的  \x33\xAB\xCC  数据转化为 hex  33ABCC
                """, False)

    def pb_bin_to_str_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                ###打成 app 就无法获取PATH值, 所以写了固定值;
                ##env_dists = os.environ.get('PATH').split(':')
                env_dists = ["/usr/local/bin", "/Users/smali/bin", "/usr/local/sbin", "/bin", "/usr/bin", "/usr/sbin"]
                protoc_path = ''
                for env_path in env_dists:
                    tmppath = env_path + '/protoc'
                    if (os.path.exists(tmppath)):
                        protoc_path = tmppath
                if (protoc_path == ''):
                    strout = 'Fail!! not installed protoc!\nTraverse the list of directories:\n'
                    for path in env_dists:
                        strout = strout + path + '\n'
                    self.return_outcome(strout)
                    return
                strout = bytes.decode(protocDecode(protoc_path, hexStringTobytes(src)), encoding='utf8')
                if (strout == ''):
                    strout = 'Fail!! decode error!'
                    self.return_outcome(strout, False)
                    return
                findlist = re.findall("""\"[\\\\01234567]*\"""", strout)
                for substr in findlist:
                    if (substr.find('\\') >= 0):
                        newstr = strOctToStr(substr)
                        strout = strout.replace(substr, newstr)
                self.return_outcome(strout)
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
        else:
            self.return_outcome(r"""
说明:
通过 protoc --decode_raw < protobuf.bin  命令去解析 protobuf 数据,所以电脑上必须要装有 protoc 工具;
                """, False)

    def proto_decode_func(self):
        src = self.textEdit_input.toPlainText().strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\x00', '')
        if src:
            try:
                pbJson = parseProtobuf.ParseProtoBufToJson(bytes.fromhex(src))
                self.return_outcome(pbJson)
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome("""
说明:
输入 ProtoBuf的 Hex 数据, 可输出,json 结构
输入:0A0638FFA4B29706122C0A0908CAE5A7A0F34010040A0908CAE5A7A0F34010020A0908CAE5A7A0F34010030A0908CAE5A7A0F3401001
输出:
{
    "01:00:embedded message": {
        "07:00:Varint": 1659671167
    },
    "02:01:embedded message": {
        "01:00:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 4
        },
        "01:01:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 2
        },
        "01:02:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 3
        },
        "01:03:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 1
        }
    }
}
                """, False)

    def proto_encode_func(self):
        src = self.textEdit_input.toPlainText().strip()
        if src:
            try:
                newProtobuf = parseProtobuf.ParseJsonToProtoBuf(src)
                self.return_outcome(bytesToHexString(newProtobuf))
                return
            except Exception as ex:
                self.return_outcome("\nException: %s" % ex, False)
                return
        else:
            self.return_outcome("""
说明:
通过输入  上面 ProtoDecode 的json 结果,修改json 中的数据, 然后可重新编译Hex数据, 下面是 ProtoDecode 的结果
{
    "01:00:embedded message": {
        "07:00:Varint": 1659671167
    },
    "02:01:embedded message": {
        "01:00:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 4
        },
        "01:01:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 2
        },
        "01:02:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 3
        },
        "01:03:embedded message": {
            "01:00:Varint": 2229961093834,
            "02:01:Varint": 1
        }
    }
}
最后的输出结果
0A0638FFA4B29706122C0A0908CAE5A7A0F34010040A0908CAE5A7A0F34010020A0908CAE5A7A0F34010030A0908CAE5A7A0F3401001
                """, False)

    # 日志动态打印, flag 表示强制不赋值到剪切板;
    def return_outcome(self, msgstr, flag = True):
        self.textEdit_output.setText(msgstr)
        if self.checkBox.isChecked() and flag:
            pyperclip.copy(msgstr)

if __name__ == '__main__':
    #os.chdir(os.path.dirname(__file__))
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
