import random

# possible CAN IDs and data patterns
can_ids = ["123", "321", "456", "789"]
data_samples = ["11223344", "AABBCCDD", "55667788", "99AA77CC"]

# open a file to write logs
with open("sample_can.log", "w") as f:
    timestamp = 0.0
    for i in range(20):  # generate 20 messages
        # increment timestamp randomly
        timestamp += round(random.uniform(0.0001, 0.001), 6)
        can_id = random.choice(can_ids)
        data = random.choice(data_samples)
        f.write(f"{timestamp:.6f} 1 {can_id}#{data}\n")

print("✅ sample_can.log created successfully!")