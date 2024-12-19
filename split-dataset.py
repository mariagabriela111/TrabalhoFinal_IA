import pandas as pd

# Carregar o dataset
file_path = 'data/100-trains-coded.csv'
df = pd.read_csv(file_path, delimiter=',')

# Identificar valores únicos na coluna 'Number_of_cars'
distinct_values = df['Number_of_cars'].unique()

# Criar lista para armazenar subconjuntos
list_df = []

# Processar e salvar subconjuntos
for value in distinct_values:
    filtered_df = df[df['Number_of_cars'] == value]
    list_df.append(filtered_df)
    
    # Salvar subconjunto como arquivo CSV
    output_path = f"subset_{value}_cars.csv"
    filtered_df.to_csv(output_path, index=False, sep=';')
    print(f"Subconjunto salvo em: {output_path}")

# Análise básica de padrões
analysis_results = []
for value, subset in zip(distinct_values, list_df):
    # Estatísticas básicas
    mean_values = subset.mean(numeric_only=True)
    mode_values = subset.mode(numeric_only=True).iloc[0]
    
    # Relação entre atributos e rótulo
    class_counts = subset['Class_attribute'].value_counts()
    class_distribution = class_counts / class_counts.sum()
    
    # Armazenar resultados
    analysis_results.append({
        'Number_of_cars': value,
        'Mean_Values': mean_values,
        'Mode_Values': mode_values,
        'Class_Distribution': class_distribution
    })

# Exibir análise de padrões
for result in analysis_results:
    print(f"Análise para Number_of_cars = {result['Number_of_cars']}:")
    print("Médias dos atributos:")
    print(result['Mean_Values'])
    print("Moda dos atributos:")
    print(result['Mode_Values'])
    print("Distribuição da classe (leste/oeste):")
    print(result['Class_Distribution'])
    print("-")
