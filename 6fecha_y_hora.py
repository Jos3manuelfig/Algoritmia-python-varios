import datetime

def main():
    ahora=datetime.datetime.now()
    print(ahora)
    print(ahora.strftime('%d/%m/%Y') )
    print(ahora.strftime('%H :%m'))


if __name__ =='__main__':
    main()