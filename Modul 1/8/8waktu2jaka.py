import datetime as dt
class Sekarang:

    time = dt.datetime.now()
    tahun = time.strftime('%Y')
    month = time.strftime('%m')
    monthID =        {  '01': 'Januari',
                        '02': 'Februari',
                        '03': 'Maret',
                        '04': 'April',
                        '05': 'Mei',
                        '06': 'Juni',
                        '07': 'Juli',
                        '08': 'Agustus',
                        '09': 'September',
                        '10': 'Oktober',
                        '11': 'November',
                        '12': 'Desember'}
    bulan = monthID[month]
    day = time.strftime('%A')
    dayID =         {   'Sunday': 'Minggu',
                        'Monday': 'Senin',
                        'Tuesday': 'Selasa',
                        'Wednesday': 'Rabu',
                        'Thursday': 'Kamis',
                        'Friday': 'Jumat',
                        'Saturday': 'Sabtu'}
    hari = dayID[day]
    jam = time.strftime('%H')
    menit = time.strftime('%M')
    detik = time.strftime('%S')


    # print(time)
    # print(tahun)
    # print(bulan)
    # print(hari)
    # print(jam)
    # print(menit)
    # print(detik)
