import sys
sys.path.append("/root/Code/pose/ba/wxcloudrun/back-end/ba")
from image_analyse import *
from image_annotate import * 

# path2 = '/home/ubuntu/Code/BD/input/深蹲错误.png' # 错误图片路径
# path1 = '/home/ubuntu/Code/BD/input/深蹲正确.png' # 正确图片路径

def analyse(true_file_path,false_file_path):

    print('开始分析')
    save_path = os.path.join('/root/Code/pose/ba/wxcloudrun/back-end/outputFile/',false_file_path.split('/')[-1])
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=2)

    df1 = detectPose_df(true_file_path,pose)
    df2 = detectPose_df(false_file_path,pose)

    df_true = standardization(df1)
    df_false = standardization(df2)

    df_distance_comparison = make_distance_comparison(df_true, df_false)
    df_angle_comparison = make_angle_comparison(df_true, df_false, 0.2)

    img = mark_pose(false_file_path,df_false)

    img1,distance_des = mark_distance(img,df_distance_comparison,3)
    #img1.save('/home/ubuntu/Code/BD/input/深蹲错误_标准距离.png')
    img2,angle_des = mark_angle(img1,df_angle_comparison,4)
    print(distance_des)
    print(angle_des)

    # 存储标注后的图片
    img2.save(save_path)
    return distance_des,angle_des,save_path

# path1 = '/root/Code/pose/ba/wxcloudrun/back-end/inputFile/squat.png'
# path2 = '/root/Code/pose/ba/wxcloudrun/back-end/inputFile/squat.png'
# analyse(path1,path2)


