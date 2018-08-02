def map(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonuçlarını liste olarak döndürür"""
    sonuc = []
    for item in liste:
        sonuc.append(func(item))
    return sonuc


def filter(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonucu True olanları liste olarak döndürür"""
    sonuc = []
    if func is None:
        for item in liste:
            if item is not None:
                sonuc.append(item)
    else:
        for item in liste:
            if func(item):
                sonuc.append(item)
    return sonuc


def reduce(func, liste):
    """Bir sekansı bir fonksyona sırayla sokup sonuçları birleştirerek döndürür"""
    sonuc = func(liste[0], liste[1])
    for item in liste[2:]:
        sonuc = func(sonuc, item)
    return sonuc
