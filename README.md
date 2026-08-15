# Supermarket Sales Analysis

## Overview

This project focuses on analyzing and cleaning supermarket sales data using Python. The analysis explores sales performance, profitability, customer behavior, payment methods, and customer satisfaction.

The dataset contains transactional information about supermarket purchases, including product categories, branches, customer types, payment methods, sales, costs, and ratings.

## Objectives

The main objectives of this project are to:

- Clean and prepare the supermarket sales dataset.
- Handle missing values and duplicate records.
- Identify and remove redundant or unnecessary columns.
- Analyze total revenue and profitability.
- Compare revenue and profit across branches and product categories.
- Analyze customer spending behavior.
- Identify the most popular payment method.
- Calculate the average transaction value.
- Analyze customer satisfaction across branches.
- Examine sales patterns by day and month.
- Present the findings using data visualizations.

## Dataset

The dataset contains supermarket transaction records with information such as:

- Invoice ID
- Branch
- City
- Customer Type
- Gender
- Product Line
- Unit Price
- Quantity
- Tax
- Sales
- Date
- Time
- Payment Method
- Cost of Goods Sold (COGS)
- Gross Margin Percentage
- Customer Rating

## Data Cleaning

The data preparation process includes:

- Checking the dataset structure and data types.
- Identifying missing values.
- Handling missing sales and unit price values.
- Removing duplicate records.
- Converting sales values into numerical format.
- Converting dates into the appropriate datetime format.
- Removing redundant columns.
- Standardizing payment method values.
- Creating additional columns required for analysis.

## Analysis

The project analyzes several key business questions, including:

### Revenue Analysis
- What is the total revenue?
- Which city generates the highest revenue?
- How does revenue vary across product categories?

### Profitability Analysis
- What is the total profit?
- Which branch is the most profitable?
- Which product category generates the highest profit?

### Customer Analysis
- Which customer type spends more?
- What is the average transaction value?
- What percentage of customers are satisfied?

### Payment Analysis
- Which payment method is most commonly used?

### Sales Trends
- How do sales vary by day of the month?
- How do sales vary by month?

### Customer Satisfaction
- Which branch has the highest average customer rating?
- What is the overall customer satisfaction level?

## Visualizations

Several visualizations are used to make the results easier to understand, including:

- Bar charts
- Grouped bar charts
- Pie charts
- Box plots

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
supermarket-sales-analysis/
│
└── SupermarketAnalysis.ipynb
