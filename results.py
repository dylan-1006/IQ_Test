def score_to_iq(score):
    iq = (score * 2.644) + 46.221

    if iq > 144:
        iq = 144

    return round(iq)


def iq_percentile(iq):
    if iq >= 132:
        return '99th'

    elif 125 <= iq < 132:
        return '95th to 98th'

    elif 119 <= iq < 125:
        return '90th to 95th'

    elif 112 <= iq < 119:
        return '80th to 90th'

    elif 104 <= iq < 112:
        return '60th to 79th'

    elif 96 <= iq < 104:
        return '40th to 60th'

    elif 87 <= iq < 96:
        return '20th to 40th'

    elif 81 <= iq < 87:
        return '10th to 20th'

    else:
        return '0th to 9th'
