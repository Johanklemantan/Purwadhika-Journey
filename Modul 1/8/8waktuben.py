import datetime as dt

class Sekarang:
    time = dt.datetime.now()
    tahun = time.strftime('%Y')
    month = time.strftime('%B')
    month_dict = {
        'January': 'Januari',
        'February': 'Februari',
        'March': 'Maret',
        'April': 'April',
        'May': 'Mei',
        'June': 'Juni',
        'July': 'Juli',
        'August': 'Agustus',
        'September': 'September',
        'October': 'Oktober',
        'November': 'November',
        'December': 'Desember'
    }
    bulan = month_dict[month.capitalize()]
    day = time.strftime('%A')
    day_dict = {
        'Monday': 'Senin',
        'Tuesday': 'Selasa',
        'Wednesday': 'Rabu',
        'Thursday': 'Kamis',
        'Friday': 'Jumat',
        'Saturday': 'Sabtu',
        'Sunday': 'Minggu',
    }
    hari = day_dict[day.capitalize()]
    jam = time.strftime('%H')
    menit = time.strftime('%M')
    detik = time.strftime('%S')