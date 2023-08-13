import subprocess
import re

def traceroute_ping(destination, max_hops=64):
    prev_ip = None
    hop_count = 1
    while hop_count <= max_hops:
        ping_command = ["ping", "-c", "3", "-m", str(hop_count), destination]
        ping_output = subprocess.run(ping_command, capture_output=True, text=True).stdout

        match_ip = re.search(r'bytes from (\d+\.\d+\.\d+\.\d+)', ping_output)
        if match_ip:
            ip_addr = match_ip.group(1)

            if ip_addr == prev_ip:
                break

            p_command = ["ping", "-c", "3", ip_addr]
            p_output = subprocess.run(p_command, capture_output=True, text=True).stdout

            match_time = re.search(r'time=(\d+\.\d+) ms', p_output)
            response_time = match_time.group(1) if match_time else "***"

            print(f"Hop: {hop_count}, IP: {ip_addr}, Time: {response_time}")
            prev_ip = ip_addr
        else:
            print(f"Hop: {hop_count}, IP: *** Time: ***")

        hop_count += 1

def main():
    destination = input("Enter the destination address: ")
    traceroute_ping(destination)

if __name__ == "__main__":
    main()
