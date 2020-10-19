Feature: Suma de python

  Scenario: Sumar usando constantes
      When hacemos 2+2
      Then obtenemos 4
      
  Scenario: Sumar usando variables
     Given x vale 2 e y vale 3
      When hacemos x+y
      Then obtenemos 5

  Scenario: Sumar tres variables
     Given x vale 2, y vale 2, z vale -4
      When hacemos x+y+z 
      Then obtenemos 0
