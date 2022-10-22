CAPITAL_PORT_BOLSA = 25
CAPITAL_PORT_CRYPTO = 20
SL_BOLSA = 10
SL_CRYPTO = 15

def print_title():
    print('''\n####################################################################################
######################### CALCULADORA GESTION DE RIESGO LUIS #######################
####################################################################################\n''')


def param_input():
    capital = float(input("Inserte capital total de la cuenta (€): "))
    portion_capital = float(input("Inserte porcentaje por operación (%): "))
    stop_loss = float(input("Inserte distancia stop loss (%): "))
    return capital, portion_capital, stop_loss


def risk_management(cap: float, market: str):
    """Function to risk management

    Args:
        cap (float): Capital to manage.
        market (str): Market selected to risk management.
    """
    if market == 'bolsa':
        percentage_capital = CAPITAL_PORT_BOLSA/100
        stop_distance = SL_BOLSA/100
    elif market == 'crypto':
        percentage_capital = CAPITAL_PORT_CRYPTO/100
        stop_distance = SL_CRYPTO/100
    else:
        print('Error with selected market')
        exit(1)
    cap_x_op = cap*percentage_capital
    risk_x_op = cap_x_op*stop_distance
    perc_risk_op = (risk_x_op*100)/cap
    total_op = cap/risk_x_op
    print_result(cap_x_op, risk_x_op, perc_risk_op, total_op)
    print(f'Parametros usados - %Capital: {percentage_capital*100}  SL: {stop_distance*100}')


def print_result(capital_x_operation, risk_x_operation, percentage_risk_op, total_op):
    print(f'\nCapital por operación: {capital_x_operation} (€)')
    print(f'Riesgo Capital por operación: {risk_x_operation} (€)')
    print(f'Riesgo capital: {percentage_risk_op} (%)')
    print(f'Total operations: {total_op} \n')


def main():
    print_title()
    resp = input('¿Quiere personalizar? (si/no): ')
    if resp == 'si':
        cap, port_cap, sl = param_input()
        percentage_capital = port_cap/100
        stop_distance = sl/100
        capital_x_operation = cap*percentage_capital
        risk_x_operation = capital_x_operation*stop_distance
        percentage_risk_op = (risk_x_operation*100)/cap
        total_op = cap/risk_x_operation
        print_result(capital_x_operation, risk_x_operation, percentage_risk_op, total_op)
    else:
        fix = input('Es para bolsa (b) o cryptos (c)? (b/c): ')
        capital = float(input("Inserte capital total de la cuenta (€): "))
        if fix == 'b':
            risk_management(capital, 'bolsa')
        elif fix == 'c':
            risk_management(capital, 'crypto')
        else:
            print('Introduzca correctamente el parametro. (b/c)')

if __name__ == '__main__':
    main()
