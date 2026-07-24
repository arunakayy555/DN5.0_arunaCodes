# Digital Nurture 5.0 — Deep Skilling (Python FSE)
## Week 1: Engineering Concepts — Design Patterns & Data Structures/Algorithms

This repo contains hands-on exercises for **Module 1 (Design Patterns and
Principles)** and **Module 2 (Data Structures and Algorithms)**, the
Week 1 deliverables of the DN 5.0 Deep Skilling program.

Every file is self-contained, runnable, and includes inline
`assert`-based checks so you can verify correctness without a separate
test runner.

## 📁 Structure

```
week1-deepskilling/
├── module1_design_patterns/
│   ├── solid/
│   │   ├── srp_example.py      # Single Responsibility Principle
│   │   ├── ocp_example.py      # Open/Closed Principle
│   │   ├── lsp_example.py      # Liskov Substitution Principle
│   │   ├── isp_example.py      # Interface Segregation Principle
│   │   └── dip_example.py      # Dependency Inversion Principle
│   └── patterns/
│       ├── creational/
│       │   ├── singleton.py
│       │   ├── factory_method.py
│       │   └── builder.py
│       ├── structural/
│       │   ├── adapter.py
│       │   ├── decorator.py
│       │   └── proxy.py
│       └── behavioral/
│           ├── observer.py
│           ├── strategy.py
│           └── command.py
├── module2_dsa/
│   ├── arrays/
│   │   └── array_operations.py     # traverse, max, reverse, rotate, dedupe
│   ├── searching/
│   │   ├── linear_search.py
│   │   └── binary_search.py
│   ├── sorting/
│   │   ├── bubble_sort.py
│   │   ├── quick_sort.py
│   │   └── merge_sort.py
│   └── complexity_analysis/
│       └── notes.md                # Big-O cheat sheet for all algorithms above
├── .gitignore
└── README.md
```

## ▶️ How to run

Requires Python 3.8+. No external dependencies — standard library only.

Run any file directly, e.g.:

```bash
python module1_design_patterns/solid/srp_example.py
python module1_design_patterns/patterns/creational/singleton.py
python module2_dsa/sorting/merge_sort.py
```

Each script prints example output and then runs its own `assert`
checks, printing a confirmation line (e.g. `All SRP checks passed.`)
if everything works.

To run everything at once:

```bash
find . -name "*.py" -exec python {} \;
```

## 📚 Topics covered

**Module 1 — Design Patterns and Principles**
- SOLID Principles: SRP, OCP, LSP, ISP, DIP
- Creational Patterns: Singleton, Factory Method, Builder
- Structural Patterns: Adapter, Decorator, Proxy
- Behavioral Patterns: Observer, Strategy, Command

**Module 2 — Data Structures and Algorithms**
- Arrays: traversal, in-memory representation, common operations
- Searching: Linear Search, Binary Search
- Sorting: Bubble Sort, Quick Sort, Merge Sort
- Time & space complexity analysis (see `complexity_analysis/notes.md`)

## 🚀 Pushing to your own GitHub repo

```bash
cd week1-deepskilling
git init
git add .
git commit -m "DN 5.0 Deep Skilling - Week 1 exercises (Design Patterns + DSA)"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

## ✅ Program Completion Note

Per the DN 5.0 handbook's exercise instructions, solutions should be
organized week-wise and pushed to a **public** GitHub repository, with
the URL shared with the POC on demand. This structure keeps Week 1 as a
clean, self-contained folder so future weeks (Database Integration,
Unit Testing, Backend Frameworks, Frontend, QA/Selenium, Agile/Git,
Cloud, GenAI) can be added as sibling folders (`week2-...`,
`week3-...`, etc.) in the same repo.
