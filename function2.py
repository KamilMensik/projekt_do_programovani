def check_list(key: str, value: str, hash: list) -> bool:
    while True:
        try:
            if hash[key] == value:
                return True
            else:
                return False
        except:
            print('Klic nebyl nalezen')    
            return False

hash = { 'klic': 'hodnota' }
print(check_list('klic', 'hodnota', hash))
print(check_list('klic', 'nehodnota', hash))
print(check_list('neklic', 'hodnota', hash))