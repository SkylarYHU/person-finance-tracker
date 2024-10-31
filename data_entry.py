import pandas as pd
import csv
# 旨在用于处理日期和时间
from datetime import datetime

class CSV:
  CSV_FILE = 'finance_data.csv'
  COLUMNS = ["date", "amount", "category", "description"]
  # 用@classmethod装饰的方法可以直接通过类名调用，而不需要创建类的实例。例如，CSV.initialize_csv()。这样可以避免为了调用此方法而创建不必要的实例对象，简化代码
  @classmethod
  # 如果文件存在，则只需使用pd.read_csv读取它
  # cls 是 Python 中 @classmethod 方法的第一个参数，表示类本身的引用。类似于实例方法中的 self，cls 允许在类方法中访问和操作类级别的属性和方法
  def initialize_csv(cls):
    try:
      pd.read_csv(cls.CSV_FILE);
    # 如果文件不存在（触发FileNotFoundError ），则会创建一个包含特定列（ "date" 、 "amount" 、 "category" 、 "description" ）的新 DataFrame，为将来的数据条目准备一个空结构
    except FileNotFoundError:
      df = pd.DataFrame(columns=cls.COLUMNS)
      df.to_csv(cls.CSV_FILE, index=False)

  @classmethod
  def add_entry(cls, date, amount, category, description):
    # 创建一个名为new_entry的字典，其中包含四个键（ "date" 、 "amount" 、 "category"和"description" ）以及作为参数传入的相应值
    new_entry = {
      "data": date,
      "amount": amount,
      "category": category,
      "description": description,
    }
    # 任何新数据都会添加到文件末尾，而不会覆盖现有数据
    # newline=""是为了避免在写入 CSV 文件时在行之间添加额外的空行
    with open(cls.CSV_FILE, "a", newline="") as csvfile:
      # 用于将字典写入 CSV 文件。它使用文件 ( csvfile ) 和fieldnames=cls.COLUMNS进行初始化
      write = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
      # 将新条目作为一行写入 CSV 文件中。 new_entry中的字段名称应与cls.COLUMNS中的字段名称匹配
      write.writerow(new_entry)
      print("Entry added successfully")


CSV.initialize_csv()