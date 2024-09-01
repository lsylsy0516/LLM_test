import argparse
import os

IFSEG = True


if IFSEG:
    from yolov5.segment.predict import main
else:
    from yolov5.detect import main

def set_detection_parameters(input_source:str,dir:str):
    # 创建解析器
    parser = argparse.ArgumentParser()
    if IFSEG:
        parser.add_argument('--weights', nargs='+', type=str, default='yolov5m-seg.pt', help='model path(s)')
        parser.add_argument("--alpha", type=float, default=0.3, help="mask transparency")
    else:
        parser.add_argument('--weights', nargs='+', type=str, default='yolov5m.pt', help='model path(s)')
    # 添加参数
    parser.add_argument('--data', type=str, default='data/coco128.yaml', help='(optional) dataset.yaml path')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='show results')
    parser.add_argument('--save-txt',default=True, action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--visualize', action='store_true', help='visualize features')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--half', action='store_true', help='use FP16 half-precision inference')
    parser.add_argument('--dnn', action='store_true', help='use OpenCV DNN for ONNX inference')
    parser.add_argument('--vid-stride', type=int, default=1, help='video frame-rate stride')
    
    parser.add_argument('--conf-thres', type=float, default=0.5, help='confidence threshold')
    parser.add_argument('--line-thickness', default=1, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--project', default='new_result', help='save results to project/name')
    parser.add_argument('--name', default=dir, help='save results to project/name')
    parser.add_argument('--classes',default='0',nargs='+', type=int, help='filter by class: --classes 0, or --classes 0 2 3')
    parser.add_argument('--source', type=str, default=input_source, help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--area_thre',type=int,default=5000,help='area threshold')

    # 解析参数
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1
    return opt

if __name__ == "__main__":
    images_all_path = "imgs"
    import os
    for root, dirs, files in os.walk(images_all_path):
        for dir in dirs:
            images_path = os.path.join(root, dir)
            opt = set_detection_parameters(images_path,dir)
            main(opt)
            print("Finish detection for images in ", images_path)
    print("Finish all detection")