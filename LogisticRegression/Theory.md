The **natural logarithm of e itself**, ln e, is 1, because **$e^1 = e$**.

The **natural logarithm of 1** is 0, since **$e^0 = 1$**.

**-(1-y)log(1-y_pred) - 1*log(y_pred)**

y = целевая переменная == класс 0 или 1 (если у = класс  1, то соответсвенно 1 - у = класс 0)
A Log Loss of 0 means the predicted probabilities match the actual outcomes perfectly, while higher values indicate increasing levels of deviation. Независимо от того, y_predicted равна 0 или 1, результат формулы лосса (выше) - будет 0, то есть 0 указывает, что классификация правильная. Только отличные от 0 значения, указывают, что классификация неправильная.

1. y=0, y_pred = 0:

-(1-0)log(1-0) - 1*log(0 (!)) = -1*log(1) - (логарифм от 0 - минус бесконечность или выдает ошибку) = 0

2. y= 1, y_pred = 1:

-(1-1)log(1-1) - 1*log(1) = 0 - 0 = 0
