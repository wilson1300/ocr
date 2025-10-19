#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 PaddleOCR 低级 API 提取 PDF 内容到 TXT 文件（绕过高级 API 的模型自动下载）
"""
import os
import sys
import cv2
from pathlib import Path
from tqdm import tqdm

# 添加 ppocr 到路径
ppocr_path = r"C:\Users\qiwei.zhang\Desktop\ocr\PaddleOCR"
sys.path.insert(0, ppocr_path)

from tools.infer.utility import parse_args
from tools.infer.predict_system import TextSystem

def create_args():
    """创建推理参数"""
    model_dir = Path.home() / '.paddleocr' / 'whl'
    det_model_dir = model_dir / 'det' / 'en' / 'en_PP-OCRv3_det_infer'
    rec_model_dir = model_dir / 'rec' / 'en' / 'en_PP-OCRv3_rec_infer'
    
    # 创建一个空的参数对象
    class Args:
        def __init__(self):
            # 检测参数
            self.det_algorithm = 'DB'
            self.det_model_dir = str(det_model_dir)
            self.det_limit_side_len = 960
            self.det_limit_type = 'max'
            self.det_db_thresh = 0.3
            self.det_db_box_thresh = 0.6
            self.det_db_unclip_ratio = 1.5
            self.use_dilation = False
            self.det_db_score_mode = 'fast'
            self.det_box_type = 'quad'  # 添加缺失的属性
            
            # 识别参数
            self.rec_algorithm = 'SVTR_LCNet'
            self.rec_model_dir = str(rec_model_dir)
            self.rec_image_shape = '3, 48, 320'
            self.rec_batch_num = 6
            self.max_text_length = 25
            self.rec_char_dict_path = os.path.join(ppocr_path, 'ppocr', 'utils', 'en_dict.txt')
            self.use_space_char = True
            
            # 分类参数（禁用）
            self.use_angle_cls = False
            self.cls_model_dir = None
            self.cls_image_shape = '3, 48, 192'
            self.label_list = ['0', '180']
            self.cls_batch_num = 6
            self.cls_thresh = 0.9
            
            # 通用参数
            self.use_gpu = False
            self.use_npu = False
            self.use_xpu = False
            self.use_mlu = False
            self.use_gcu = False
            self.ir_optim = True
            self.use_tensorrt = False
            self.min_subgraph_size = 15
            self.precision = 'fp32'
            self.gpu_mem = 500
            self.gpu_id = 0
            self.image_dir = None
            self.page_num = 0
            self.process_id = 0
            self.total_process_num = 1
            self.use_pdserving = False
            self.warmup = False
            self.draw_img_save_dir = './inference_results'
            self.save_crop_res = False
            self.crop_res_save_dir = './output'
            self.use_mp = False
            self.total_process_num = 1
            self.process_id = 0
            self.benchmark = False
            self.save_log_path = './log_output/'
            self.show_log = False
            self.use_onnx = False
            self.output = './output'
            self.lang = 'en'
            self.det = True
            self.rec = True
            self.type = 'ocr'
            self.ocr_version = 'PP-OCRv3'
            self.structure_version = 'PP-StructureV2'
            self.recovery = False
            self.use_pdf2docx_api = False
            self.infer_mode = False
            self.cpu_threads = 10
            self.enable_mkldnn = False
            self.table_max_len = 488
            self.table_algorithm = 'TableAttn'
            self.table_model_dir = None
            self.merge_no_span_structure = True
            self.table_char_dict_path = None
            self.layout_model_dir = None
            self.layout_dict_path = None
            self.layout_score_threshold = 0.5
            self.layout_nms_threshold = 0.5
            self.kie_algorithm = 'LayoutXLM'
            self.ser_model_dir = None
            self.re_model_dir = None
            self.use_visual_backbone = True
            self.ser_dict_path = None
            self.ocr_order_method = None
            self.mode = 'structure'
            self.image_orientation = False
            self.layout = True
            self.table = True
            self.ocr = True
            self.pdf2docx_api = False
    
    return Args()

def ocr_images_to_text(images_dir, output_file):
    """
    对文件夹中的图片进行 OCR 识别并保存到文本文件
    
    Args:
        images_dir: 图片文件夹路径
        output_file: 输出文本文件路径
    """
    # 初始化 TextSystem
    print("正在初始化 PaddleOCR TextSystem...")
    args = create_args()
    
    try:
        text_sys = TextSystem(args)
    except Exception as e:
        print(f"初始化失败: {e}")
        print("\n请确保模型文件存在:")
        print(f"  检测模型: {args.det_model_dir}")
        print(f"  识别模型: {args.rec_model_dir}")
        return
    
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
                # 读取图片
                img = cv2.imread(image_path)
                if img is None:
                    print(f"\n无法读取图片: {image_file}")
                    continue
                
                # 执行 OCR
                dt_boxes, rec_res = text_sys(img)
                
                # 写入页码标记
                f.write(f"\n{'='*60}\n")
                f.write(f"第 {idx}/{total_images} 页 ({image_file})\n")
                f.write(f"{'='*60}\n\n")
                
                # 提取并写入文本
                if rec_res:
                    for line in rec_res:
                        text = line[0]  # 提取识别的文本
                        confidence = line[1]  # 置信度
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
