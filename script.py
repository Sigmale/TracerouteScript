import subprocess
import re
def traceroute(destination, max_hops=64):
    prev_ip = None
    hop_count = 1
    while hop_count <= max_hops:
        ping_command = ["ping", "-c", "3", "-m", str(hop_count), destination]
        ping_output = subprocess.run(ping_command, capture_output=True, text=True).stdout

        ip_match = re.search(r'bytes from (\d+\.\d+\.\d+\.\d+)', ping_output)
        if ip_match:
            ip_address = ip_match.group(1)

            if ip_address == prev_ip:
                break
            ping_to_ip_command = ["ping", "-c", "3", ip_address]
            ping_to_ip_output = subprocess.run(ping_to_ip_command, capture_output=True, text=True).stdout
            time_match = re.search(r'time=(\d+\.\d+) ms', ping_to_ip_output)
            response_time = time_match.group(1) if time_match else "**"
            print(f"Hop: {hop_count}, IP: {ip_address}, Time: {response_time}")
            prev_ip = ip_address
        else:
            print(f"Hop: {hop_count}, IP: **, Time: **")

        hop_count += 1
def main():
    destination = input("Enter the destination address: ")
    traceroute(destination)
if __name__ == "__main__":
    main()
