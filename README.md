# PDF OCR Extraction Project

使用 PaddleOCR 从 PDF 文件提取文本的项目。

## 功能

- 将 PDF 转换为图片
- 使用 PaddleOCR 进行 OCR 文字识别
- 输出提取的文本到 TXT 文件

## 文件说明

- `extract_pdf_ssl_disabled.py` - **推荐使用**：禁用 SSL 验证的 OCR 脚本（最终工作版本）
- `SAP-C_BCSBS_2502_extracted.txt` - OCR 提取结果
- `extract_pdf_final.py` - OCR 脚本（标准版本）
- `extract_pdf_lowlevel.py` - 使用低级 API 的版本
- `extract_pdf_cli.py` - 命令行工具版本

## 环境配置

### 依赖项

```bash
Python 3.12.10
PaddlePaddle 2.6.2
PaddleOCR 2.7.3
numpy 1.26.4
PyMuPDF 1.26.5
opencv-python 4.6.0.66
```

### 安装步骤

```bash
# 安装 PaddlePaddle
pip install paddlepaddle==2.6.2

# 安装 PaddleOCR
pip install paddleocr==2.7.3

# 安装其他依赖
pip install PyMuPDF scikit-image opencv-python-headless albumentations pyclipper lmdb

# 降级 numpy（兼容性）
pip install "numpy<2.0.0" --force-reinstall
```

## 使用方法

```bash
# 运行 OCR 提取
python extract_pdf_ssl_disabled.py
```

## 注意事项

- 首次运行会自动下载 PP-OCRv3 英文模型
- 模型会保存在 `~/.paddleocr/whl/` 目录
- 如果网络环境有 SSL 证书问题，使用 `extract_pdf_ssl_disabled.py`

## 问题解决

### PaddlePaddle 版本兼容性
- PaddlePaddle 3.2.0 与 PaddleOCR 2.7.3 模型不兼容
- 建议使用 PaddlePaddle 2.6.2

### SSL 证书问题
- 企业网络环境可能阻止模型下载
- 使用禁用 SSL 验证的脚本或手动下载模型

## 作者

Wilson Zhang

## 许可证

MIT License
