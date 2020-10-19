'''
作者；jing
日期：2020-08-01
'''
rmb_str_value = input('输入人民币金额:')

rmb_value = eval(rmb_str_value)

rmb_vs_usd = 6.77

usd_value = rmb_value / rmb_vs_usd
print('美元：', usd_value)