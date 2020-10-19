'''
    developer: Wendy
    date: Aug 26,2020
    version: 1.0
    function: air quality index calculations
'''

def cal_linear(iaqi_lo,iaqi_hi, bp_lo, bp_hi, cp):
    '''
        范围缩放
    '''
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo)/(bp_hi - bp_lo) + iaqi_lo


def cal_pm_iaqi(pm_val):
    '''
        calculate pm iaqi
    '''
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36<= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)



def cal_co_iaqi(co_val):
    '''
        calculate co iaqi
    '''
    pass

def cal_aqi(param_list):
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    am_iaqi = cal_co_iaqi(co_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi

def main():
    input('Please provide the information, devided by a space:')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    aqi_val = cal_aqi(param_list)
    print('air quality index is: {}'.format(aqi_val))

if __name__=='__main__':
    main()