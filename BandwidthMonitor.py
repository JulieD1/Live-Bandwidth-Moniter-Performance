import time  
import psutil  

# Get the initial bytes received and sent
initial_bytes_received = psutil.net_io_counters().bytes_recv
initial_bytes_sent = psutil.net_io_counters().bytes_sent

# Calculate the initial total bytes
initial_total_bytes = initial_bytes_received + initial_bytes_sent

# Get the initial time
initial_time = time.time()

while True:
    # Get the current bytes received and sent
    current_bytes_received = psutil.net_io_counters().bytes_recv
    current_bytes_sent = psutil.net_io_counters().bytes_sent

    # Calculate the current total bytes
    current_total_bytes = current_bytes_received + current_bytes_sent

    # Get the current packets sent and received
    current_packets_sent = psutil.net_io_counters().packets_sent
    current_packets_received = psutil.net_io_counters().packets_recv

    # Calculate the elapsed time since the start of monitoring
    elapsed_time = time.time() - initial_time


    # Convert bytes to Kilobytes
    kb_new_received = (current_bytes_received - initial_bytes_received) / 1024 
    kb_new_sent = (current_bytes_sent - initial_bytes_sent) / 1024
    kb_new_total = (current_total_bytes - initial_total_bytes) / 1024 

    # Calculate the network performance metrics
    throughput = (current_total_bytes - initial_total_bytes) / 1024 / elapsed_time  # Kilobytes per second
    latency = elapsed_time / (current_total_bytes / 1024)  # Seconds per kilobyte
    
    if current_packets_sent != 0:
        packet_loss = ((current_packets_sent - current_packets_received)/ current_bytes_sent) * 100
    else: 
        packet_loss = 0 # To avoid dividing by zero
    

    # Print the network traffic information
    print(f"{kb_new_received:.2f} KB received, {kb_new_sent:.2f} KB sent, {kb_new_total:.2f} KB total")
    print(f"Throughput: {throughput:.2f} KB/s, Latency: {latency: .6f}, Packet Loss Percentage: {packet_loss:.2f}%")

    # Update the 'initial' variables for the next iteration
    initial_bytes_received = current_bytes_received
    initial_bytes_sent = current_bytes_sent
    initial_total_bytes = current_total_bytes

    # Wait for 1 second before the next check
    time.sleep(1)
