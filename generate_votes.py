"""为孔多塞投票法提供输入."""

import random

import numpy as np
import pandas as pd


class GenerateVotes():

  """为孔多塞投票法提供输入

  Attributes:
    option_num {int} 选项数量.
    voter_num {int} 投票人数量.
    options {list} 可用的选项.
    votes {pandas.DataFrame} 选票.
  Functions:
    print_votes: 以阅读友好的形式打印选票.
  """

  option_num = None  # 选项数量
  voter_num = None  # 投票人数量
  options = None  # 可用的选项
  votes = None  # 选票

  def __init__(self):
    # 生成随机列表
    self.option_num = option_num = np.random.randint(3, 10)  # 选项数量
    self.voter_num = voter_num = np.random.randint(3, 20)  # 投票人数量
    # option_num, voter_num = 10, 4  # 先用一个较小的例子做后续测试

    # 选项字符串
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # 可用的选项为
    self.options = options = list(alphabet[:option_num])

    # 创建一个指定大小的空df
    df = pd.DataFrame(
        index=list(range(voter_num)),
        columns=list(range(option_num)),
    )
    # 按行不重复的随机选取(random.sample)可选项填充df
    self.votes = df = df.apply(
        lambda x: pd.Series(random.sample(options, option_num)),
        axis=1,
    )

  def print_votes(self):
    """以阅读友好的形式打印选票
    """
    print(self.votes.to_string(index=False, header=False))


if __name__ == '__main__':
  votes_obj = GenerateVotes()
  print(f'''投票人数: {votes_obj.voter_num}''')
  print(f'''选项数量: {votes_obj.option_num}''')
  print(f'''选项为: {votes_obj.options}''')
  print('''投票结果如下:''')
  votes_obj.print_votes()
