import matplotlib.pyplot as plt

data = [
    {
        "test_accuracy": 89.38271604938272,
        "test_precision": 0.9322033898305084,
        "test_recall": 0.8480176211453745,
        "F_score": 0.8881199538638985,
        "mse_loss": 0.27085084801596215,
        "ce_loss": 0.2956534036628003,
    },
    {
        "test_accuracy": 88.58024691358025,
        "test_precision": 0.927536231884058,
        "test_recall": 0.8458149779735683,
        "F_score": 0.8847926267281105,
        "mse_loss": 0.24073407271396077,
        "ce_loss": 0.303899966560956,
    },
    {
        "test_accuracy": 88.20987654320987,
        "test_precision": 0.9245283018867925,
        "test_recall": 0.8634361233480177,
        "F_score": 0.8929384965831435,
        "mse_loss": 0.22406025855943495,
        "ce_loss": 0.3014544171226984,
    },
    {
        "test_accuracy": 88.95061728395062,
        "test_precision": 0.9290780141843972,
        "test_recall": 0.8656387665198237,
        "F_score": 0.8962371721778791,
        "mse_loss": 0.21443953390152826,
        "ce_loss": 0.29426012683003416,
    },
    {
        "test_accuracy": 89.25925925925927,
        "test_precision": 0.9334916864608076,
        "test_recall": 0.8656387665198237,
        "F_score": 0.8982857142857142,
        "mse_loss": 0.23561281538173495,
        "ce_loss": 0.29387918306709326,
    },
    {
        "test_accuracy": 89.19753086419753,
        "test_precision": 0.9290780141843972,
        "test_recall": 0.8656387665198237,
        "F_score": 0.8962371721778791,
        "mse_loss": 0.2223810931143396,
        "ce_loss": 0.29429703659491785,
    },
    {
        "test_accuracy": 89.81481481481481,
        "test_precision": 0.9292452830188679,
        "test_recall": 0.8678414096916299,
        "F_score": 0.89749430523918,
        "mse_loss": 0.2044824636242505,
        "ce_loss": 0.29091142363967254,
    },
    {
        "test_accuracy": 89.01234567901236,
        "test_precision": 0.9354066985645934,
        "test_recall": 0.8612334801762115,
        "F_score": 0.8967889908256881,
        "mse_loss": 0.18775352775773202,
        "ce_loss": 0.29279772178288743,
    },
    {
        "test_accuracy": 89.44444444444444,
        "test_precision": 0.9304556354916067,
        "test_recall": 0.8546255506607929,
        "F_score": 0.8909299655568311,
        "mse_loss": 0.1976137332660775,
        "ce_loss": 0.2926681158682634,
    },
    {
        "test_accuracy": 89.62962962962962,
        "test_precision": 0.9371980676328503,
        "test_recall": 0.8546255506607929,
        "F_score": 0.8940092165898618,
        "mse_loss": 0.17108777161329194,
        "ce_loss": 0.2885570568481537,
    },
]

n = len(data)

plt.plot(
    list(range(3, 2 * n + 1, 2)),
    [d["test_accuracy"] / 100 for d in data[1:]],
    label="accuracy",
)
plt.plot(
    list(range(3, 2 * n + 1, 2)), [d["test_precision"] for d in data[1:]], label="precision"
)
plt.plot(list(range(3, 2 * n + 1, 2)), [d["test_recall"] for d in data[1:]], label="recall")
plt.plot(list(range(3, 2 * n + 1, 2)), [d["F_score"] for d in data[1:]], label="F_score")
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()

plt.plot(list(range(3, 2 * n + 1, 2)), [d["mse_loss"] for d in data[1:]], label="mse_loss")
plt.plot(list(range(3, 2 * n + 1, 2)), [d["ce_loss"] for d in data[1:]], label="ce_loss")
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()
