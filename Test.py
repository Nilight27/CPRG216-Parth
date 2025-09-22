y = ['AB','BC','MC','BMW']



province = input('what is ur province')
province = province.upper()

if province in y[0:2]:
    gst = 0.05
if province in y[4]:
    gst = 0.13