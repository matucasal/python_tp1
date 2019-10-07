grammar Logica;

logica :
    predicado+
    ;

predicado :
      a=conjuncion {print($a.res)}
    | b=disyuncion {print($b.res)}
    ;

conjuncion returns [boolean res]:
      a=value op_and b=value {$res=$a.res and $b.res}
    ;

disyuncion returns [boolean res]:
      a=value op_or b=value {$res=$a.res or $b.res}
    ;

op_and: 
      'and'
    | 'y'
    | '&'
    ;
op_or:
      'or'
    | 'o'
    | '|'
    ;

value returns [boolean res]:
      'true' {$res=True}
    | 't'    {$res=True}
    | 'v'    {$res=True}
    | 'false'{$res=False}
    | 'f'    {$res=False}
    ;

WS : [ \r\n\t] -> skip;