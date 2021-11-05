import Foundation

func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    var cache = [String]()
    var time = 0
    
    if cacheSize == 0{
        return cities.count * 5
    }
    
    for city in cities{
        let target = city.uppercased(), result = cache.contains(target)
        if result, cache.count <= cacheSize{
            var index = 0
            for i in 0..<cacheSize{
                if cache[i] == target{
                    index = i
                    break
                }
            }6
            cache.remove(at: index)
            cache.append(target)
            time += 1
        }else if !result, cache.count < cacheSize{
            cache.append(target)
            time += 5
        }else if !result, cache.count == cacheSize{
            cache.removeFirst()
            cache.append(target)
            time += 5
        }
    }
    return time
}
