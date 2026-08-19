from calculadora import soma, subtracao, multiplicacao, divisao

def testSoma():
    assert soma(5, 2) == 7
    
def testSubtracao():
    assert subtracao(5, 2) == 3

def testMultiplicacao():
    assert multiplicacao(5, 2) == 10
    
def testDivisao():
    assert divisao(10, 2) == 5
