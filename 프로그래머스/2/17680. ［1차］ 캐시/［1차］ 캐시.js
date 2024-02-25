function solution(cacheSize, cities) {
    let answer = 0;
    let cache = []
    if (cacheSize === 0) {
        return 5 * cities.length
    }
    for (let idx = 0; idx < cities.length; idx++) {
        let newCity = cities[idx].toLowerCase();
        if (cache.length === 0){
            cache.push(newCity);
            answer += 5
        } else {
            if (cache.includes(newCity)) {
                answer += 1
                cache.splice(cache.indexOf(newCity), 1);
                cache.push(newCity);
            } else {
                if (cache.length >= cacheSize) {
                    // 그냥 추가해도 되는 경우
                    cache.shift()
                }
                cache.push(newCity)
                answer += 5
            }
        }
    }
    return answer;
}