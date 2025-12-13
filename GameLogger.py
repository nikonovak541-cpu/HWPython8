# ЗАДАНИЕ 1. “Игровой логгер событий” (Синглтон + Наблюдатель + Декоратор — вместе)

# Создать мини-систему событий игры, используя три паттерна одновременно:

# Синглтон:
# Создайте класс GameLogger, который хранит журнал всех событий игры.
# Независимо от количества созданных объектов — логгер должен быть один.

# Наблюдатель:
# Создайте объект GameEventManager, который рассылает события подписчикам:
# например, PlayerUI, SoundSystem, Analytics.

# Декоратор:
# Реализуйте декоратор, который:
# добавляет метку времени к любому записываемому событию,
# или красиво форматирует строку события.

# Пример сценария:
# Игрок подобрал предмет.
# Игрок получил урон.
# Враг появился рядом.

# Каждое событие должно:
# пройти через декоратор (форматирование текста),
# отправиться всем подписчикам,
# записаться в Singleton-логгер.

# from datetime import datetime, date
import datetime
from functools import wraps # Декоратор сохраняет имя, документацию и другие атрибуты оригинальной функции, предотвращая их потерю при декорировании
from typing import Callable, List # Модуль содержит классы и функции для работы с аннотациями типов, и с его помощью можно описывать различные конструкции, например, функции и списки

# -----------------------
# Singleton: GameLogger
# -----------------------
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class GameLogger(metaclass=SingletonMeta):
    def __init__(self):
        self.records: List[str] = []

    def log(self, message: str):
        self.records.append(message)

    def dump(self) -> List[str]:
        return list(self.records)

# -----------------------

def format_event(prefix: str = "") -> Callable:
    # """
    # Декоратор для форматирования события:
    # добавляет метку времени и префикс (например, роль/источник).
    # """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            raw = func(*args, **kwargs)              # исходная строка события
            ts = datetime.datetime.now() #utcnow().isoformat(timespec='seconds') + "Z" # Z - привязка к опеределенной стране (время)  # ВОТ В ЧЁМ БЫЛА ПРОБЛЕМА, PIZDEC!!!!
            formatted = f"[{ts}] {prefix}{raw}"     # красивое форматирование
            return formatted
        return wrapper
    return decorator

# -----------------------
# Observer
# -----------------------
class GameEventManager:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self, event: str):
        # Отправка всем подписчикам и запись в логгер Singleton
        logger = GameLogger()
        for sub in self._subscribers:
            try:
                sub.on_event(event)
            except Exception as e:
                # Подписчики не должны ломать распространение событий
                print(f"Ошибка у подписчика {sub}: {e}")
        logger.log(event)

# -----------------------
# Подписчики (Observers)
# -----------------------
class PlayerUI:
    def __init__(self, player_name: str):
        self.player_name = player_name

    def on_event(self, event: str):
        # UI показывает событие
        print(f"UI[{self.player_name}]: {event}")

class SoundSystem:
    def on_event(self, event: str):
         # Демонстрация — по ключевым словам воспроизводим
        if "подобрал" in event or "подобрал(а)" in event:
            print("Звук: проигрывает 'звуковое сопровождение при поднятии'") # pickup_sound  # Так понимаю, можно и так и так
        elif "получил" in event or "получила" in event:
            print("Sound: play 'звуковое сопровождение при получении урона'") # damage_sound  # Так понимаю, можно и так и так
        elif "появился" in event:
            print("Sound: play 'spawn_sound'") # Звуковое сопровождение при обнаружении врага  # Так понимаю, можно и так и так

class Analytics:
    def __init__(self):
        self.counts = {}

    def on_event(self, event: str):
        # Аналитика событий
        key = event.split()[2] if len(event.split()) > 2 else event
        self.counts[key] = self.counts.get(key, 0) + 1

    def report(self):
        print("Analytics report:", self.counts)

# -----------------------
# Сценарий: события в мире Newerwinter Nights (Компот, Коржик, Карамелька)
# -----------------------
event_manager = GameEventManager()

# создаём подписчиков и регистрируем их
ui_kompot = PlayerUI("Компот")
ui_korzhik = PlayerUI("Коржик")
sound = SoundSystem()
analytics = Analytics()

for sub in (ui_kompot, ui_korzhik, sound, analytics):
    event_manager.subscribe(sub)

# события — функции, декорированные для форматирования
@format_event(prefix="Компот: ")
def kompots_pick_item(item_name: str) -> str:
    return f"подобрал(а) предмет '{item_name}'"

@format_event(prefix="Коржик: ")
def korzhik_take_damage(amount: int) -> str:
    return f"получил(а) {amount} урона"


# @format_event(prefix="Коржик: ")
# def korzhik_take_shield(amount: int) -> str:       # -----------  КАК ПРИМЕР, НО НЕ ПОЛУЧИЛОСЬ -------------
#     return f"поднимает(а) предмет снаряжения 'Башенный щит'"

@format_event(prefix="Карамелька: ")
def karamelka_enemy_spawned(enemy_type: str) -> str:
    return f"враг '{enemy_type}' появился рядом"

# Генерируем события: каждый результат проходит через декоратор,
# затем рассылается всем подписчикам и записывается в логгер.


e1 = kompots_pick_item("Зелье ловкости")
event_manager.notify(e1)

e2 = korzhik_take_damage(10)
event_manager.notify(e2)


e3 = karamelka_enemy_spawned("Гоблин-воин")
event_manager.notify(e3)

# e4 = korzhik_take_shield("Башенный щит")
# event_manager.notify(e4)                 # ----------- ДУБЛИРУЕТСЯ, НЕ ПОЛУЧИЛОСЬ, ТРЕБУЕТСЯ ДОРАБОТКА ------------


# Показать содержимое логгера и отчёт аналитики
print("\n--- Лог игры (из GameLogger) ---")
for line in GameLogger().dump():
    print(line)

print("\n--- Аналитика ---")
print("Отчёт по аналитике")
analytics.report()

print(datetime.datetime.today())
# print(datetime.datetime.now())
