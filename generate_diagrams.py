import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as FancyArrowPatch
import japanize_matplotlib
import numpy as np
import os

os.makedirs("diagrams", exist_ok=True)

# カラーパレット
PRIMARY   = "#2D6A4F"
SECONDARY = "#52B788"
ACCENT    = "#F4A261"
LIGHT     = "#D8F3DC"
DARK      = "#1B4332"
BG        = "#F8F9FA"
WHITE     = "#FFFFFF"
GRAY      = "#6C757D"

# ==========================================
# 図1: 4周イメージ学習法
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis("off")

# タイトル
ax.text(5, 7.4, "4周イメージ学習法", fontsize=22, fontweight="bold",
        ha="center", va="center", color=DARK)
ax.text(5, 6.9, "かかる時間は加速度的に短くなる", fontsize=12,
        ha="center", va="center", color=GRAY)

# 階段データ
steps = [
    (1.0, 1.0, "1周目", "理解度 約3割", "わからなくて当然\n止まらず進む", "#B7E4C7"),
    (3.0, 2.2, "2周目", "理解度 約5割", "「聞いたことある」\nが増える", "#74C69D"),
    (5.0, 3.6, "3周目", "理解度 約7割", "イメージが\n像を結ぶ", "#40916C"),
    (7.0, 5.2, "4周目", "理解度 約9割 ★", "「なぜ？」が見える\n本質理解へ", "#1B4332"),
]

for x, y, label, pct, desc, color in steps:
    # ボックス
    rect = mpatches.FancyBboxPatch((x - 0.9, y - 0.5), 1.8, 1.1,
                                    boxstyle="round,pad=0.1",
                                    facecolor=color, edgecolor=WHITE,
                                    linewidth=2, zorder=3)
    ax.add_patch(rect)
    txt_color = WHITE if color in ["#40916C", "#1B4332"] else DARK
    ax.text(x, y + 0.15, label, fontsize=13, fontweight="bold",
            ha="center", va="center", color=txt_color, zorder=4)
    ax.text(x, y - 0.2, pct, fontsize=9,
            ha="center", va="center", color=txt_color, zorder=4)
    ax.text(x, y - 1.1, desc, fontsize=8.5, ha="center", va="center",
            color=GRAY, linespacing=1.5)

# 矢印
for i in range(len(steps) - 1):
    x1 = steps[i][0] + 0.9
    y1 = steps[i][1] + 0.05
    x2 = steps[i+1][0] - 0.9
    y2 = steps[i+1][1] + 0.05
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=SECONDARY,
                                lw=2.5, connectionstyle="arc3,rad=0.0"))

# 最終ゴール
rect_goal = mpatches.FancyBboxPatch((8.0, 5.2 - 0.5 + 0.3), 1.7, 0.7,
                                     boxstyle="round,pad=0.1",
                                     facecolor=ACCENT, edgecolor=WHITE,
                                     linewidth=2, zorder=3)
ax.add_patch(rect_goal)
ax.annotate("", xy=(8.05, 5.55), xytext=(7.9, 5.55),
            arrowprops=dict(arrowstyle="->", color=ACCENT, lw=2.5))
ax.text(8.85, 5.55, "○×・模試\n実戦力へ", fontsize=9, fontweight="bold",
        ha="center", va="center", color=WHITE, zorder=4)

plt.tight_layout()
plt.savefig("diagrams/fig1_4round.png", dpi=150, bbox_inches="tight",
            facecolor=BG)
plt.close()
print("✅ fig1_4round.png 生成完了")


# ==========================================
# 図2: スポーツ・仕事・資格の共通構造
# ==========================================
fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(5.5, 5.6, "3つの領域、1つの哲学", fontsize=22, fontweight="bold",
        ha="center", color=DARK)

columns = [
    (1.5,  "スポーツ",    PRIMARY,   ["毎日の振り返りノート", "1000回の反復練習", "フォームの修正"],  "インカレ出場"),
    (5.5,  "仕事・AI",    "#E76F51",  ["YouTube で事前研究", "1日単位でテスト", "失敗→改善を繰り返す"], "残業200時間削減"),
    (9.5,  "資格勉強",    SECONDARY,  ["YouTube 予習で地図作り", "4周イメージ学習法", "耳学習・シャドーイング"], "3資格取得"),
]

for cx, title, color, items, result in columns:
    # ヘッダー
    rect = mpatches.FancyBboxPatch((cx - 1.5, 3.6), 3.0, 1.0,
                                    boxstyle="round,pad=0.15",
                                    facecolor=color, edgecolor=WHITE, linewidth=2)
    ax.add_patch(rect)
    ax.text(cx, 4.1, title, fontsize=13, fontweight="bold",
            ha="center", va="center", color=WHITE)

    # 内容
    for i, item in enumerate(items):
        y_pos = 3.0 - i * 0.55
        ax.plot(cx - 1.2, y_pos, "o", color=color, markersize=5)
        ax.text(cx - 1.0, y_pos, item, fontsize=9.5,
                va="center", color=DARK)

    # 矢印
    ax.annotate("", xy=(cx, 0.85), xytext=(cx, 1.15),
                arrowprops=dict(arrowstyle="->", color=color, lw=2))

    # 結果
    rect_r = mpatches.FancyBboxPatch((cx - 1.4, 0.3), 2.8, 0.55,
                                      boxstyle="round,pad=0.1",
                                      facecolor=LIGHT, edgecolor=color, linewidth=2)
    ax.add_patch(rect_r)
    ax.text(cx, 0.58, result, fontsize=10, fontweight="bold",
            ha="center", va="center", color=color)

# 中央の共通哲学ラベル
for x in [3.5, 7.5]:
    ax.text(x, 2.1, "＝", fontsize=20, ha="center", va="center", color=GRAY)

ax.text(5.5, 0.05, "共通する哲学：「小さく・繰り返す・続ける」",
        fontsize=11, ha="center", va="center", color=GRAY,
        style="italic")

plt.tight_layout()
plt.savefig("diagrams/fig2_common_structure.png", dpi=150, bbox_inches="tight",
            facecolor=BG)
plt.close()
print("✅ fig2_common_structure.png 生成完了")


# ==========================================
# 図3: 資格マップ（複利）
# ==========================================
fig, ax = plt.subplots(figsize=(9, 7))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-5, 5)
ax.set_ylim(-4.5, 4.5)
ax.axis("off")

ax.text(0, 4.1, "資格の複利マップ", fontsize=22, fontweight="bold",
        ha="center", color=DARK)
ax.text(0, 3.5, "宅建を起点に、知識が四方へ広がる", fontsize=11,
        ha="center", color=GRAY)

# 中心: 宅建士
center = plt.Circle((0, 0), 1.0, color=PRIMARY, zorder=3)
ax.add_patch(center)
ax.text(0, 0.15, "宅建士", fontsize=16, fontweight="bold",
        ha="center", va="center", color=WHITE, zorder=4)
ax.text(0, -0.35, "起点", fontsize=10,
        ha="center", va="center", color=LIGHT, zorder=4)

# 周辺資格
nodes = [
    ( 0,    3.0,  "FP2級",          SECONDARY, "不動産・税が重なる\n▶ 約100時間短縮"),
    ( 3.2,  0,    "TOEIC",          "#E76F51",  "不動産英語・\n外国人対応力"),
    ( 0,   -3.0,  "マンション\n管理士", "#9B5DE5", "管理業務主任者\nとセット取得"),
    (-3.2,  0,    "行政書士",        "#F4A261",  "法律思考の\n土台が活きる"),
]

for nx, ny, name, color, desc in nodes:
    # 接続線
    angle = np.arctan2(ny, nx)
    sx = np.cos(angle) * 1.05
    sy = np.sin(angle) * 1.05
    ex = nx - np.cos(angle) * 0.85
    ey = ny - np.sin(angle) * 0.85
    ax.annotate("", xy=(ex, ey), xytext=(sx, sy),
                arrowprops=dict(arrowstyle="->", color=color,
                                lw=2, linestyle="dashed"))

    # ノード
    circ = plt.Circle((nx, ny), 0.82, color=color, zorder=3, alpha=0.9)
    ax.add_patch(circ)
    lines = name.split("\n")
    for i, line in enumerate(lines):
        offset = 0.15 if len(lines) > 1 else 0
        ax.text(nx, ny + offset - i * 0.32, line, fontsize=12,
                fontweight="bold", ha="center", va="center",
                color=WHITE, zorder=4)

    # 説明
    desc_x = nx * 1.55
    desc_y = ny * 1.45
    ax.text(desc_x, desc_y, desc, fontsize=8.5, ha="center",
            va="center", color=GRAY, linespacing=1.5)

# 縦展開の矢印 (FP2→FP1)
ax.annotate("", xy=(1.2, 3.5), xytext=(0.6, 3.1),
            arrowprops=dict(arrowstyle="->", color="#888", lw=1.5))
ax.text(2.0, 3.6, "FP1級へ\n（縦展開）", fontsize=8.5,
        ha="center", color=GRAY)

plt.tight_layout()
plt.savefig("diagrams/fig3_license_map.png", dpi=150, bbox_inches="tight",
            facecolor=BG)
plt.close()
print("✅ fig3_license_map.png 生成完了")


# ==========================================
# 図4: 3つの哲学
# ==========================================
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

ax.text(5, 4.6, "私の3つの哲学", fontsize=22, fontweight="bold",
        ha="center", color=DARK)

philosophies = [
    (1.5, "① すぐやる",    PRIMARY,  "いまやってもあとでやっても\n評価が変わらないものは、すぐやる。", "先延ばしゼロ"),
    (5.0, "② 5分始める",  SECONDARY, "ここで5分取り掛かれないものは\n頑張っても終わらせられない。",    "完璧主義ゼロ"),
    (8.5, "③ 回数を信じる", ACCENT,   "続けることを決めたなら\n意味を求めるな。回数を信じろ。",     "継続が発見を生む"),
]

for cx, title, color, body, tag in philosophies:
    # カード背景
    rect = mpatches.FancyBboxPatch((cx - 1.55, 0.5), 3.1, 3.4,
                                    boxstyle="round,pad=0.2",
                                    facecolor=WHITE, edgecolor=color,
                                    linewidth=3, zorder=2)
    ax.add_patch(rect)

    # タイトルバー
    rect_top = mpatches.FancyBboxPatch((cx - 1.55, 3.2), 3.1, 0.7,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, edgecolor=color,
                                        linewidth=0, zorder=3)
    ax.add_patch(rect_top)
    ax.text(cx, 3.55, title, fontsize=13, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=4)

    # 本文
    ax.text(cx, 2.3, body, fontsize=9.5, ha="center", va="center",
            color=DARK, linespacing=1.7, zorder=3)

    # タグ
    rect_tag = mpatches.FancyBboxPatch((cx - 1.1, 0.6), 2.2, 0.5,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, edgecolor=color,
                                        linewidth=0, alpha=0.15, zorder=3)
    ax.add_patch(rect_tag)
    ax.text(cx, 0.85, tag, fontsize=9.5, fontweight="bold",
            ha="center", va="center", color=color, zorder=4)

# カード間の矢印
for x in [3.1, 6.6]:
    ax.annotate("", xy=(x + 0.25, 2.2), xytext=(x - 0.25, 2.2),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=2))

plt.tight_layout()
plt.savefig("diagrams/fig4_philosophy.png", dpi=150, bbox_inches="tight",
            facecolor=BG)
plt.close()
print("✅ fig4_philosophy.png 生成完了")

print("\n🎉 全4枚の図解を diagrams/ フォルダに生成しました！")
