"""
Thinking Cost Benchmark - Day 1 Project
Demonstrates the trade-off between Zero-Shot and Explicit Chain-of-Thought prompting.

This script compares token usage vs. accuracy for two prompting strategies:
- Zero-Shot: "Answer immediately"
- Explicit CoT: "Think step by step"

The goal is to quantify why researchers want Latent CoT by showing that
explicit reasoning is more accurate but costs 2-4x more tokens.
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for file saving
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

MOCK_MODE = True  # Set to False to use actual OpenAI API
API_KEY = "your-api-key-here"  # Only needed when MOCK_MODE = False
MODEL_NAME = "gpt-3.5-turbo"

# ============================================================================
# DATA: 5 CHALLENGING MATH PROBLEMS
# ============================================================================

MATH_PROBLEMS = [
    {
        "id": "Q1",
        "question": "If 5 machines can make 5 widgets in 5 minutes, how many minutes would it take 100 machines to make 100 widgets?",
        "answer": "5"
    },
    {
        "id": "Q2",
        "question": "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?",
        "answer": "0.05"
    },
    {
        "id": "Q3",
        "question": "In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half the lake?",
        "answer": "47"
    },
    {
        "id": "Q4",
        "question": "If you're running a race and you pass the person in second place, what place are you in?",
        "answer": "2"
    },
    {
        "id": "Q5",
        "question": "A farmer has 17 sheep, and all but 9 die. How many are left?",
        "answer": "9"
    }
]

# ============================================================================
# MOCK RESPONSES (Used when MOCK_MODE = True)
# ============================================================================

MOCK_RESPONSES = {
    "Q1": {
        "zero_shot": {
            "text": "100 minutes",
            "tokens": 10,
            "correct": False
        },
        "cot": {
            "text": "Let me think step by step. If 5 machines make 5 widgets in 5 minutes, that means each machine makes 1 widget in 5 minutes. So 100 machines would each make 1 widget in 5 minutes, producing 100 widgets total. The answer is 5 minutes.",
            "tokens": 45,
            "correct": True
        }
    },
    "Q2": {
        "zero_shot": {
            "text": "$0.10",
            "tokens": 8,
            "correct": False
        },
        "cot": {
            "text": "Let me work through this carefully. Let's say the ball costs x dollars. Then the bat costs x + $1.00. Together they cost x + (x + $1.00) = $1.10. So 2x + $1.00 = $1.10, which means 2x = $0.10, and x = $0.05. The ball costs $0.05.",
            "tokens": 52,
            "correct": True
        }
    },
    "Q3": {
        "zero_shot": {
            "text": "24 days, half the time",
            "tokens": 12,
            "correct": False
        },
        "cot": {
            "text": "Let me reason about this. The lily pads double each day. On day 48, they cover the whole lake. So on day 47, they must have covered half the lake, because they doubled from day 47 to day 48. Wait, let me reconsider... Actually it would be 24 days.",
            "tokens": 38,
            "correct": False
        }
    },
    "Q4": {
        "zero_shot": {
            "text": "Second place",
            "tokens": 7,
            "correct": True
        },
        "cot": {
            "text": "Let me think through this step by step. If I'm running a race and I pass the person in second place, that means I was behind them (in third or worse). When I pass them, I take their position, which was second place. So I'm now in second place, and they drop to third.",
            "tokens": 60,
            "correct": True
        }
    },
    "Q5": {
        "zero_shot": {
            "text": "8 sheep",
            "tokens": 9,
            "correct": False
        },
        "cot": {
            "text": "Let me carefully parse this. The farmer has 17 sheep. 'All but 9 die' means all except 9 die. So if all except 9 die, that means 9 survive. The answer is 9 sheep are left alive.",
            "tokens": 48,
            "correct": True
        }
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def mock_api_call(question_id: str, is_cot: bool) -> Dict:
    """
    Simulates an API call with pre-defined responses.
    
    Args:
        question_id: The question ID (Q1, Q2, etc.)
        is_cot: True for Chain-of-Thought, False for Zero-Shot
    
    Returns:
        Dictionary with 'text', 'tokens', and 'correct' keys
    """
    mode = "cot" if is_cot else "zero_shot"
    return MOCK_RESPONSES[question_id][mode]


def real_api_call(question: str, is_cot: bool) -> Dict:
    """
    Makes an actual OpenAI API call.
    
    Args:
        question: The math problem to solve
        is_cot: True for Chain-of-Thought, False for Zero-Shot
    
    Returns:
        Dictionary with 'text', 'tokens', and 'correct' keys
    """
    try:
        import openai
        openai.api_key = API_KEY
        
        if is_cot:
            prompt = f"Think step by step and then answer: {question}"
        else:
            prompt = f"Answer this question immediately with just the number: {question}"
        
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        text = response['choices'][0]['message']['content']
        tokens = response['usage']['total_tokens']
        
        return {
            "text": text,
            "tokens": tokens,
            "correct": None  # Will be checked separately
        }
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return {"text": "", "tokens": 0, "correct": False}


def get_response(question_id: str, question: str, is_cot: bool) -> Dict:
    """
    Gets response from either mock or real API based on MOCK_MODE.
    
    Args:
        question_id: The question ID (Q1, Q2, etc.)
        question: The math problem text
        is_cot: True for Chain-of-Thought, False for Zero-Shot
    
    Returns:
        Dictionary with response data
    """
    if MOCK_MODE:
        return mock_api_call(question_id, is_cot)
    else:
        return real_api_call(question, is_cot)


def check_correctness(response_text: str, expected_answer: str) -> bool:
    """
    Checks if the response contains the correct answer.
    
    Args:
        response_text: The model's response
        expected_answer: The correct answer
    
    Returns:
        True if correct, False otherwise
    """
    # Simple check: see if the expected answer appears in the response
    return expected_answer.lower() in response_text.lower()


def extract_token_count(response: Dict) -> int:
    """
    Extracts token count from response.
    
    Args:
        response: Response dictionary
    
    Returns:
        Number of tokens used
    """
    return response.get("tokens", 0)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def run_benchmark() -> Dict:
    """
    Runs the full benchmark comparing Zero-Shot vs Explicit CoT.
    
    Returns:
        Dictionary containing all results
    """
    print("=" * 70)
    print("THINKING COST BENCHMARK - Explicit CoT vs Zero-Shot")
    print("=" * 70)
    print(f"\nMode: {'MOCK (Simulated)' if MOCK_MODE else 'REAL API'}")
    print(f"\nRunning benchmark on {len(MATH_PROBLEMS)} math problems...\n")
    
    results = {
        "question_ids": [],
        "questions": [],
        "expected_answers": [],
        "zero_shot": {
            "tokens": [],
            "correct": [],
            "responses": []
        },
        "cot": {
            "tokens": [],
            "correct": [],
            "responses": []
        }
    }
    
    for problem in MATH_PROBLEMS:
        q_id = problem["id"]
        question = problem["question"]
        expected = problem["answer"]
        
        print(f"\n{q_id}: {question[:60]}...")
        
        # Zero-Shot Pass
        zero_shot_response = get_response(q_id, question, is_cot=False)
        zero_shot_tokens = extract_token_count(zero_shot_response)
        
        if MOCK_MODE:
            zero_shot_correct = zero_shot_response["correct"]
        else:
            zero_shot_correct = check_correctness(zero_shot_response["text"], expected)
        
        print(f"  Zero-Shot: {zero_shot_tokens} tokens | {'✓ Correct' if zero_shot_correct else '✗ Wrong'}")
        
        # Explicit CoT Pass
        cot_response = get_response(q_id, question, is_cot=True)
        cot_tokens = extract_token_count(cot_response)
        
        if MOCK_MODE:
            cot_correct = cot_response["correct"]
        else:
            cot_correct = check_correctness(cot_response["text"], expected)
        
        print(f"  Explicit CoT: {cot_tokens} tokens | {'✓ Correct' if cot_correct else '✗ Wrong'}")
        
        # Store results
        results["question_ids"].append(q_id)
        results["questions"].append(question)
        results["expected_answers"].append(expected)
        
        results["zero_shot"]["tokens"].append(zero_shot_tokens)
        results["zero_shot"]["correct"].append(zero_shot_correct)
        results["zero_shot"]["responses"].append(zero_shot_response["text"])
        
        results["cot"]["tokens"].append(cot_tokens)
        results["cot"]["correct"].append(cot_correct)
        results["cot"]["responses"].append(cot_response["text"])
    
    return results


def print_summary(results: Dict):
    """
    Prints a summary of the benchmark results.
    
    Args:
        results: Results dictionary from run_benchmark()
    """
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    # Calculate totals
    total_zero_shot_tokens = sum(results["zero_shot"]["tokens"])
    total_cot_tokens = sum(results["cot"]["tokens"])
    
    zero_shot_correct_count = sum(results["zero_shot"]["correct"])
    cot_correct_count = sum(results["cot"]["correct"])
    
    total_questions = len(results["question_ids"])
    
    zero_shot_accuracy = (zero_shot_correct_count / total_questions) * 100
    cot_accuracy = (cot_correct_count / total_questions) * 100
    
    token_multiplier = total_cot_tokens / total_zero_shot_tokens if total_zero_shot_tokens > 0 else 0
    
    print(f"\n📊 Token Usage:")
    print(f"  Zero-Shot:    {total_zero_shot_tokens} tokens")
    print(f"  Explicit CoT: {total_cot_tokens} tokens")
    print(f"  Multiplier:   {token_multiplier:.2f}x (CoT uses {token_multiplier:.2f}x more tokens)")
    
    print(f"\n✓ Accuracy:")
    print(f"  Zero-Shot:    {zero_shot_correct_count}/{total_questions} = {zero_shot_accuracy:.0f}%")
    print(f"  Explicit CoT: {cot_correct_count}/{total_questions} = {cot_accuracy:.0f}%")
    
    print(f"\n💡 Key Insight:")
    print(f"  Explicit CoT improves accuracy by {cot_accuracy - zero_shot_accuracy:.0f}% but costs {token_multiplier:.2f}x more tokens.")
    print(f"  This demonstrates why Latent CoT is valuable: reasoning without the token cost!")


# ============================================================================
# VISUALIZATION
# ============================================================================

def create_visualization(results: Dict):
    """
    Creates a dual-axis chart showing token usage vs accuracy.
    
    Args:
        results: Results dictionary from run_benchmark()
    """
    print("\n" + "=" * 70)
    print("Creating visualization...")
    print("=" * 70)
    
    # Prepare data
    question_ids = results["question_ids"]
    x_pos = np.arange(len(question_ids))
    width = 0.35  # Width of bars
    
    zero_shot_tokens = results["zero_shot"]["tokens"]
    cot_tokens = results["cot"]["tokens"]
    
    zero_shot_correct = results["zero_shot"]["correct"]
    cot_correct = results["cot"]["correct"]
    
    # Create figure with dual axes
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Primary axis: Token count (bars)
    ax1.set_xlabel('Question ID', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Token Count', fontsize=12, fontweight='bold', color='black')
    
    # Plot bars
    bars1 = ax1.bar(x_pos - width/2, zero_shot_tokens, width, 
                    label='Zero-Shot', color='#3498db', alpha=0.8)
    bars2 = ax1.bar(x_pos + width/2, cot_tokens, width,
                    label='Explicit CoT', color='#e74c3c', alpha=0.8)
    
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(question_ids)
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Secondary axis: Correctness markers
    ax2 = ax1.twinx()
    ax2.set_ylabel('Correctness', fontsize=12, fontweight='bold', color='black')
    ax2.set_ylim(0, 1.5)
    ax2.set_yticks([])
    
    # Add correctness markers on top of each bar
    for i, (zs_correct, cot_correct) in enumerate(zip(zero_shot_correct, cot_correct)):
        # Zero-shot marker - position on top of zero-shot bar
        marker = '✓' if zs_correct else '✗'
        color = '#27ae60' if zs_correct else '#c0392b'
        bar_height = zero_shot_tokens[i]
        ax1.text(x_pos[i] - width/2, bar_height + 1, marker, 
                ha='center', va='bottom', fontsize=16, color=color, fontweight='bold')
        
        # CoT marker - position on top of CoT bar
        marker = '✓' if cot_correct else '✗'
        color = '#27ae60' if cot_correct else '#c0392b'
        bar_height = cot_tokens[i]
        ax1.text(x_pos[i] + width/2, bar_height + 1, marker,
                ha='center', va='bottom', fontsize=16, color=color, fontweight='bold')
    
    # Add legend elements for markers
    from matplotlib.patches import Patch
    legend_elements = [
        bars1,
        bars2,
        Patch(facecolor='white', edgecolor='#27ae60', label='✓ Correct'),
        Patch(facecolor='white', edgecolor='#c0392b', label='✗ Incorrect')
    ]
    
    ax1.legend(handles=legend_elements, loc='upper left', fontsize=10, framealpha=0.9)
    
    # Title
    plt.title('The Price of Reasoning: Tokens vs Accuracy', 
             fontsize=16, fontweight='bold', pad=20)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('project1_cost.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved as 'project1_cost.png'")
    
    plt.close()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # Run the benchmark
    results = run_benchmark()
    
    # Print summary
    print_summary(results)
    
    # Create visualization
    create_visualization(results)
    
    print("\n" + "=" * 70)
    print("BENCHMARK COMPLETE!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Check 'project1_cost.png' for the visualization")
    print("2. To use real API: Set MOCK_MODE = False and add your API key")
    print("3. This data quantifies why Latent CoT is needed!")
    print()
