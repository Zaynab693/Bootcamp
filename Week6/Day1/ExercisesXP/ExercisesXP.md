#Exercise 1: Defining the Problem and Data Collection for Loan Default Prediction
Problem Statement

The objective of this project is to predict whether a loan applicant will default on a loan, where the target variable is the loan default status (default or non-default).
This prediction will support credit approval decisions and risk management by helping financial institutions identify high-risk borrowers before granting loans.

Data Types Required

Personal applicant data such as age, marital status, education level, and employment status are required because they provide demographic context that can correlate with financial stability.
Financial data including annual income, monthly expenses, and existing debts are essential because they directly reflect the applicant’s ability to repay the loan.
Loan-related information such as loan amount, loan term, interest rate, and loan purpose is needed because these factors influence repayment difficulty and borrower behavior.
Credit history data such as credit score, previous defaults, number of late payments, and debt-to-income ratio are critical because past financial behavior is a strong predictor of future default risk.

Data Sources

Financial institution internal records can provide loan applications, repayment histories, and transaction data through secure internal databases.
Credit bureaus can supply standardized credit scores and detailed credit histories that are integrated using applicant identifiers.
Applicant-provided information can be collected during the loan application process through digital or paper forms.
Public datasets from platforms such as Kaggle or the UCI Machine Learning Repository can be used for model development and benchmarking when internal data is unavailable.

Risks and Constraints

This project must address privacy and regulatory constraints such as data protection laws and consent requirements when handling personal financial data.
Data quality issues such as missing values, reporting errors, and outdated credit information may affect model accuracy.
Sampling bias may occur if historical data underrepresents certain demographic groups, leading to unfair predictions.
Strong governance policies are required to ensure transparency, explainability, and ethical use of the model in decision-making.

#Exercise 2: Feature Selection and Model Choice for Loan Default Prediction
Selected Features

The most relevant features for predicting loan default are credit_score, debt_to_income, annual_income, loan_amount, interest_rate, employment_length, num_delinquencies, and total_utilization.

Justification of Selected Features

The credit score is a strong indicator of an applicant’s historical creditworthiness and repayment behavior.
The debt-to-income ratio reflects how much of the applicant’s income is already committed to debt obligations, which directly affects repayment capacity.
Annual income provides insight into the borrower’s financial stability and ability to meet loan payments.
The loan amount is important because larger loans generally increase repayment risk.
The interest rate influences monthly payments and borrower burden, making higher rates more likely to lead to default.
Employment length indicates income stability, as longer employment typically correlates with consistent earnings.
The number of delinquencies captures past repayment issues, which are strong predictors of future defaults.
Total credit utilization reflects how heavily the borrower relies on existing credit, signaling financial stress.

Excluded Features

Geographical features such as state and zip code are excluded because they may introduce bias without adding strong predictive value.
Application type is excluded because it often correlates with other variables already captured, such as income and loan size.

Encoding and Imputation

Categorical variables such as home ownership and loan purpose would be encoded using one-hot encoding to avoid introducing ordinal assumptions.
Missing values would be imputed using median values for numerical features and the most frequent category for categorical features to preserve data consistency.

#Exercise 3: Training, Evaluating, and Optimizing the Model

For loan default prediction, I would select Logistic Regression and Gradient Boosting (e.g., XGBoost) as candidate models because they perform well on binary classification problems and handle non-linear relationships effectively.
The dataset would be split into training, validation, and test sets using stratified sampling to preserve class proportions, and cross-validation would be applied to ensure robust evaluation.
Model performance would be evaluated using precision, recall, F1-score, ROC-AUC, and PR-AUC to capture both predictive accuracy and risk sensitivity.
The decision threshold would be selected based on the business objective, prioritizing recall to minimize false negatives when default risk is costly.
Class imbalance would be handled using class weights or resampling techniques such as SMOTE to ensure minority default cases are properly learned.
Hyperparameter tuning would be performed using grid search within cross-validation while strictly separating training and validation data to prevent data leakage.

#Exercise 4: Designing Machine Learning Solutions for Specific Problems

Predicting Stock Prices is best addressed using supervised learning with time-series regression models because historical prices and indicators are used to predict future values.
The input data consists of historical stock prices and market indicators, the output is a predicted future price, and the learning objective is to minimize prediction error.

Organizing a Library of Books is best solved using unsupervised learning, specifically clustering or topic modeling, because labeled genres may not be available.
The input data consists of book metadata or text embeddings, the output is groups of similar books, and the objective is to maximize similarity within clusters.

Programming a Robot to Navigate a Maze is best handled using reinforcement learning because the agent must learn optimal actions through interaction with the environment.
The input data consists of the robot’s state and environment feedback, the output is a sequence of actions, and the objective is to maximize cumulative reward by reaching the goal efficiently.

##Exercise 5: Designing an Evaluation Strategy for Different ML Models
Supervised Learning Evaluation

For a supervised classification model, performance would be evaluated using stratified cross-validation and metrics such as accuracy, precision, recall, F1-score, ROC-AUC, and PR-AUC.
ROC curves and precision-recall curves would be used to analyze threshold sensitivity and class imbalance effects.
A key challenge in supervised evaluation is selecting metrics that align with real business costs rather than overall accuracy.

Unsupervised Learning Evaluation

For an unsupervised clustering model, effectiveness would be assessed using silhouette score, inertia, and the elbow method to evaluate cluster cohesion and separation.
Diagnostic plots such as silhouette plots would be used to visualize cluster quality.
A major challenge in unsupervised evaluation is the absence of ground truth labels, making interpretation subjective.

Reinforcement Learning Evaluation

For a reinforcement learning model, success would be measured by tracking cumulative reward over episodes and observing convergence behavior.
Exploration versus exploitation balance would be monitored to ensure stable learning and avoid premature convergence.
The primary challenge in reinforcement learning evaluation is that performance can vary significantly due to stochastic environments and training instability.