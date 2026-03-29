# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import japanize_matplotlib
import numpy as np
import os

os.makedirs("diagrams", exist_ok=True)

# ─── カラーパレット ───────────────────────────────────────
C1  = "#FF6B6B"   # 赤・情熱
C2  = "#4ECDC4"   # ターコイズ
C3  = "#FFE66D"   # 黄・アクセント
C4  = "#2C3E50"   # ダーク
C5  = "#A8E6CF"   # ミントグリーン
C6  = "#FF8B94"   # ピンク
C7  = "#6C5CE7"   # パープル
BG1 = "#FAFAFA"
BG2 = "#F0F4FF"
WHITE = "#FFFFFF"

# ─── アニメキャラ描画関数 ─────────────────────────────────
def draw_anime_character(ax, cx, cy, scale=1.0, color="#FFB6C1",
                          hair_color="#4A4A4A", expression="normal",
                          direction="right"):
    """シンプルなアニメ風キャラクターをmatplotlibで描画"""
    s = scale

    # --- 髪（後ろ）
    hair_back = patches.Ellipse((cx, cy + 0.32*s), 0.38*s, 0.22*s,
                                  facecolor=hair_color, zorder=3)
    ax.add_patch(hair_back)

    # --- 首
    neck = patches.Rectangle((cx - 0.05*s, cy - 0.1*s), 0.10*s, 0.15*s,
                               facecolor=color, zorder=4)
    ax.add_patch(neck)

    # --- 体
    body = patches.FancyBboxPatch((cx - 0.22*s, cy - 0.55*s), 0.44*s, 0.45*s,
                                   boxstyle="round,pad=0.04",
                                   facecolor=C2 if direction=="right" else C7,
                                   edgecolor=C4, linewidth=1.2*s, zorder=4)
    ax.add_patch(body)

    # --- 腕（左）
    arm_l = patches.FancyBboxPatch((cx - 0.36*s, cy - 0.52*s), 0.14*s, 0.32*s,
                                    boxstyle="round,pad=0.03",
                                    facecolor=color, edgecolor=C4,
                                    linewidth=0.8*s, zorder=3)
    ax.add_patch(arm_l)

    # --- 腕（右）
    arm_r = patches.FancyBboxPatch((cx + 0.22*s, cy - 0.52*s), 0.14*s, 0.32*s,
                                    boxstyle="round,pad=0.03",
                                    facecolor=color, edgecolor=C4,
                                    linewidth=0.8*s, zorder=3)
    ax.add_patch(arm_r)

    # --- 顔
    face = patches.Ellipse((cx, cy + 0.12*s), 0.34*s, 0.38*s,
                             facecolor=color, edgecolor=C4,
                             linewidth=1.2*s, zorder=5)
    ax.add_patch(face)

    # --- 髪（前・バング）
    for dx in [-0.10, 0.0, 0.10]:
        bang = patches.FancyBboxPatch((cx + dx*s - 0.06*s, cy + 0.28*s),
                                       0.13*s, 0.16*s,
                                       boxstyle="round,pad=0.02",
                                       facecolor=hair_color, zorder=6)
        ax.add_patch(bang)
    hair_top = patches.Ellipse((cx, cy + 0.42*s), 0.36*s, 0.18*s,
                                 facecolor=hair_color, zorder=6)
    ax.add_patch(hair_top)

    # --- 目
    eye_y = cy + 0.12*s
    for ex in [cx - 0.08*s, cx + 0.08*s]:
        white_eye = patches.Ellipse((ex, eye_y), 0.07*s, 0.08*s,
                                     facecolor=WHITE, zorder=7)
        ax.add_patch(white_eye)
        iris = patches.Ellipse((ex, eye_y - 0.01*s), 0.045*s, 0.055*s,
                                facecolor=C7 if direction=="right" else C1,
                                zorder=8)
        ax.add_patch(iris)
        pupil = patches.Ellipse((ex, eye_y - 0.01*s), 0.02*s, 0.025*s,
                                 facecolor=C4, zorder=9)
        ax.add_patch(pupil)
        # ハイライト
        hl = patches.Ellipse((ex + 0.01*s, eye_y + 0.01*s), 0.012*s, 0.012*s,
                               facecolor=WHITE, zorder=10)
        ax.add_patch(hl)

    # --- 表情
    if expression == "smile":
        theta = np.linspace(np.pi + 0.3, 2*np.pi - 0.3, 30)
        mx = cx + 0.04*s * np.cos(theta)
        my = (cy + 0.00*s) + 0.03*s * np.sin(theta)
        ax.plot(mx, my, color=C1, linewidth=1.5*s, zorder=9)
    elif expression == "excited":
        theta = np.linspace(np.pi + 0.2, 2*np.pi - 0.2, 30)
        mx = cx + 0.06*s * np.cos(theta)
        my = (cy - 0.01*s) + 0.04*s * np.sin(theta)
        ax.plot(mx, my, color=C1, linewidth=2.0*s, zorder=9)
    else:
        ax.plot([cx - 0.04*s, cx + 0.04*s], [cy + 0.00*s, cy + 0.00*s],
                color=C4, linewidth=1.2*s, zorder=9)

    # --- 眉毛
    brow_y = cy + 0.21*s
    for bx in [cx - 0.08*s, cx + 0.08*s]:
        ax.plot([bx - 0.04*s, bx + 0.04*s],
                [brow_y + (0.01*s if expression=="excited" else 0),
                 brow_y],
                color=hair_color, linewidth=2.0*s, zorder=9,
                solid_capstyle="round")

    # --- 脚
    for lx in [cx - 0.10*s, cx + 0.10*s]:
        leg = patches.FancyBboxPatch((lx - 0.07*s, cy - 0.82*s), 0.14*s, 0.28*s,
                                      boxstyle="round,pad=0.02",
                                      facecolor=C4, edgecolor=C4,
                                      linewidth=0.5, zorder=4)
        ax.add_patch(leg)
        shoe = patches.Ellipse((lx, cy - 0.82*s), 0.17*s, 0.08*s,
                                facecolor=C4, zorder=5)
        ax.add_patch(shoe)


def add_speech_bubble(ax, cx, cy, text, tail_dir="left", color=WHITE,
                       border=C4, fontsize=9, width=1.8, height=0.55):
    """吹き出しを描画"""
    rect = patches.FancyBboxPatch((cx - width/2, cy - height/2),
                                   width, height,
                                   boxstyle="round,pad=0.12",
                                   facecolor=color, edgecolor=border,
                                   linewidth=1.5, zorder=12)
    ax.add_patch(rect)
    # しっぽ
    if tail_dir == "left":
        tail = plt.Polygon([[cx - width/2 + 0.1, cy - height/2 + 0.05],
                             [cx - width/2 - 0.2, cy - height/2 - 0.15],
                             [cx - width/2 + 0.3, cy - height/2 + 0.05]],
                            facecolor=color, edgecolor=border, linewidth=1.5,
                            zorder=11)
    else:
        tail = plt.Polygon([[cx + width/2 - 0.1, cy - height/2 + 0.05],
                             [cx + width/2 + 0.2, cy - height/2 - 0.15],
                             [cx + width/2 - 0.3, cy - height/2 + 0.05]],
                            facecolor=color, edgecolor=border, linewidth=1.5,
                            zorder=11)
    ax.add_patch(tail)
    ax.text(cx, cy, text, fontsize=fontsize, ha="center", va="center",
            color=C4, fontweight="bold", zorder=13, linespacing=1.5)


# ══════════════════════════════════════════════════════════════
#  図1: 4周イメージ学習法（雑誌風）
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor(BG2)
ax.set_facecolor(BG2)
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

# 背景装飾
for i, (x, y, r, alpha) in enumerate([
        (1, 7, 1.2, 0.07), (11, 0.5, 0.9, 0.06), (0.5, 1, 0.7, 0.05)]):
    circ = plt.Circle((x, y), r, color=C7, alpha=alpha)
    ax.add_patch(circ)

# タイトル帯
title_bar = patches.FancyBboxPatch((0.3, 7.0), 11.4, 0.8,
                                    boxstyle="round,pad=0.1",
                                    facecolor=C4, zorder=2)
ax.add_patch(title_bar)
ax.text(6, 7.42, "4周イメージ学習法", fontsize=26, fontweight="bold",
        ha="center", va="center", color=WHITE, zorder=3,
        path_effects=[pe.withStroke(linewidth=3, foreground=C7)])
ax.text(6, 7.08, "〜 同じ教材を繰り返すだけで、景色が変わる 〜",
        fontsize=11, ha="center", va="center", color=C3, zorder=3)

# ステップカード
steps = [
    (1.4,  4.5, "1周目", "理解度\n約3割", "わからなくて\n当然！\n止まらず進もう", C1,   "#FFE5E5", "normal"),
    (3.85, 4.5, "2周目", "理解度\n約5割", "「聞いた\nことある！」\nが増えてくる",  C2,   "#E0FAF8", "smile"),
    (6.3,  4.5, "3周目", "理解度\n約7割", "全体像が\n頭の中で\n像を結ぶ！",      C7,   "#EDE9FF", "smile"),
    (8.75, 4.5, "4周目", "理解度\n約9割", "なぜ？が\n見える！\n本質理解へ★",    C4,   "#E8F4E8", "excited"),
]

for cx, cy, title, pct, bubble_text, color, bg, expr in steps:
    # カード
    card = patches.FancyBboxPatch((cx - 1.1, cy - 2.0), 2.2, 4.0,
                                   boxstyle="round,pad=0.15",
                                   facecolor=bg, edgecolor=color,
                                   linewidth=3, zorder=2)
    ax.add_patch(card)

    # ステップ番号バッジ
    badge = plt.Circle((cx, cy + 1.75), 0.35, facecolor=color,
                        edgecolor=WHITE, linewidth=2, zorder=4)
    ax.add_patch(badge)
    ax.text(cx, cy + 1.75, title[:1] + "周", fontsize=8, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=5)

    # タイトル
    ax.text(cx, cy + 1.2, title, fontsize=14, fontweight="bold",
            ha="center", va="center", color=color, zorder=3)

    # 理解度
    pct_bg = patches.FancyBboxPatch((cx - 0.75, cy + 0.55), 1.5, 0.55,
                                     boxstyle="round,pad=0.08",
                                     facecolor=color, zorder=3)
    ax.add_patch(pct_bg)
    ax.text(cx, cy + 0.82, pct, fontsize=11, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=4,
            linespacing=1.3)

    # キャラ
    draw_anime_character(ax, cx, cy - 0.5, scale=0.7,
                          color="#FFDAB9", hair_color=C4,
                          expression=expr,
                          direction="right" if cx < 7 else "left")

    # 吹き出し
    add_speech_bubble(ax, cx, cy - 1.55, bubble_text,
                       tail_dir="left" if cx < 7 else "right",
                       color=WHITE, border=color, fontsize=7.5,
                       width=1.95, height=0.72)

# 矢印
for i in range(len(steps) - 1):
    x1 = steps[i][0] + 1.1
    x2 = steps[i+1][0] - 1.1
    y  = 4.5 + 1.2
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="-|>",
                                color=C4, lw=2.5,
                                mutation_scale=18))

# ゴールバナー
goal = patches.FancyBboxPatch((10.0, 3.2), 1.7, 2.0,
                               boxstyle="round,pad=0.12",
                               facecolor=C3, edgecolor=C4,
                               linewidth=2.5, zorder=2)
ax.add_patch(goal)
ax.text(10.85, 4.6, "○×", fontsize=16, fontweight="bold",
        ha="center", va="center", color=C4, zorder=3)
ax.text(10.85, 4.2, "模試", fontsize=14, fontweight="bold",
        ha="center", va="center", color=C4, zorder=3)
ax.text(10.85, 3.75, "実戦力\nへ！", fontsize=10,
        ha="center", va="center", color=C4, zorder=3, linespacing=1.4)
ax.annotate("", xy=(10.05, 4.2), xytext=(9.85, 4.2),
            arrowprops=dict(arrowstyle="-|>", color=C4, lw=2.5,
                            mutation_scale=18))

# フッター
ax.text(6, 0.3, "1周目は3割でいい。続けるだけで、4周目に景色が変わる。",
        fontsize=11, ha="center", va="center", color=C4,
        fontweight="bold", style="italic")

plt.tight_layout(pad=0.5)
plt.savefig("diagrams/fig1_4round.png", dpi=180, bbox_inches="tight",
            facecolor=BG2)
plt.close()
print("fig1 完了")


# ══════════════════════════════════════════════════════════════
#  図2: 3つの領域・1つの哲学（雑誌風）
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor("#FFF9F0")
ax.set_facecolor("#FFF9F0")
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis("off")

# タイトル
title_bar = patches.FancyBboxPatch((0.3, 6.1), 12.4, 0.75,
                                    boxstyle="round,pad=0.1",
                                    facecolor=C4, zorder=2)
ax.add_patch(title_bar)
ax.text(6.5, 6.48, "3つの領域、1つの哲学",
        fontsize=24, fontweight="bold", ha="center", va="center",
        color=WHITE, zorder=3)
ax.text(6.5, 6.18, "スポーツ・仕事・資格勉強──すべて同じ構造だった",
        fontsize=10.5, ha="center", va="center", color=C3, zorder=3)

cols = [
    (2.0,  C1,  C6,   "スポーツ",
     ["毎日の振り返りノート", "1000回の反復練習", "フォームを修正し続ける"],
     "インカレ\n出場！", "excited", "#FF6B6B"),
    (6.5,  C7,  "#C5B8FF", "仕事・AI",
     ["YouTube で徹底的に予習", "1日単位でテスト・失敗", "改善を繰り返し3か月"],
     "残業200時間\n削減！", "smile", C7),
    (11.0, C2,  C5,   "資格勉強",
     ["YouTube 予習で地図作り", "4周イメージ学習法", "耳学習・シャドーイング"],
     "3資格\n取得！", "smile", C2),
]

for cx, color, bg, title, items, result, expr, badge_c in cols:
    # カード
    card = patches.FancyBboxPatch((cx - 1.7, 0.5), 3.4, 5.4,
                                   boxstyle="round,pad=0.18",
                                   facecolor=bg, edgecolor=color,
                                   linewidth=3, alpha=0.5, zorder=2)
    ax.add_patch(card)

    # ヘッダー
    hdr = patches.FancyBboxPatch((cx - 1.7, 5.1), 3.4, 0.8,
                                  boxstyle="round,pad=0.1",
                                  facecolor=color, zorder=3)
    ax.add_patch(hdr)
    ax.text(cx, 5.52, title, fontsize=15, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=4)

    # キャラ
    draw_anime_character(ax, cx, 3.9, scale=0.75,
                          color="#FFDAB9", hair_color=C4,
                          expression=expr, direction="right")

    # アイテムリスト
    for i, item in enumerate(items):
        iy = 2.85 - i * 0.52
        dot = plt.Circle((cx - 1.3, iy), 0.1, facecolor=color, zorder=4)
        ax.add_patch(dot)
        ax.text(cx - 1.1, iy, item, fontsize=9.5, va="center",
                color=C4, zorder=4)

    # 結果バッジ
    res_bg = patches.FancyBboxPatch((cx - 1.1, 0.55), 2.2, 0.75,
                                     boxstyle="round,pad=0.1",
                                     facecolor=color, zorder=4)
    ax.add_patch(res_bg)
    ax.text(cx, 0.93, result, fontsize=10, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=5,
            linespacing=1.3)

# = 記号
for x in [4.3, 8.8]:
    circ = plt.Circle((x, 3.2), 0.42, facecolor=C3, edgecolor=C4,
                       linewidth=2, zorder=5)
    ax.add_patch(circ)
    ax.text(x, 3.2, "＝", fontsize=18, fontweight="bold",
            ha="center", va="center", color=C4, zorder=6)

# 共通哲学フッター
phil = patches.FancyBboxPatch((1.5, 0.05), 10.0, 0.42,
                               boxstyle="round,pad=0.08",
                               facecolor=C4, zorder=3)
ax.add_patch(phil)
ax.text(6.5, 0.26, "共通する哲学：「小さく・繰り返す・続ける」",
        fontsize=12, fontweight="bold", ha="center", va="center",
        color=C3, zorder=4)

plt.tight_layout(pad=0.5)
plt.savefig("diagrams/fig2_common_structure.png", dpi=180,
            bbox_inches="tight", facecolor="#FFF9F0")
plt.close()
print("fig2 完了")


# ══════════════════════════════════════════════════════════════
#  図3: 資格の複利マップ（雑誌風）
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 9))
fig.patch.set_facecolor("#F0FFF4")
ax.set_facecolor("#F0FFF4")
ax.set_xlim(-6, 6)
ax.set_ylim(-5, 5.5)
ax.axis("off")

# タイトル
ax.text(0, 5.1, "資格の複利マップ", fontsize=26, fontweight="bold",
        ha="center", color=C4,
        path_effects=[pe.withStroke(linewidth=4, foreground=C5)])
ax.text(0, 4.6, "宅建士を起点に知識が四方へ広がる──学習コスト100時間超を削減",
        fontsize=10.5, ha="center", color="#555")

# 中心
center_glow = plt.Circle((0, 0), 1.5, color=C5, alpha=0.3, zorder=1)
ax.add_patch(center_glow)
center = plt.Circle((0, 0), 1.15, facecolor="#2D6A4F",
                     edgecolor=WHITE, linewidth=3, zorder=3)
ax.add_patch(center)
ax.text(0, 0.22, "宅建士", fontsize=18, fontweight="bold",
        ha="center", va="center", color=WHITE, zorder=4)
ax.text(0, -0.28, "起点", fontsize=11, ha="center",
        va="center", color=C5, zorder=4)

# キャラ（中心近く）
draw_anime_character(ax, -2.5, -3.8, scale=0.82,
                      color="#FFDAB9", hair_color=C4,
                      expression="excited", direction="right")
add_speech_bubble(ax, -1.0, -3.5, "複利で\n加速してる！",
                   tail_dir="right", color=C3, border=C4,
                   fontsize=9, width=1.8, height=0.65)

# 周辺ノード
nodes = [
    ( 0,    3.5, "FP2級",      C2,   "不動産・税が重なる\n▶ 約100時間短縮！"),
    ( 3.8,  0,   "TOEIC",     C1,   "不動産英語・\n外国人対応力UP"),
    ( 0,   -3.5, "マンション\n管理士", C7, "管理業務主任者と\nセット取得が王道"),
    (-3.8,  0,   "行政書士",  "#E67E22", "法律思考の\n土台が活きる"),
]

for nx, ny, name, color, desc in nodes:
    # 波線コネクタ
    t = np.linspace(0, 1, 60)
    angle = np.arctan2(ny, nx)
    dist = np.sqrt(nx**2 + ny**2)
    perp = np.array([-np.sin(angle), np.cos(angle)])
    wave = 0.18 * np.sin(t * np.pi * 4)
    lx = np.cos(angle) * (1.15 + t * (dist - 2.0)) + perp[0] * wave
    ly = np.sin(angle) * (1.15 + t * (dist - 2.0)) + perp[1] * wave
    ax.plot(lx, ly, color=color, lw=2.5, alpha=0.7,
            linestyle="--", zorder=2)
    ax.annotate("", xy=(nx * 0.52, ny * 0.52),
                xytext=(nx * 0.56, ny * 0.56),
                arrowprops=dict(arrowstyle="-|>", color=color,
                                lw=2, mutation_scale=16))

    # ノード
    glow = plt.Circle((nx, ny), 0.95, color=color, alpha=0.15, zorder=2)
    ax.add_patch(glow)
    circ = plt.Circle((nx, ny), 0.80, facecolor=color,
                       edgecolor=WHITE, linewidth=2.5, zorder=3)
    ax.add_patch(circ)
    for i, line in enumerate(name.split("\n")):
        offset = 0.17 if "\n" in name else 0
        ax.text(nx, ny + offset - i * 0.34, line,
                fontsize=12 if "\n" not in name else 10,
                fontweight="bold", ha="center", va="center",
                color=WHITE, zorder=4)

    # 説明
    desc_x = nx * 1.65
    desc_y = ny * 1.65
    desc_bg = patches.FancyBboxPatch(
        (desc_x - 1.25, desc_y - 0.42), 2.5, 0.84,
        boxstyle="round,pad=0.1",
        facecolor=WHITE, edgecolor=color, linewidth=2, zorder=5)
    ax.add_patch(desc_bg)
    ax.text(desc_x, desc_y, desc, fontsize=8.5, ha="center",
            va="center", color=C4, linespacing=1.5, zorder=6)

# FP1縦展開
ax.annotate("", xy=(0.8, 4.35), xytext=(0.35, 3.75),
            arrowprops=dict(arrowstyle="-|>", color="#888",
                            lw=2, mutation_scale=14))
fp1_bg = patches.FancyBboxPatch((0.7, 4.35), 1.9, 0.52,
                                  boxstyle="round,pad=0.08",
                                  facecolor="#888", zorder=5)
ax.add_patch(fp1_bg)
ax.text(1.65, 4.61, "FP1級へ（縦展開）", fontsize=9,
        ha="center", va="center", color=WHITE, zorder=6)

plt.tight_layout(pad=0.5)
plt.savefig("diagrams/fig3_license_map.png", dpi=180,
            bbox_inches="tight", facecolor="#F0FFF4")
plt.close()
print("fig3 完了")


# ══════════════════════════════════════════════════════════════
#  図4: 3つの哲学（雑誌カード風）
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor("#FFFBF0")
ax.set_facecolor("#FFFBF0")
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis("off")

# タイトル
title_bar = patches.FancyBboxPatch((0.3, 6.1), 12.4, 0.76,
                                    boxstyle="round,pad=0.1",
                                    facecolor=C4, zorder=2)
ax.add_patch(title_bar)
ax.text(6.5, 6.5, "私の3つの哲学",
        fontsize=26, fontweight="bold", ha="center", va="center",
        color=WHITE, zorder=3)
ax.text(6.5, 6.18, "スポーツ・AI・資格、すべての経験から生まれた言葉",
        fontsize=10, ha="center", va="center", color=C3, zorder=3)

cards = [
    (2.2,  C1,  "#FFF0F0",
     "① すぐやる",
     "いまやってもあとでやっても\n評価が変わらないものは、\nすぐやる。",
     "先延ばしゼロ", "normal", "right"),
    (6.5,  C7,  "#F5F0FF",
     "② 5分始める",
     "ここで5分取り掛かれないものは\n頑張っても\n終わらせられない。",
     "完璧主義ゼロ", "smile", "left"),
    (10.8, "#27AE60", "#F0FFF4",
     "③ 回数を信じる",
     "続けることを決めたなら\n意味を求めるな。\n回数を信じろ。",
     "継続が発見を生む", "excited", "right"),
]

for cx, color, bg, title, body, tag, expr, direction in cards:
    # カード
    card = patches.FancyBboxPatch((cx - 1.9, 0.4), 3.8, 5.5,
                                   boxstyle="round,pad=0.2",
                                   facecolor=bg, edgecolor=color,
                                   linewidth=3.5, zorder=2)
    ax.add_patch(card)

    # ヘッダーバー
    hdr = patches.FancyBboxPatch((cx - 1.9, 5.15), 3.8, 0.75,
                                  boxstyle="round,pad=0.1",
                                  facecolor=color, zorder=3)
    ax.add_patch(hdr)
    ax.text(cx, 5.54, title, fontsize=14, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=4)

    # キャラ
    draw_anime_character(ax, cx, 3.55, scale=0.78,
                          color="#FFDAB9", hair_color=C4,
                          expression=expr, direction=direction)

    # 本文
    ax.text(cx, 2.3, body, fontsize=10, ha="center", va="center",
            color=C4, linespacing=1.8, zorder=3)

    # タグ
    tag_bg = patches.FancyBboxPatch((cx - 1.4, 0.5), 2.8, 0.6,
                                     boxstyle="round,pad=0.1",
                                     facecolor=color, zorder=4)
    ax.add_patch(tag_bg)
    ax.text(cx, 0.80, tag, fontsize=10.5, fontweight="bold",
            ha="center", va="center", color=WHITE, zorder=5)

# 矢印（カード間）
for x in [4.2, 8.5]:
    ax.annotate("", xy=(x + 0.25, 3.5), xytext=(x - 0.25, 3.5),
                arrowprops=dict(arrowstyle="-|>", color=C4,
                                lw=3, mutation_scale=22))

plt.tight_layout(pad=0.5)
plt.savefig("diagrams/fig4_philosophy.png", dpi=180,
            bbox_inches="tight", facecolor="#FFFBF0")
plt.close()
print("fig4 完了")

print("\n全4枚の図解を diagrams/ フォルダに生成しました！")
