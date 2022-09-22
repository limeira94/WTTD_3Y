import pytest

'''
Faça um programa que receba uma palavra e um caracter 
e substitua todas as vogais da palavra
pelo caracter
'''

def troca_vogal(palavra, caracter):
    
    
    for vogal in 'aeiouAEIOU':
        if vogal in palavra:
            palavra = palavra.replace(vogal, caracter)
            
    return palavra    
    
# quando definimos uma função para teste lembrar de colocar test + nome da função
def test_troca_vogal():
    assert troca_vogal('python', '@') == 'pyth@n'
    assert troca_vogal('a', '@') == '@'
    assert troca_vogal('aa', '@') =='@@'
    assert troca_vogal('Joao', '@') == 'J@@@'
    assert troca_vogal('pythOn', '@') == 'pyth@n'

if __name__ == "__main__":
    pytest.main(['-svv', __file__])

print(troca_vogal('Felipe', 'L'))