# 身份选择
# 提示信息
print('欢迎进入游戏:《唐僧大战白骨精》！')
print('=' * 40)


print('请选择你的身份：')
print('1、唐僧')
print('2、白骨精')
user_id = input('请选择(1-2)：')
print('='*40)

if user_id == '1':
    print('你已经选择了唐僧')
elif user_id == '2':
    print('你选择了该游戏的BOSS，现将你的身份修改为唐僧')
else:
    print('没有这个选项，现将你的身份修改为唐僧')


# 开始游戏
# 基本信息
player_firepower = 10  # 唐僧初始攻击力
player_life = 10  # 唐僧初始生命值
boss_firepower = 100  # boss总攻击力
boss_life = 100  # boss总生命值

print('=' * 40)
print('->唐僧<-', '攻击力', player_firepower, '生命值', player_life)
print('=' * 40)

while True:
    # 玩家可选操作
    print('可选操作:')
    print('1、练级')
    print('2、打BOSS')
    print('3、逃跑')
    user_play = input('请选择你要进行的操作[1-3]:')

    print('=' * 40)

    if user_play == '1':
        player_firepower += 10
        player_life += 10
        print('恭喜你升级了！你的攻击力提升至', player_firepower, '生命值提升至', player_life)
    elif user_play == '2':
        # 玩家对BOSS进行攻击
        boss_life -= player_firepower
        print('->唐僧<- 对 ->白骨精<- 了发起攻击，造成了', player_firepower, '点伤害')

        print('=' * 40)

        if boss_life <= 0:
            print('白骨精受到致命一击，不治身亡! 你获得了胜利')
            break
        # BOSS进行反击
        player_life -= boss_firepower
        print('->白骨精<- 开始反击')

        print('=' * 40)

        if player_life <= 0:
            print('你激怒了 ->白骨精<- 被她一下打死! GAME OVER')
            break
    elif user_play == '3':
        print('->唐僧<- 扭头就跑，不料却被白骨精发现，被她一下拍死！GAME OVER')
        break
    else:
        print('你的选择有误，请重新选择！')
