"""
Logit Lens Visualization - Day 2 Project
Peek inside GPT-2's layers to see when it "realizes" the answer is Paris.

This script implements the "Logit Lens" technique to visualize how a transformer
model's internal representations evolve across layers. By projecting each layer's
hidden states through the language modeling head, we can see when the model
becomes confident about its answer.

The technique reveals that:
- Early layers are confused (low probability for correct answer)
- Middle layers start forming the answer (rising probability)
- Final layers are very confident (high probability)
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for file saving
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import torch
from typing import List, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

MODEL_NAME = "gpt2"  # GPT-2 small (117M parameters, 12 layers)
DEVICE = "cpu"  # Force CPU execution (no GPU required)
PROMPT = "The Eiffel Tower is located in the city of"
TARGET_WORD = "Paris"  # The word we expect the model to predict

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_model_and_tokenizer():
    """
    Loads GPT-2 model and tokenizer, configured for CPU execution.
    
    Returns:
        tuple: (model, tokenizer)
    """
    print("=" * 70)
    print("LOGIT LENS: PEERING INSIDE GPT-2")
    print("=" * 70)
    print(f"\nLoading model '{MODEL_NAME}'...")
    
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        # Load tokenizer with resume capability
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, resume_download=True)
        
        # Load model and move to CPU with resume capability
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, resume_download=True)
        model = model.to(DEVICE)
        model.eval()  # Set to evaluation mode (no dropout, etc.)
        
        print(f"✓ Model loaded successfully")
        print(f"  - Parameters: ~117M")
        print(f"  - Layers: 12")
        print(f"  - Hidden dim: 768")
        print(f"  - Vocabulary size: {model.config.vocab_size}")
        
        return model, tokenizer
    
    except ImportError:
        print("\n❌ ERROR: transformers library not found!")
        print("Please install it with: pip install transformers torch")
        raise
    except Exception as e:
        print(f"\n❌ ERROR loading model: {e}")
        raise


def get_target_token_id(tokenizer, target_word: str) -> int:
    """
    Gets the token ID for the target word.
    
    Args:
        tokenizer: GPT-2 tokenizer
        target_word: The word to find (e.g., "Paris")
    
    Returns:
        int: Token ID for the target word
    """
    # Try with leading space first (GPT-2 tokenizer convention)
    token_ids_with_space = tokenizer.encode(f" {target_word}", add_special_tokens=False)
    
    if len(token_ids_with_space) == 1:
        token_id = token_ids_with_space[0]
        print(f"\n✓ Target token: ' {target_word}' (ID: {token_id})")
        return token_id
    
    # Try without space
    token_ids_without_space = tokenizer.encode(target_word, add_special_tokens=False)
    
    if len(token_ids_without_space) == 1:
        token_id = token_ids_without_space[0]
        print(f"\n✓ Target token: '{target_word}' (ID: {token_id})")
        return token_id
    
    # If target word is multiple tokens, use the first one
    token_id = token_ids_with_space[0] if token_ids_with_space else token_ids_without_space[0]
    print(f"\n⚠ Warning: '{target_word}' tokenizes to multiple tokens. Using first token (ID: {token_id})")
    
    return token_id


def extract_layer_probabilities(model, tokenizer, prompt: str, target_token_id: int) -> List[float]:
    """
    Extracts the probability of the target token at each layer.
    
    This is the core "Logit Lens" technique:
    1. Run the prompt through the model
    2. For each layer, get the hidden state of the last token
    3. Project it through the language model head to get logits
    4. Apply softmax to get probabilities
    5. Extract the probability for our target token
    
    Args:
        model: GPT-2 model
        tokenizer: GPT-2 tokenizer
        prompt: Input text
        target_token_id: Token ID to track
    
    Returns:
        List of probabilities (one per layer, 0-11)
    """
    print(f"\n{'=' * 70}")
    print("RUNNING LOGIT LENS ANALYSIS")
    print("=" * 70)
    print(f"\nPrompt: \"{prompt}\"")
    print(f"Target: \"{TARGET_WORD}\"")
    
    # Tokenize input
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(DEVICE)
    print(f"\nTokenized input: {input_ids.shape[1]} tokens")
    
    # Run forward pass with hidden states output
    with torch.no_grad():
        outputs = model(input_ids, output_hidden_states=True)
    
    # Get all hidden states (tuple of 13 tensors: embedding + 12 layers)
    hidden_states = outputs.hidden_states
    print(f"Hidden states extracted: {len(hidden_states)} layers (including embedding)")
    
    # Extract probabilities for each layer
    layer_probabilities = []
    
    print(f"\n{'Layer':<8} {'Probability':<15} {'Confidence'}")
    print("-" * 70)
    
    # Note: hidden_states[0] is the embedding layer
    # hidden_states[1] through hidden_states[12] are transformer layers 0-11
    for layer_idx in range(1, 13):  # Skip embedding (index 0), process layers 1-12
        # Get hidden state at the last token position
        # Shape: (batch_size=1, seq_len, hidden_dim=768)
        hidden = hidden_states[layer_idx][:, -1, :]  # Shape: (1, 768)
        
        # Project through language model head to get logits
        # Shape: (1, vocab_size=50257)
        logits = model.lm_head(hidden)
        
        # Apply softmax to get probabilities
        probs = torch.softmax(logits, dim=-1)
        
        # Get probability for target token and convert to percentage
        target_prob = probs[0, target_token_id].item() * 100
        layer_probabilities.append(target_prob)
        
        # Visual indicator of confidence
        if target_prob < 1:
            confidence = "Very Low 🔴"
        elif target_prob < 10:
            confidence = "Low 🟠"
        elif target_prob < 30:
            confidence = "Medium 🟡"
        elif target_prob < 70:
            confidence = "High 🟢"
        else:
            confidence = "Very High 🟢🟢"
        
        print(f"Layer {layer_idx-1:<2}  {target_prob:>6.2f}%          {confidence}")
    
    return layer_probabilities


def create_heatmap_visualization(probabilities: List[float], output_file: str = "project2_logit_lens.png"):
    """
    Creates a heatmap visualization showing the probability progression.
    
    Args:
        probabilities: List of probabilities (one per layer)
        output_file: Output filename for the visualization
    """
    print(f"\n{'=' * 70}")
    print("CREATING VISUALIZATION")
    print("=" * 70)
    
    # Prepare data as 1x12 array (one row, 12 columns)
    data = np.array(probabilities).reshape(1, -1)
    
    # Create figure with appropriate size
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
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=0, ha='center')
    plt.yticks(rotation=0)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n✓ Visualization saved as '{output_file}'")
    
    plt.close()


def print_summary(probabilities: List[float]):
    """
    Prints a summary analysis of the results.
    
    Args:
        probabilities: List of probabilities (one per layer)
    """
    print(f"\n{'=' * 70}")
    print("ANALYSIS SUMMARY")
    print("=" * 70)
    
    # Find key transition points
    early_avg = np.mean(probabilities[:4])  # Layers 0-3
    middle_avg = np.mean(probabilities[4:8])  # Layers 4-7
    late_avg = np.mean(probabilities[8:])  # Layers 8-11
    
    # Find when probability crosses thresholds
    layer_10_percent = next((i for i, p in enumerate(probabilities) if p >= 10), None)
    layer_50_percent = next((i for i, p in enumerate(probabilities) if p >= 50), None)
    
    print(f"\n📊 Average Probability by Stage:")
    print(f"  Early layers (0-3):  {early_avg:>6.2f}%")
    print(f"  Middle layers (4-7): {middle_avg:>6.2f}%")
    print(f"  Late layers (8-11):  {late_avg:>6.2f}%")
    
    print(f"\n🎯 Key Milestones:")
    if layer_10_percent is not None:
        print(f"  Reached 10% confidence: Layer {layer_10_percent}")
    else:
        print(f"  Never reached 10% confidence")
    
    if layer_50_percent is not None:
        print(f"  Reached 50% confidence: Layer {layer_50_percent}")
    else:
        print(f"  Never reached 50% confidence")
    
    print(f"  Final confidence (Layer 11): {probabilities[-1]:.2f}%")
    
    print(f"\n💡 Interpretation:")
    if early_avg < 5 and late_avg > 50:
        print("  ✓ Classic logit lens pattern observed!")
        print("  ✓ Model starts confused, becomes confident in later layers")
    elif late_avg > 50:
        print("  ✓ Model is confident in the answer by final layers")
    else:
        print("  ⚠ Unexpected pattern - model may not be confident about 'Paris'")
    
    print(f"\n🔬 Research Insight:")
    print("  This demonstrates that transformers build understanding progressively.")
    print("  Early layers focus on syntax/patterns, late layers form semantic meaning.")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function that runs the full Logit Lens analysis.
    """
    try:
        # Step 1: Load model and tokenizer
        model, tokenizer = load_model_and_tokenizer()
        
        # Step 2: Get target token ID
        target_token_id = get_target_token_id(tokenizer, TARGET_WORD)
        
        # Step 3: Extract probabilities at each layer
        probabilities = extract_layer_probabilities(model, tokenizer, PROMPT, target_token_id)
        
        # Step 4: Create visualization
        create_heatmap_visualization(probabilities)
        
        # Step 5: Print summary analysis
        print_summary(probabilities)
        
        print(f"\n{'=' * 70}")
        print("✅ LOGIT LENS ANALYSIS COMPLETE!")
        print("=" * 70)
        print(f"\nGenerated files:")
        print(f"  - project2_logit_lens.png")
        print(f"\nNext steps:")
        print(f"  1. Open the visualization to see the heatmap")
        print(f"  2. Try different prompts and target words")
        print(f"  3. Compare with other models (gpt2-medium, gpt2-large)")
        print()
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nTroubleshooting:")
        print("  1. Ensure you have installed: pip install torch transformers matplotlib seaborn")
        print("  2. Check that you have internet connection (for model download)")
        print("  3. Ensure you have enough disk space (~500MB for GPT-2)")
        raise


if __name__ == "__main__":
    main()
