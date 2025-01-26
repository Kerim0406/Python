def giris(ulanyjy_ady, parol, mumkincilik):
    question = 0

    while question < mumkincilik:
        question += 1
        
        ulanyjy_ady_ = input("Ulanyjy ady: ")
        paroly = input("Paroly: ")

        if paroly == parol and ulanyjy_ady_ == ulanyjy_ady:
            print("Hos geldiniz !")
            return
        
        else:
            print("Ulanyjy ady yada paroly NADOGRY !")
    if question == mumkincilik:
        print("Hasaba girmek mumkinciginiz gutardy !")

giris("Kerim", "12345", 3)