# Chain-of-Thought Research: Latent vs Explicit Reasoning

A comprehensive research project exploring Chain-of-Thought (CoT) prompting techniques in Large Language Models, featuring three hands-on experiments that demonstrate the trade-offs between explicit reasoning and latent computation.

## 📚 Overview

This repository contains a survey paper and three practical implementations investigating how language models reason:

1. **Project 1: Thinking Cost Benchmark** - Quantifies the token cost vs accuracy trade-off
2. **Project 2: Logit Lens Visualization** - Reveals internal layer-by-layer reasoning
3. **Project 3: Pause Token Simulation** - Tests whether computation time alone improves reasoning

## 🎯 Key Findings

- **Explicit CoT** improves accuracy by 60% but costs 5.28x more tokens
- Models build understanding **progressively** across layers (not instantly)
- **Structure matters more than time** - adding computation without reasoning doesn't help
- Language is **essential** for complex reasoning in current LLMs

## 📖 Survey Paper

**[Survey-Paper.md](Survey-Paper.md)** - Comprehensive overview of Chain-of-Thought prompting, including:
- Fundamental principles and variations (Zero-shot, Few-shot, Auto-CoT)
- Applications across arithmetic, common-sense, and symbolic tasks
- Analysis of explicit vs latent reasoning mechanisms
- Future directions and research challenges

## 🔬 Projects

### Project 1: Thinking Cost Benchmark

**Directory**: [`project1-thinking-cost/`](project1-thinking-cost/)

Demonstrates why researchers want Latent CoT by measuring the cost-accuracy trade-off between Zero-Shot and Explicit CoT prompting.

**Key Results**:
- Zero-Shot: 20% accuracy, 46 tokens
- Explicit CoT: 80% accuracy, 243 tokens (5.28x more)
- **Conclusion**: Explicit reasoning is expensive but necessary

**Quick Start**:
```bash
cd project1-thinking-cost/
python3 thinking_cost_benchmark.py
```

**Technologies**: Python, Matplotlib, OpenAI API (mock mode available)

---

### Project 2: Logit Lens Visualization

**Directory**: [`project2-logit-lens/`](project2-logit-lens/)

Implements the Logit Lens technique to visualize how GPT-2 progressively builds confidence across its 12 layers when answering "The Eiffel Tower is located in the city of [Paris]".

**Key Results**:
- Early layers (0-3): < 5% confidence
- Middle layers (4-7): 5-60% confidence
- Late layers (8-11): 60-99% confidence
- **Conclusion**: Models reason progressively, not instantly

**Quick Start**:
```bash
cd project2-logit-lens/
pip install -r requirements.txt
python3 logit_lens.py
```

**Technologies**: PyTorch, Transformers (GPT-2), Seaborn

---

### Project 3: Pause Token Simulation

**Directory**: [`project3-pause-token/`](project3-pause-token/)

Tests whether adding "pause tokens" (dots) without structured reasoning improves performance compared to explicit Chain-of-Thought.

**Key Results**:
- Baseline: 60% accuracy
- Pause/Dots: 60% accuracy (no improvement!)
- Explicit CoT: 100% accuracy
- **Conclusion**: Structure (words) is essential, not just computation time

**Quick Start**:
```bash
cd project3-pause-token/
python3 pause_token.py
```

**Technologies**: Python, Matplotlib

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.7 or higher
python3 --version

# Install all dependencies
pip install -r requirements.txt
```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/chain-of-thought-research.git
cd chain-of-thought-research
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run any project**:
```bash
# Project 1
cd project1-thinking-cost/
python3 thinking_cost_benchmark.py

# Project 2
cd project2-logit-lens/
python3 logit_lens.py

# Project 3
cd project3-pause-token/
python3 pause_token.py
```

## 📊 Visual Results

Each project generates publication-ready visualizations:

- **Project 1**: `project1_cost.png` - Token usage vs accuracy comparison
- **Project 2**: `project2_logit_lens.png` - Layer-by-layer confidence heatmap
- **Project 3**: `project3_pause_token.png` - Strategy comparison bar chart

## 🎓 Research Context

This project addresses fundamental questions in LLM reasoning:

1. **Why is explicit reasoning expensive?** → Project 1 quantifies the 5x token cost
2. **How do models build understanding?** → Project 2 shows progressive layer-by-layer refinement
3. **Can we reason without words?** → Project 3 proves structure is essential

These findings have important implications for:
- **Production systems**: Understanding cost-accuracy trade-offs
- **Model architecture**: Designing better reasoning mechanisms
- **Interpretability**: Making AI decision-making more transparent
- **AI Safety**: Ensuring auditable reasoning processes

## 📁 Repository Structure

```
chain-of-thought-research/
├── README.md                          # This file
├── Survey-Paper.md                    # Comprehensive survey paper
├── requirements.txt                   # Consolidated dependencies
├── LICENSE                            # MIT License
├── .gitignore                         # Git ignore patterns
│
├── project1-thinking-cost/            # Token cost vs accuracy benchmark
│   ├── README.md                      # Detailed project documentation
│   ├── thinking_cost_benchmark.py     # Main script
│   ├── project1_cost.png              # Generated visualization
│   ├── QUICKSTART.txt                 # Quick reference
│   ├── RESULTS_SUMMARY.md             # Findings summary
│   └── VERIFICATION_CHECKLIST.md      # Testing checklist
│
├── project2-logit-lens/               # Layer-by-layer reasoning visualization
│   ├── README.md                      # Detailed project documentation
│   ├── logit_lens.py                  # Main script
│   ├── generate_heatmap_mock.py       # Mock data generator
│   ├── project2_logit_lens.png        # Generated heatmap
│   ├── requirements.txt               # Project-specific dependencies
│   ├── QUICKSTART.txt                 # Quick reference
│   ├── RESULTS_SUMMARY.md             # Findings summary
│   └── VERIFICATION_CHECKLIST.md      # Testing checklist
│
└── project3-pause-token/              # Pause token hypothesis test
    ├── README.md                      # Detailed project documentation
    ├── pause_token.py                 # Main script
    └── project3_pause_token.png       # Generated bar chart
```

## 🔧 Technologies Used

- **Python 3.7+** - Core programming language
- **PyTorch** - Deep learning framework
- **Transformers** - Hugging Face library for GPT-2
- **Matplotlib** - Visualization library
- **Seaborn** - Statistical visualization
- **NumPy** - Numerical computing
- **OpenAI API** - Optional for real API testing (mock mode available)

## 📝 Key Concepts

### Chain-of-Thought (CoT) Prompting
A technique where models articulate step-by-step reasoning rather than directly answering questions.

**Types**:
- **Zero-shot CoT**: "Let's think step by step"
- **Few-shot CoT**: Providing examples with reasoning steps
- **Auto-CoT**: Automatically generating diverse reasoning paths

### Explicit vs Latent Reasoning
- **Explicit**: Model outputs visible reasoning steps (accurate but expensive)
- **Latent**: Model reasons internally without output (goal: maintain accuracy, reduce cost)

### Logit Lens
A technique to "peek inside" transformer layers by projecting hidden states through the language model head, revealing how confidence builds progressively.

## 🎯 Use Cases

### For Researchers
- Understand CoT mechanisms and trade-offs
- Replicate and extend experiments
- Explore new reasoning techniques
- Benchmark different models

### For Practitioners
- Optimize prompting strategies for production
- Balance cost vs accuracy in deployed systems
- Debug model reasoning behavior
- Improve prompt engineering skills

### For Students
- Learn about LLM reasoning mechanisms
- Hands-on experience with transformers
- Practical ML experimentation
- Reproducible research examples

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- Test on different models (GPT-4, Claude, Llama)
- Add more reasoning benchmarks
- Extend to other domains (code, science, logic)
- Improve visualizations
- Add interactive demos

## 📚 References

**Key Papers**:
- Wei et al. (2022) - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Kojima et al. (2022) - "Large Language Models are Zero-Shot Reasoners"
- nostalgebraist (2020) - "Interpreting GPT: the Logit Lens"

**Related Research**:
- Tree-of-Thought (ToT)
- Graph-of-Thought (GoT)
- Self-Consistency Decoding
- Constitutional AI

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Created as part of the Research Tsinghua project series.

## 🙏 Acknowledgments

- Hugging Face for the Transformers library
- OpenAI for GPT models and research
- The research community for advancing interpretability

---

**Questions or improvements?** Feel free to open an issue or submit a pull request!

## 📈 Project Statistics

- **Lines of Code**: ~2,000
- **Projects**: 3 complete implementations
- **Visualizations**: 3 publication-ready figures
- **Documentation**: Comprehensive READMEs for each project
- **Mock Mode**: All projects runnable without API keys

---

⭐ **Star this repo** if you find it helpful for your research or learning!
