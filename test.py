import os
import glob

path_data2 = '/Behavior data/FreezeFrame/MeA/20170816_fear_cond_MeA_ck2a/'

path_3 = 'E:\\'  # drive letter
os.chdir(path_3)
os.getcwd()
join_path = os.path.join(path_3, path_data2)

os.getcwd()  # current directory
os.listdir()  # current lists
os.chdir(join_path)
path_list = []
file_list = []
count = 0

for (path, _, files) in os.walk():  # walk: 계속 깊이 들어갈 수 있음. glob 도 가능은 함
    path_list.append(path)
    file_list.append(files)

    # print(len(glob.glob(path+'/*.csv')))

    for filename in files:
        ext = os.path.splitext(filename)[-1]
        file_glob_list = glob.glob('./*.csv')
        # print(ext)
        if ext == '.csv':  # csv 확장자일 때
            print(filename)  # 파일 이름 출력
            count += 1
print('csv 파일 수는 {}개\n'.format(count))

idx = 4

print(path_list[idx])
print(file_list[idx])