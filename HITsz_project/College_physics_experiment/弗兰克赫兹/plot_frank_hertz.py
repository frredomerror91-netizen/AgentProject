from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib"))

import matplotlib
import pandas as pd


matplotlib.use("Agg")
import matplotlib.pyplot as plt
INPUT_FILE = BASE_DIR / "弗兰克赫兹实验_原始数据.xlsx"
OUTPUT_FILE = BASE_DIR / "弗兰克赫兹实验_I-U曲线.png"


def main() -> None:
    data = pd.read_excel(INPUT_FILE, sheet_name="原始数据")

    # Use a Chinese-capable font when available on Windows; fall back gracefully.
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=160)
    ax.plot(
        data["U_G2K / V"],
        data["I_A1 / nA"],
        color="#1769AA",
        linewidth=1.8,
        marker="o",
        markersize=2.5,
        markevery=2,
        label="I_A1",
    )
    ax.plot(
        data["U_G2K / V"],
        data["I_A2 / nA"],
        color="#D55E00",
        linewidth=1.8,
        marker="s",
        markersize=2.5,
        markevery=2,
        label="I_A2",
    )

    ax.set_title("弗兰克-赫兹实验 I-U 曲线", fontsize=15, pad=12)
    ax.set_xlabel("加速电压 U_G2K / V", fontsize=11)
    ax.set_ylabel("电流 I / nA", fontsize=11)
    ax.set_xlim(0, 90.5)
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.35)
    ax.legend(frameon=False, loc="best")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUTPUT_FILE, bbox_inches="tight")
    print(f"saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
