def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbolds = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbolds:
        for uninterupted_match_length in range(10,5,-1):
            winning_symbol_repetition = current_winning_symbol * uninterupted_match_length
            if (winning_symbol_repetition in left_part
                    and winning_symbol_repetition in right_part):
                if uninterupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterupted_match_length}{current_winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterupted_match_length}{current_winning_symbol}'
    return f'ticket "{ticket}" - no match'




tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))
