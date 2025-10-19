# PDF OCR 提取工具 🚀# PDF OCR 提取工具 🚀# PDF OCR 提取工具 🚀# PDF OCR 提取工具 🚀# PDF OCR 提取工具 🚀# PDF OCR 提取项目 ✨# PDF OCR Extraction Project



使用 PaddleOCR 多语言模型从 PDF 文件提取文本，支持 80+ 种语言。



**✅ 支持中英日韩法德等多种语言！**使用 PaddleOCR（支持中英日韩等多语言）从 PDF 文件提取文本。



## 🎉 项目状态



✅ **完成并可用** - PaddleOCR 多语言模型，简单高效**✅ 支持中英文混合识别 + 多语言支持！**使用 PaddleOCR（中英文）和 Tesseract OCR（日文）从 PDF 文件提取文本。



## 📋 核心功能



- ✅ PDF 转图片（pypdfium2，无需外部 poppler 依赖）## 🎉 项目状态

- ✅ **中英文混合 OCR 识别**（PaddleOCR PP-OCRv4 中文模型）

- ✅ **多语言支持**（PaddleOCR 多语言模型：日文、韩文、法文、德文等）

- ✅ 命令行参数支持，灵活配置

- ✅ 批量处理多页 PDF✅ **完成并可用** - 通用 CLI 工具，支持多种语言**✅ 支持中英文混合识别 + 日文识别！**使用纯 PaddleOCR 从 PDF 文件提取文本（不使用 PyMuPDF）。

- ✅ 可选进度显示

- ✅ UTF-8 格式输出

- ✅ 自定义图片质量和置信度阈值

## 📋 核心功能

## 📌 语言支持说明



### ✅ 优秀支持（PaddleOCR）

- **中文**（简体/繁体）：⭐⭐⭐⭐⭐ 完美识别- ✅ PDF 转图片（pypdfium2，无需外部 poppler 依赖）## 🎉 项目状态

- **英文**：⭐⭐⭐⭐⭐ 完美识别

- **中英文混合**：⭐⭐⭐⭐⭐ 完美识别- ✅ **中英文混合 OCR 识别**（PaddleOCR PP-OCRv4 中文模型）



### ✨ 多语言支持（PaddleOCR 多语言模型）- ✅ **多语言支持**（PaddleOCR 多语言模型：日文、韩文、法文、德文等）

- **日文**：⭐⭐⭐⭐⭐ 优秀识别（假名+汉字）

- **韩文**：⭐⭐⭐⭐ 良好识别- ✅ **Tesseract OCR 集成**（可选，作为备用方案）

- **法文/德文**：⭐⭐⭐⭐ 支持欧洲语言

- **阿拉伯文/拉丁文**：⭐⭐⭐⭐ 支持多种语系- ✅ 命令行参数支持，灵活配置✅ **完成并可用** - 通用 CLI 工具，智能选择 OCR 引擎**✅ 支持中英文混合识别！**使用纯 PaddleOCR 从 PDF 文件提取文本（不使用 PyMuPDF）。



> 💡 **提示**：首次使用多语言需要从网络下载模型（约 10-20MB）。在企业网络环境下可能需要手动下载，详见 [PaddleOCR多语言模型下载指南.md](PaddleOCR多语言模型下载指南.md)- ✅ 批量处理多页 PDF



## 🚀 快速开始- ✅ 可选进度显示



### 1️⃣ 安装 Python 依赖- ✅ UTF-8 格式输出



```bash- ✅ 自定义图片质量和置信度阈值## 📋 核心功能

# 安装 PaddleOCR 及相关依赖

pip install paddlepaddle==2.6.2

pip install paddleocr==2.7.3

pip install pypdfium2 Pillow tqdm opencv-python-headless## 📌 语言支持说明

pip install "numpy<2.0.0" --force-reinstall

```



### 2️⃣ 基本使用### ✅ 优秀支持（PaddleOCR，无需额外安装）- ✅ PDF 转图片（pypdfium2，无需外部 poppler 依赖）## 🎉 项目状态



```bash- **中文**（简体/繁体）：⭐⭐⭐⭐⭐ 完美识别

# 中文 PDF（默认）

python extract_pdf.py chinese_document.pdf- **英文**：⭐⭐⭐⭐⭐ 完美识别- ✅ **中英文混合 OCR 识别**（PaddleOCR PP-OCRv4 中文模型）



# 日文 PDF- **中英文混合**：⭐⭐⭐⭐⭐ 完美识别

python extract_pdf.py japanese_document.pdf --lang japan

- ✅ **日文 OCR 识别**（Tesseract OCR + 日文语言包）✨ 新增

# 韩文 PDF

python extract_pdf.py korean_document.pdf --lang korean### ✨ 多语言支持（PaddleOCR 多语言模型）



# 英文 PDF- **日文**：⭐⭐⭐⭐ 良好识别（需要下载多语言模型）- ✅ 智能选择 OCR 引擎（根据语言自动切换）

python extract_pdf.py english_document.pdf --lang en

- **韩文**：⭐⭐⭐⭐ 良好识别（需要下载多语言模型）

# 指定输出文件名

python extract_pdf.py input.pdf -o output.txt- **法文/德文**：⭐⭐⭐⭐ 支持欧洲语言- ✅ 命令行参数支持，灵活配置✅ **完成并可用** - 通用 CLI 工具，支持灵活配置**✅ 支持中英文混合识别！**使用纯 PaddleOCR 从 PDF 文件提取文本（不使用 PyMuPDF）。使用纯 PaddleOCR 从 PDF 文件提取文本的项目（不使用 PyMuPDF）。

```

- **阿拉伯文/拉丁文**：⭐⭐⭐⭐ 支持多种语系

### 3️⃣ 高级选项

- ✅ 批量处理多页 PDF

```bash

# 提高图片质量（推荐用于日文和低质量扫描件）⚠️ **注意**：首次使用多语言模型需要从网络下载（约 10-20MB）。在企业网络环境下可能遇到 SSL 证书问题，详见 [PaddleOCR多语言模型下载指南.md](PaddleOCR多语言模型下载指南.md)

python extract_pdf.py file.pdf --lang japan --scale 3.0

- ✅ 可选进度显示

# 调整置信度阈值（0.0-1.0，越低保留越多内容）

python extract_pdf.py file.pdf --confidence 0.3### 🔄 备选方案（Tesseract OCR）



# 不显示进度条（避免某些环境的中断问题）如果 PaddleOCR 多语言模型无法下载，可以使用 Tesseract OCR：- ✅ UTF-8 格式输出

python extract_pdf.py file.pdf --no-progress

- 使用 `--use-tesseract` 参数

# 组合多个选项

python extract_pdf.py file.pdf --lang japan -o result.txt --scale 3.0 --no-progress- 需要单独安装，详见 [Tesseract安装指南.md](Tesseract安装指南.md)- ✅ 自定义图片质量和置信度阈值## 📋 核心功能

```



### 4️⃣ 查看帮助

## 🚀 快速开始

```bash

python extract_pdf.py --help

```

### 1️⃣ 安装 Python 依赖## 📌 语言支持说明

## 📝 文件说明



| 文件 | 功能 | 说明 |

|------|------|------|```bash

| `extract_pdf.py` | ⭐ **通用提取脚本** | 支持中英日韩等 80+ 种语言 |

| `PaddleOCR多语言模型下载指南.md` | 📖 下载指南 | 手动下载多语言模型的方法 |# PaddleOCR 依赖（必装）

| `verify_models.py` | 🔧 模型验证工具 | 检查 PaddleOCR 模型状态 |

| `install_chinese_models.py` | 🔧 模型安装助手 | 手动安装中文模型 |pip install paddlepaddle==2.6.2### ✅ 优秀支持（PaddleOCR）- ✅ PDF 转图片（pypdfium2，无需外部 poppler 依赖）## 🎉 项目状态**✅ 支持中英文混合识别！**

| `README.md` | 📖 项目文档 | 本文件 |

pip install paddleocr==2.7.3

## 🎯 使用场景

pip install pypdfium2 Pillow tqdm opencv-python-headless- **中文**（简体/繁体）：⭐⭐⭐⭐⭐ 完美识别

### 场景 1：处理中英文混合 PDF

```bashpip install "numpy<2.0.0" --force-reinstall

python extract_pdf.py CDS.pdf

# 使用 PaddleOCR，效果极佳- **英文**：⭐⭐⭐⭐⭐ 完美识别- ✅ **中英文混合 OCR 识别**（PaddleOCR PP-OCRv4 中文模型）

```

# Tesseract OCR 依赖（可选，仅作为备用方案）

### 场景 2：处理日文 PDF ⭐

```bashpip install pytesseract- **中英文混合**：⭐⭐⭐⭐⭐ 完美识别

python extract_pdf.py cdsjp.pdf --lang japan --scale 3.0

# 日文假名和汉字识别效果优秀```

```

- ✅ 命令行参数支持，灵活配置

### 场景 3：处理韩文 PDF

```bash### 2️⃣ 基本使用

python extract_pdf.py korean.pdf --lang korean --scale 3.0

```### ✅ 日文支持（Tesseract OCR）✨ 新增



### 场景 4：大文件处理（70+ 页）```bash

```bash

python extract_pdf.py large_document.pdf --scale 2.5 --no-progress# 中文 PDF（默认，使用 PaddleOCR）- **日文**（汉字 + 假名）：⭐⭐⭐⭐ 良好识别- ✅ 批量处理多页 PDF

```

python extract_pdf.py chinese_document.pdf

### 场景 5：低质量扫描文档

```bash  - 需要安装 Tesseract OCR 和日文语言包

python extract_pdf.py scan.pdf --scale 3.0 --confidence 0.3

# 更高图片质量 + 更宽松的置信度# 日文 PDF（使用 PaddleOCR 多语言模型）

```

python extract_pdf.py japanese_document.pdf --lang japan  - 详见：[Tesseract安装指南.md](Tesseract安装指南.md)- ✅ 可选进度显示✅ **完成并可用** - 通用 CLI 工具，支持灵活配置## 功能

## ⚙️ 参数说明



| 参数 | 默认值 | 说明 |

|------|--------|------|# 韩文 PDF  - 使用方法：`python extract_pdf.py file.pdf --lang japan`

| `pdf_file` | 必填 | 输入 PDF 文件路径 |

| `-o, --output` | `{PDF名}_extracted.txt` | 输出文本文件路径 |python extract_pdf.py korean_document.pdf --lang korean

| `-t, --temp-dir` | `temp_images_{PDF名}` | 临时图片存储目录 |

| `--lang` | `ch` | 语言：`ch`, `en`, `japan`, `korean`, `french`, `german`等 |- ✅ UTF-8 格式输出

| `--scale` | `2.0` | 图片缩放倍数（1.0-4.0，推荐 2.0-3.0） |

| `--confidence` | `0.5` | 置信度阈值（0.0-1.0） |# 英文 PDF

| `--no-progress` | 否 | 禁用进度条 |

python extract_pdf.py english_document.pdf --lang en### 🔄 OCR 引擎选择

## 📊 支持的语言



| 语言 | PaddleOCR 参数 | 识别效果 | 模型版本 |

|------|---------------|---------|---------|# 指定输出文件名- ✅ 自定义图片质量和置信度阈值

| 中文（简体） | `ch` | ⭐⭐⭐⭐⭐ | PP-OCRv4 |

| 英文 | `en` | ⭐⭐⭐⭐⭐ | PP-OCRv3 |python extract_pdf.py input.pdf -o output.txt

| 日文 | `japan` | ⭐⭐⭐⭐⭐ | PP-OCRv4 |

| 韩文 | `korean` | ⭐⭐⭐⭐ | PP-OCRv4 |```| 语言参数 | OCR 引擎 | 识别效果 |

| 法文 | `french` | ⭐⭐⭐⭐ | PP-OCRv3 |

| 德文 | `german` | ⭐⭐⭐⭐ | PP-OCRv3 |

| 阿拉伯文 | `arabic` | ⭐⭐⭐⭐ | PP-OCRv3 |

| 拉丁文 | `latin` | ⭐⭐⭐⭐ | PP-OCRv3 |### 3️⃣ 高级选项|---------|---------|---------|



## 📊 测试结果



| 测试文件 | 页数 | 内容类型 | 语言模型 | 耗时 | 输出大小 | 识别效果 |```bash| `--lang ch` | PaddleOCR | ⭐⭐⭐⭐⭐ 中文+英文 |

|---------|------|---------|---------|------|---------|---------|

| SAP-C_BCSBS_2502(1).pdf | 70 | 纯英文 | en | ~7-9 秒/页 | 95 KB | ⭐⭐⭐⭐⭐ 优秀 |# 提高图片质量（推荐用于日文和低质量扫描件）

| CDS.pdf | 2 | 中英文混合 | ch | ~3 秒/页 | 2.9 KB | ⭐⭐⭐⭐⭐ 优秀 |

| cdsjp.pdf | 3 | 日文 | japan (v4) | ~5 秒/页 | 7.9 KB | ⭐⭐⭐⭐⭐ 优秀 |python extract_pdf.py file.pdf --lang japan --scale 3.0| `--lang en` | PaddleOCR | ⭐⭐⭐⭐⭐ 纯英文 |## 📌 语言支持说明## 📋 核心功能## 🎉 项目状态



## 🔧 故障排除



### 问题 1：中文内容无法识别# 调整置信度阈值| `--lang japan` | **Tesseract OCR** | ⭐⭐⭐⭐ 日文 |

**解决方案**：确保使用中文模型（默认）

```bashpython extract_pdf.py file.pdf --confidence 0.3

python extract_pdf.py your_file.pdf --lang ch

```| `--lang korean` | Tesseract OCR | ⭐⭐⭐⭐ 韩文 |



### 问题 2：日文模型下载失败（SSL 证书错误）# 不显示进度条（避免某些环境的中断问题）

**原因**：企业网络环境下的 SSL 证书验证问题

python extract_pdf.py file.pdf --no-progress

**解决方案**：手动下载模型

1. 参考 [PaddleOCR多语言模型下载指南.md](PaddleOCR多语言模型下载指南.md)

2. 下载 `Multilingual_PP-OCRv3_det_infer.tar`（检测模型）

3. 下载 `japan_PP-OCRv4_rec_infer.tar`（日文识别模型）# 强制使用 Tesseract OCR（需要先安装）## 🚀 快速开始### ✅ 优秀支持

4. 按指南放置到正确目录

python extract_pdf.py file.pdf --lang japan --use-tesseract

### 问题 3：识别内容太少

**解决方案**：降低置信度阈值，提高图片质量

```bash

python extract_pdf.py your_file.pdf --scale 3.0 --confidence 0.3# 组合多个选项

```

python extract_pdf.py file.pdf --lang japan -o result.txt --scale 3.0 --no-progress### 1️⃣ 安装 Python 依赖- **中文**（简体/繁体）：⭐⭐⭐⭐⭐ 完美识别

### 问题 4：进度条导致程序中断

**解决方案**：使用 `--no-progress` 参数```

```bash

python extract_pdf.py your_file.pdf --no-progress

```

### 4️⃣ 查看帮助

### 问题 5：检查模型是否安装

```bash```bash- **英文**：⭐⭐⭐⭐⭐ 完美识别- ✅ PDF 转图片（pypdfium2，无需外部 poppler 依赖）- 将 PDF 转换为图片（使用 pypdfium2，无需外部依赖）

python verify_models.py

``````bash



## 📚 技术细节python extract_pdf.py --help# PaddleOCR 依赖（必装，用于中英文）



### 架构设计```

```

PDF 文件pip install paddlepaddle==2.6.2- **中英文混合**：⭐⭐⭐⭐⭐ 完美识别

    ↓

pypdfium2 (PDF → 图片)## 📝 文件说明

    ↓

临时图片目录 (PNG 格式)pip install paddleocr==2.7.3

    ↓

PaddleOCR 多语言模型| 文件 | 功能 | 说明 |

    ├─ 中英文 → PP-OCRv4

    ├─ 日韩等 → PP-OCRv4/v3 多语言模型|------|------|------|pip install pypdfium2 Pillow tqdm opencv-python-headless- ✅ **中英文混合 OCR 识别**（PaddleOCR PP-OCRv4 中文模型）

    └─ 其他语言 → PP-OCRv3 多语言模型

    ↓| `extract_pdf.py` | ⭐ **通用提取脚本** | 支持中英日韩等多语言 |

文本输出 (UTF-8 TXT)

```| `PaddleOCR多语言模型下载指南.md` | 📖 下载指南 | 解决 SSL 证书问题 |pip install "numpy<2.0.0" --force-reinstall



### 依赖版本| `Tesseract安装指南.md` | 📖 安装指南 | Tesseract OCR 备用方案 |

- Python: 3.12+

- PaddlePaddle: 2.6.2| `verify_models.py` | 🔧 模型验证工具 | 检查 PaddleOCR 模型状态 |### ⚠️ 有限支持  

- PaddleOCR: 2.7.3

- pypdfium2: 4.30.0| `install_chinese_models.py` | 🔧 模型安装助手 | 手动安装中文模型 |

- Pillow: 12.0.0

- opencv-python: 4.6.0+| `README.md` | 📖 项目文档 | 本文件 |# Tesseract OCR 依赖（可选，用于日文）

- numpy: <2.0.0

- tqdm: 最新版



### PaddleOCR 模型说明## 🎯 使用场景pip install pytesseract- **日文汉字**：⭐⭐⭐ 部分正确（仅限与中文相似的汉字）- ✅ 命令行参数支持，灵活配置✅ **完成并可用** - 中英文内容提取成功！- 使用 PaddleOCR 进行 OCR 文字识别

- **中文模型**：`ch_PP-OCRv4_det` + `ch_PP-OCRv4_rec`

- **多语言检测模型**：`Multilingual_PP-OCRv3_det`（所有多语言共用）

- **日文识别模型**：`japan_PP-OCRv4_rec`

- **韩文识别模型**：`korean_PP-OCRv4_rec`### 场景 1：处理中英文混合 PDF```



## 🌟 特性亮点```bash



1. ✨ **零外部依赖**：pypdfium2 无需安装 popplerpython extract_pdf.py CDS.pdf- **日文假名**（平假名/片假名）：⭐ 识别率低，**不推荐使用**

2. 🌍 **真正的多语言**：PaddleOCR 原生支持 80+ 种语言

3. 🚀 **简单高效**：单一 OCR 引擎，无需切换# 使用 PaddleOCR，效果极佳，无需额外配置

4. 📊 **进度可视化**：可选的 tqdm 进度条

5. ⚡ **灵活配置**：图片质量、置信度、语言模型均可调整```### 2️⃣ 安装 Tesseract OCR（仅日文需要）

6. 🛠️ **错误处理**：完善的异常处理和用户提示

7. 📝 **编码正确**：UTF-8 输出，完美支持各种语言

8. 🎯 **日文优化**：使用 PP-OCRv4 模型，假名识别准确

### 场景 2：处理日文 PDF- ✅ 批量处理多页 PDF

## ⚠️ 使用限制

```bash

1. **多语言模型下载**：首次使用日文/韩文等需要从网络下载模型（约 10-20MB）

2. **手写文字**：主要针对印刷体，手写识别效果较差# 方法 1：使用 PaddleOCR 多语言模型（推荐）**如果需要处理日文 PDF**，请按照 [Tesseract安装指南.md](Tesseract安装指南.md) 安装 Tesseract OCR 和日文语言包。

3. **复杂排版**：多栏、表格等复杂排版可能顺序混乱

4. **图片质量**：低质量扫描件识别效果受限python extract_pdf.py cdsjp.pdf --lang japan --scale 3.0



## 📄 许可证### 💡 日文文档处理建议



本项目使用的开源组件：# 方法 2：使用 Tesseract OCR（备选）

- PaddleOCR: Apache-2.0 License

- pypdfium2: Apache-2.0 / BSD-3-Clause Licensepython extract_pdf.py cdsjp.pdf --lang japan --use-tesseract --scale 3.0**如果只处理中英文 PDF**，无需安装 Tesseract，直接使用即可。



## 🙏 致谢```



- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度飞桨 OCR 工具库如需处理日文 PDF，建议使用：- ✅ 可选进度显示- 输出提取的文本到 TXT 文件

- [pypdfium2](https://github.com/pypdfium2-team/pypdfium2) - 轻量级 PDF 处理库

### 场景 3：处理韩文 PDF

---

```bash### 3️⃣ 基本使用

**项目状态**：✅ 生产可用（中英日韩等多语言）  

**最后更新**：2025-01  python extract_pdf.py korean.pdf --lang korean --scale 3.0

**维护者**：qiwei.zhang

```1. **Tesseract OCR** + 日文语言包（推荐）



### 场景 4：大文件处理（70+ 页）```bash

```bash

python extract_pdf.py large_document.pdf --scale 2.5 --no-progress# 中文 PDF（默认，使用 PaddleOCR）2. 商业云 OCR 服务（Google Cloud Vision、Azure Computer Vision 等）- ✅ UTF-8 格式输出

```

python extract_pdf.py chinese_document.pdf

### 场景 5：低质量扫描文档

```bash

python extract_pdf.py scan.pdf --scale 3.0 --confidence 0.3

# 更高图片质量 + 更宽松的置信度# 日文 PDF（使用 Tesseract OCR）

```

python extract_pdf.py japanese_document.pdf --lang japan详见：[日文识别说明.md](日文识别说明.md)- ✅ 自定义图片质量和置信度阈值## 📋 核心功能

## ⚙️ 参数说明



| 参数 | 默认值 | 说明 |

|------|--------|------|# 英文 PDF（使用 PaddleOCR）

| `pdf_file` | 必填 | 输入 PDF 文件路径 |

| `-o, --output` | `{PDF名}_extracted.txt` | 输出文本文件路径 |python extract_pdf.py english_document.pdf --lang en

| `-t, --temp-dir` | `temp_images_{PDF名}` | 临时图片存储目录 |

| `--lang` | `ch` | 语言：`ch`, `en`, `japan`, `korean`, `french`, `german`等 |## 🚀 快速开始

| `--scale` | `2.0` | 图片缩放倍数（1.0-4.0，推荐 2.0-3.0） |

| `--confidence` | `0.5` | 置信度阈值（0.0-1.0） |# 指定输出文件名

| `--no-progress` | 否 | 禁用进度条 |

| `--use-tesseract` | 否 | 强制使用 Tesseract OCR |python extract_pdf.py input.pdf -o output.txt



## 📊 支持的语言```



| 语言 | PaddleOCR 参数 | 状态 | 备注 |### 1️⃣ 安装依赖## 🚀 快速开始## 文件说明

|------|---------------|------|------|

| 中文（简体） | `ch` | ✅ 优秀 | 默认，无需下载 |### 4️⃣ 高级选项

| 英文 | `en` | ✅ 优秀 | 无需下载 |

| 日文 | `japan` | ✅ 良好 | 需下载多语言模型 |

| 韩文 | `korean` | ✅ 良好 | 需下载多语言模型 |

| 法文 | `french` | ✅ 支持 | 需下载多语言模型 |```bash

| 德文 | `german` | ✅ 支持 | 需下载多语言模型 |

| 阿拉伯文 | `arabic` | ✅ 支持 | 需下载多语言模型 |# 提高图片质量（推荐用于日文和低质量扫描件）```bash

| 拉丁文 | `latin` | ✅ 支持 | 需下载多语言模型 |

python extract_pdf.py file.pdf --lang japan --scale 3.0

## 🔧 故障排除

pip install paddlepaddle==2.6.2

### 问题 1：中文内容无法识别

**解决方案**：确保使用中文模型（默认）# 调整置信度阈值（仅 PaddleOCR，不适用于 Tesseract）

```bash

python extract_pdf.py your_file.pdf --lang chpython extract_pdf.py file.pdf --lang ch --confidence 0.3pip install paddleocr==2.7.3### 1️⃣ 安装依赖- ✅ PDF 转图片（pypdfium2，无需外部依赖）

```



### 问题 2：日文模型下载失败（SSL 证书错误）

**原因**：企业网络环境下的 SSL 证书验证问题# 不显示进度条（避免某些环境的中断问题）pip install pypdfium2 Pillow tqdm opencv-python-headless



**解决方案**：python extract_pdf.py file.pdf --no-progress

1. 参考 [PaddleOCR多语言模型下载指南.md](PaddleOCR多语言模型下载指南.md) 手动下载模型

2. 或使用 Tesseract OCR 作为备选方案：pip install "numpy<2.0.0" --force-reinstall

```bash

python extract_pdf.py file.pdf --lang japan --use-tesseract# 组合多个选项

```

python extract_pdf.py file.pdf --lang japan -o result.txt --scale 3.0 --no-progress```

### 问题 3：提示"Tesseract OCR 未安装"

**解决方案**：仅在使用 `--use-tesseract` 时需要```

1. 下载安装 Tesseract：https://github.com/UB-Mannheim/tesseract/wiki

2. 安装时勾选对应语言包```bash- ✅ **中英文混合 OCR 识别**（PaddleOCR 中文模型）- `extract_pdf_paddleocr_final.py` - **推荐使用**：使用 pypdfium2 + PaddleOCR 的完整方案（无需 poppler）

3. 详见：[Tesseract安装指南.md](Tesseract安装指南.md)

### 5️⃣ 查看帮助

### 问题 4：识别内容太少

**解决方案**：降低置信度阈值，提高图片质量### 2️⃣ 基本使用

```bash

python extract_pdf.py your_file.pdf --scale 3.0 --confidence 0.3```bash

```

python extract_pdf.py --helppip install paddlepaddle==2.6.2

### 问题 5：进度条导致程序中断

**解决方案**：使用 `--no-progress` 参数```

```bash

python extract_pdf.py your_file.pdf --no-progress```bash

```

## 📝 文件说明

## 📚 技术细节

# 最简单的用法（使用默认参数：中文模型，scale=2.0）pip install paddleocr==2.7.3- ✅ 批量处理多页 PDF- `extract_pdf_cli.py` - 使用 paddleocr 命令行工具的版本（需要预先转换好的图片）

### 架构设计

```| 文件 | 功能 | 说明 |

PDF 文件

    ↓|------|------|------|python extract_pdf.py your_file.pdf

pypdfium2 (PDF → 图片)

    ↓| `extract_pdf.py` | ⭐ **通用提取脚本** | 自动选择 OCR 引擎，支持中英日韩 |

临时图片目录 (PNG 格式)

    ↓| `Tesseract安装指南.md` | 📖 安装指南 | Tesseract OCR 详细安装步骤 |pip install pypdfium2 Pillow tqdm opencv-python-headless

    ├─ 中英文 → PaddleOCR PP-OCRv4（本地模型）

    ├─ 日韩等 → PaddleOCR 多语言模型（需下载）| `verify_models.py` | 🔧 模型验证工具 | 检查 PaddleOCR 模型安装状态 |

    └─ 备选 → Tesseract OCR（需手动安装）

    ↓| `install_chinese_models.py` | 🔧 模型安装助手 | 手动安装中文模型（网络受限时使用） |# 指定输出文件名

文本输出 (UTF-8 TXT)

```| `日文识别说明.md` | 📖 技术说明 | 日文 OCR 的问题分析（旧版） |



### 依赖版本| `README.md` | 📖 项目文档 | 本文件 |python extract_pdf.py input.pdf -o output.txtpip install "numpy<2.0.0" --force-reinstall- ✅ 进度显示和错误处理- `SAP_extracted_paddleocr.txt` - OCR 提取结果示例

- Python: 3.12+

- PaddlePaddle: 2.6.2

- PaddleOCR: 2.7.3

- pypdfium2: 4.30.0## 🎯 使用场景

- Pillow: 12.0.0

- opencv-python: 4.6.0+

- numpy: <2.0.0

- tqdm: 最新版### 场景 1：处理中英文混合 PDF# 自定义临时图片目录```

- pytesseract: 0.3+ （可选）

- Tesseract OCR: 5.x+ （可选）```bash



### OCR 引擎对比python extract_pdf.py CDS.pdfpython extract_pdf.py input.pdf -t ./my_temp_dir



| 特性 | PaddleOCR 中文 | PaddleOCR 多语言 | Tesseract OCR |# 使用 PaddleOCR，效果极佳

|------|---------------|-----------------|---------------|

| **中文识别** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |``````- ✅ UTF-8 格式输出- `temp_images/` - PDF 转换后的图片存储目录

| **英文识别** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

| **日文识别** | ⭐（差） | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

| **安装难度** | 简单 | 简单 | 中等 |

| **模型下载** | 自动 | 自动（可能失败） | 手动安装 |### 场景 2：处理日文 PDF ✨ 新增

| **速度** | 快 | 快 | 中等 |

| **网络要求** | 首次自动下载 | 首次需下载 | 仅安装时 |```bash



## 🌟 特性亮点python extract_pdf.py cdsjp.pdf --lang japan --scale 3.0### 3️⃣ 高级选项### 2️⃣ 基本使用



1. ✨ **零外部依赖**：pypdfium2 无需安装 poppler# 使用 Tesseract OCR，日文假名识别准确

2. 🌍 **真正的多语言**：PaddleOCR 支持 80+ 种语言

3. 🔄 **智能降级**：PaddleOCR 优先，Tesseract 备选```

4. 📊 **进度可视化**：可选的 tqdm 进度条

5. ⚡ **灵活配置**：图片质量、置信度、语言模型均可调整

6. 🛠️ **错误处理**：完善的异常处理和用户提示

7. 📝 **编码正确**：UTF-8 输出，完美支持各种语言### 场景 3：大文件处理（70+ 页）```bash



## ⚠️ 使用限制```bash



1. **多语言模型下载**：首次使用日文/韩文等需要从网络下载模型（约 10-20MB），企业网络可能遇到 SSL 问题python extract_pdf.py large_document.pdf --scale 2.5 --no-progress# 使用英文模型（仅英文识别，速度更快）

2. **手写文字**：主要针对印刷体，手写识别效果较差

3. **复杂排版**：多栏、表格等复杂排版可能顺序混乱# 提高图片质量 + 不显示进度条

4. **图片质量**：低质量扫描件识别效果受限

```python extract_pdf.py input.pdf --lang en```bash

## 📄 许可证



本项目使用的开源组件：

- PaddleOCR: Apache-2.0 License### 场景 4：仅英文 PDF（速度更快）

- pypdfium2: Apache-2.0 / BSD-3-Clause License

- Tesseract OCR: Apache-2.0 License```bash



## 🙏 致谢python extract_pdf.py english_doc.pdf --lang en# 调整图片质量（默认 2.0，越高质量越好但速度越慢）# 最简单的用法（使用默认参数：中文模型，scale=2.0）## 🚀 快速使用## 环境配置



- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度飞桨 OCR 工具库# 使用英文专用模型

- [pypdfium2](https://github.com/pypdfium2-team/pypdfium2) - 轻量级 PDF 处理库

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Google 开源 OCR 引擎```python extract_pdf.py input.pdf --scale 3.0



---



**项目状态**：✅ 生产可用（中英文优秀，多语言良好）  ### 场景 5：低质量扫描文档python extract_pdf.py your_file.pdf

**最后更新**：2025-01  

**维护者**：qiwei.zhang```bash


python extract_pdf.py scan.pdf --scale 3.0 --confidence 0.3# 调整置信度阈值（默认 0.5，0-1 之间，越低保留越多内容）

# 更高图片质量 + 更宽松的置信度

```python extract_pdf.py input.pdf --confidence 0.3



## ⚙️ 参数说明



| 参数 | 默认值 | 说明 |# 不显示进度条（避免某些环境的中断问题）# 指定输出文件名

|------|--------|------|

| `pdf_file` | 必填 | 输入 PDF 文件路径 |python extract_pdf.py input.pdf --no-progress

| `-o, --output` | `{PDF名}_extracted.txt` | 输出文本文件路径 |

| `-t, --temp-dir` | `temp_images_{PDF名}` | 临时图片存储目录 |python extract_pdf.py input.pdf -o output.txt### 安装依赖### 依赖项

| `--lang` | `ch` | 语言：`ch`（中英文），`en`（英文），`japan`（日文），`korean`（韩文） |

| `--scale` | `2.0` | 图片缩放倍数（1.0-4.0，推荐 2.0-3.0） |# 组合多个选项

| `--confidence` | `0.5` | 置信度阈值（0.0-1.0，仅用于 PaddleOCR） |

| `--no-progress` | 否 | 禁用进度条 |python extract_pdf.py input.pdf -o result.txt --scale 3.0 --no-progress



## 📊 测试结果```



| 测试文件 | 页数 | 内容类型 | OCR 引擎 | 耗时 | 输出大小 | 状态 |# 自定义临时图片目录

|---------|------|---------|---------|------|---------|------|

| SAP-C_BCSBS_2502(1).pdf | 70 | 纯英文 | PaddleOCR | ~7-9 秒/页 | 95 KB | ✅ 优秀 |### 4️⃣ 查看帮助

| CDS.pdf | 2 | 中英文混合 | PaddleOCR | ~3 秒/页 | 2.9 KB | ✅ 优秀 |

| cdsjp.pdf (PaddleOCR) | 3 | 日文 | PaddleOCR | ~3 秒/页 | 3.7 KB | ⚠️ 差 |python extract_pdf.py input.pdf -t ./my_temp_dir

| cdsjp.pdf (Tesseract) | 3 | 日文 | **Tesseract** | ~5 秒/页 | 预计 4+ KB | ✅ 良好 |

```bash

## 🔧 故障排除

python extract_pdf.py --help``````bash```bash

### 问题 1：中文内容无法识别

**解决方案**：确保使用中文模型（默认）```

```bash

python extract_pdf.py your_file.pdf --lang ch

```

## 📝 文件说明

### 问题 2：日文内容识别不准确

**解决方案**：使用 Tesseract OCR 日文模式### 3️⃣ 高级选项pip install paddlepaddle==2.6.2Python 3.12+

```bash

# 先安装 Tesseract OCR（参考 Tesseract安装指南.md）| 文件 | 功能 | 说明 |

python extract_pdf.py your_file.pdf --lang japan --scale 3.0

```|------|------|------|



### 问题 3：提示"Tesseract OCR 未安装"| `extract_pdf.py` | ⭐ **通用提取脚本** | 推荐使用，支持完整命令行参数 |

**解决方案**：

1. 下载安装 Tesseract：https://github.com/UB-Mannheim/tesseract/wiki| `verify_models.py` | 🔧 模型验证工具 | 检查 PaddleOCR 模型安装状态 |```bashpip install paddleocr==2.7.3PaddlePaddle 2.6.2

2. 安装时勾选"Japanese language data"

3. 安装 Python 包：`pip install pytesseract`| `install_chinese_models.py` | 🔧 模型安装助手 | 手动安装中文模型（网络受限时使用） |

4. 详见：[Tesseract安装指南.md](Tesseract安装指南.md)

| `日文识别说明.md` | 📖 日文处理指南 | 日文 OCR 的问题分析和解决方案 |# 使用英文模型（仅英文识别）

### 问题 4：识别内容太少

**解决方案**：降低置信度阈值，提高图片质量| `README.md` | 📖 项目文档 | 本文件 |

```bash

python extract_pdf.py your_file.pdf --scale 3.0 --confidence 0.3python extract_pdf.py input.pdf --lang enpip install pypdfium2 Pillow tqdm opencv-python-headlessPaddleOCR 2.7.3

```

## 🎯 使用场景

### 问题 5：进度条导致程序中断

**解决方案**：使用 `--no-progress` 参数

```bash

python extract_pdf.py your_file.pdf --no-progress### 场景 1：处理中英文混合 PDF（推荐）

```

```bash# 调整图片质量（默认 2.0，越高质量越好但速度越慢）pip install "numpy<2.0.0" --force-reinstallpypdfium2 4.30.0

### 问题 6：检查 PaddleOCR 模型是否安装

```bashpython extract_pdf.py CDS.pdf

python verify_models.py

```# 输出：CDS_extracted.txtpython extract_pdf.py input.pdf --scale 3.0



## 📚 技术细节# 适用：中文文档、中英文混合文档



### 架构设计``````Pillow 12.0.0

```

PDF 文件

    ↓

pypdfium2 (PDF → 图片)### 场景 2：大文件处理（70+ 页）# 调整置信度阈值（默认 0.5，0-1 之间）

    ↓

临时图片目录 (PNG 格式)```bash

    ↓

    ├─ 中英文 → PaddleOCR PP-OCRv4python extract_pdf.py large_document.pdf --scale 2.5 --no-progresspython extract_pdf.py input.pdf --confidence 0.6numpy 1.26.4

    └─ 日韩文 → Tesseract OCR

    ↓# 提高图片质量 + 不显示进度条

文本输出 (UTF-8 TXT)

```# 适用：长篇文档、扫描版PDF



### 依赖版本```

- Python: 3.12+

- PaddlePaddle: 2.6.2# 不显示进度条（避免某些环境的中断问题）### 运行提取opencv-python 4.6.0.66

- PaddleOCR: 2.7.3

- pypdfium2: 4.30.0### 场景 3：仅英文 PDF（速度更快）

- Pillow: 12.0.0

- opencv-python: 4.6.0+```bashpython extract_pdf.py input.pdf --no-progress

- numpy: <2.0.0

- tqdm: 最新版python extract_pdf.py english_doc.pdf --lang en

- pytesseract: 0.3+ （可选，用于日文）

- Tesseract OCR: 5.x+ （可选，用于日文）# 使用英文专用模型，速度更快tqdm (进度条)



### OCR 引擎对比# 适用：纯英文文档



| 特性 | PaddleOCR | Tesseract OCR |```# 组合多个选项

|------|-----------|---------------|

| **中文识别** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

| **英文识别** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

| **日文识别** | ⭐（假名识别差） | ⭐⭐⭐⭐ |### 场景 4：高精度提取python extract_pdf.py input.pdf -o result.txt --scale 3.0 --no-progress```bash```

| **安装难度** | 简单（pip） | 中等（需额外安装） |

| **速度** | 快 | 中等 |```bash

| **置信度控制** | ✅ 支持 | ❌ 不支持 |

| **GPU 加速** | ✅ 支持 | ❌ 不支持 |python extract_pdf.py important.pdf --scale 3.0 --confidence 0.7```



## 🌟 特性亮点# 更高图片质量 + 更严格的置信度过滤



1. ✨ **零外部依赖**：pypdfium2 无需安装 poppler# 适用：重要文档、需要高准确率的场景# 主脚本（推荐）

2. 🚀 **智能引擎切换**：根据语言自动选择最佳 OCR 引擎

3. 🌏 **多语言支持**：中英日韩，一个脚本搞定```

4. 📊 **进度可视化**：可选的 tqdm 进度条

5. ⚡ **灵活配置**：图片质量、置信度、语言模型均可调整### 4️⃣ 查看帮助

6. 🛠️ **错误处理**：完善的异常处理和用户提示

7. 📝 **编码正确**：UTF-8 输出，完美支持各种语言### 场景 5：低质量扫描文档



## ⚠️ 使用限制```bashpython extract_pdf_paddleocr_final.py### 安装步骤



1. **日文识别**：需要单独安装 Tesseract OCR 和日文语言包python extract_pdf.py scan.pdf --scale 3.0 --confidence 0.3

2. **手写文字**：主要针对印刷体，手写识别效果较差

3. **图片文字**：对于图片中的文字可能识别效果不佳# 更高图片质量 + 更宽松的置信度（保留更多内容）```bash

4. **复杂排版**：多栏、表格等复杂排版可能顺序混乱

# 适用：模糊扫描件、老旧文档

## 📄 许可证

```python extract_pdf.py --help

本项目使用的开源组件：

- PaddleOCR: Apache-2.0 License

- pypdfium2: Apache-2.0 / BSD-3-Clause License

- Tesseract OCR: Apache-2.0 License## ⚙️ 参数说明```



## 🙏 致谢



- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度飞桨 OCR 工具库| 参数 | 默认值 | 说明 |# 小文件测试```bash

- [pypdfium2](https://github.com/pypdfium2-team/pypdfium2) - 轻量级 PDF 处理库

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Google 开源 OCR 引擎|------|--------|------|



---| `pdf_file` | 必填 | 输入 PDF 文件路径 |输出示例：



**项目状态**：✅ 生产可用（中英文 + 日文）  | `-o, --output` | `{PDF名}_extracted.txt` | 输出文本文件路径 |

**最后更新**：2025-01  

**维护者**：qiwei.zhang| `-t, --temp-dir` | `temp_images_{PDF名}` | 临时图片存储目录 |```python extract_cds_simple.py# 安装 PaddlePaddle


| `--lang` | `ch` | OCR 语言：`ch`（中英文）或 `en`（英文） |

| `--scale` | `2.0` | 图片缩放倍数（1.0-4.0，推荐 2.0-3.0） |usage: extract_pdf.py [-h] [-o OUTPUT] [-t TEMP_DIR] [--lang {ch,en}] 

| `--confidence` | `0.5` | 置信度阈值（0.0-1.0，越低保留越多） |

| `--no-progress` | 否 | 禁用进度条（某些环境可能需要） |                      [--scale SCALE] [--confidence CONFIDENCE] [--no-progress]```pip install paddlepaddle==2.6.2



## 📊 测试结果                      pdf_file



| 测试文件 | 页数 | 内容类型 | 耗时 | 输出大小 | 状态 |

|---------|------|---------|------|---------|------|

| SAP-C_BCSBS_2502(1).pdf | 70 | 纯英文 | ~7-9 秒/页 | 95 KB | ✅ 成功 |从 PDF 提取文字（使用 PaddleOCR）

| CDS.pdf | 2 | 中英文混合 | ~3 秒/页 | 2.9 KB | ✅ 成功 |

| cdsjp.pdf | 3 | 日文 | ~3 秒/页 | 3.7 KB | ⚠️ 识别率低 |## 📝 脚本说明# 安装 PaddleOCR



## 🔧 故障排除positional arguments:



### 问题 1：中文内容无法识别  pdf_file              输入的 PDF 文件路径pip install paddleocr==2.7.3

**解决方案**：确保使用中文模型（默认）

```bash

python extract_pdf.py your_file.pdf --lang ch

```options:| 脚本 | 功能 | 推荐 |



### 问题 2：识别内容太少  -h, --help            显示帮助信息

**解决方案**：降低置信度阈值，提高图片质量

```bash  -o, --output OUTPUT   输出文本文件路径（默认：PDF文件名_extracted.txt）|------|------|------|# 安装 PDF 处理库（无需外部 poppler 依赖）

python extract_pdf.py your_file.pdf --scale 3.0 --confidence 0.3

```  -t, --temp-dir TEMP_DIR



### 问题 3：进度条导致程序中断                        临时图片目录（默认：temp_images）| `extract_pdf_paddleocr_final.py` | 完整功能，带进度条 | ⭐⭐⭐ |pip install pypdfium2

**解决方案**：使用 `--no-progress` 参数

```bash  --lang {ch,en}        OCR 语言模型：ch=中文+英文（默认），en=仅英文

python extract_pdf.py your_file.pdf --no-progress

```  --scale SCALE         图片缩放倍数，越大质量越高（默认：2.0）| `extract_cds_simple.py` | 简化版，适合测试 | ⭐⭐ |



### 问题 4：SSL 证书错误（下载模型时）  --confidence CONFIDENCE

**解决方案**：脚本已内置 SSL 绕过，或使用 `install_chinese_models.py` 手动安装

                        置信度阈值 0-1（默认：0.5）| `extract_cds.py` | CDS 完整版 | ⭐ |# 安装其他依赖

### 问题 5：识别质量不佳

**解决方案**：提高图片质量  --no-progress         不显示进度条

```bash

python extract_pdf.py your_file.pdf --scale 3.0```| `verify_models.py` | 验证模型安装 | 🔧 |pip install Pillow tqdm opencv-python-headless

```



### 问题 6：日文识别不准确

**解决方案**：PaddleOCR 中文模型不适合日文，请参考 [日文识别说明.md](日文识别说明.md) 使用 Tesseract OCR## 📝 文件说明| `install_chinese_models.py` | 手动安装模型 | 🔧 |



### 问题 7：检查模型是否安装

```bash

python verify_models.py| 文件 | 功能 | 说明 |# 降级 numpy（兼容性）

```

|------|------|------|

## 📚 技术细节

| `extract_pdf.py` | ⭐ **通用提取脚本** | 推荐使用，支持完整命令行参数 |## 🎯 提取效果示例pip install "numpy<2.0.0" --force-reinstall

### 架构设计

```| `verify_models.py` | 🔧 模型验证工具 | 检查 PaddleOCR 模型安装状态 |

PDF 文件

    ↓| `install_chinese_models.py` | 🔧 模型安装助手 | 手动安装中文模型（网络受限时使用） |```

pypdfium2 (PDF → 图片)

    ↓| `README.md` | 📖 项目文档 | 本文件 |

临时图片目录 (PNG 格式)

    ↓### 输入 PDF

PaddleOCR PP-OCRv4 (OCR 识别)

    ↓## 🎯 使用场景

文本输出 (UTF-8 TXT)

``````## 使用方法



### 依赖版本### 场景 1：处理中英文混合 PDF

- Python: 3.12+

- PaddlePaddle: 2.6.2```bash本文档经过机器翻译。

- PaddleOCR: 2.7.3

- pypdfium2: 4.30.0python extract_pdf.py CDS.pdf

- Pillow: 12.0.0

- opencv-python: 4.6.0+# 输出：CDS_extracted.txtSAP PowerDesigner | 16.6 SP01### 方法一：使用完整脚本（推荐）

- numpy: <2.0.0

- tqdm: 最新版```



### PaddleOCR 模型数据建模 Data Modeling

- **中文模型** (`--lang ch`): ch_PP-OCRv4_det + ch_PP-OCRv4_rec

  - 支持中文 + 英文混合识别### 场景 2：大文件处理（70+ 页）

  - 模型路径：`~/.paddleocr/whl/det/ch/` 和 `rec/ch/`

  - 适用范围：简体中文、繁体中文、英文```bash概念数据模型(CDM)```bash

- **英文模型** (`--lang en`): en_PP-OCRv3_det + en_PP-OCRv3_rec

  - 仅英文识别，速度更快python extract_pdf.py large_document.pdf --scale 2.5 --no-progress

  - 适用范围：纯英文文档

# 提高图片质量 + 不显示进度条```# 直接从 PDF 提取文字到 TXT

## 🌟 特性亮点

```

1. ✨ **零外部依赖**：pypdfium2 无需安装 poppler

2. 🚀 **命令行友好**：完整的 argparse CLI 支持python extract_pdf_paddleocr_final.py

3. 🌏 **中英文双语**：一个模型搞定中英文混合文档

4. 📊 **进度可视化**：可选的 tqdm 进度条### 场景 3：仅英文 PDF（速度更快）

5. ⚡ **灵活配置**：图片质量、置信度、语言模型均可调整

6. 🛠️ **错误处理**：完善的异常处理和用户提示```bash### 输出 TXT```

7. 📝 **编码正确**：UTF-8 输出，完美支持中文

python extract_pdf.py english_doc.pdf --lang en

## ⚠️ 使用限制

``````

1. **日文识别**：PaddleOCR 中文模型对日文假名识别率低，不推荐用于日文文档

2. **手写文字**：主要针对印刷体，手写识别效果较差

3. **图片文字**：对于图片中的文字可能识别效果不佳

4. **复杂排版**：多栏、表格等复杂排版可能顺序混乱### 场景 4：高精度提取本文档经过机器翻译。该脚本会：



## 📄 许可证```bash



本项目使用的开源组件：python extract_pdf.py important.pdf --scale 3.0 --confidence 0.7SAP PowerDesigner | 16.6 SP011. 自动将 PDF 转换为图片（保存到 `temp_images/` 目录）

- PaddleOCR: Apache-2.0 License

- pypdfium2: Apache-2.0 / BSD-3-Clause License# 更高图片质量 + 更严格的置信度过滤



## 🙏 致谢```数据建模 Data Modeling2. 使用 PaddleOCR 识别每张图片的文字



- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度飞桨 OCR 工具库

- [pypdfium2](https://github.com/pypdfium2-team/pypdfium2) - 轻量级 PDF 处理库

## ⚙️ 参数说明概念数据模型(CDM)3. 输出结果到 `SAP_extracted_paddleocr.txt`

---



**项目状态**：✅ 生产可用（中英文）  

**最后更新**：2025-01  | 参数 | 默认值 | 说明 |```

**维护者**：qiwei.zhang

|------|--------|------|

| `pdf_file` | 必填 | 输入 PDF 文件路径 |### 方法二：使用命令行工具

| `-o, --output` | `{PDF名}_extracted.txt` | 输出文本文件路径 |

| `-t, --temp-dir` | `temp_images` | 临时图片存储目录 |✅ **中文和英文都能完整识别！**

| `--lang` | `ch` | OCR 语言：`ch`（中英文）或 `en`（英文） |

| `--scale` | `2.0` | 图片缩放倍数（1.0-4.0，推荐 2.0-3.0） |如果已有图片文件：

| `--confidence` | `0.5` | 置信度阈值（0.0-1.0） |

| `--no-progress` | 否 | 禁用进度条（某些环境可能需要） |## ⚙️ 自定义配置



## 📊 测试结果```bash



| 测试文件 | 页数 | 内容类型 | 耗时 | 输出大小 | 状态 |编辑脚本中的路径：# 修改脚本中的路径后运行

|---------|------|---------|------|---------|------|

| SAP-C_BCSBS_2502(1).pdf | 70 | 纯英文 | ~7-9 秒/页 | 95 KB | ✅ 成功 |python extract_pdf_cli.py

| CDS.pdf | 2 | 中英文混合 | ~3 秒/页 | 2.9 KB | ✅ 成功 |

```python```

## 🔧 故障排除

def main():

### 问题 1：中文内容无法识别

**解决方案**：确保使用中文模型    pdf_file = r"C:\path\to\your\file.pdf"          # 输入 PDF## 注意事项

```bash

python extract_pdf.py your_file.pdf --lang ch    temp_images_dir = r"C:\path\to\temp_images"     # 临时目录

```

    output_file = r"C:\path\to\output.txt"          # 输出文件- 首次运行会自动下载 PP-OCRv3 英文模型

### 问题 2：进度条导致程序中断

**解决方案**：使用 `--no-progress` 参数```- 模型会保存在 `~/.paddleocr/whl/` 目录

```bash

python extract_pdf.py your_file.pdf --no-progress- 使用 pypdfium2 转换 PDF，无需安装 poppler

```

调整参数：- OCR 处理速度：约 9 秒/页（CPU 模式）

### 问题 3：SSL 证书错误（下载模型时）

**解决方案**：脚本已内置 SSL 绕过，或使用 `install_chinese_models.py` 手动安装- 大文件处理建议：脚本会显示进度条，请耐心等待



### 问题 4：识别质量不佳```python

**解决方案**：提高图片质量和置信度

```bash# PDF 转图片分辨率## 技术特点

python extract_pdf.py your_file.pdf --scale 3.0 --confidence 0.6

```scale=2.0  # 1.5-3.0，越大越清晰



### 问题 5：检查模型是否安装✅ **纯 Python 方案**：不依赖 PyMuPDF，避免许可证问题  

```bash

python verify_models.py# OCR 置信度阈值✅ **无外部依赖**：pypdfium2 无需安装 poppler  

```

if confidence > 0.5:  # 0.3-0.8，越高越严格✅ **高质量 OCR**：使用 PaddleOCR PP-OCRv3 英文模型  

## 📚 技术细节

```✅ **进度可视化**：tqdm 进度条实时显示处理进度  

### 架构设计

```✅ **错误处理**：自动处理异常页面，确保流程完整  

PDF 文件

    ↓## 📊 性能参数

pypdfium2 (PDF → 图片)

    ↓## 问题解决

临时图片目录 (PNG 格式)

    ↓- **PDF 转图片**: ~0.5 秒/页

PaddleOCR PP-OCRv4 (OCR 识别)

    ↓- **OCR 识别**: ~3-9 秒/页（CPU）### PaddlePaddle 版本兼容性

文本输出 (UTF-8 TXT)

```- **70 页处理**: 约 10-15 分钟- PaddlePaddle 3.0+ 与 PaddleOCR 2.7.3 模型可能不兼容



### 依赖版本- **内存占用**: < 500 MB- 建议使用 PaddlePaddle 2.6.2

- Python: 3.12+

- PaddlePaddle: 2.6.2

- PaddleOCR: 2.7.3

- pypdfium2: 4.30.0## 💡 注意事项### SSL 证书问题

- Pillow: 12.0.0

- opencv-python: 4.6.0+- 脚本已内置 SSL 验证禁用（仅用于模型下载）

- numpy: <2.0.0

- tqdm: 最新版### 首次运行- 企业网络环境下可正常使用



### PaddleOCR 模型- 会自动下载中文模型（约 15 MB）

- **中文模型** (`--lang ch`): ch_PP-OCRv4_det + ch_PP-OCRv4_rec

  - 支持中文 + 英文混合识别- 需要网络连接### PDF 转换失败

  - 模型路径：`~/.paddleocr/whl/det/ch/` 和 `rec/ch/`

- **英文模型** (`--lang en`): en_PP-OCRv3_det + en_PP-OCRv3_rec- 模型只需下载一次- 确保已安装 `pypdfium2`：`pip install pypdfium2`

  - 仅英文识别，速度更快

- 如遇到问题，检查 PDF 文件是否损坏

## 🌟 特性亮点

### 网络问题

1. ✨ **零外部依赖**：pypdfium2 无需安装 poppler

2. 🚀 **命令行友好**：完整的 argparse CLI 支持如遇 SSL 错误：### 内存不足

3. 🌏 **中英文双语**：一个模型搞定中英文混合文档

4. 📊 **进度可视化**：可选的 tqdm 进度条1. 换网络环境（家庭网络/手机热点）- 对于大型 PDF，脚本会逐页处理，不会占用过多内存

5. ⚡ **灵活配置**：图片质量、置信度、语言模型均可调整

6. 🛠️ **错误处理**：完善的异常处理和用户提示2. 手动下载模型 + 运行 `install_chinese_models.py`- 临时图片会保存到 `temp_images/` 目录



## 📄 许可证



本项目使用的开源组件：### 验证安装## 作者

- PaddleOCR: Apache-2.0 License

- pypdfium2: Apache-2.0 / BSD-3-Clause License```bash



## 🙏 致谢python verify_models.pyWilson Zhang



- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度飞桨 OCR 工具库```

- [pypdfium2](https://github.com/pypdfium2-team/pypdfium2) - 轻量级 PDF 处理库

## 许可证

---

## 🐛 常见问题

**项目状态**：✅ 生产可用  

**最后更新**：2025-01  MIT License

**维护者**：qiwei.zhang

**Q: 提取速度慢？**  
A: 正常现象，CPU 模式每页 3-9 秒。有 GPU 可改 `use_gpu=True`

**Q: 中文乱码？**  
A: 确保使用 `lang='ch'` 和 UTF-8 编码查看

**Q: 只想提取英文？**  
A: 改为 `lang='en'` 即可

## 🎓 技术栈

```
PDF → pypdfium2 → 图片 → PaddleOCR → 文字 → TXT
```

- **PDF 处理**: pypdfium2
- **OCR 引擎**: PaddleOCR PP-OCRv4 中文模型
- **图片处理**: Pillow + OpenCV
- **进度显示**: tqdm

## 📚 测试文件

| 文件 | 页数 | 内容 | 输出 |
|------|------|------|------|
| `SAP-C_BCSBS_2502(1).pdf` | 70 | 英文 | `SAP_extracted_paddleocr.txt` |
| `CDS.pdf` | 2 | 中英文 | `CDS_extracted.txt` |

## 📄 许可证

MIT License

## 👤 作者

Wilson Zhang

---

**最后更新**: 2025-10-20  
**状态**: ✅ 中英文识别正常工作
