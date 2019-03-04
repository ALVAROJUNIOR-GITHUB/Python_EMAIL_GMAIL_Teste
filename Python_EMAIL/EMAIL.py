# -*- coding: utf-8 -*-
import gmail

try:
    print('Aguarde, enviando Email...')
    send_from = 'alvaroinatel@gmail.com'
    password  = 'CB4001982'
    send_to   = ['alvaroinatel@gmail.com']
    subject   = 'Email enviando pelo Python'
    text      = 'Aqui fica a mensagem principal'
    #files     = ['/pasta/arquivo_a_ser_enviado_em_anexo'] 
    gmail.send_mail(send_from, password, send_to, subject, text)
    print('Email enviado !!!')
    
except IOError:
    print('sem rede')
