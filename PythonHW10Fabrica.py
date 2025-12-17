# Задача:
# Создайте фабрику, которая по строковому названию создаёт разные типы сообщений для приложения
# '----------Cadian Regiment----------'

class TextMessage:
    def __init__(self, text: str):
        self.text = text
    
    def __repr__(self):
        return f"Текстовое Сообщение(текст ='{self.text}')"

class VoiceMessage:
    def __init__(self, record_id: str, duration: float):
        self.record_id = record_id  # Используется ID записи вместо прямого пути к файлу( по другому без понятия как сделать, чтобы текстом выводилось)
        self.duration = duration
        
    def __repr__(self):
        return f"Голосовое Сообщение(ID ='{self.record_id}', длительность={self.duration} сек)"

class ImageMessage:
    def __init__(self, image_id: str, caption: str = None):
        self.image_id = image_id  #  Используется ID изображения вместо прямого пути к файлу( по другому без понятия как сделать, чтобы текстом выводилось)
        self.caption = caption
        
    def __repr__(self):
        caption_str = f", подпись='{self.caption}'" if self.caption else ""
        return f"Изображение Сообщение(ID ='{self.image_id}'{caption_str})"

# --- ФАБРИКА ---

def create_message(kind: str, **kwargs):
    message_types = {
        'text': TextMessage,
        'voice': VoiceMessage,
        'image': ImageMessage,
    }
    
    cls = message_types.get(kind.lower())
    
    if not cls:
        raise ValueError(f"Неизвестный тип сообщения: {kind}")
        
    return cls(**kwargs)

print("-*-*-*- Запуск фабрики -*-*-*-")

# Текстовое сообщение
text = create_message('text', text='Кадия стоит!')
print(text)

# Голосовое сообщение
voice = create_message('voice', record_id='Гимн Кадианского Полка', duration=20.6)
print(voice)

# Изображение-сообщение
image = create_message('image', image_id='img_screen_A1B2C3', caption='Оборона Кадии!')
print(image)

