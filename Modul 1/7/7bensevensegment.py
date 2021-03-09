def seven_segment():
    logo_seven = ['''
            
        ██████╗ ███████╗███╗   ██╗███████╗    ███████╗███████╗██╗   ██╗███████╗███╗   ██╗    ███████╗███████╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
        ██╔══██╗██╔════╝████╗  ██║██╔════╝    ██╔════╝██╔════╝██║   ██║██╔════╝████╗  ██║    ██╔════╝██╔════╝██╔════╝ ████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
        ██████╔╝█████╗  ██╔██╗ ██║███████╗    ███████╗█████╗  ██║   ██║█████╗  ██╔██╗ ██║    ███████╗█████╗  ██║  ███╗██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
        ██╔══██╗██╔══╝  ██║╚██╗██║╚════██║    ╚════██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║    ╚════██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
        ██████╔╝███████╗██║ ╚████║███████║    ███████║███████╗ ╚████╔╝ ███████╗██║ ╚████║    ███████║███████╗╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                                            
        ''']
    angka = {
        '0': [' __ ', '|  |', '|__|'],
        '1': ['    ', '   |', '   |'],
        '2': [' __ ', ' __|', '|__ '],
        '3': [' __ ', ' __|', ' __|'],
        '4': ['    ', '|__|', '   |'],
        '5': [' __ ', '|__ ', ' __|'],
        '6': [' __ ', '|__ ', '|__|'],
        '7': [' __ ', '   |', '   |'],
        '8': [' __ ', '|__|', '|__|'],
        '9': [' __ ', '|__|', ' __|']
    }
    while True:
        print(logo_seven[0])
        print()
        num7b = input("Masukkan angka : ")
        # ngambil dictionary angka >>> angka['key'] sesuai input user
        abstrak = [angka[k] for k in num7b]
        for l in range(3):  # bikin row per - baris
            container = list()  # bikin container sementara
            for part in abstrak:
                # Append per bagian dari part (mulai dari baris atas dulu; total ada 3 baris)
                container.append(part[l])
            print(' '.join(container))  # butuh d join kalo ga ada petiknya
        askuser = input('Do you want to play again? (y/n) : ')
        if askuser == 'y':
            continue
        elif askuser == 'n':
            print('Game Over, Starting over... ')
            break


seven_segment()