function solution(bandage, health, attacks) {
    let maxHealth = health;
    let curTime = 0;
    let attackIdx = 0;
    let healTime = 0;
    let lastTime = attacks[attacks.length - 1][0];
    let spendTime = bandage[0];
    let healPerSec = bandage[1];
    let addHeal = bandage[2];

    while (curTime <= lastTime) {
        if (curTime === attacks[attackIdx][0]) {
            // 공격 받음
            health -= attacks[attackIdx][1];
            attackIdx += 1;
            healTime = 1;
        } else {
            let addHealth = healPerSec;
            if (healTime === spendTime) {
                // 붕대 다 감은 경우에만 추가적으로 체력 세이브
                addHealth += addHeal;
                healTime = 1;
            } else {
                healTime += 1;
            }
            health = Math.min(addHealth + health, maxHealth);
        }
        console.log(curTime, health);
        if (health <= 0) {
            return -1; // 죽은 경우
        }
        curTime += 1;
    }
    return health;
}
