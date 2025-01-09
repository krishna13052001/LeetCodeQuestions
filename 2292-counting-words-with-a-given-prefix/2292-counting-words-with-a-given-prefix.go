func prefixCount(words []string, pref string) int {
    count := 0
    for _, word := range words {
        if len(word) < len(pref) {
            continue
        } 
        if pref == word[:len(pref)] {
            count += 1
        }
    }
    return count
}