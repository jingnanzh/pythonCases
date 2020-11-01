import pandas as pd
import sweetviz as sv

# https://pypi.org/project/sweetviz/

data = pd.read_csv('taobao_consume.csv')
taobao_report = sv.analyze(data)
taobao_report.show_html()