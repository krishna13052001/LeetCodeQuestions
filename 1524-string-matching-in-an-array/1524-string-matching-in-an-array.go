func stringMatching(words []string) []string {
    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) < len(words[j])
    })

    res := []string{}
    for i := 0; i < len(words); i++ {
        for j := i + 1; j < len(words); j++ {
            if contains(words[j], words[i]) {
                res = append(res, words[i])
                break
            }
        }
    }
    return res
}

func contains(word, sub string) bool {
    return len(sub) <= len(word) && len(word) > 0 && len(sub) > 0 && strings.Contains(word, sub)
}