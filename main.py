import pandas as pd
def main():
    # Asumiendo que el archivo se descargó en la misma carpeta con el nombre 'heart_attack_data.csv'
    data_path = 'data/heart_attack_prediction_dataset.csv'
    data = pd.read_csv(data_path)

    # Mostrar las primeras 5 filas del DataFrame
    data.head()

    # Mostrar las últimas 5 filas del DataFrame
    data.tail()


if __name__ == '__main__':
    main()
