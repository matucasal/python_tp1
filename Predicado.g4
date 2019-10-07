grammar Predicado;
// agregar: resta, dividir, potencia
statement:
    e=expression                {print('Result: ' + str($e.value))}
    ;

expression returns [boolean value]: 
      t=term                    {$value = $t.value}
    | t1=term '==' t2=term   {$value = $t1.value == $t2.value }
    | t1=term '!=' t2=term   {$value = $t1.value != $t2.value }
    | t1=term '>=' t2=term   {$value = $t1.value >= $t2.value }
    | t1=term '<=' t2=term   {$value = $t1.value <= $t2.value }
    | t1=term '<' t2=term   {$value = $t1.value < $t2.value }
    | t1=term '>' t2=term   {$value = $t1.value > $t2.value }
    ;

term returns [int value]:
      f=factor                  {$value = $f.value}
    ;

factor returns [int value]:
      NUMBER                    {$value = int($NUMBER.text)}
    ;



NUMBER : DIGIT+;
DIGIT  : [0-9];

WS : [ \r\n\t] -> skip;
