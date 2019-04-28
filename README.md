<div class="problem-statement">
<div class="header">
<h1 class="title">SmallData</h1>
<table>
<tbody>
<tr class="time-limit">
<td class="property-title">Ограничение времени</td>
<td>1&nbsp;секунда</td>
</tr>
<tr class="memory-limit">
<td class="property-title">Ограничение памяти</td>
<td>64Mb</td>
</tr>
<tr class="input-file">
<td class="property-title">Ввод</td>
<td colspan="1">стандартный ввод или input.txt</td>
</tr>
<tr class="output-file">
<td class="property-title">Вывод</td>
<td colspan="1">стандартный вывод или output.txt</td>
</tr>
</tbody>
</table>
</div>
<h2></h2>
<div class="legend">
<p>Зинаида очень рада, что вы отважно учились весь этот год, и приготовила несколько испытаний для вас.</p>
<p>Сперва она решила проверить, насколько хорошо вы «подружились» с функцией <span style="font-weight: bold;">filter</span> и объектом <span style="font-weight: bold;">stdin</span>.</p>
<p>Зинаида просит вас проанализировать поток «маленьких данных», полученных от низконагруженного сервера сбора статистики.</p>
<p>Вы должны получить максимальную моду (мода — наиболее часто встречающееся значение) чисел, входящих в заданный диапазон, для каждой выборки крайне важных данных.</p>
<p>Если моду, входящую в диапазон, найти невозможно, считайте её равной -1.</p>
</div>
<h2>Формат ввода</h2>
<div class="input-specification">
<p>В первой строке записано два натуральных числа X, Y.</p>
<p>Во всех последующих строках записано некоторое количество натуральных чисел, разделённых пробелами.</p>
</div>
<h2>Формат вывода</h2>
<div class="output-specification">
<p>Для каждой строки требуется вычислить <span style="font-weight: bold;">максимальную</span> моду чисел, входящих в диапазон [X, Y] (границы включены).</p>
</div>
<h3>Пример 1</h3>
<table class="sample-tests">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>2 3
1 2 2 3 3 3 4 4 4 4
</pre>
</td>
<td>
<pre>3
</pre>
</td>
</tr>
</tbody>
</table>
<h3>Пример 2</h3>
<table class="sample-tests">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>2 9
3 6 9 6 3
1 1 1
</pre>
</td>
<td>
<pre>6
-1
</pre>
</td>
</tr>
</tbody>
</table>
</div>

<div class="task-description__content-wrapper"><article class="task-description__description"><div class="problem-statement">
<div class="header">
<h1 class="title">Вложенный сортировщик</h1>
<table class="table table-sm table-from-contest">
<tbody>
<tr class="time-limit">
<td class="property-title">Ограничение времени</td>
<td>1&nbsp;секунда</td>
</tr>
<tr class="memory-limit">
<td class="property-title">Ограничение памяти</td>
<td>64Mb</td>
</tr>
<tr class="input-file">
<td class="property-title">Ввод</td>
<td colspan="1">стандартный ввод или input.txt</td>
</tr>
<tr class="output-file">
<td class="property-title">Вывод</td>
<td colspan="1">стандартный вывод или output.txt</td>
</tr>
</tbody>
</table>
</div>
<h2></h2>
<div class="legend">
<p>Теперь Зинаида просит вас создать функцию <span style="font-weight: bold;">sorted2(data, key)</span>, способную сортировать вложенные списки, содержащие целые числа.</p>
<p>Сортировка должна производиться следующим образом:</p>
<ol>
<li>Сначала список преобразуется в линейный по столбцам (например, из списка <span>[<span>[1, 2]</span>, <span>[3, 4]</span>, <span>[5, 6]</span>]</span> получается список <span>[1, 3, 5, 2, 4, 6]</span>).</li>
<li>Затем сортируется по заданному ключу.</li>
<li>Затем список преобразуется к изначальной структуре.</li>
</ol>
<p>Параметр data содержит вложенный список, который требуется обработать.</p>
<p>Параметр key задаёт функцию, определяющую правило сортировки. Задайте значение по умолчанию так, чтобы сортировка производилась по убыванию.</p>
</div>
<h2>Формат ввода</h2>
<div class="input-specification">
<p>Функция не должна ничего считывать.</p>
</div>
<h2>Формат вывода</h2>
<div class="output-specification">
<p>Функция не должна ничего выводить.</p>
</div>
<h3>Пример 1</h3>
<table class="table table-sm table-from-contest">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>data = [[1, 2], [3, 4], [5, 6]]
</pre>
</td>
<td>
<pre>res = [[6, 3], [5, 2], [4, 1]]
</pre>
</td>
</tr>
</tbody>
</table>
<h3>Пример 2</h3>
<table class="table table-sm table-from-contest">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>data = [[6, 5, 4], [3, 2, 1]]
key = lambda x: x
</pre>
</td>
<td>
<pre>res = [[1, 3, 5], [2, 4, 6]]
</pre>
</td>
</tr>
</tbody>
</table>
<h2>Примечания</h2>
<div class="notes">
<p>Все строки вложенных списков имеют одинаковую длину.</p>
<p>В примерах:</p>
<ul>
<li>data — передаваемый функции список;</li>
<li>key — передаваемая функции функция;</li>
<li>res — получаемый от функции результат.</li>
</ul>
<p>Список должен возвращаться к первоначальной форме, по алгоритму обратному преобразованию к линейному по столбцам</p>
</div>
</div></article></div>
<div class="task-header__task-description"><section class="task-description"><div class="task-description__content-wrapper"><article class="task-description__description"><div class="problem-statement">
<div class="header">
<h1 class="title">Подушка 2: Наследование</h1>
<table class="table table-sm table-from-contest">
<tbody>
<tr class="time-limit">
<td class="property-title">Ограничение времени</td>
<td>1&nbsp;секунда</td>
</tr>
<tr class="memory-limit">
<td class="property-title">Ограничение памяти</td>
<td>64Mb</td>
</tr>
<tr class="input-file">
<td class="property-title">Ввод</td>
<td colspan="1">стандартный ввод или input.txt</td>
</tr>
<tr class="output-file">
<td class="property-title">Вывод</td>
<td colspan="1">стандартный вывод или output.png</td>
</tr>
</tbody>
</table>
</div>
<h2></h2>
<div class="legend">
<p>По мнению Зинаиды, вы уже точно знаете всё о библиотеке PIL.</p>
<p>Сейчас её больше интересует, насколько хорошо вы изучили работу с пакетом ImageDraw.</p>
<p>Как вам известно, этот пакет предназначен для отрисовки на изображении различных примитивов, однако Зинаиде не хватает функциональности.</p>
<p>Она просит вас расширить класс PIL.ImageDraw.ImageDraw и создать его наследника ImageDrawer.</p>
<p>От нового класса требуется реализовать два новых метода: down_parallelogram(xy, height, fill, outline), up_parallelogram(xy, height, fill, outline).</p>
<p>Метод down_parallelogram предназначен для отрисовки параллелограмма, наклонённого вниз. Параметр xy задаёт левый верхний угол и нижний правый угол прямоугольника, описанного вокруг параллелограмма. Параметр height задаёт высоту вертикальных сторон.</p>
<p>Метод up_parallelogram предназначен для отрисовки параллелограмма, наклонённого вверх. Параметр xy задаёт левый верхний угол и нижний правый угол прямоугольника, описанного вокруг параллелограмма. Параметр height задаёт высоту вертикальных сторон.</p>
<p>Параметры fill (цвет заливки), outline(цвет границы) у обоих методов являются необязательными, задайте им значение по умолчанию «в духе» PIL.ImageDraw.ImageDraw.</p>
<p>Решение должно содержать только требуемый класс, ничего вызывать не надо.</p>
</div>
<h2>Формат ввода</h2>
<div class="input-specification">
<p>Ничего не вводится.</p>
</div>
<h2>Формат вывода</h2>
<div class="output-specification">
<p>Ничего выводить не требуется</p>
</div>
<h3>Пример 1</h3>
<table class="table table-sm table-from-contest">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>{
    'background': 'black',
    'down_parallelograms': [
        {
            'fill': 'white',
            'height': 60,
            'outline': 'red',
            'xy': (10, 10, 90, 90)
        },
        {
            'fill': 'white',
            'height': 60,
            'outline': 'red',
            'xy': (110, 110, 190, 190)
        }
    ],
    'size': (200, 200),
    'up_parallelograms': [
        {
            'fill': 'white',
            'height': 60,
            'outline': 'red',
            'xy': (10, 110, 90, 190)
        },
        {
            'fill': 'white',
            'height': 60,
            'outline': 'red',
            'xy': (110, 10, 190, 90)
        }
    ]
}

</pre>
</td>
<td><img src="https://yastatic.net/s3/lyceum/content/resources/control2/output-10.png"></td>
</tr>
</tbody>
</table>
<h2>Примечания</h2>
<div class="notes">
<p>В примерах в качестве ввода представлены параметры будущего изображения:</p>
<p>size — размер будущей картинки;</p>
<p>background — цвет фона;</p>
<p>down_parallelograms — список, содержащий параметры каждого параллелограмма, наклонённого вниз, который требуется отрисовать;</p>
<p>up_parallelograms — список, содержащий параметры каждого параллелограмма наклонённого вверх, который требуется отрисовать.</p>
</div>
</div></article></div></section></div>
<div class="task-details-student__main-content"><div class="task-details-student__task-header"><header class="task-header"><a class="nav-tab nav-tab_view_button" href="/courses/89/groups/409/lessons/826"><span data-lego="react" class="icon icon_type_arrow icon_direction_left icon_size_xs nav-tab__arrow-icon"></span>Урок КР №2</a><h1 class="task-header__title">Game of Python</h1><div class="task-header__info"><div class="student-task-info__tag"><div class="indicator indicator_color_white indicator_size_m"></div><div class="student-task-info__tag-name">Kлассная работа</div></div><div class="student-task-info__max-score">max&nbsp;<span class="student-task-info__score">35 бал.</span></div></div></header></div><div class="task-details-student__description"><section class="task-viewer"><div class="task-viewer__solution-sender"><div class="solution-sender"><span data-lego="react" class="attach attach_theme_action attach_size_m"><span data-lego="react" class="control button2 button2_view_classic button2_size_m button2_theme_action button2_has-control_yes attach__button"><span data-lego="react" class="button2__text">Сдать задачу</span><input data-lego="react" autocomplete="off" aria-disabled="false" type="file" id="uniq4" name="attachment" aria-labelledby="textuniq4" class="button2__control attach__control" value=""></span></span></div></div><section class="task-description"><div class="task-description__content-wrapper"><article class="task-description__description"><p></p>
<div class="problem-statement">
<div class="header">
<h1 class="title">Game of Python</h1>
<table>
<tbody>
<tr class="time-limit">
<td class="property-title">Ограничение времени</td>
<td>1&nbsp;секунда</td>
</tr>
<tr class="memory-limit">
<td class="property-title">Ограничение памяти</td>
<td>64Mb</td>
</tr>
<tr class="input-file">
<td class="property-title">Ввод</td>
<td colspan="1">run.py</td>
</tr>
<tr class="output-file">
<td class="property-title">Вывод</td>
<td colspan="1">стандартный вывод или output.txt</td>
</tr>
</tbody>
</table>
</div>
<h2></h2>
<div class="legend">Зинаида считает ООП великолепным подходом к программированию различных систем. <!--l. 47-->
<p style="text-indent: 0em;">Сегодня она хочет, чтобы вы начали разрабатывать основу для pyRPG (Python role-playing game). <!--l. 49--></p>
<p style="text-indent: 0em;">Представьте себе мир, в котором у игроков есть три основных характеристики: сила (strength), ловкость (agility), интеллект (intelligence) и скорость атаки (speed). По умолчанию у каждого героя (Player) игры все характеристики равны нулю. <!--l. 51--></p>
<p style="text-indent: 0em;">В игре используется оружие (Weapon), ношение которого накладывает определённый эффект на игрока. <!--l. 53--></p>
<p style="text-indent: 0em;">Перед вами стоит задача создать два класса Weapon и Player, описывающие данную механику. <!--l. 55--></p>
<p style="text-indent: 0em;">Класс Weapon описывает оружие. <!--l. 57--></p>
<p style="text-indent: 0em;">Конструктор класса Weapon должен иметь вид: Weapon(one_handed, strength, agility, intelligence). Параметры strength, agility, intelligence описывают силу, ловкость и интеллект оружия соответственно и являются необязательными. Параметр one_handed описывает флаг «одноручности» оружия, также является необязательным и имеет значение по умолчанию False. <!--l. 59--></p>
<p style="text-indent: 0em;">Класс Weapon должен иметь методы:</p>
<ul>
<li>is_one_handed() — возвращает True, если оружие является «одноручным», иначе — False;</li>
<li>strength() — возвращает силу, получаемую от оружия;</li>
<li>agility() — возвращает ловкость, получаемую от оружия;</li>
<li>intelligence() — возвращает интеллект, получаемый от оружия;</li>
<li>speed() — возвращает скорость атаки, вычисляемую как сумма остальных параметров, помноженных на соответствующие коэффициенты мира;</li>
<li>copy() — возвращает копию оружия.</li>
</ul>
<!--l. 70-->
<p style="text-indent: 0em;">Над объектами класса Weapon должна быть возможность производить следующие действия:</p>
<ul>
<li>weapon + number — создаёт новое оружие, параметры которого являются увеличенными параметрами переданного объекта. Увеличение каждого параметра производится на переданное число, помноженное на соответствующий коэффициент мира. Если переданное число чётно — новое оружие становится «одноручным», иначе — «двуручным»;</li>
<li>weapon += number — изменяет оружие, увеличивая каждый параметр на переданное число, помноженное на соответствующий коэффициент мира. Если переданное число четно — оружие становится «одноручным», иначе — «двуручным»;</li>
<li>round(weapon, number) — создаёт новое оружие, являющееся «выравненной» копией первого. Каждый параметр оружия выравнивается до ближайшего меньше либо равного числа, кратного переданному. По умолчанию параметр number=2;</li>
<li>str(weapon) — возвращает строковое представление оружия в виде: «Weapon[N](strength: St, agility: A, intelligence: I, speed: Sp)», где N = 1, если оружие «одноручное» и N = 2, если «двуручное».</li>
</ul>
<!--l. 79-->
<p style="text-indent: 0em;">Класс Player описывает игрока. <!--l. 81--></p>
<p style="text-indent: 0em;">Конструктор класса Player должен иметь вид: Player(). <!--l. 83--></p>
<p style="text-indent: 0em;">Класс Player должен иметь методы:</p>
<ul>
<li>strength() — возвращает силу героя, суммирая силу всех оружий;</li>
<li>agility() — возвращает ловкость героя, суммируя ловкость всех оружий;</li>
<li>intelligence() — возвращает интеллект героя, суммируя интеллект всех оружий;</li>
<li>speed() — возвращает скорость атаки героя, вычиcляемую как сумму скоростей всех оружий;</li>
<li>take_up_weapon(weapon) — добавляет копию оружия герою. Игрок может держать одновременно либо два «одноручных» оружия, либо одно «двуручное». Если герой не может взять в руки ещё одно оружие, то он сбрасывает одно или два оружия (самое старое);</li>
<li>throw_a_weapon() — скидывает самое старое оружие игрока.</li>
</ul>
<!--l. 94-->
<p style="text-indent: 0em;">Над объектами класса Player должна быть возможность производить следующие операции:</p>
<ul>
<li>player &amp; weapon — добавляет копию оружия герою. Игрок может держать одновременно либо два «одноручных» оружия, либо одно «двуручное». Если герой не может взять в руки ещё одно оружие, то он сбрасывает одно или два оружия (самое старое);</li>
<li>next(player) — скидывает самое старое оружие игрока;</li>
<li>str(player) — возвращает строку, описывающую игрока в формате:</li>
</ul>
<!--l. 101-->
<div style="font-family: monospace; margin-bottom: 0.5em; margin-top: 0.5em; white-space: nowrap;"><span style="margin-right: 0.5em;"><a></a></span>Player[N](&nbsp;<br><span style="margin-right: 0.5em;"><a></a></span>Strength:&nbsp;St,&nbsp;<br><span style="margin-right: 0.5em;"><a></a></span>Agility:&nbsp;Ag,&nbsp;<br><span style="margin-right: 0.5em;"><a></a></span>Intelligence:&nbsp;I,&nbsp;<br><span style="margin-right: 0.5em;"><a></a></span>Speed:&nbsp;Sp&nbsp;<br><span style="margin-right: 0.5em;"><a></a></span>)</div>
<!--l. 110-->
<p style="text-indent: 0em;">где N — количество оружий у игрока. <!--l. 112--></p>
<p style="text-indent: 0em;">Коэффициент силы данного мира: 2. <!--l. 114--></p>
<p style="text-indent: 0em;">Коэффициент ловкости данного мира: 3. <!--l. 116--></p>
<p style="text-indent: 0em;">Коэффициент интеллекта данного мира: 1.</p>
<p></p>
<p></p>
</div>
<h3>Пример 1</h3>
<table class="sample-tests">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>from solution import Weapon

weapon1 = Weapon(strength=3)
weapon2 = Weapon(one_handed=False, agility=5)
weapon3 = weapon1 + 2
weapon4 = weapon3.copy()
weapon4 += 4
weapon5 = round(weapon1)
weapon6 = weapon4.copy()
weapon6 = round(weapon6, 3)

print(weapon1)
print(weapon2)
print(weapon3)
print(weapon4)
print(weapon5)
print(weapon6)
</pre>
</td>
<td>
<pre>Weapon[2](strength: 3, agility: 0, intelligence: 0, speed: 6)
Weapon[2](strength: 0, agility: 5, intelligence: 0, speed: 15)
Weapon[1](strength: 7, agility: 6, intelligence: 2, speed: 34)
Weapon[1](strength: 15, agility: 18, intelligence: 6, speed: 90)
Weapon[2](strength: 2, agility: 0, intelligence: 0, speed: 4)
Weapon[1](strength: 15, agility: 18, intelligence: 6, speed: 90)
</pre>
</td>
</tr>
</tbody>
</table>
<h3>Пример 2</h3>
<table class="sample-tests">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>from solution import Weapon, Player

weapon1 = Weapon(strength=2)
weapon2 = Weapon(intelligence=5)
weapon3 = round(weapon1)

print(weapon1)
print(weapon2)
print(weapon3)
print('---')

player = Player()
player.take_up_weapon(weapon1)
print(player, end='\n---\n')
player.take_up_weapon(weapon2)
print(player, end='\n---\n')
player.throw_a_weapon()
print(player, end='\n---\n')
player &amp; weapon1
player &amp; weapon2
player &amp; weapon3
print(player, end='\n---\n')
next(player)
print(player, end='\n---\n')
</pre>
</td>
<td>
<pre>Weapon[2](strength: 2, agility: 0, intelligence: 0, speed: 4)
Weapon[2](strength: 0, agility: 0, intelligence: 5, speed: 5)
Weapon[2](strength: 2, agility: 0, intelligence: 0, speed: 4)
---
Player[1](
Strength: 2,
Agility: 0,
Intelligence: 0, 
Speed: 4
)
---
Player[1](
Strength: 0,
Agility: 0,
Intelligence: 5, 
Speed: 5
)
---
Player[0](
Strength: 0,
Agility: 0,
Intelligence: 0, 
Speed: 0
)
---
Player[1](
Strength: 2,
Agility: 0,
Intelligence: 0, 
Speed: 4
)
---
Player[0](
Strength: 0,
Agility: 0,
Intelligence: 0, 
Speed: 0
)
---
</pre>
</td>
</tr>
</tbody>
</table>
<h3>Пример 3</h3>
<table class="sample-tests">
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>from solution import Weapon, Player


class InfinityGlove(Weapon):

    def __init__(self):
        Weapon.__init__(self, strength=100500, agility=100500,
                        intelligence=100500)


class Titan(Player):
    pass


Thanos = Titan()
Thanos &amp; InfinityGlove()
print(Thanos)
</pre>
</td>
<td>
<pre>Player[1](
Strength: 100500,
Agility: 100500,
Intelligence: 100500, 
Speed: 603000
)
</pre>
</td>
</tr>
</tbody>
</table>
</div></article></div></section></section></div><a class="task-details-student__previous-task" href="/courses/89/groups/409/lessons/826/tasks/7662"><span data-lego="react" class="icon icon_type_arrow icon_direction_left icon_size_l"></span></a></div>
