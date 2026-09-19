# From Data to AI

### A personal learning repository for exploring Data Science, Machine Learning, and AI Engineering.

**From Data to AI** is my personal learning repository, built while exploring different areas of Data Science, Machine Learning, and AI engineering.

What started with the fundamentals gradually branched into different areas as I became interested in how things work beneath the surface — from statistics and classical machine learning to NLP, computer vision, deep learning, deployment, MLOps, and AI agents.

This repository brings that exploration together in one place through **notebooks, implementations, experiments, and supporting resources**.

It is primarily intended as a **searchable learning resource**. You don't need to follow it from beginning to end. If you need to revisit a concept, explore a new topic, or see how something is implemented, find the relevant section and dive in.

---

## What You'll Find

### Machine Learning

**Fundamentals · Regression · Classification · Unsupervised Learning · PCA · Pipelines · Explainability · From-Scratch Implementations**

The most extensive section of the repository, with detailed notebooks covering core ML concepts and focused implementations beyond the fundamentals.

### Deep Learning

**Deep Learning · PyTorch · Image Classification**

Introductory Deep Learning material and the _Is It a Hotdog?_ image-classification exercise. This is also one of the areas I am currently exploring further.

### Computer Vision

**OpenCV · Image Processing · Video Processing · Face Detection · Contours · Histograms · Transformations**

A collection of hands-on implementations covering fundamental Computer Vision operations and techniques.

### Natural Language Processing

**NLP · NLTK · spaCy · Text Processing · Custom NLP Models**

Multiple notebooks and supporting artifacts exploring different approaches to Natural Language Processing.

### Data

**MySQL · Power BI · Web Scraping · BeautifulSoup · Selenium**

Learning material and practical examples around data handling, analysis, visualization, and collection.

### Deployment

**Flask · Streamlit**

Introductory work around turning Python-based work into interactive applications.

### MLOps

**DVC · Data Version Control**

Introductory experimentation with tools and workflows used around machine learning development.

### AI Agents & LangGraph

**LangGraph · AI Agents · Agent Workflows · Jupyter Notebook Experiments**

Multiple agent implementations and experiments exploring different approaches to building graph-based AI agents.

### Python

**Object-Oriented Programming**

Foundational Python OOP material supporting the programming side of the repository.

---

The repository is intentionally broad. Some areas contain extensive learning material, while others are smaller collections of experiments. **The goal is not to cover every topic completely, but to provide useful material that can be explored, revisited, and built upon.**

The repository is not meant to be a fixed curriculum. It is a collection that grows as I explore more of the ecosystem.

---

# Machine Learning

Machine Learning is currently the most extensive part of the repository.

If you're starting out with ML, the **Fundamentals** section is the best place to begin. If you already know the basics, the repository can instead be used as a reference — jump directly to the concept you're looking for.

## Fundamentals

The `Fundamentals/` section contains three detailed notebooks covering a broad set of statistics and machine learning concepts.

### Part 1 — Statistics

Covers:

- Mean, Median, Mode & Range
- Mean Absolute Deviation
- Variance & Standard Deviation
- Percentiles
- Skewness
- Correlation & Covariance
- Central Limit Theorem
- Hypothesis Testing

### Part 2 — Regression

Introduces regression through concepts including:

- Train/Test Split
- Regression Analysis
- Cost Functions
- Evaluation Metrics

The notebook contains additional concepts and examples beyond this overview.

### Part 3 — Classification & Unsupervised Learning

Includes:

- Classification
- Confusion Matrix
- Imbalanced Data
- Naive Bayes
- Decision Trees
- k-Nearest Neighbors
- Support Vector Machines
- Hyperparameter Tuning
- Cross-Validation
- Unsupervised Learning

The notebooks are labeled by topic, making them useful for both learning and quickly revisiting individual concepts.

## Beyond the Fundamentals

The section also contains more focused implementations and experiments:

- **Linear Regression**
- **Principal Component Analysis (PCA)**
- **Machine Learning Pipelines**
- **Model Explainability with LIME**

Some of these go beyond simply using a model and instead focus on understanding the underlying ideas and workflows.

---

# Deep Learning

Deep Learning is one of the areas I am currently exploring more seriously.

The current section contains my introductory work with:

- Deep Learning
- PyTorch
- Image classification

It also includes an **"Is It a Hotdog?"** image-classification exercise with its supporting dataset.

This section is still being developed and will continue to expand as I work through more of Deep Learning.

---

# Computer Vision

The Computer Vision section contains hands-on OpenCV implementations covering a range of fundamental image and video-processing concepts.

Topics include:

- Reading Images & Videos
- Rescaling
- Drawing
- Bitwise Operations
- Color Spaces
- Split & Merge
- Transformations
- Smoothing
- Thresholding
- Gradients
- Histograms
- Masking
- Contours
- Face Detection

Sample images and videos used by the implementations are included alongside the examples.

---

# Natural Language Processing

The NLP section contains several notebooks exploring different approaches to working with text.

It includes:

- NLP fundamentals
- NLTK
- spaCy
- Text processing
- Custom NLP model experimentation

The repository also contains the supporting artifacts for a custom spaCy-based NLP model.

---

# Data

The Data section contains material around some of the tools and workflows that sit around the broader Data Science ecosystem.

### MySQL

Introductory MySQL learning material and SQL practice.

### Power BI

A Power BI project exploring data analysis and visualization.

### Web Scraping

Examples using:

- BeautifulSoup
- Selenium

These explore basic approaches to collecting data from the web and preparing it for further use.

---

# Deployment

The Deployment section contains introductory work with tools used to turn Python-based work into usable applications.

### Flask

Basic Flask application development, including templates and application structure.

### Streamlit

Learning material and experimentation with Streamlit applications.

---

# MLOps

The MLOps section currently contains introductory experimentation with **DVC (Data Version Control)**.

It is currently a smaller section of the repository, but is included as part of the broader exploration of the ML engineering ecosystem.

---

# AI Agents & LangGraph

The LangGraph section contains several experiments exploring **AI agents and graph-based workflows**.

It includes multiple agent implementations, different approaches to building agents, and Jupyter Notebook experimentation.

This section is more experimental and less structured than the Machine Learning Fundamentals material, but it contains several different implementations that can be useful when exploring how agent-based systems are built.

---

# Python

The repository also contains Python Object-Oriented Programming material in:

```text
OOPS.py
```

This covers foundational OOP concepts that support the programming side of the work throughout the repository.

---

# How to Explore

There is no prescribed order.

The repository can be approached in two ways:

**Learning something new**

Start with the area you're interested in and work through the available notebooks and implementations.

**Looking something up**

Treat the repository like a technical reference. Search for the concept, open the relevant notebook or implementation, and use it as a starting point for revisiting the idea.

If you're new to Machine Learning specifically, start with:

`Machine-Learning → Fundamentals`

The Fundamentals notebooks provide a broad base in statistics, regression, classification, and unsupervised learning before moving into more focused topics.

---

# Learning Resources

Most of the material in this repository was created while following **external tutorials, courses, documentation, and other learning resources**.

This repository is transparent about that: it is a collection of learning implementations and experiments, not a claim that all of the material here was created from scratch.

I'm gradually compiling the original resources used for each section so that anyone interested in going deeper can follow the sources directly.

| Area                  | Learning Resource                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Machine Learning      | [Data Science Full Course for Beginners - WsCube Tech](https://www.youtube.com/watch?v=gDZ6czwuQ18)                            |
| Deep Learning         | [Practical Deep Learning for Coders - Jeremy Howard](https://www.youtube.com/playlist?list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU) |
| Computer Vision       | [OpenCV Course - freeCodeCamp.org](https://www.youtube.com/watch?v=oXlwWbU8l2o)                                                |
| NLP                   | [Natural Language Processing with spaCy & Python - freeCodeCamp.org](https://www.youtube.com/watch?v=dIUTsFT2MeQ)              |
| LangGraph / AI Agents | [LangGraph Complete Course for Beginners - freeCodeCamp.org](https://www.youtube.com/watch?v=jGg_1h0qzaM)                      |
| Deployment            | [Complete Streamlit course for python developers - Chai aur Code](https://www.youtube.com/watch?v=yKTEC1Y5bEQ)                 |
| MLOps                 | _To be added_                                                                                                                  |
| Data / Web Scraping   | [Seleninum Tutorial for Beginners using Python - CodeWithHarry](https://www.youtube.com/watch?v=XI5_nsClCYI&t=675s)            |

If you recognize a resource that hasn't been credited yet, feel free to open an issue or pull request.

---

# Open Source & Contributions

This repository is open to improvements.

If you find an error, have a better implementation, want to improve the organization, or have something useful to add, feel free to contribute.

**Fork → improve → open a Pull Request.**

The idea is simple: the repository can become more useful as more people learn from it and contribute back to it.

---

# Keep Exploring

This repository will continue to evolve as I explore more of the AI and ML ecosystem.

There will always be something else to learn, another implementation to understand, or another branch of the tree worth exploring.

If you find something useful here, **star the repository**, share it with someone who's learning, or open an issue with a suggestion.

And if you're exploring something in the same space, I'd be interested to hear what you're working on.

**From Data to AI — one branch at a time.**
