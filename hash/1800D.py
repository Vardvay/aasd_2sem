t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    MOD1 = 10**9 + 7
    MOD2 = 10**9 + 9
    P= 31
    
    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    p_pow1 = [1] * (n + 1)
    p_pow2 = [1] * (n + 1)
    
    for i in range(n):
        val = ord(s[i])
        pref1[i+1] = (pref1[i] * P + val) % MOD1
        pref2[i+1] = (pref2[i] * P + val) % MOD2
        p_pow1[i+1] = (p_pow1[i] * P) % MOD1
        p_pow2[i+1] = (p_pow2[i] * P) % MOD2
        
    unique_hashes = set()
    
    for i in range(n - 1):
        len_suffix = n - 2 - i
        
        hash_pref1 = pref1[i]
        hash_pref2 = pref2[i]
        
        hash_suff1 = (pref1[n] - pref1[i+2] * p_pow1[len_suffix]) % MOD1
        hash_suff2 = (pref2[n] - pref2[i+2] * p_pow2[len_suffix]) % MOD2

        comb_hash1 = (hash_pref1 * p_pow1[len_suffix] + hash_suff1) % MOD1
        comb_hash2 = (hash_pref2 * p_pow2[len_suffix] + hash_suff2) % MOD2
        
        unique_hashes.add((comb_hash1, comb_hash2))
        
    print(len(unique_hashes))