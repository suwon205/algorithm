def solution(bandage, health, attacks):
    maxHealth = health
    curTime = attackIdx = healTime = 0 # 현재 초
    lastTime = attacks[-1][0] # 공격을 받는 마지막 시간
    spendTime = bandage[0]
    healPerSec = bandage[1]
    addHeal = bandage[2]
    while curTime <= lastTime:
        # print('지금 시간은', curTime, health, attacks[attackIdx], healTime)
        if curTime == attacks[attackIdx][0]: # 공격 받을 시간
            health -= attacks[attackIdx][1]
            attackIdx += 1
            healTime = 1
        else:
            addHealAmount = 0
            if healTime == spendTime: #붕대 다 감음
                addHealAmount = healPerSec + addHeal
                healTime = 1
            else:
                addHealAmount = healPerSec
                healTime += 1
            health = min(maxHealth, health + addHealAmount) # 힐링~
        # print(curTime, health)
        if health <= 0: # 죽을 경우
            # print('사망!')
            return -1
        curTime += 1
    return health