"""Examples of set and dictionary syntax"""

pids: set[int] = {710000000, 712345678}
pids.add(730733853)

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

for key in ice_cream:
    print(key)
    print(ice_cream[key])
