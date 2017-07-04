import os
import shutil
from os.path import join


def forceRemove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)


def forceCopy(source, dest):
    forceRemove(dest)

    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))

    if os.path.isdir(source):
        shutil.copytree(source, dest)
    elif os.path.isfile(source):
        shutil.copyfile(source, dest)


def forceMkdir(path):
    if os.path.exists(path) and os.path.isdir(path):
        return

    os.makedirs(path)


projectFolder = os.path.abspath(os.path.join(__file__, '..'))
outputFolder = r'C:\Users\Administrator\Desktop\Tmp\beautify_unity_shader'

# 目标目录处理
forceRemove(outputFolder)
forceMkdir(outputFolder)

# 遍历app目录
for path, dirs, files in os.walk(os.path.join(projectFolder, 'app')):
    for file in files:
        if os.path.splitext(file)[1] == '.py' or file == '3_edges.json':
            srcFullPath = join(path, file)
            dstFullPath = srcFullPath.replace(projectFolder, outputFolder)
            forceCopy(srcFullPath, join(outputFolder, dstFullPath))

# 遍历工程根目录
for name in os.listdir(projectFolder):
    fullPath = join(projectFolder, name)
    if os.path.isdir(fullPath):
        if name in ('.git', '__pycache__'):
            continue
        forceMkdir(fullPath.replace(projectFolder, outputFolder))
    else:
        forceCopy(fullPath, fullPath.replace(projectFolder, outputFolder))
