# byteProcessor

> 一款面向逆向工程场景的字节码处理工具，基于 PyQt5 编写，提供常见的进制、编码、压缩与 Protobuf 转换能力。

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)

---

## 简介

在逆向分析中，我们经常需要在不同的字节表示形式之间来回切换：从 Charles 抓包导出的格式、从 gdb / hexdump 拷贝出的内存视图、Java 数组定义、Python `\x` 字面量、Protobuf 二进制等。`byteProcessor` 把这些零碎的转换需求收敛到一个图形界面里，左边粘贴原始数据，点对应按钮即可拿到目标格式，结果可自动复制到剪贴板。

## 主要特性

### 编码 / 解码
| 功能 | 说明 |
| --- | --- |
| **Hex → UTF-8 / UTF-16** | Hex 数据解码为可读字符串 |
| **UTF-8 → Hex** | 字符串编码为 Hex |
| **Unicode → 字符串** | `空道` → `空道` |
| **大小写互转** | 字符串大小写统一转换 |
| **`/` → `.`** | 路径分隔符替换（常用于类名转换） |

### Hex 格式归一化
| 功能 | 输入示例 | 输出 |
| --- | --- | --- |
| **紧凑格式化** | `AB CC DD ED` | `ABCCDDED` |
| **Python 字面量** | `\x33\xAB\xCC` | `33ABCC` |
| **Charles 格式** | Charles 抓包面板复制的混合视图 | 提取出纯 Hex |
| **gdb 内存** | `0x7718242e58: 0x20 0x1c ...` | `201c...` |
| **hexdump** | `00000000: 48 54 54 50 ...` | `48545450...` |
| **字节倒序** | `12 34 56 78` | `78563412` |

### Java 互转
| 功能 | 说明 |
| --- | --- |
| **Java 数组 → Hex** | `{101,32,(byte)0xe0,-91}` → `65202ce0a5` |
| **Hex → Java 数组** | Hex 字符串生成 `byte data[] = { (byte)0x.., ... };` 定义 |

### 压缩 / 解压（基于 Hex）
- gzip 压缩 / 解压
- zlib 压缩 / 解压

### Protobuf
| 功能 | 说明 |
| --- | --- |
| **Proto Decode** | 输入 Protobuf 的 Hex 数据，输出结构化 JSON（自带解析器，无需 `.proto` 文件） |
| **Proto Encode** | 修改 Decode 出的 JSON 后重新编码为 Hex |
| **PB → Str** | 调用本机 `protoc --decode_raw` 解析（需安装 `protoc`） |

## 截图

> 在输入框留空并点击任一功能按钮，会显示该功能的使用说明与示例。

## 环境要求

- Python 3.x
- 依赖库：

  ```bash
  pip install PyQt5 pyperclip chardet
  ```

- 可选：`protoc`（仅 **PB → Str** 功能需要）
  - macOS：`brew install protobuf`
  - Linux：`apt install protobuf-compiler`

## 快速开始

### 直接运行源码

```bash
python3 main.py
```

### 打包为可执行应用（macOS）

```bash
chmod +x buildapp.sh
./buildapp.sh
```

构建完成后可在 `dist/` 目录下得到：

- `dist/byteProcessor`     可执行文件
- `dist/byteProcessor.app` macOS 应用包

打包基于 [PyInstaller](https://pyinstaller.org/)，使用前请先 `pip install pyinstaller`。

### 重新生成 UI

界面由 Qt Designer 设计的 `ui/login.ui` 编译而来。如修改了 UI 文件，重新生成 `login.py`：

```bash
cd ui
sh buidui.sh
```

## 项目结构

```
byteProcessor/
├── main.py             # 主程序入口，包含所有功能实现
├── parseProtobuf.py    # 自实现的 Protobuf 编解码器（无需 .proto 描述文件）
├── buildapp.sh         # macOS 打包脚本
├── ui/
│   ├── login.ui        # Qt Designer 设计文件
│   ├── login.py        # 由 .ui 编译而来的 Python 界面代码
│   ├── buidui.sh       # UI 重新编译脚本
│   └── HexToBytes.icns # 应用图标
└── README.md
```

## 使用提示

- 输入框 **留空** 并点击任意按钮，会在输出区显示该功能的说明与样例。
- 勾选界面上的复选框后，输出结果会自动写入系统剪贴板。
- 多数 Hex 类功能在处理前会自动剔除空格、换行、Tab 等空白符，无需手动整理。

## 开发与扩展

每个功能均为 `MyMainForm` 类下的 `xxx_func` 方法，遵循统一模式：

1. 从 `textEdit_input` 读入并清洗输入；
2. 输入为空 → 调用 `return_outcome(说明文本, False)` 仅显示帮助；
3. 输入非空 → 计算结果并 `return_outcome(结果)`，遇异常时打印 `Exception` 信息，不会让程序崩溃。

新增功能只需：

1. 在 `ui/login.ui` 中添加按钮并命名 `btn_xxx`；
2. 重新编译 UI；
3. 在 `MyMainForm.__init__` 中绑定 `clicked` 信号，并实现对应 `xxx_func`。

## 作者

**空道 (Kongdao)** — 创建于 2020/11/12

## License

未指定开源协议。如需在生产或商业环境使用，请先与作者确认授权方式。
