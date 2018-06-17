def k_factor(s: float, c: float) -> int:
    """
    K-factor calculation

    :param s: number of shares sent by each user
    :param c: percent conversion of each invite
    :return:
    """
    k = s * c

    return k


def shares_cr(s: int, c: int) -> float:
    """
    Shares Conversion Rate

    :param s: total shares sent
    :param c: total conversions
    :return:
    """
    cr = c / s

    return cr


def shares_per_user(tu: int, ts: int) -> float:
    """
    Returns shares per user
    :param tu: total users
    :param ts: total shares
    :return:
    """
    spu = ts / tu

    return spu


def is_ad_working(ts: int, tc: int, tu: int):
    """
    Based on your K-factor, it will tell you if your creative is working

    :param ts: total shares sent
    :param tc: total conversions
    :param tu: total users
    :return: mixed
    """
    cr = shares_cr(ts, tc)
    spu = shares_per_user(tu, ts)
    k = k_factor(spu, cr)

    if k < 1:
        return False

    return True, spu, k, cr


if __name__ == '__main__':
    # you can get this data at ad level for a given time range
    users = 100  # paid clicks
    shares_sent = 500  # how many times your link was shared
    conversions = 150  # acquired customers from shares

    # K-factor calculation
    is_working, spu, k, cr = is_ad_working(shares_sent, conversions, users)

    # status
    print("")
    print("Total users (paid clicks): {}".format(users))
    print("Total shares generated: {}".format(shares_sent))
    print("Avg. shares per user: {}".format(int(spu)))
    print("Total referred conversions: {}".format(conversions))
    print("Referred conversion rate: {}%".format(int(cr * 100)))
    print("K-factor: {}".format(k))
    print("")

    if is_working:
        print("Your ad is working! :)")
    else:
        print("Your ad is not working :(")
    print("")
