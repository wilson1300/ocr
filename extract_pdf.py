#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用 PDF 文字提取工具
使用 PaddleOCR 多语言模型支持中英日韩等多种语言
"""
import os
import sys
import ssl
import argparse
from pathlib import Path
import pypdfium2 as pdfium
from paddleocr import PaddleOCR
from tqdm import tqdm

# 禁用 SSL 验证
ssl._create_default_https_context = ssl._create_unverified_context


def convert_pdf_to_images(pdf_path, output_dir, scale=2.0):
    """
    将 PDF 转换为图片
    
    Args:
        pdf_path: PDF 文件路径
        output_dir: 输出图片目录
        scale: 缩放比例（越大图片越清晰，默认 2.0）
    Returns:
        图片文件列表
    """
    print(f"正在将 PDF 转换为图片...")
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        pdf = pdfium.PdfDocument(pdf_path)
        page_count = len(pdf)
        print(f"PDF 共 {page_count} 页")
        
        image_files = []
        for page_num in range(page_count):
            page = pdf[page_num]
            pil_image = page.render(scale=scale, rotation=0).to_pil()
            image_path = os.path.join(output_dir, f"page_{page_num+1:04d}.png")
            pil_image.save(image_path, 'PNG')
            image_files.append(image_path)
            print(f"  保存第 {page_num+1}/{page_count} 页", end='\r')
        
        print(f"\n✓ 图片已保存到: {output_dir}")
        pdf.close()
        return image_files
        
    except Exception as e:
        print(f"✗ 转换 PDF 失败: {e}")
        import traceback
        traceback.print_exc()
        return None


def extract_text_with_paddleocr(image_files, output_file, lang='ch', confidence_threshold=0.5, use_progress_bar=True):
    """
    使用 PaddleOCR 从图片提取文字
    
    Args:
        image_files: 图片文件列表
        output_file: 输出 TXT 文件路径
        lang: 语言模型 ('ch' 中英文混合, 'en' 纯英文)
        confidence_threshold: 置信度阈值（0-1）
        use_progress_bar: 是否显示进度条
    """
    if not image_files:
        print("✗ 没有可处理的图片")
        return False
    
    total_images = len(image_files)
    lang_names = {
        'ch': '中英文混合', 'en': '英文', 'japan': '日文', 'korean': '韩文',
        'french': '法文', 'german': '德文', 'latin': '拉丁文', 'arabic': '阿拉伯文'
    }
    lang_name = lang_names.get(lang, lang)
    print(f"\n开始使用 PaddleOCR 识别 {total_images} 张图片（{lang_name}模式）...")
    
    # 初始化 PaddleOCR
    print("初始化 PaddleOCR...")
    try:
        ocr = PaddleOCR(
            use_angle_cls=False,
            lang=lang,
            use_gpu=False,
            show_log=False
        )
        print("✓ PaddleOCR 初始化成功")
    except Exception as e:
        print(f"✗ PaddleOCR 初始化失败: {e}")
        return False
    
    # 处理图片
    with open(output_file, 'w', encoding='utf-8') as f:
        if use_progress_bar:
            iterator = enumerate(tqdm(image_files, desc="OCR 识别进度"), 1)
        else:
            iterator = enumerate(image_files, 1)
            
        for idx, image_path in iterator:
            image_name = os.path.basename(image_path)
            
            if not use_progress_bar:
                print(f"  处理第 {idx}/{total_images} 页...")
            
            # 写入页码标记
            f.write(f"\n{'='*60}\n")
            f.write(f"第 {idx}/{total_images} 页 ({image_name})\n")
            f.write(f"{'='*60}\n\n")
            
            try:
                # 使用 PaddleOCR 进行识别
                result = ocr.ocr(image_path, cls=False)
                
                # 提取文字
                if result and result[0]:
                    text_count = 0
                    for line in result[0]:
                        if line and len(line) >= 2:
                            text = line[1][0]
                            confidence = line[1][1]
                            if confidence > confidence_threshold:
                                f.write(f"{text}\n")
                                text_count += 1
                    
                    if text_count == 0:
                        f.write("[此页无高置信度文本内容]\n")
                else:
                    f.write("[此页无文本内容]\n")
                
                f.flush()
                    
            except KeyboardInterrupt:
                print(f"\n✗ 用户中断，已保存 {idx-1} 页内容")
                f.flush()
                return False
            except Exception as e:
                print(f"\n✗ 处理 {image_name} 时出错: {e}")
                f.write(f"[处理此页时出错: {e}]\n")
                f.flush()
    
    print(f"\n✓ 完成！共处理 {total_images} 页")
    print(f"✓ 结果已保存到: {output_file}")
    
    # 显示文件大小
    if os.path.exists(output_file):
        file_size = os.path.getsize(output_file)
        print(f"✓ 文件大小: {file_size:,} 字节")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='PDF 文字提取工具 - 使用 PaddleOCR 多语言模型支持 80+ 种语言',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本使用（中文）
  python extract_pdf.py input.pdf
  
  # 日文识别
  python extract_pdf.py japanese.pdf --lang japan
  
  # 韩文识别
  python extract_pdf.py korean.pdf --lang korean
  
  # 法文识别
  python extract_pdf.py french.pdf --lang french
  
  # 调整参数
  python extract_pdf.py input.pdf --scale 3.0 --confidence 0.6
  
  # 不显示进度条（避免中断问题）
  python extract_pdf.py input.pdf --no-progress
        """
    )
    
    parser.add_argument('pdf_file', help='输入 PDF 文件路径')
    parser.add_argument('-o', '--output', help='输出 TXT 文件路径（默认：PDF文件名_extracted.txt）')
    parser.add_argument('-t', '--temp-dir', help='临时图片目录（默认：temp_images）')
    parser.add_argument('--lang', choices=['ch', 'en', 'japan', 'korean', 'french', 'german', 'latin', 'arabic'], default='ch', 
                       help='语言模型：ch=中英文, en=英文, japan=日文, korean=韩文, french=法文, german=德文等（PaddleOCR 多语言模型）')
    parser.add_argument('--scale', type=float, default=2.0, 
                       help='图片缩放比例（默认：2.0，范围：1.0-3.0）')
    parser.add_argument('--confidence', type=float, default=0.5, 
                       help='置信度阈值（默认：0.5，范围：0.0-1.0）')
    parser.add_argument('--no-progress', action='store_true', 
                       help='不显示进度条（避免某些环境下的中断问题）')
    
    args = parser.parse_args()
    
    # 检查输入文件
    if not os.path.exists(args.pdf_file):
        print(f"✗ 错误：PDF 文件不存在: {args.pdf_file}")
        sys.exit(1)
    
    # 设置默认输出文件名
    if args.output is None:
        pdf_name = Path(args.pdf_file).stem
        args.output = f"{pdf_name}_extracted.txt"
    
    # 设置默认临时目录
    if args.temp_dir is None:
        pdf_name = Path(args.pdf_file).stem
        args.temp_dir = f"temp_images_{pdf_name}"
    
    # 显示配置
    print("=" * 60)
    print("PDF 文字提取工具")
    print("=" * 60)
    print(f"输入文件: {args.pdf_file}")
    print(f"输出文件: {args.output}")
    print(f"临时目录: {args.temp_dir}")
    lang_names = {
        'ch': '中英文混合', 'en': '英文', 'japan': '日文', 'korean': '韩文',
        'french': '法文', 'german': '德文', 'latin': '拉丁文', 'arabic': '阿拉伯文'
    }
    print(f"语言模型: {lang_names.get(args.lang, args.lang)}")
    print(f"OCR 引擎: PaddleOCR 多语言模型")
    
    print(f"图片缩放: {args.scale}x")
    print(f"置信度阈值: {args.confidence}")
    print(f"进度条: {'否' if args.no_progress else '是'}")
    print("=" * 60)
    
    # 步骤 1: 转换 PDF 为图片
    print("\n【步骤 1/2】PDF 转图片")
    print("-" * 60)
    image_files = convert_pdf_to_images(args.pdf_file, args.temp_dir, args.scale)
    
    if not image_files:
        print("\n✗ PDF 转图片失败，无法继续")
        sys.exit(1)
    
    # 步骤 2: OCR 识别
    print("\n【步骤 2/2】OCR 文字识别")
    print("-" * 60)
    
    # 使用 PaddleOCR 多语言模型
    success = extract_text_with_paddleocr(
        image_files, 
        args.output, 
        lang=args.lang,
        confidence_threshold=args.confidence,
        use_progress_bar=not args.no_progress
    )
    
    if success:
        print("\n" + "=" * 60)
        print("✓ 全部完成！")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("✗ 处理未完成")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
