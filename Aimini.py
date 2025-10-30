//21172400700087
//GAYATHRI P

PROGRAM:
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# --- Step 1: Define Classroom and Students ---
rows, cols = 5, 6  # 5 rows × 6 columns
students = [
    {"id": "S01", "dept": "CS", "special": False},
    {"id": "S02", "dept": "CS", "special": False},
    {"id": "S03", "dept": "ECE", "special": False},
    {"id": "S04", "dept": "ME", "special": True},  # special seat
    {"id": "S05", "dept": "ME", "special": False},
    {"id": "S06", "dept": "CS", "special": False},
    {"id": "S07", "dept": "ME", "special": False},
    {"id": "S08", "dept": "CS", "special": False},
    {"id": "S09", "dept": "ECE", "special": False},
    {"id": "S10", "dept": "ME", "special": False},
]

# --- Step 2: Generate Seating Plan (Simple Rule) ---
grid = [[None for _ in range(cols)] for _ in range(rows)]
r, c = 0, 0
for s in students:
    grid[r][c] = s
    c += 1
    if c == cols:
        c = 0
        r += 1
    if r == rows:
        break

# --- Step 3: Print Output in Terminal ---
print("\n--- AI Exam Seating Plan (Text Output) ---\n")
for r in range(rows):
    for c in range(cols):
        seat = grid[r][c]
        if seat:
            print(f"Seat ({r+1},{c+1}): {seat['id']} - {seat['dept']}", end="\t")
        else:
            print(f"Seat ({r+1},{c+1}): Empty", end="\t")
    print()  # new line per row

# --- Step 4: Visualization using Matplotlib ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("AI Exam Seating Plan - Classroom Layout", fontsize=14, fontweight="bold")
ax.set_xlim(-0.5, cols - 0.5)
ax.set_ylim(-0.5, rows - 0.5)
ax.invert_yaxis()
ax.set_xticks(range(cols))
ax.set_yticks(range(rows))
ax.grid(True, which="both", color="gray", linestyle="--", linewidth=0.5)
ax.set_xlabel("Column")
ax.set_ylabel("Row")

# Department colors
dept_colors = {"CS": "skyblue", "ECE": "lightgreen", "ME": "salmon"}

# Draw seats
for r in range(rows):
    for c in range(cols):
        student = grid[r][c]
        if student is not None:
            color = "gold" if student["special"] else dept_colors.get(student["dept"], "lightgray")
            ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, facecolor=color, edgecolor="black"))
            ax.text(c, r, student["id"], ha="center", va="center", fontsize=9, fontweight="bold")
        else:
            ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, facecolor="white", edgecolor="black"))

# Legend
legend_elements = [
    Patch(facecolor='skyblue', edgecolor='black', label='CS Dept'),
    Patch(facecolor='lightgreen', edgecolor='black', label='ECE Dept'),
    Patch(facecolor='salmon', edgecolor='black', label='ME Dept'),
    Patch(facecolor='gold', edgecolor='black', label='Special Seat'),
    Patch(facecolor='white', edgecolor='black', label='Empty Seat')
]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.25, 1))

plt.tight_layout()

# --- Step 5: Save and Show Output ---
plt.savefig("AI_Exam_SeatingPlan.png")   # saves image in your VS Code folder
plt.show()
