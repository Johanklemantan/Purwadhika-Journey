import datetime as dt
class Sekarang:
    time = dt.datetime.now()
    tahun = time.strftime('%Y')
    month = time.strftime('%m')
    month_IN = {
        '01':'Januari',
        '02':'Febuari',
        '03':'Maret',
        '04':'April',
        '05':'Mei',
        '06':'Juni',
        '07':'Juli',
        '08':'Agustus',
        '09':'September',
        '10':'Oktober',
        '11':'November',
        '12':'Desember'}
    bulan = month_IN[month]
    day = time.strftime('%A')
    hari_IN = {
        'Monday':'Senin',
        'Tuesday':'Selasa',
        'Wednesday':'Rabu',
        'Thursday':'Kamis',
        'Friday':'Jumat',
        'Saturday':'Sabtu',
        'Sunday':'Minggu'
    }
    hari = hari_IN[day]
    jam = time.strftime('%H')
    menit = time.strftime('%M')
    detik = time.strftime('%S')
    
