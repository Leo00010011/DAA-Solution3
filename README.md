# DAA-Solution3

## El problema

# <center>La pregunta</center>

Estaba Karlos pasando (tal vez perdiendo) el tiempo cuando viene Karel y le hace una pregunta. Karlos quería responder que "no" a la pregunta, pero Karel le dijo que no era tan facil, que la respuesta a esa pregunta iba a depender de un conjunto de pequeñas preguntas de "si" o "no" que este tenía. Luego, con las respuestas a esas preguntas de "si" o "no" armó una expresión booleana conformada por negaciones, expresiones "and", expresiones "or" e implicaciones de las pequeñas preguntas. La respuesta de la pregunta grande dependería de la expresión booleana que a la vez dependía de las pequeñas preguntas. Ayude a Karlos a encontrar si existe una distribución de respuestas a las pequeñas preguntas que le permitan responder que "no" a la pregunta grande.

## Demostracion de NP-Completitud

Nuestro problema se puede resumir en encontrar un algoritmo que dada una expresion booleana con "and", "or", "not" e "implica" encuentre una asignación de las variables que participan tal que la evaluación de la expresion de false.

Para hablar de la complejidad computacional de nuestro problema primero deberíamos definir un encoding para expresiones booleanas. Teniendo en cuenta que estas consisten en operadores, paréntisis y literales;y la cantidad de operadores y paréntisis no debe ser mayor que dos veces la cantidad de literales, se puede decir que sea n la cantidad de literales de la expresion el tamaño de un encoding sencillo de la entrada es O(n).

Cuando comenzamos con este problema la primera idea que tuvimos fue reducir el problema de SAT (Formula Satisfiability) al nuestro. Este problema consiste en decir si existe una asignación de las variables tal que la evaluación de la expresión de true. Nuestra idea era, sea E la expresion booleana que es entrada de SAT, sustituir los operadores bicondicionales (A ssi B) por la conjunción de dos implicas ($A\Rightarrow B$ and $ B\Rightarrow A$) donde se obtendría E' (que es equivalente a la original) y después negar E'; esta nueva expresion es una entrada válida de nuestro algoritmo y si este encuentra una asignacion tal que la evaluacion da false, se encontraría una asignación tal que la evaluación de la negación de una expresión equivalente a la original es false por lo que la expresion original evaluada en esta asignacion sería true por lo que la formula sería satisfacible. Fue difícil encontrar el fallo en esta idea, pero sustituir el operador bicondicional por la conjuncion de implicas, duplica el tamaño de la expresión y se podría consrtuir una expresión como la siguiente

$$ A_1 \Leftrightarrow [A_2 \Leftrightarrow [A_3 \Leftrightarrow [...[A_{n-1}\Leftrightarrow A_n]...]] $$

Donde el tamaño de la expresion resultante de realizar la transformacion sería O($2^n$) donde n es la cantidad de literales

La alternativa que encontramos para esto fue reducir 3-CNF-SAT al problema de nosotros. 3-CNF-SAT es un caso partícular de SAT en el que la expresion se encuentra en forma normal conjuntiva con solo 3 literales por clausula. En este caso la formula negada es una entrada válida para nuestro problema y la salida sería una asignación con la que evalue false y como esta es una negación de la formula original entonces esta asignación da true en la formula original, por lo que en caso de encontrar solución la fórmula original sería satisfacible y en caso de no encotrar evaluación que de false, la formula original no sería satisfacible (de ser satisfacible existiría una asignación que de true en la original y por lo tanto una que de false en su negación por lo que si nuestro algoritmo es correcto debería encontrarlo).
La reducción consiste en negar toda la expresión y como nuestro problema puede recibir como entradas fórmulas con cualquier tipo de anidaciones se puede agrupar toda la expresion en paréntesis y negar la agrupación entera es decir, sea E la formula original, la reducción sería ^[E], esto se puede efectuar en tiempo constante. Luego como se encontró una reducción polinomial de un problema NP-Completo al nuestro entonces el nuestro es NP-Hard y asumiendo que el problema de decisión asociado al nuestro es dada una expresion booleana con "and", "or", "not" e "implica" diga si existe una asignación de las variables que participan tal que la evaluación de la expresion de false, se puede notar que este es NP pues se puede se puede hacer un algoritmo que use la asignación que da false para verificar que realmente da falso; por lo tanto nuestro problema es NP-Completo.

## Algoritmo DPLL

DPLL es un algoritmo completo para la satisfacibilidad booleana, que busca determinar si existe una asignaci&oacute;n de valores a las variables en una f&oacute;rmula proposicional que la haga verdadera.

Este utiliza una estrategia de b&uacute;squeda en espacio de estados para explorar sistem&aacute;ticamente las posibles asignaciones de valores a las variables. Basado en la idea de la resoluci&oacute;n por unit propagation (clausulas de 1 solo literal) y la eliminaci&oacute;n de literales puros(literales que solo aparecen de 1 sola forma en toda la expresi&oacute;n), DPLL es capaz de reducir el espacio de b&uacute;squeda de manera significativa, evitando explorar ramas innecesarias.

En nuestra implementaci&oacute;n del algoritmo, este recibe una expresi&oacute;n booleana que esta en CNF. Para esto se crea un archivo .txt y se escribe la f&oacute;rmula en CNF con el siguiente formato:

- Cada l&iacute;nea del .txt es una cl&aacute;usula, donde los literales est&aacute;n separados por espacio. No hace falta poner par&eacute;ntesis. Para negar un literal se usa el caracter '!'. Ver ejemplo del archivo sample1.txt y su resultado en output_sample1.txt .

En el archivo output.txt se guardan los pasos de cada iteraci&oacute;n, como se va reduciendo la CNF. Al final se devuelve si fue SATISFIABLE o UNSATISFIABLE. Para añadir otro archivo .txt con una nueva expresi&oacute;n booleana basta con cambiar en el c&oacute;digo la variable 'filename' y poner el nombre del archivo con la extensi&oacute;n(.txt).

A continuaci&oacute;n le mostramos el pseudoc&oacute;digo:

![DPLL](/dpll_pseudocode.jpg)

### Demostraci&oacute;n de correctitud de DPLL

El algoritmo DPLL es un backtrack con podas. En el peor caso chequea todos los literales y su negaci&oacute;n con una complejidad temporal de O($2^n$). La poda que aplica es aquellos literales que est&eacute;n solos en una cl&aacute;usula  tienen que tomar valor True necesariamente, para que la f&oacute;rmula sea satisfacible. Luego, elimina las cláusulas que contienen el literal seleccionado, porque al ser una disyunci&oacute;n de literales, con al menos uno que sea True es suficiente. De las otras cl&aacute;usulas, se elimina el opuesto del literal (si lo contienen), porque al ser False no influyen en que la cl&aacute;usula sea verdadera. Esto deriva a que si se llega a una cl&aacute;usula vac&iacute;a es porque todos los literales que contienen dieron False y por tanto, con la asignaci&oacute;n actual de literales no se llega a una satisfacer la f&oacute;rmula. En cambio si se llega a no tener clausulas es que todas llegaron a ser TRUE, pues una clausula se elimina ssi contiene al menos un literal que es TRUE. 

## K-approximaci&oacute;n

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

Debido a la simplicidad de este primer algoritmo optamos por implementar otro algoritmo que utiliza una idea greedy. La explicación de este algortimo va a utilizar la palabra "literal" para referirse a las ocurrencias de variables en las clausulas y se debe tener en cuenta que si x es una variable entonces se referira a su ocurrencia en positivo y en negativo como literales distintos. Luego la idea del algortimo es la siguiente:

* 1:Sea S el conjutno de clausulas de la forma normal conjuntiva que se recibe
* 2:Sea L el conjunto de todos los literales
* 3:Sea SUB = $\empty$, TRUE = $\empty$, LEFT = $S$ y LIT = L
* 4:Si ningún literal en LIT está en alguna clausula de LEFT retornar SUB
* 5:Sea $y$ el literal que se encuentra en la mayor cantidad de clausulas
* 6:Sea $YT$ el conjunto de clausulas que contienen a $y$
* 7:SUB = SUB $\cup$ $YT$ , LEFT = LEFT - $YT$, TRUE = TRUE $\cup$ {$y$}, LIT = LIT $\cup$ {$y$,$\overline{y}$}
* 8: goto 4

Cabe recalcar que hacer TRUE un literal negativo es hacer FALSE la variable que le corresponde. Como se puede notar la idea es hacer TRUE el literal que se encuentra en la mayor cantidad de clausulas repetidamente hasta la iteración en la que las clausulas no contengan variables para hacer TRUE (solo contengan negaciones de literales que ya se hicieron TRUE)

A continuacion vamos a demostrar que para formas normales conjuntivas con clausulas con al menos k literales distintos este algoritmo es (k + 1)/k-aprox. La demostracion se basa en varias propiedades del algoritmo:
 * La cantidad de clausulas que se hacen TRUE cuando se hace TRUE un literal es mayor o igual que la cantidad de clausulas que se quedan con el literal negado, pues el algoritmo siempre toma el literal que aparece en la mayor cantidad de clausulas
 * Si se hace TRUE un literal, la cantidad de clausulas que tienen el literal negado al final de la ejecucion del algoritmo es menor o igual a la cantidad de clausulas que hubo en el momento que se tomó el literal y por tanto es menor o igual a la cantidad de clausulas que se hicieron TRUE al hacer TRUE el literal
 * Como se hizo notar en la explicacion de del funcionamiento del algoritmo, cuando el algoritmo termina las clausulas que quedan en LEFT cumplen que estan constituidas por negaciones de literales que fueron tomados en las iteraciones anteriores
 * Como se sabe que cada clausula tiene al menos k literales distintos al terminar el algoritmo hay al menos k*|LEFT| literales distintos negados
 * Como la cantidad de clausulas que se hicieron positivas en el momento que se tomo el literal es mayor que la cantidad de negaciones de ese literal en las clausulas en LEFT al final del algoritmo, y como se sabe que la negacion de cada literal que quedo en las clausulas de LEFT al final del algoritmo fue hecha TRUE en algun momento de la ejecución entonces |SUB| $\geq$ k*|LEFT|
 * Luego sea $|S*|$ la cantidad de clausulas de la solución óptima y $|S|$ la cantidad de clausulas de la entrada del algoritmo entonces por definicion se tiene
 $$ |S*| \leq |S|$$
 $$|S*| \leq |LEFT| + |SUB|$$
 $$|S*| \leq \frac{|SUB|}{k} + |SUB|$$
 $$|S*| \leq \frac{k + 1}{k}|SUB|$$

 Por lo que queda demostrado que para ese k es una (k + 1)/k-aprox