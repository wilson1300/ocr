#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 PaddleOCR 提取 PDF 内容（禁用 SSL 验证）
"""
import os
import ssl
import urllib.request

# 全局禁用 SSL 证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# 禁用 urllib3 的 SSL 警告并修改 requests 库
import warnings
warnings.filterwarnings('ignore')

# Monkey-patch requests 库禁用 SSL 验证
import requests
_original_get = requests.get
_original_post = requests.post

def patched_get(*args, **kwargs):
    kwargs.setdefault('verify', False)
    return _original_get(*args, **kwargs)

def patched_post(*args, **kwargs):
    kwargs.setdefault('verify', False)
    return _original_post(*args, **kwargs)

requests.get = patched_get
requests.post = patched_post

# 导入 PaddleOCR
from paddleocr import PaddleOCR
from tqdm import tqdm

def ocr_images_to_text(images_dir, output_file):
    """
    对文件夹中的图片进行 OCR 识别并保存到文本文件
    
    Args:
        images_dir: 图片文件夹路径
        output_file: 输出文本文件路径
    """
    # 初始化 PaddleOCR
    print("正在初始化 PaddleOCR（首次运行会自动下载模型）...")
    ocr = PaddleOCR(
        use_angle_cls=False,  # 禁用角度分类器
        lang='en',            # 识别英文
        use_gpu=False,        # 使用 CPU
        show_log=False        # 不显示详细日志
    )
    
    # 获取所有图片文件并排序
    image_files = sorted([
        f for f in os.listdir(images_dir) 
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ], key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    
    total_images = len(image_files)
    print(f"找到 {total_images} 张图片，开始 OCR 识别...")
    
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        # 遍历所有图片
        for idx, image_file in enumerate(tqdm(image_files, desc="OCR 进度"), 1):
            image_path = os.path.join(images_dir, image_file)
            
            try:
                # 执行 OCR
                result = ocr.ocr(image_path, cls=False)
                
                # 写入页码标记
                f.write(f"\n{'='*60}\n")
                f.write(f"第 {idx}/{total_images} 页 ({image_file})\n")
                f.write(f"{'='*60}\n\n")
                
                # 提取并写入文本
                if result and result[0]:
                    for line in result[0]:
                        text = line[1][0]  # 提取识别的文本
                        f.write(f"{text}\n")
                else:
                    f.write("[此页无文本内容]\n")
                    
            except Exception as e:
                print(f"\n处理 {image_file} 时出错: {e}")
                f.write(f"[处理此页时出错: {e}]\n")
    
    print(f"\n完成！结果已保存到: {output_file}")

if __name__ == "__main__":
    # 配置路径
    images_dir = r"C:\Users\qiwei.zhang\Desktop\ocr\PaddleOCR\temp_images"
    output_file = r"C:\Users\qiwei.zhang\Desktop\ocr\SAP-C_BCSBS_2502_extracted.txt"
    
    # 检查图片文件夹
    if not os.path.exists(images_dir):
        print(f"错误：图片文件夹不存在: {images_dir}")
        exit(1)
    
    # 执行 OCR
    ocr_images_to_text(images_dir, output_file)
