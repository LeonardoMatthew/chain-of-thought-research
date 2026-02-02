# Project 1: The "Thinking Cost" Benchmark

## Overview

This project demonstrates the fundamental trade-off between **Zero-Shot** and **Explicit Chain-of-Thought (CoT)** prompting strategies. It quantifies why researchers are interested in **Latent CoT** by proving that explicit reasoning is more accurate but comes at a significant token cost.

## The Problem

When language models solve complex problems, they can either:
- **Answer immediately** (Zero-Shot) - Fast and cheap, but often wrong
- **Think step by step** (Explicit CoT) - More accurate, but uses 2-5x more tokens

This project measures both approaches on 5 difficult math problems to visualize the cost-accuracy trade-off.

## Results Summary

### Key Findings (Mock Mode)

| Metric | Zero-Shot | Explicit CoT | Difference |
|--------|-----------|--------------|------------|
| **Token Usage** | 46 tokens | 243 tokens | **5.28x more** |
| **Accuracy** | 1/5 (20%) | 4/5 (80%) | **+60%** |

**Conclusion**: Explicit CoT improves accuracy by 60% but costs 5.28x more tokens. This demonstrates why Latent CoT (reasoning without visible tokens) is valuable for production systems.

### Visual Results

The generated chart (`project1_cost.png`) shows:
- **Blue bars**: Token usage for Zero-Shot prompts
- **Orange bars**: Token usage for Explicit CoT prompts
- **Checkmarks (✓)**: Correct answers
- **X marks (✗)**: Incorrect answers

This visualization clearly illustrates the "price of reasoning."

## Files

- `thinking_cost_benchmark.py` - Main benchmark script
- `project1_cost.png` - Generated visualization
- `README.md` - This documentation file

## Installation

### Prerequisites

```bash
# Python 3.7 or higher required
python3 --version

# Install required packages
pip install matplotlib numpy
```

### For Real API Mode (Optional)

```bash
pip install openai
```

## Usage

### Quick Start (Mock Mode)

The script runs in **mock mode** by default, which simulates API responses without requiring an OpenAI API key. This is perfect for testing and demonstration.

```bash
python3 thinking_cost_benchmark.py
```

This will:
1. Run 5 math problems through both prompting strategies
2. Display results in the terminal
3. Generate `project1_cost.png` visualization

### Using Real OpenAI API

To use actual GPT models instead of simulated responses:

1. **Edit the configuration** in `thinking_cost_benchmark.py`:

```python
MOCK_MODE = False  # Change from True to False
API_KEY = "sk-your-api-key-here"  # Add your OpenAI API key
MODEL_NAME = "gpt-3.5-turbo"  # Or "gpt-4", etc.
```

2. **Run the script**:

```bash
python3 thinking_cost_benchmark.py
```

## The 5 Test Problems

These are classic reasoning problems that humans often get wrong:

1. **Machine Problem**: If 5 machines make 5 widgets in 5 minutes, how long for 100 machines to make 100 widgets?
   - Common wrong answer: 100 minutes
   - Correct answer: **5 minutes**

2. **Bat and Ball**: A bat and ball cost $1.10 total. The bat costs $1.00 more than the ball. How much does the ball cost?
   - Common wrong answer: $0.10
   - Correct answer: **$0.05**

3. **Lily Pads**: Lily pads double daily. If they cover the lake in 48 days, when do they cover half?
   - Common wrong answer: 24 days
   - Correct answer: **47 days**

4. **Race Position**: If you pass the person in second place, what place are you in?
   - Common wrong answer: First place
   - Correct answer: **Second place**

5. **Sheep Problem**: A farmer has 17 sheep, all but 9 die. How many are left?
   - Common wrong answer: 8
   - Correct answer: **9**

## Understanding the Output

### Terminal Output

The script prints:

1. **Per-Question Results**: Token count and correctness for each problem
2. **Summary Statistics**: Total tokens, accuracy rates, cost multiplier
3. **Key Insight**: The fundamental trade-off statement

Example output:

```
Q1: If 5 machines can make 5 widgets in 5 minutes, how many minu...
  Zero-Shot: 10 tokens | ✗ Wrong
  Explicit CoT: 45 tokens | ✓ Correct

[...]

💡 Key Insight:
  Explicit CoT improves accuracy by 60% but costs 5.28x more tokens.
  This demonstrates why Latent CoT is valuable: reasoning without the token cost!
```

### Visualization

The chart (`project1_cost.png`) uses:
- **X-axis**: Question IDs (Q1 through Q5)
- **Left Y-axis**: Token count (height of bars)
- **Right Y-axis**: Correctness (checkmarks and X marks)
- **Blue bars**: Zero-Shot token usage
- **Orange bars**: Explicit CoT token usage
- **Green ✓**: Correct answer
- **Red ✗**: Incorrect answer

## How It Works

### Mock Mode Logic

When `MOCK_MODE = True`, the script uses pre-defined responses stored in the `MOCK_RESPONSES` dictionary. This simulates realistic model behavior:

- **Zero-Shot responses**: Short (5-15 tokens), low accuracy
- **CoT responses**: Long (30-80 tokens), high accuracy
- **Question 3 (Lily Pads)**: Both methods get it wrong, showing CoT isn't perfect

### Real API Mode Logic

When `MOCK_MODE = False`, the script:
1. Calls OpenAI's API with the appropriate prompt
2. Extracts the response text and token count from API metadata
3. Checks correctness by looking for the expected answer in the response

### Prompting Strategies

**Zero-Shot Prompt Template**:
```
"Answer this question immediately with just the number: {question}"
```

**Explicit CoT Prompt Template**:
```
"Think step by step and then answer: {question}"
```

## Code Structure

The script is organized into logical sections:

1. **Configuration**: `MOCK_MODE`, `API_KEY`, `MODEL_NAME`
2. **Data**: Math problems with expected answers
3. **Mock Responses**: Pre-defined simulated responses
4. **Helper Functions**:
   - `mock_api_call()` - Simulates API responses
   - `real_api_call()` - Makes actual OpenAI API calls
   - `get_response()` - Routes to mock or real API
   - `check_correctness()` - Validates answers
   - `extract_token_count()` - Gets token usage
5. **Main Execution**:
   - `run_benchmark()` - Runs all tests
   - `print_summary()` - Displays results
   - `create_visualization()` - Generates chart

## Customization

### Adding More Problems

Edit the `MATH_PROBLEMS` list:

```python
MATH_PROBLEMS = [
    {
        "id": "Q6",
        "question": "Your custom question here?",
        "answer": "expected_answer"
    },
    # ... add more
]
```

If using mock mode, also add entries to `MOCK_RESPONSES`.

### Changing the Model

For real API mode, modify:

```python
MODEL_NAME = "gpt-4"  # or "gpt-3.5-turbo", "gpt-4-turbo", etc.
```

### Adjusting Visualization

Customize colors, sizes, and labels in the `create_visualization()` function:

```python
# Change bar colors
bars1 = ax1.bar(..., color='#3498db')  # Zero-Shot color
bars2 = ax1.bar(..., color='#e74c3c')  # CoT color

# Change figure size
fig, ax1 = plt.subplots(figsize=(14, 7))  # Wider chart

# Change DPI for higher quality
plt.savefig('project1_cost.png', dpi=600)  # Higher resolution
```

## Why This Matters

### The Research Context

This project demonstrates the motivation behind **Latent CoT** research:

1. **Current Problem**: Explicit CoT reasoning takes up valuable tokens
2. **Token Cost**: In production, more tokens = higher API costs
3. **Solution Goal**: Train models to reason internally without outputting reasoning steps
4. **Expected Benefit**: Keep the accuracy of CoT but reduce token usage to Zero-Shot levels

### Real-World Impact

For a production system processing 1 million queries:
- Zero-Shot: 46M tokens
- Explicit CoT: 243M tokens (5.28x cost)
- **Latent CoT Goal**: 46M tokens with 80% accuracy

At $0.002 per 1K tokens (GPT-3.5-turbo pricing):
- Zero-Shot: $92
- Explicit CoT: $486
- **Potential Savings**: $394 (81% cost reduction)

## Troubleshooting

### Issue: "Module not found"

**Solution**: Install required packages:
```bash
pip install matplotlib numpy openai
```

### Issue: Matplotlib warnings about cache directory

**Solution**: This is a warning, not an error. The script will still work. To suppress:
```bash
export MPLCONFIGDIR=/tmp/matplotlib
python3 thinking_cost_benchmark.py
```

### Issue: API key errors (Real mode)

**Solution**: 
1. Verify your API key is correct
2. Check you have sufficient credits
3. Ensure you're using a valid model name

### Issue: Chart doesn't display

**Solution**: The script saves the chart as a file (`project1_cost.png`) rather than displaying it interactively. Check the current directory for the file.

## Next Steps

### Day 2 Project Ideas

Now that you've quantified the cost of explicit reasoning:

1. **Implement a simple Latent CoT approach**: Train a model to reason without visible outputs
2. **Compare multiple models**: Test GPT-3.5, GPT-4, Claude, etc.
3. **Test on different domains**: Code problems, logic puzzles, science questions
4. **Measure cost vs accuracy curves**: Find the optimal trade-off point

## License

This is an educational project for research purposes.

## Author

Created as part of the "Research Tsinghua" project series.

---

**Questions or improvements?** Feel free to modify and extend this benchmark for your research needs!
