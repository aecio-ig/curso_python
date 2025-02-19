# Format

a = 'A' 
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'


## Passando argumeto que é diferente de parametro
formato = string.format(a, b, c)
print(formato)

## Aqui vamos utilizar parametro passando o nome que deve ser passado o parametro no format
string = 'a={param_a} b={param_b} c={param_c:.2f}'
formato = string.format(param_a=a, param_b= b, param_c=c)
print(formato)

