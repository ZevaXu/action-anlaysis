import sys
sys.path.append("/root/Code/pose/ba/wxcloudrun/back-end/")
from main_process import *

false_file_path = '/root/Code/pose/ba/wxcloudrun/back-end/inputFile/squat.png'
true_file_path = '/root/Code/pose/ba/wxcloudrun/back-end/inputFile/squat.png'
print('开始分析')
distance_des,angle_des,save_path = analyse(true_file_path,false_file_path)
print('分析结束')