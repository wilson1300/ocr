#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 PaddleOCR 2.7.3 提取 PDF 内容到 TXT 文件
"""
import os
from paddleocr import PaddleOCR
from tqdm import tqdm

def ocr_images_to_text(images_dir, output_file):
    """
    对文件夹中的图片进行 OCR 识别并保存到文本文件
    
    Args:
        images_dir: 图片文件夹路径
        output_file: 输出文本文件路径
    """
    # 初始化 PaddleOCR，指定使用 v3 模型
    print("正在初始化 PaddleOCR...")
    
    # 模型路径
    model_dir = os.path.join(os.path.expanduser("~"), ".paddleocr", "whl")
    det_model_dir = os.path.join(model_dir, "det", "en", "en_PP-OCRv3_det_infer")
    rec_model_dir = os.path.join(model_dir, "rec", "en", "en_PP-OCRv3_rec_infer")
    
    ocr = PaddleOCR(
        use_angle_cls=False,    # 禁用角度分类器避免额外下载
        lang='en',              # 识别英文
        use_gpu=False,          # 使用 CPU
        show_log=False,         # 不显示详细日志
        det_model_dir=det_model_dir,  # 指定检测模型
        rec_model_dir=rec_model_dir   # 指定识别模型
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
                # 执行 OCR，禁用分类
                result = ocr.ocr(image_path, cls=False)
                
                # 写入页码标记
                f.write(f"\n{'='*60}\n")
                f.write(f"第 {idx}/{total_images} 页 ({image_file})\n")
                f.write(f"{'='*60}\n\n")
                
                # 提取并写入文本
                if result and result[0]:
                    for line in result[0]:
                        text = line[1][0]  # 提取识别的文本
                        confidence = line[1][1]  # 置信度
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
    output_file = r"C:\Users\qiwei.zhang\Desktop\ocr\PaddleOCR\SAP-C_BCSBS_2502_extracted.txt"
    
    # 检查图片文件夹
    if not os.path.exists(images_dir):
        print(f"错误：图片文件夹不存在: {images_dir}")
        exit(1)
    
    # 执行 OCR
    ocr_images_to_text(images_dir, output_file)
