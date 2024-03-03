print('Jaylen Smith')
print('3/3/2024')
print('P2LAB1')
print('Assignment tests students knowledge of how to write code that performs mathematical calculations and displays information to users')

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven/miles_per_gallon)*dollars_per_gallon

if __name__ == '__main__':
    miles_per_gallon=float(input())
    dollars_per_gallon=float(input())
    
    print(driving_cost(500, miles_per_gallon, dollars_per_gallon))
    print(driving_cost(75, miles_per_gallon, dollars_per_gallon))
    print(driving_cost(20, miles_per_gallon, dollars_per_gallon))
print(f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')
