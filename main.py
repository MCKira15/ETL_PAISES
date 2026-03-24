from tabulate import tabulate
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load

def main():
    data = extract()
    data_transform = transform(data)
    encabezados = ['nombre','capital','subregion','poblacion']
    print(tabulate(data_transform, headers=encabezados,tablefmt='grid'))
    resultado = load(data_transform)
    print(f'Se insertaron {resultado} registros en la tabla paises')
    
if __name__ == "__main__":
    main()