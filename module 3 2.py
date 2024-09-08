def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not sender.endswith((".com", ",ru", ".net")) or not recipient.endswith((".com", ",ru", ".net")):
        print(f"Невозможно отправить с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе")
    elif sender == "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с {sender} на {recipient}")
    else:
        print(f"Письмо отправлено успешно c адреса {sender} на адрес {recipient}")


send_email("Срочно!", "vicha82@gmail.com", sender="urban@mail.com")
send_email("Привет!", "example@mail.com")
send_email("Привет!", "boss@mail.uk")
send_email("Привет!", "university.help@gmail.com")