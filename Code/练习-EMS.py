# # 显示欢迎信息
# print('=' * 20, '欢迎来到员工管理系统', '=' * 20)
# # 创建一个列表，保存员工信息
# emps = ['孙悟空\t18\t男\t花果山', '猪八戒\t19\t男\t高老庄']

# # 创建死循环
# while True:
#     # 显示可以选择的操作
#     print('请选择要做的操作')
#     print('1.查询员工')
#     print('2.添加员工')
#     print('3.删除员工')
#     print('4.退出系统')
#     user_choose = input('请选择[1-4]')
#     # 打印分隔线
#     print('-'*62)
#     # 根据用户的选择进行不同的操作
#     if user_choose == '1':
#         # 查询
#         # 打印表头
#         print('\t序号\t姓名\t年龄\t性别\t住址')
#         # 创建一个变量，保存序号
#         n = 1
#         for emp in emps:
#             print(f'\t{n}\t{emp}')
#             n += 1
#     elif user_choose == '2':
#         # 添加
#         name = input('请输入姓名:')
#         age = input('请输入年龄:')
#         sex = input('请输入性别:')
#         address = input('请输入住址:')
#         emp = f'{name}\t{age}\t{sex}\t{address}'

#         # 显示提示信息
#         print('员工信息将会被添加至系统:')

#         print('-' * 62)
#         print('姓名\t年龄\t性别\t住址')
#         print(emp)
#         print('-' * 62)

#         user_confirm = input('是否确认该操作[Y/N]:')
#         if user_confirm == 'y' or user_confirm == 'yes' or user_confirm == 'Y':
#             emps.append(emp)
#             # 提示
#             print('添加成功！')
#         else:
#             print('操作终止，添加已取消！')

#         # 打印分隔符
#         print('-'*62)
#     elif user_choose == '3':
#         # 删除
#         # 获取员工的序号
#         del_num = int(input('请输入员工的序号:'))
#         # 判断输入是否合法
#         if 0 < del_num <= len(emps):
#             # 合法
#             del_i = del_num - 1

#             # 显示提示信息
#             print('该员工信息将会被删除:')

#             print('-' * 62)
#             print('\t序号\t姓名\t年龄\t性别\t住址')
#             print(f'\t{del_num}\t{emps[del_i]}')
#             print('-' * 62)

#             # 提示
#             user_confirm = input('该操作无法恢复，是否确认该操作[Y/N]:')
#             # 判断
#             if user_confirm == 'y' or user_confirm == 'yes':
#                 emps.pop(del_i)
#                 print('已删除！')
#             else:
#                 print('操作已取消！')
#         else:
#             # 异常
#             print('你的输入有误，请重新操作！')

#     elif user_choose == '4':
#         # 退出
#         input('按任意键退出:')
#         break
#     else:
#         # 提示
#         print('你的输入有误，请重新输入！')
#     # 打印分隔线
#     print('-'*62)


# 查询员工
# 添加员工
# 删除员工
# 退出系统


# 显示提示信息
print('=' * 20, '欢迎来到员工管理系统', '='*20)
# 创建一个列表，保存员工信息
emps = ['孙悟空\t18\t男\t花果山', '沙和尚\t38\t男\t流沙河']

while True:
    # 显示可以操作的选项
    print('请选择要进行的操作:')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose = input('请输入你的选择[1-4]:')

    print('-'*62)
    if user_choose == '1':
        # 查询
        # 打印表头
        print('\t序号\t姓名\t年龄\t性别\t住址')
        # 创建变量，保存序号
        n = 1
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
        print('-'*62)
    elif user_choose == '2':
        # 添加
        # 用户输入添加的信息
        name = input('请输入员工的姓名:')
        age = input('请输入员工的年龄:')
        sex = input('请输入员工的姓别:')
        address = input('请输入员工的住址:')
        emp = f'{name}\t{age}\t{sex}\t{address}'

        print('-'*62)

        # 提示用户是否添加信息至系统
        print('以下信息将被添加至系统:')
        print('姓名\t年龄\t性别\t住址')
        print(emp)

        print('-'*62)

        # 提示用户是否确认操作
        user_confirm = input('是否确认该操作[Y/N]:')
        if user_confirm == 'y' or user_confirm == 'yes' or user_confirm == 'Y':
            emps.append(emp)
            print('员工信息已添加至系统！')
        else:
            print('操作已取消！')

    elif user_choose == '3':
        # 删除
        # 获取员工的序号，根据序号删除员工的信息
        del_num = int(input('请输入员工的序号:'))

        if 0 < del_num <= len(emps):
            # 获取索引
            del_i = del_num - 1

            # 提示信息
            print('以下信息将被删除:')
            print('序号\t姓名\t年龄\t性别\t住址')
            print(f'{del_num}\t{emps[del_i]}')

            print('-' * 62)

            # 提示用户是否确认操作
            user_confirm = input('该操作将导致数据无法恢复！，是否确认[Y/N]:')
            if user_confirm == 'y' or user_confirm == 'Y' or user_confirm == 'yes':
                emps.pop(del_i)
            else:
                print('操作已取消')

        else:
            print('你的输入有误，请重新操作！')

    elif user_choose == '4':
        # 退出系统
        input('按任意键退出！')
        break
    else:
        # 输入有误
        print('你的输入有误，请重新操作！')
    print('-'*62)
