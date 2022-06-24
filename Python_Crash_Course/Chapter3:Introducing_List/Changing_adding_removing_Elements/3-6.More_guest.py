guest = ['MR.Du', 'MS.White', "MS.Lee", "MR.Klaus"]
invite_msg = "would you like to have a dinner with me?"
print("[Invite who:]")
print(guest)
print(f"{guest[0]}, {invite_msg}")
print(f"{guest[1]}, {invite_msg}")
print(f"{guest[2]}, {invite_msg}")
print(f"{guest[3]}, {invite_msg}")

print(
    f"\n[!]Oops, {guest[2]} can not come in, maybe I can invite Zack wo here\n")
guest[2] = 'MR.Zack'
print(guest)
print("[Inviration message:]")
print(f"{guest[0]}, {invite_msg}")
print(f"{guest[1]}, {invite_msg}")
print(f"{guest[2]}, {invite_msg}")
print(f"{guest[3]}, {invite_msg}")

print("\n[!]Guys I found a bigger table, we can have three more person!\n")
guest.insert(0, 'Joey')
print(guest)
guest.insert(2, 'Ross')
print(guest)
guest.insert(6, 'Chandler')
print(guest)
print("[Inviration message:]")
print(f"{guest[0]}, {invite_msg}")
print(f"{guest[1]}, {invite_msg}")
print(f"{guest[2]}, {invite_msg}")
print(f"{guest[3]}, {invite_msg}")
print(f"{guest[4]}, {invite_msg}")
print(f"{guest[5]}, {invite_msg}")
print(f"{guest[6]}, {invite_msg}")
