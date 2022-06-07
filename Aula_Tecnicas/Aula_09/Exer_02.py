def adicionar_sufixo_email(emails: list, salvar=True):
    emails_com_sufixo = [email + 'gmail.com'
                        for email in emails]
    print(emails_com_sufixo)

    if salvar:
        with open('emails.txt', 'a') as arq:
            arq.write(emails)