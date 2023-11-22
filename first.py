import threading
import subprocess

def issue_ping(ip_addr, count=5):
    print("Ping: " + ip_addr + " with count: " + str(count))
    output = subprocess.check_output("ping -c " + str(count) + " " + ip_addr, shell=True)
    print(output.decode('utf-8'))

def main():
    threads = []
    iplist = [('8.8.8.8',20),('9.9.9.9',10)]
    for ip in iplist:
        threads.append(threading.Thread(target=issue_ping, args=(ip[0], ip[1])))
        threads[-1].daemon = True
        threads[-1].start()
        
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()