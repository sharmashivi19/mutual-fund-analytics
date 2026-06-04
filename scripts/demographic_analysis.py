import matplotlib.pyplot as plt
import seaborn as sns


def age_distribution(tx):

    age = (
        tx["age_group"]
        .value_counts()
    )

    plt.figure(figsize=(8,8))

    plt.pie(
        age,
        labels=age.index,
        autopct="%1.1f%%"
    )

    plt.savefig(
        "../reports/charts/age_distribution.png"
    )
def sip_boxplot(tx):

      sip = tx[
          tx["transaction_type"]=="SIP"]

      plt.figure(figsize=(10,6))

      sns.boxplot(
        data=sip,
        x="age_group",
        y="amount_inr")

      plt.savefig(
        "../reports/charts/sip_boxplot.png")
    
def gender_split(tx):

       gender = tx["gender"].value_counts()

       plt.figure(figsize=(8,8))

       plt.pie(
        gender,
        labels=gender.index,
        autopct="%1.1f%%"
    )

       plt.savefig(
        "../reports/charts/gender_split.png"
    )