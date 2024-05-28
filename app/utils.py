from datetime import timedelta


def calcular_dia_colheita(data_plantio, condicao):
    
    if condicao == 'seca':
        delta_mes = 18.1
         
    elif condicao == 'umida':
        delta_mes = 17
        
    elif condicao == 'normal':
        delta_mes = 17.5
          
    elif condicao == 'temp_alta':
        delta_mes = 18 
        
    elif condicao == 'temp_baixa':
        delta_mes = 17.7             
    
    dias = delta_mes * 30.44  # Aproximação do número de dias em um mês
    
    dia_colheita = data_plantio + timedelta(days=dias)
    
    return dia_colheita.strftime("%d/%m/%Y")
