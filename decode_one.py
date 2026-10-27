line = "(1698400000.000000) can0 0CF00400#FFFFFF502DFFFFFF"

parts = line.split()
can_id, data_hex = parts[2].split("#")
data = bytes.fromhex(data_hex)

raw = data[3] + data[4] * 256
rpm = raw * 0.125

print("ID:", can_id)
print("Bytes:", list(data))
print("Raw:", raw)
print("Engine speed:", rpm, "rpm")
