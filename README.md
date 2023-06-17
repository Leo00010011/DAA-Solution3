# DAA-Solution3

## El problema

## Demostratracion de NP-Completitud

Nuestro problema se puede resumir en encontrar un algoritmo que dada una expresion booleana con "and", "or", "not" e "implica" encuentre una asignación de las variables que participan tal que la evaluación de la expresion de false.

Para hablar de la complejidad computacional de nuestro problema primero deberíamos definir un encoding para expresiones booleanas. Teniendo en cuenta que estas consisten en operadores, paréntisis y literales;y la cantidad de operadores y paréntisis no debe ser mayor que dos veces la cantidad de literales, se puede decir que sea n la cantidad de literales de la expresion el tamaño de un encoding sencillo de la entrada es O(n).

Cuando comenzamos con este problema la primera idea que tuvimos fue reducir el problema de SAT (Formula Satisfiability) al nuestro. Este problema consiste en decir si existe una asignación de las variables tal que la evaluación de la expresión de true. Nuestra idea era, sea E la expresion booleana que es entrada de SAT, sustituir los operadores bicondicionales (A ssi B) por la conjunción de dos implicas ($A\Rightarrow B$ and $ B\Rightarrow A$) donde se obtendría E' (que es equivalente a la original) y después negar E'; esta nueva expresion es una entrada válida de nuestro algoritmo y si este encuentra una asignacion tal que la evaluacion da false, se encontraría una asignación tal que la evaluación de la negación de una expresión equivalente a la original es false por lo que la expresion original evaluada en esta asignacion sería true por lo que la formula sería satisfacible. Fue difícil encontrar el fallo en esta idea, pero sustituir el operador bicondicional por la conjuncion de implicas, duplica el tamaño de la expresión y se podría consrtuir una expresión como la siguiente

$$ A_1 \Leftrightarrow [A_2 \Leftrightarrow [A_3 \Leftrightarrow [...[A_{n-1}\Leftrightarrow A_n]...]] $$

Donde el tamaño de la expresion resultante de realizar la transformacion sería O($2^n$) donde n es la cantidad de literales

La alternativa que encontramos para esto fue reducir 3-CNF-SAT al problema de nosotros. 3-CNF-SAT es un caso partícular de SAT en el que la expresion se encuentra en forma normal conjuntiva con solo 3 literales por clausula. En este caso la formula negada es una entrada válida para nuestro problema y la salida sería una asignación con la que evalue false y como esta es una negación de la formula original entonces esta asignación da true en la formula original, por lo que en caso de encontrar solución la fórmula original sería satisfacible y en caso de no encotrar evaluación que de false la formula original no sería satisfacible (de ser satisfacible existiría una asignación que de true en la original y por lo tanto una que de false en su negación por lo que si nuestro algoritmo es correcto debería encontrarlo).
La reducción consiste en negar toda la expresión y como nuestro problema puede recibir como entradas fórmulas con cualquier tipo de anidaciones se puede agrupar toda la expresion en paréntesis y negar la agrupación entera es decir, sea E la formula original, la reducción sería ^[E], esto se puede efectuar en tiempo constante evidentemente. Luego como se encontró una reducción polinomial de un problema NP-Completo al nuestro entonces el nuestro es NP-Hard y asumiendo que el problema de decisión asociado al nuestro es dada una expresion booleana con "and", "or", "not" e "implica" diga si existe una asignación de las variables que participan tal que la evaluación de la expresion de false, se puede notar que este es NP pues se puede usar la asignación que da false como verificación de que existe; por lo tanto nuestro problema es NP-Completo.

## Algoritmo DPLL

DPLL es un algoritmo eficiente y completo para la satisfacibilidad booleana, que busca determinar si existe una asignaci&oacute;n de valores a las variables en una f&oacute;rmula proposicional que la haga verdadera.

Este utiliza una estrategia de b&uacute;squeda en espacio de estados para explorar sistem&aacute;ticamente las posibles asignaciones de valores a las variables. Basado en la idea de la resoluci&oacute;n por unit propagation (clausulas de 1 solo literal) y la eliminaci&oacute;n de literales puros(literales que solo aparecen de 1 sola forma en toda la expresi&oacute;n), DPLL es capaz de reducir el espacio de b&uacute;squeda de manera significativa, evitando explorar ramas innecesarias.

En nuestra implementaci&oacute;n del algoritmo, este recibe una expresi&oacute;n booleana que esta en CNF. Para esto se crea un archivo .txt y se escribe la f&oacute;rmula en CNF con el siguiente formato:

- Cada l&iacute;nea del .txt es una cl&aacute;usula, donde los literales est&aacute;n separados por espacio. No hace falta poner par&eacute;ntesis. Para negar un literal se usa el caracter '!'. Ver ejemplo del archivo sample1.txt y su resultado en output_sample1.txt .

En el archivo output.txt se guardan los pasos de cada iteraci&oacute;n, como se va reduciendo la CNF. Al final se devuelve si fue SATISFIABLE o UNSATISFIABLE. Para añadir otro archivo .txt con una nueva expresi&oacute;n booleana basta con cambiar en el c&oacute;digo la variable 'filename' y poner el nombre del archivo con la extensi&oacute;n(.txt).

A continuaci&oacute;n le mostramos el pseudoc&oacute;digo:

![DPLL](/dpll_pseudocode.jpg)

### Demostraci&oacute;n de correctitud de DPLL

El algoritmo DPLL es un backtrack con podas. En el peor caso chequea todos los literales y su negaci&oacute;n con una complejidad temporal de O(2^n). La poda que aplica es aquellos literales que est&eacute;n en una cl&aacute;usula unitaria tienen que tomar valor True necesariamente, para que la f&oacute;rmula sea satisfacible. Luego, elimina las cláusulas que contienen el literal seleccionado, porque al ser una disyunci&oacute;n de literales, con al menos uno que sea True es suficiente. De las otras cl&aacute;, se elimina el opuesto del literal (si lo contienen), porque al ser False no se completa que la cl&aacute;usula sea verdadera. Esto deriva a que si se llega a una cl&aacute;usula vac&iacute;a es porque todos los literales que conten&iacute;n dieron False y por tanto, con la asignaci&oacute;n actual de literales no se llega a una satisfacer la f&oacute;rmula. Por tanto, por lo antes explicado, las soluciones que descarta la poda no son soluciones factibles.

## K-approximati&oacute;n

Una k-aproximaci&oacute;n es un algoritmo para resolver problemas de optimizaci&oacute;n, donde se quiere encontrar una soluci&oacute;n que se acerque al &oacute;ptimo en un factor de aproximaci&oacute;n k, o sea, como m&aacute;ximo k veces peor que nuestra soluci&oacute;n &oacute;ptima.

Para nuestra implementaci&oacute;n del mismo, ofrecemos una 2-aproximaci&oacute;n del problema original. Para determinar si la expresi&oacute;n en CNF es satisfacible o no, comprobamos cu&aacute;ntas cl&aacute;usulas se eval&uacute;an True asignando valor True a todos los literales(caso I); y cuantas clausulas se hacen True dandole valor False a todos los literales(caso II).
Aquellas cl&aacute;usulas que contengan tanto literales positivos como negativos ser&aacute;n en ambas asignasiciones True. Solo en las cl&aacute;usulas de un solo tipo de literal es que ser&aacute; True en alguna de las 2 asignaciones. Este algoritmo devuelve en cada caso m&aacute;s de la mitad de las cl&aacute;usulas de la CNF.

### Demostraci&oacute;n

Demostremos esta afirmaci&oacute;n por reducci&oacute;n al absurdo.
Supongamos que en ambos casos (I) y (II), se devuelven menos de la mitad de las cl&aacute;usulas en True.
Esto quiere decir que exite al menos una cl&aacute;usula que en ambas asignaciones siempre es False. Pero esa cl&aacute;usula solo puede ser de 3 formas:

1- Solo contiene literales positivos => hubiese devuelto True en (I).
2- Solo contiene literales negativos => hubiese devuelto True en (II).
3- Contiene ambos literales => hubiese devuelto True en (I) y (II).

Contradicci&oacute;n! Luego, el algoritmo devuelve en cada caso m&aacute;s de la mitad de las cl&aacute;usulas de la CNF.

### El otro k-aprox

Debido a la simplicidad de este primer algoritmo optamos por implementar otro algoritmo que utiliza una idea greedy. La explicación de este algortimo va a utilizar la palabra "literal" para referirse a las ocurrencias de variables en las clausulas y cabe recalcar que si x es una variable entonces su ocurrencia en positivo constituye un literal y en negativo constituye otro distinto. Luego la idea del algortimo es la siguiente:

* 1:Sea S el conjutno de clausulas
* 2:Sea LIT el conjunto de todos los literales
* 3:Sea SUB = $\empty$, TRUE = $\empty$, LEFT = $S$ y LEFT = LIT
* 4:Si ningún literal en LIT está en alguna clausula de LEFT retornar SUB
* 5:Sea $y$ el literal que se encuentra en la mayor cantidad de clausulas
* 6:Sea $YT$ el conjunto de clausulas que contienen a $y$
* 7:SUB = SUB $\cup$ $YT$ , LEFT = LEFT - $YT$, TRUE = TRUE $\cup$ {$y$}, LIT = LIT $\cup$ {$y$,$\overline{y}$}
* 8: goto 2

Como se puede notar la idea es hacer TRUE el literal que se encuentra en la mayor(cabe recalcar que hacer true un literal negativo es hacer FAlSE la variable que le corresponde) cantidad de clausulas repetidamente hasta la iteración en la que las clausulas no contengan variables para hacer TRUE (solo contengan negaciones de literales que ya se hicieron TRUE)