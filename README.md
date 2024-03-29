Предыстория
------------

Владелец крупного магазина, для которого вы писали ПО, захотел повысить привлекательность своего магазина для клиентов. Для этого он решил внедрить систему скидок. Но вот беда, кассовые аппараты в магазине не умеют подсчитывать итоговую стоимость покупок с учётом действующих скидок. Поэтому владелец магазина решил снова обратиться к Вам за помощью (естесственно, не бесплатной).

Перед Вами стоит задача разработать такую программу, которая умеет рассчитывать общую стоимость покупок с учётом скидок. Беда в том, что скидки не даются просто так. Суть их в том, что скидка предоставляется при покупке определённого количества товара. Например покупатель может приобрести пачку макарошек за 1 р., а при покупке 3-х сразу каждая упаковка обойдётся ему в
90 к. Таким образом вместо 3 рублей, будет потрачено 2 рубля 70 копеек.

Возможен также вариант, прикотором покупая одну единицу товара, вторую покупатель получает бесплатно.

## Начальные условия
1. Список товаров. Для простоты товары можно обозначать буквами A, B, C и т.д. или любым другим удобным способом.
2. Стоимость единицы товара.
3. Правила расчёта стоимости.

Для правил можно использовать нотацию вида:

 - 2 за 120 для обозначения стоимости при покупке нескольких единиц товара
 - 2 + 1 для обозначения нулевой стоимости при покупке определённого количества единиц товара

## Ожидаемый результат
В результате у вас должна получиться программа, в которую можно загрузить набор правил для расчёта стоимости определённых товаров. После того как программа получит набор правил, ей можно передавать списки товаров (т.е. содержимое чеков покупателей), а она должна рассчитывать итоговую стоимость с учётом переданных ранее правил.

Подразумевается, что список товаров известен заранее.
