#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 paddleocr 命令行工具批量 OCR（禁用 SSL 验证）
"""
import os
import ssl
import subprocess
from pathlib import Path
from tqdm import tqdm

# 禁用 SSL 验证
ssl._create_default_https_context = ssl._create_unverified_context

def ocr_images_to_text(images_dir, output_file):
    """
    对文件夹中的图片进行 OCR 识别并保存到文本文件
    
    Args:
        images_dir: 图片文件夹路径
        output_file: 输出文本文件路径
    """
    # 获取所有图片文件并排序
    image_files = sorted([
        f for f in os.listdir(images_dir) 
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ], key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    
    total_images = len(image_files)
    print(f"找到 {total_images} 张图片，开始 OCR 识别...")
    
    # 模型路径
    model_dir = Path.home() / '.paddleocr' / 'whl'
    det_model_dir = model_dir / 'det' / 'en' / 'en_PP-OCRv3_det_infer'
    rec_model_dir = model_dir / 'rec' / 'en' / 'en_PP-OCRv3_rec_infer'
    
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        # 遍历所有图片
        for idx, image_file in enumerate(tqdm(image_files, desc="OCR 进度"), 1):
            image_path = os.path.join(images_dir, image_file)
            
            try:
                # 使用 paddleocr 命令行工具
                cmd = [
                    'paddleocr',
                    '--image_dir', image_path,
                    '--use_angle_cls', 'false',
                    '--use_gpu', 'false',
                    '--lang', 'en',
                    '--det_model_dir', str(det_model_dir),
                    '--rec_model_dir', str(rec_model_dir),
                    '--show_log', 'false'
                ]
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore'
                )
                
                # 写入页码标记
                f.write(f"\n{'='*60}\n")
                f.write(f"第 {idx}/{total_images} 页 ({image_file})\n")
                f.write(f"{'='*60}\n\n")
                
                # 写入识别结果
                if result.stdout:
                    # 解析输出
                    lines = result.stdout.split('\n')
                    for line in lines:
                        if line.strip() and not line.startswith('['):
                            f.write(f"{line}\n")
                else:
                    f.write("[此页无文本内容]\n")
                
                if result.stderr and 'error' in result.stderr.lower():
                    print(f"\n警告 ({image_file}): {result.stderr[:200]}")
                    
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
