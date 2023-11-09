import os
# path = '/Users/shengjiehou/intov2imwallet/alpha-wallet-ios/AlphaWallet'       # 文件夹地址
path = '/Users/shengjiehou/intov2imwallet/alpha-wallet-ios/AlphaWallet/INTO/ViewControllers/UpdateVersionConfigViewController'
for filepath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        file_data = ""
        realfilePath = os.path.join(filepath, filename)
        if filename[-5:] == 'swift':  # 判断文件是否为swift文件
            with open(realfilePath, 'r') as f:
                lines = f.readlines()
                print("read lines =", lines)
                st = '456'
                for line in lines:
                    if st in line:
                        line = line.replace(st, "123")
                    file_data += line
            with open(realfilePath,"w",encoding="utf-8") as fw:
                fw.write(file_data)
            
print('Done')
