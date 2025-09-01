with open("sample_can.log") as file_object:
    for line in file_object:
        parts = line.strip().split()
        timestamp = parts[0]
        can_id, data = parts[2].split('#')
        print("Timestamp:", timestamp, "CAN ID:", can_id, "Data:", data)