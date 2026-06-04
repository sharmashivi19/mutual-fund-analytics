import matplotlib.pyplot as plt


def state_sip(tx):

    sip = tx[
        tx["transaction_type"]=="SIP"
    ]

    state = (
        sip.groupby("state")
        ["amount_inr"]
        .sum()
        .sort_values()
    )

    plt.figure(figsize=(10,8))

    state.plot(
        kind="barh"
    )

    plt.savefig(
        "../reports/charts/state_sip.png"
    )
def city_tier(tx):

      tier = tx["city_tier"].value_counts()

      plt.figure(figsize=(8,8))

      plt.pie(tier,
        labels=tier.index,
        autopct="%1.1f%%" )

      plt.savefig(
         "../reports/charts/city_tier.png"
    )