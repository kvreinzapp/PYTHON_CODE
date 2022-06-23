guest = ['MR.Du', 'MS.White', "MS.Lee", "MR.Klaus"]
invite_msg = "would you like to have a dinner with me?"
print(f"{guest[0]}, {invite_msg}")
print(f"{guest[1]}, {invite_msg}")
print(f"{guest[2]}, {invite_msg}")
print(f"{guest[3]}, {invite_msg}")

print(f"\nOops, {guest[2]} can not come in, maybe I can invite Zack wo here\n")
guest[2] = 'MR.Zack'
print(f"{guest[0]}, {invite_msg}")
print(f"{guest[1]}, {invite_msg}")
print(f"{guest[2]}, {invite_msg}")
print(f"{guest[3]}, {invite_msg}")
