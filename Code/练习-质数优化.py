# 获取1--100所有的质数
# 导入 time 模块
import time
# 优化前，获取10000以内所有的质数所用的时间：
# 8.114秒
# 第一次优化后，所用的时间:
# 0.879秒
# 第二次优化后，所用的时间：
# 0.045秒
begin = time.time()
i = 2
while i <= 100000:
    Flag = True
    j = 2
    # 第二次优化
    while j <= i ** 0.5:
        if i % j == 0:
            Flag = False
            # 第一次优化
            # 判断成立，则证明这个数一定不是质数，不需要继续往下执行
            break
        j += 1
    if Flag:
        # print(i)
        pass
    i += 1
end = time.time()
print(end - begin, "秒")
