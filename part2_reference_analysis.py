import json

with open("measurements.example.json", "r", encoding="utf-8") as f:
    data = json.load(f)

complaint = data["token_counts"]["complaint"]

en = complaint["en"]
ru = complaint["ru"]
kk = complaint["kk"]

print("PART 2 — REFERENCE MEASUREMENT")
print("Classroom API key was unavailable.")
print("Using instructor-provided measurements.example.json.")
print()

print("Complaint token counts:")
print(f"EN = {en}")
print(f"RU = {ru}")
print(f"KK = {kk}")
print()

print("Measured reference ratios:")
print(f"RU / EN = {ru / en:.2f}x")
print(f"KK / EN = {kk / en:.2f}x")
