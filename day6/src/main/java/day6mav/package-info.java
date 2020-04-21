package day6mav;

/*
Дописать/изменить структуру кода (task http://jira.it-academy.by:8080/browse/ATYG-1):



Общая структура:

package entity
--AutomatedTest
--ManualTest
--Result
--Test
--TestLevel
package worker
--AutomationEngineer
--Engineer
--TestEngineer

Подробности:

- в классах POJO поля должны быть private или protected и иметь соответствующие getters и setters
- класс Engineer должен быть абстрактный
- класс Engineer должен иметь метод public Result executeTest(Test test)
- класс Engineer должен иметь поле int skill, инициализирующееся случайным числом от 1 до 10 включительно
- класс Engineer должен иметь поле int anxiety = 3
- класс Engineer должен иметь 2 производных класса AutomationEngineer и TestEngineer, дополнительные свойства не обязательны
- enum TestLevel, имеющий публичную константу int COMPLEXITY и имеющий значения UNIT(1), API(3), GUI(9)
- enum Result меющий значения PASSED, FAILED;
- класс Test должен быть абстрактный
- класс Test должен иметь поля int complexity (инициализируется в конструкторе класса) и int instability (инициализируется в конструкторе производного класса)
- класс Test должен иметь конструктор принимающий аргумент типа TestLevel и инициализирующий поле complexity
- класс Test должен иметь 2 производных класса AutomatedTest и ManualTest
- класс Test должен иметь реализовывать интерфейс Function<Engineer, Result>, при этом переопределенный метод apply должен:
-- иметь локальную переменную int anxiety
-- присвоить локальной переменной anxiety значение anxiety в экземпляре класса производного Engineer в случаях:
--- если данный экземпляр Test является экземпляром класса ManualTest и данный экземпляр Engineer является экземпляром AutomationEngineer
--- если данный экземпляр Test является экземпляром класса AutomatedTest и данный экземпляр Engineer является экземпляром TestEngineer
-- в противном случае присвоить локальной переменной anxiety значение равное 1
-- в случае, если произведение complexity, instability и anxiety больше 30, вернуть FAILED
-- в противном случае вернуть PASSED
- все изменения сделать в отдельной ветке
- готовые изменения смержить в мастер
 */