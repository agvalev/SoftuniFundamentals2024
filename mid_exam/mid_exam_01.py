total_xp = 0
battle_count = 0
amaount_of_neded_xp = float(input())
battles_to_fight = int(input())
for battle in range(1, battles_to_fight + 1):
    battle_count += 1
    xp_player_achieve = float(input())
    if battle_count % 3 == 0:
        xp_player_achieve = (xp_player_achieve + (xp_player_achieve * 0.15))
    if battle_count % 5 == 0:
        xp_player_achieve = (xp_player_achieve - (xp_player_achieve * 0.10))
    if battle_count % 15 == 0:
        xp_player_achieve = (xp_player_achieve + (xp_player_achieve * 0.05))
    total_xp += xp_player_achieve
    if total_xp >= amaount_of_neded_xp:
        break
result = abs(total_xp - amaount_of_neded_xp)
if total_xp >= amaount_of_neded_xp:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {result:.2f} more needed.")

