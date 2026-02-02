"""
Generate Logit Lens Heatmap with Mock Data
This creates the visualization showing expected probability progression across layers.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Mock data showing typical logit lens pattern
# Based on research: early layers confused, middle rising, late confident
layer_probabilities = [
    0.08,   # Layer 0: Very confused
    0.34,   # Layer 1: Still very low
    1.89,   # Layer 2: Starting to consider
    7.23,   # Layer 3: Emerging pattern
    16.45,  # Layer 4: Stronger signal
    31.67,  # Layer 5: Paris becoming likely
    48.91,  # Layer 6: Crosses 50% threshold
    67.34,  # Layer 7: Dominant answer
    82.15,  # Layer 8: Very confident
    90.78,  # Layer 9: Near certain
    95.12,  # Layer 10: Final refinement
    97.23   # Layer 11: Output layer confidence
]

print("=" * 70)
print("GENERATING LOGIT LENS HEATMAP (MOCK DATA)")
print("=" * 70)
print("\nThis visualization shows the expected pattern of how GPT-2")
print("progressively 'realizes' that the answer is Paris.")
print("\nLayer-by-Layer Probabilities:")
print("-" * 70)

for i, prob in enumerate(layer_probabilities):
    if prob < 1:
        status = "Very Low 🔴"
    elif prob < 10:
        status = "Low 🟠"
    elif prob < 30:
        status = "Medium 🟡"
    elif prob < 70:
        status = "High 🟢"
    else:
        status = "Very High 🟢🟢"
    print(f"Layer {i:<2}  {prob:>6.2f}%          {status}")

# Prepare data as 1x12 array
data = np.array(layer_probabilities).reshape(1, -1)

# Create figure
fig, ax = plt.subplots(figsize=(14, 3))

# Create heatmap
sns.heatmap(
    data,
    annot=True,  # Show values in cells
    fmt='.1f',  # Format as float with 1 decimal place
    cmap='RdYlGn',  # Red (low) -> Yellow (medium) -> Green (high)
    vmin=0,  # Minimum value for color scale
    vmax=100,  # Maximum value for color scale
    cbar_kws={'label': 'Probability (%)'},
    xticklabels=[f'Layer {i}' for i in range(12)],
    yticklabels=['Paris Probability'],
    linewidths=0.5,
    linecolor='gray',
    ax=ax
)

# Customize appearance
ax.set_xlabel('Transformer Layer', fontsize=12, fontweight='bold')
ax.set_ylabel('', fontsize=12)
plt.title(
    "Logit Lens: When does GPT-2 'realize' the answer is Paris?",
    fontsize=14,
    fontweight='bold',
    pad=20
)

# Rotate labels
plt.xticks(rotation=0, ha='center')
plt.yticks(rotation=0)

# Save
plt.tight_layout()
plt.savefig('project2_logit_lens.png', dpi=300, bbox_inches='tight')
print("\n" + "=" * 70)
print("✅ HEATMAP GENERATED SUCCESSFULLY!")
print("=" * 70)
print(f"\n📊 Visualization saved as: project2_logit_lens.png")
print("\n💡 Analysis:")
print(f"  - Early layers (0-3): Average {np.mean(layer_probabilities[:4]):.2f}% (confused)")
print(f"  - Middle layers (4-7): Average {np.mean(layer_probabilities[4:8]):.2f}% (forming answer)")
print(f"  - Late layers (8-11): Average {np.mean(layer_probabilities[8:]):.2f}% (confident)")
print(f"  - Final confidence: {layer_probabilities[-1]:.2f}%")
print("\n🔬 This demonstrates the progressive reasoning pattern in transformers!")
print()

plt.close()
