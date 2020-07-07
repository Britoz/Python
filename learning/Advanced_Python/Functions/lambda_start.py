# Demonstrate the using of lambda function
'''
lambda (parameters) : (expression)
'''

def CelsisusToFahrenheit(temp):
    '''
    CelsisusToFahrenheit(temp) used to transfer Celsius to Fahrenheit

    :param temp: input Celsisus temperature
    :return: Fahrenheit temperature
    '''

    # TODO: return result in Fah
    return (temp * 9/5) + 32

def FahrenheitToCelsisus(temp):
    '''
    FahrenheitToCelsisus(temp) used to transfer Fahrenheit to Celsius

    :param temp: input Fahrenheit temperature
    :return: Celsius temperature
    '''

    # TODO: return result in Cel
    return (temp - 32) * 5/9

def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # TODO: Use regular functions to covert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # TODO: Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t - 32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))
    '''
    using lambda we will have 
    
    t: element of list
    after : is the fomular
    
    '''

if __name__ == '__main__':
    main()