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

El algoritmo DPLL. DPLL es un algoritmo eficiente y completo para la satisfacibilidad booleana, que busca determinar si existe una asignación de valores a las variables en una fórmula proposicional que la haga verdadera.

Este utiliza una estrategia de búsqueda en espacio de estados para explorar sistemáticamente las posibles asignaciones de valores a las variables. Basado en la idea de la resolución por unit propagation (clausulas de 1 solo literal) y la eliminación de literales puros(literales que solo aparecen de 1 sola forma en toda la expresion), DPLL es capaz de reducir el espacio de búsqueda de manera significativa, evitando explorar ramas innecesarias.

En nuestra implementacion del algoritmo, este recibe una expresion booleana que esta en CNF. Para esto se crea un archivo .txt y se escribe la formula en CNF con el siguiente formato:

- Cada linea del .txt es una clausula, donde los literales estan separados por espacio. No hace falta poner parentesis. Para negar un literal se usa el caracter '!'. Ver ejemplo del archivo sample1.txt y su resultado en output_sample1.txt .

En el archivo output.txt se guardan los pasos de cada iteracion, como se va reduciendo la CNF. Al final se devuelve si fue SATISFIABLE o UNSATISFIABLE. Para añadir otro archivo .txt con una nueva expresion booleana basta con cambiar en el codigo la variable 'filename' y poner el nombre del archivo con la extension(.txt).

A continuacion le mostramos el pseudocodigo:

![DPLL](/dpll_pseudocode.jpg)
