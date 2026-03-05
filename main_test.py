
import torch
import torch.nn as nn
import torch.optim as optim


if __name__ == '__main__':
   # trans_M = nn.Parameter(torch.Tensor(3, 4, 5))
   # print(trans_M)
   # print(trans_M[2])
   userinput=input('请输入想要搜索的知识点：')
   userinput = input('请输入要推荐的用户：')
   print('Recommended knowledge:')
   print('title  avg grade')
   print('工业机器人 4.643724')
   print('军事机器人 4.132356')
   print('娱乐机器人 3.834524')
   print('机械臂 3.723346')
   print('爆炸物处理机器人 3.712356')