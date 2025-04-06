
# DNS Cache Flush Attack Workshop

This repository contains materials for reproducing and analyzing a DNS Cache Flush Attack on Knot resolver and Bind9.
It also includes instructions on building a Docker image to facilitate the process, along with the results of various tests conducted during the research.

---

## Projet overview, analysis and conclusions

Can be evaluated in the presentation link:
*https://github.com/asheri1/DNS_CacheFlushAttack_workshop/blob/master/Project%20overview%2C%20analysis%2C%20and%20final%20conclusions.pdf*

---

## Repository Structure

- **reproduction_A_attack**: This folder contains instructions and scripts to reproduce the DNS cache flush attack using A records.
  
- **Build Docker Image**: This folder contains all necessary files and instructions for building a Docker image that supports the attack reproduction and analysis.

- **Test Results**: This folder includes the results of tests performed during the workshop, providing insights into the attack's impact and effectiveness.


 ## Analyze the Test Results
   Test results are located in the `Test Results` folder.
   The results are divided to each testing scenario.
   Each one contains one query results (the response of 2 DNS queries, a PCAP file and cache content file). 
   It's also contains the queries flooding test results (using resperf).  

   In order to examine Knot cache contents:
   run `dump_cache_to_csv.py` in the current cache.lmdb file is located.


## How to replicate the experiments: 

1. **Download docker to your machine.** 

2. **Pull the docker image from docker hub repository.**
   open terminal and run 
    ```bash
    `docker pull asherio/knot_res:v2`
    ```

   or alternatively, build the image locally by running
    ```bash
    docker build -t knot_res .
    ```

3. **run the image.**
    ```bash
    docker container run --dns 127.0.0.1 --mount type=bind,source=<source>,target=/app -it asherio/knot_res:v2 /bin/bash
    ```
  open additional terminals using:
    ```bash
    docker exec -it <container_id> bash
    ```

4. **turn Knot resolver up.**
   if you wish to try the attack on knot resolver, 
   do it by open a new termainal and run
      ```bash
      kresd -c /etc/knot-resolver/kresd.conf
      ``` 

5. **turn on the authorative servers, Bind9 resolver (if needed), and loading the zonefiles:**
  everything is as in instructed at shoham's repository: github.com/shohamda/CacheFlushSimulator

6. **Reproduce the A records Attack**
   - Navigate to the `Reproduction of A Records attack` folder and copy `home.lan.forward` to the docker into nsd_attack_home directory. 
   - next, run the following:
      ```bash
         cd /env/nsd_attack_home
      chmod 777 home.lan.forward
      ``` 

    In order to load the new zonefile, run in /env/nsd_attack_home :
      ```bash
      nsd -c nsd.conf -d -f nsd.db
      ```

7. **replicate resolver queries flooding test**, 

   - open termainal and run:
      ```bash
      resperf -d /env/reproduction/Attack_domains.txt -s 127.0.0.1 -v -m 10000 -C 1000 -q 640000 -r 0 -c 100 -R
      ```
   - open another terminal and run:
      ```bash
         resperf -d  /env/reproduction/Benign_domains.txt -s 127.0.0.1 -v -m 100 -C 1000 -q 640000 -r 0 -c 100 -R
      ```

## Requirements
- Docker








