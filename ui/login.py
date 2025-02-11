# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1260, 646)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(2048, 1024))
        self.textEdit_input = QtWidgets.QTextEdit(Form)
        self.textEdit_input.setGeometry(QtCore.QRect(10, 50, 471, 591))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        self.textEdit_input.setFont(font)
        self.textEdit_input.setAcceptRichText(False)
        self.textEdit_input.setObjectName("textEdit_input")
        self.btn_bytes_memory_hex = QtWidgets.QPushButton(Form)
        self.btn_bytes_memory_hex.setGeometry(QtCore.QRect(490, 80, 121, 32))
        self.btn_bytes_memory_hex.setObjectName("btn_bytes_memory_hex")
        self.btn_unicode_to_str = QtWidgets.QPushButton(Form)
        self.btn_unicode_to_str.setGeometry(QtCore.QRect(490, 120, 121, 32))
        self.btn_unicode_to_str.setObjectName("btn_unicode_to_str")
        self.btn_hex_to_java_bytes = QtWidgets.QPushButton(Form)
        self.btn_hex_to_java_bytes.setGeometry(QtCore.QRect(490, 160, 121, 32))
        self.btn_hex_to_java_bytes.setObjectName("btn_hex_to_java_bytes")
        self.btn_hex_to_utf8 = QtWidgets.QPushButton(Form)
        self.btn_hex_to_utf8.setGeometry(QtCore.QRect(490, 200, 121, 32))
        self.btn_hex_to_utf8.setObjectName("btn_hex_to_utf8")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(490, 50, 131, 20))
        self.checkBox.setTabletTracking(False)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.textEdit_output = QtWidgets.QTextEdit(Form)
        self.textEdit_output.setGeometry(QtCore.QRect(750, 50, 501, 591))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        self.textEdit_output.setFont(font)
        self.textEdit_output.setAcceptRichText(False)
        self.textEdit_output.setObjectName("textEdit_output")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(750, 20, 60, 16))
        self.label_2.setObjectName("label_2")
        self.btn_hex_to_utf16 = QtWidgets.QPushButton(Form)
        self.btn_hex_to_utf16.setGeometry(QtCore.QRect(490, 240, 121, 32))
        self.btn_hex_to_utf16.setObjectName("btn_hex_to_utf16")
        self.btn_gzip_compression = QtWidgets.QPushButton(Form)
        self.btn_gzip_compression.setGeometry(QtCore.QRect(490, 280, 121, 32))
        self.btn_gzip_compression.setObjectName("btn_gzip_compression")
        self.btn_gzip_decompression = QtWidgets.QPushButton(Form)
        self.btn_gzip_decompression.setGeometry(QtCore.QRect(490, 320, 121, 32))
        self.btn_gzip_decompression.setObjectName("btn_gzip_decompression")
        self.btn_zlib_compression = QtWidgets.QPushButton(Form)
        self.btn_zlib_compression.setGeometry(QtCore.QRect(490, 360, 121, 32))
        self.btn_zlib_compression.setObjectName("btn_zlib_compression")
        self.btn_zlib_decompression = QtWidgets.QPushButton(Form)
        self.btn_zlib_decompression.setGeometry(QtCore.QRect(490, 400, 121, 32))
        self.btn_zlib_decompression.setObjectName("btn_zlib_decompression")
        self.btn_slip_to_point = QtWidgets.QPushButton(Form)
        self.btn_slip_to_point.setGeometry(QtCore.QRect(620, 80, 121, 32))
        self.btn_slip_to_point.setObjectName("btn_slip_to_point")
        self.btn_utf8_to_hex = QtWidgets.QPushButton(Form)
        self.btn_utf8_to_hex.setGeometry(QtCore.QRect(620, 200, 121, 32))
        self.btn_utf8_to_hex.setObjectName("btn_utf8_to_hex")
        self.btn_lower_to_upper = QtWidgets.QPushButton(Form)
        self.btn_lower_to_upper.setGeometry(QtCore.QRect(620, 120, 121, 32))
        self.btn_lower_to_upper.setObjectName("btn_lower_to_upper")
        self.btn_upper_to_lower = QtWidgets.QPushButton(Form)
        self.btn_upper_to_lower.setGeometry(QtCore.QRect(620, 160, 121, 32))
        self.btn_upper_to_lower.setObjectName("btn_upper_to_lower")
        self.btn_charles_hex_to_hex = QtWidgets.QPushButton(Form)
        self.btn_charles_hex_to_hex.setGeometry(QtCore.QRect(620, 240, 121, 32))
        self.btn_charles_hex_to_hex.setObjectName("btn_charles_hex_to_hex")
        self.btn_compact_hex_to_hex = QtWidgets.QPushButton(Form)
        self.btn_compact_hex_to_hex.setGeometry(QtCore.QRect(620, 280, 121, 32))
        self.btn_compact_hex_to_hex.setObjectName("btn_compact_hex_to_hex")
        self.btn_python_hex_to_hex = QtWidgets.QPushButton(Form)
        self.btn_python_hex_to_hex.setGeometry(QtCore.QRect(620, 320, 121, 32))
        self.btn_python_hex_to_hex.setObjectName("btn_python_hex_to_hex")
        self.btn_pb_bin_to_str = QtWidgets.QPushButton(Form)
        self.btn_pb_bin_to_str.setGeometry(QtCore.QRect(490, 440, 121, 32))
        self.btn_pb_bin_to_str.setObjectName("btn_pb_bin_to_str")
        self.btn_proto_decode = QtWidgets.QPushButton(Form)
        self.btn_proto_decode.setGeometry(QtCore.QRect(620, 360, 121, 32))
        self.btn_proto_decode.setObjectName("btn_proto_decode")
        self.btn_proto_encode = QtWidgets.QPushButton(Form)
        self.btn_proto_encode.setGeometry(QtCore.QRect(620, 400, 121, 32))
        self.btn_proto_encode.setObjectName("btn_proto_encode")
        self.btn_gdb_hex_to_hex = QtWidgets.QPushButton(Form)
        self.btn_gdb_hex_to_hex.setGeometry(QtCore.QRect(620, 440, 121, 32))
        self.btn_gdb_hex_to_hex.setObjectName("btn_gdb_hex_to_hex")
        self.btn_byte_reverse_byte = QtWidgets.QPushButton(Form)
        self.btn_byte_reverse_byte.setGeometry(QtCore.QRect(490, 480, 121, 32))
        self.btn_byte_reverse_byte.setObjectName("btn_byte_reverse_byte")
        self.btn_hex_dump_to_hex = QtWidgets.QPushButton(Form)
        self.btn_hex_dump_to_hex.setGeometry(QtCore.QRect(620, 480, 121, 32))
        self.btn_hex_dump_to_hex.setObjectName("btn_hex_dump_to_hex")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "空道 字节处理_v2.1"))
        self.btn_bytes_memory_hex.setText(_translate("Form", "Bytes转Hex"))
        self.btn_unicode_to_str.setText(_translate("Form", "unicode转字符"))
        self.btn_hex_to_java_bytes.setText(_translate("Form", "Hex转JavaByte"))
        self.btn_hex_to_utf8.setText(_translate("Form", "hex转utf8"))
        self.checkBox.setText(_translate("Form", "结果复制到剪贴板"))
        self.label.setText(_translate("Form", "输入数据"))
        self.label_2.setText(_translate("Form", "输出数据"))
        self.btn_hex_to_utf16.setText(_translate("Form", "hex转utf16"))
        self.btn_gzip_compression.setText(_translate("Form", "Gzip压缩"))
        self.btn_gzip_decompression.setText(_translate("Form", "Gunzip解压"))
        self.btn_zlib_compression.setText(_translate("Form", "zlib压缩"))
        self.btn_zlib_decompression.setText(_translate("Form", "unZlib解压"))
        self.btn_slip_to_point.setText(_translate("Form", "/转."))
        self.btn_utf8_to_hex.setText(_translate("Form", "utf8转hex"))
        self.btn_lower_to_upper.setText(_translate("Form", "upper"))
        self.btn_upper_to_lower.setText(_translate("Form", "lower"))
        self.btn_charles_hex_to_hex.setText(_translate("Form", "charles转hex"))
        self.btn_compact_hex_to_hex.setText(_translate("Form", "compactHex"))
        self.btn_python_hex_to_hex.setText(_translate("Form", "PyHexToHex"))
        self.btn_pb_bin_to_str.setText(_translate("Form", "pb用命令解码"))
        self.btn_proto_decode.setText(_translate("Form", "protoDecode"))
        self.btn_proto_encode.setText(_translate("Form", "protoEncode"))
        self.btn_gdb_hex_to_hex.setText(_translate("Form", "gdbHexToHex"))
        self.btn_byte_reverse_byte.setText(_translate("Form", "字节倒序"))
        self.btn_hex_dump_to_hex.setText(_translate("Form", "HexdumpToHex"))
