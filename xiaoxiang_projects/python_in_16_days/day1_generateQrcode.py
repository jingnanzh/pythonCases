import qrcode

img = qrcode.make('我有100个微信好友\n没有一个人和我说话\n万圣节快乐')
img.save("qrcode.jpg")