import math
def timeConverter(seconds):
    # jam = math.floor(seconds/3600)
    # menit = math.floor((seconds-(jam*3600))/60)
    # detik = ((seconds-(jam*3600))%60)
    jam = seconds // 3600
    menit = (seconds%3600)//60
    detik = (seconds%3600)%60
    if seconds >=0 and seconds<=359999:
        print (f'"{jam:02d}:{menit:02d}:{detik:02d}"')
    elif seconds>359999:
        print('Invalid Input')
    else:
        print('please input positive integer')
timeConverter(34341)
# a = 115324
# jam = math.floor(a/3600)
# menit = math.floor((a-(jam*3600))/60)
# detik = ((a-(jam*3600))%60)

# print('jam ',jam)
# print('menit ',menit)
# print('detik ', detik)

# print(f"{1:02d}")