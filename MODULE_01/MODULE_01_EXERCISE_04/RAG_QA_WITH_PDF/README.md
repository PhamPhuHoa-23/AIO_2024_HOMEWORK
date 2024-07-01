# RAG - QA WITH PDF

This repository contains a project for implementing a Retrieval-Augmented Generation (RAG) Question Answering system with PDF documents as part of Module 01 Exercise 04 for the AIO 2024 Homework series.

## What is RAG?

Retrieval-Augmented Generation (RAG) is a model that leverages retrieved documents to generate more accurate and contextually relevant answers to queries. This approach combines retrieval-based and generation-based techniques for question answering.

## Project Structure

- **scripts/**
  - **app.py**: Main application script for running the RAG QA system.
  
- **notebooks/**
  - **Chainlit.ipynb**: Jupyter notebook for experimenting with Chainlit.
  - **RAG.ipynb**: Jupyter notebook for implementing and testing the RAG QA system.
  
- **documents/**
  - **YOLOv10_Tutorials.pdf**: Example PDF document used for QA.

## Features

- **RAG Question Answering**: Implements a RAG QA system that can answer questions based on information retrieved from PDF documents.
- **PDF Processing**: Processes and extracts text from PDF documents for retrieval and QA.
- **Interactive Notebooks**: Provides Jupyter notebooks for experimentation and development.

## Installation

To install the required packages, you can use:

```bash
pip install -r requirements.txt
```

# Usage

To run the RAG QA system(if you have GPU), use the following command:

```bash
chainlit run app.py --host 0.0.0.0 --port 8000 &>/content/logs.txt &
```
