import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Check data types and missing values
    print("\nDataset structure:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Clean data (though Iris dataset is already clean)
    df.dropna(inplace=True)
    
    # Task 2: Basic Data Analysis
    # Basic statistics
    print("\nBasic statistics:")
    print(df.describe())
    
    # Group by species and calculate means
    print("\nMean measurements by species:")
    print(df.groupby('species').mean())
    
    # Task 3: Data Visualization
    plt.figure(figsize=(15, 10))
    
    # 1. Line chart (using sepal length as example)
    plt.subplot(2, 2, 1)
    df['sepal length (cm)'].plot(kind='line', title='Sepal Length Trend')
    plt.ylabel('Length (cm)')
    
    # 2. Bar chart (average sepal width by species)
    plt.subplot(2, 2, 2)
    df.groupby('species')['sepal width (cm)'].mean().plot(kind='bar')
    plt.title('Average Sepal Width by Species')
    plt.ylabel('Width (cm)')
    
    # 3. Histogram (petal length distribution)
    plt.subplot(2, 2, 3)
    df['petal length (cm)'].plot(kind='hist', bins=20)
    plt.title('Petal Length Distribution')
    plt.xlabel('Length (cm)')
    
    # 4. Scatter plot (sepal length vs petal length)
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title('Sepal vs Petal Length')
    
    plt.tight_layout()
    plt.savefig('iris_analysis.png')
    plt.show()
    
    print("\nAnalysis complete. Visualizations saved as 'iris_analysis.png'")

except Exception as e:
    print(f"An error occurred: {str(e)}")
